topic: AWS identity and credentials
slug: identity_and_credentials
target: skills/phase_1/output/identity_and_credentials/TARGET.md
source_map: skills/phase_1/output/aws_oidc_flow/MAP.md (domain 1 only)
domains:
  1. aws_account             container, 12 digit account ID, ARN
  2. iam_user_access_keys    long-term credentials
  3. iam_role                identity with no keys, assumed for a session
  4. sts_temporary_credentials   three values, expiry
  5. static_vs_temporary     why AWS prefers temporary
order: aws_account, iam_user_access_keys, iam_role, sts_temporary_credentials, static_vs_temporary
acquired:
handoff: explainer run in phase 2, prompts from MAP.html (Explain, Evidence, Go deeper)
