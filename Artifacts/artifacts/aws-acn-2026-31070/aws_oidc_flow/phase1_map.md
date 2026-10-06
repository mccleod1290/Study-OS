topic: AWS OIDC flow
slug: aws_oidc_flow
target: skills/phase_1/output/aws_oidc_flow/TARGET.md
domains:
  1. identity_and_credentials   AWS accounts, IAM users, access keys, roles, STS temporary credentials
  2. oidc_and_tokens            OIDC, identity provider (IdP), JWT, claims iss / aud / sub, discovery and keys
  3. the_flow                   Azure DevOps pipeline -> OIDC token -> AWS STS -> role -> AWS resources
  4. iam_oidc_provider          The trust anchor in AWS: issuer URL, audience
  5. role_trust_policy          Who may assume the role: Principal, Action, Condition aud / sub, StringEquals vs wildcard
  6. permissions_and_least_privilege   Permission policy, policy evaluation, deny wins, boundaries and SCPs
  7. pipeline_side_and_secrets  Service connection, static key removal, no secrets in logs, change control
  8. logging_monitoring_response   CloudTrail, alerts, incident response, inventory
  9. audit_method               Control -> evidence -> pass / fail -> finding (the 16 controls)
  10. adjacent_aws_auth         Where else AWS authenticates: humans, SAML / Identity Center, Cognito, cross-account, service roles
prerequisites:
  - what a cloud account is, what a CI/CD pipeline is, what JSON is (computer literacy plus a minute of gloss each)
acquired: []   # zero mode, no file shows a skill
stuck:
  - "Role vs user: a role has no password or key, you borrow it. Source: AWS IAM roles page."
  - "Two policies on one role: the trust policy says who may assume it, the permission policy says what it can do. Source: AWS IAM roles page, AWS blog on Azure DevOps federation."
  - "aud and sub look like boilerplate but they are the whole lock. A missing or wildcard sub lets the wrong pipeline in. Source: AWS blog on Azure DevOps federation."
  - "Condition key names carry the provider URL, so they look different per provider. Source: AWS blog on Azure DevOps federation."
  - "A condition on a key that is absent evaluates false, so mistakes can fail closed or open depending on the operator. Source: AWS condition operators page."
  - "Login works but the job still gets AccessDenied: authentication and authorization are separate steps. Source: AWS policy evaluation page."
order: identity_and_credentials, oidc_and_tokens, the_flow, iam_oidc_provider, role_trust_policy, permissions_and_least_privilege, pipeline_side_and_secrets, logging_monitoring_response, audit_method, adjacent_aws_auth
sources:
  - claim: temporary credentials via OIDC federation replace stored keys; JWT exchanged for role credentials
    url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html
    grounded: yes
  - claim: IdP prerequisites (issuer, jwks_uri, aud, iss)
    url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html
    grounded: yes
  - claim: Azure DevOps to AWS setup, trust policy shape, sub format
    url: https://aws.amazon.com/blogs/modernizing-with-aws/how-to-federate-into-aws-from-azure-devops-using-openid-connect/
    grounded: yes
  - claim: AssumeRoleWithWebIdentity returns temporary credentials
    url: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html
    grounded: yes
  - claim: policy evaluation, explicit deny, SCP and boundary intersection
    url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html
    grounded: yes
  - claim: IAM and STS calls are logged in CloudTrail
    url: https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html
    grounded: yes
ungrounded:
  - "Template check 5 names AWS_ROLE_ARN and AWS_WEB_IDENTITY_TOKEN_FILE. These are not shown in the captured Azure DevOps evidence; the AWS Toolkit task is what called STS. Confirm whether this check applies."
  - "Template check 3 says only s3:ListBucket, yet the captured evidence ran 'aws s3 ls' with no bucket. Which S3 permission that command needs was not opened."
  - "Template check 1 names a thumbprint. The thumbprint page was not opened."
handoff: explainer not run
