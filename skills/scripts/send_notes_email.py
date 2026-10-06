#!/usr/bin/env python3
"""Email Notes deliverables. Prefer ~/.config/pwnjournal/smtp.env; fallback CVE-brief config.json."""

from __future__ import annotations

import argparse
import json
import os
import smtplib
import sys
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


def load_smtp() -> dict:
    env_path = Path.home() / ".config/pwnjournal/smtp.env"
    if env_path.is_file():
        data: dict = {}
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            data[k.strip()] = v.strip().strip('"').strip("'")
        return {
            "host": data.get("SMTP_HOST", "smtp.gmail.com"),
            "port": int(data.get("SMTP_PORT", "587")),
            "username": data.get("SMTP_USER") or data.get("SMTP_USERNAME", ""),
            "password": data.get("SMTP_PASS") or data.get("SMTP_PASSWORD") or data.get("SMTP_APP_PASSWORD", ""),
            "from": data.get("SMTP_FROM") or data.get("SMTP_USER", ""),
            "to": data.get("SMTP_TO") or data.get("SMTP_USER", ""),
            "use_tls": True,
        }

    brief = Path.home() / ".grok/skills/cve-daily-brief/config.json"
    if brief.is_file():
        cfg = json.loads(brief.read_text())
        smtp = cfg.get("smtp", {})
        email = cfg.get("email", {})
        return {
            "host": smtp.get("host", "smtp.gmail.com"),
            "port": int(smtp.get("port", 587)),
            "username": smtp.get("username", ""),
            "password": smtp.get("app_password", ""),
            "from": email.get("from") or smtp.get("username", ""),
            "to": email.get("to") or smtp.get("username", ""),
            "use_tls": bool(smtp.get("use_tls", True)),
        }

    raise SystemExit("No SMTP config: ~/.config/pwnjournal/smtp.env or cve-daily-brief config.json")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", required=True)
    ap.add_argument("--body", required=True)
    ap.add_argument("paths", nargs="+", help="Files to attach")
    args = ap.parse_args()

    smtp = load_smtp()
    if not smtp["username"] or not smtp["password"]:
        print("SMTP username/password missing", file=sys.stderr)
        return 1

    files = [Path(p) for p in args.paths]
    for f in files:
        if not f.is_file():
            print(f"missing attachment: {f}", file=sys.stderr)
            return 1

    to_addr = smtp["to"] or smtp["username"]
    from_addr = smtp["from"] or smtp["username"]

    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = args.subject
    msg.attach(MIMEText(args.body + "\n", "plain"))

    for path in files:
        data = path.read_bytes()
        subtype = "pdf" if path.suffix.lower() == ".pdf" else "octet-stream"
        part = MIMEApplication(data, _subtype=subtype)
        part.add_header("Content-Disposition", "attachment", filename=path.name)
        msg.attach(part)

    with smtplib.SMTP(smtp["host"], smtp["port"], timeout=60) as server:
        if smtp.get("use_tls", True):
            server.starttls()
        server.login(smtp["username"], smtp["password"])
        server.sendmail(from_addr, [to_addr], msg.as_string())

    print(f"sent_to={to_addr} files={[f.name for f in files]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
