topic: AWS OIDC flow (Azure DevOps to AWS, no static secrets)
slug: aws_oidc_flow
kind: work
title: ACN-2026-31070 - AWS IAM key update with OIDC authentication (security architect advisory, final)
path: user-input-learning-text/AWS - OIDC Case/SA-Report-ACN-2026-31070-IAM-OIDC-Final.docx
done_when: >-
  He can audit each control in the security architect advisory on his own: say what it
  protects, where to look in AWS and Azure DevOps for the evidence, what a pass and a fail
  look like, and write the finding. Then the same base carries any other AWS authentication
  case (federation, roles, keys).
supporting_files:
  - user-input-learning-text/AWS - OIDC Case/SA-Report-ACN-2026-31070-IAM-OIDC-Draft-1.0.docx   (draft, superseded)
  - user-input-learning-text/AWS - OIDC Case/OIDC Authentication-AWS - No Static Secrets-OIS-TEMPLATE (1).docx   (solution architect template, 14 pre/post validation checks)
  - user-input-learning-text/AWS - OIDC Case/ACN-2026-31070 - OIDC authenticaiton captured inforamtion for ACN-2026-31070.docx   (pipeline log evidence)
flag: >-
  He was told 20+ controls. The final advisory lists 16 controls across 8 domains, and the
  solution architect template adds 14 validation checks. 16 + 14 = 30 items overlap in part.
  Confirm with the requester which list is the audit scope.
