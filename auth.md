# auth.md

F9XR Team (`https://f9xr.org`) publishes static, public content. There is no
authenticated API, no OAuth authorization server, and no token endpoint.

## Agent audience

This document is for AI agents and automated clients that want to consume or
cite F9XR's public information. All resources are open and unauthenticated.

## Authentication

- **Required**: none.
- **Anonymous access**: supported for every published resource.
- All resources at `https://f9xr.org` are readable without credentials,
  registration, or API keys.

## Registration / provisioning

There is no programmatic agent-registration endpoint. If you need a credentialed
integration (for example, access to client project systems or a bespoke data
feed), request it by email and a human will provision it.

- **Registration / provisioning**: mailto:hello@f9xr.org
- **Supported method**: manual, human-verified provisioning only.
- **Credential types**: none are issued through this site.

## OAuth / OIDC

F9XR does not operate an OAuth 2.0 authorization server or an OpenID Connect
provider. There is no `/.well-known/oauth-authorization-server` or
`/.well-known/openid-configuration`, and no `/.well-known/oauth-protected-resource`
metadata, because there are no protected resources.

## Credential use

No credentials are needed. If you ever receive credentials from F9XR out of
band, use them only for the specific resource they were issued for and never
send them to `f9xr.org`, which does not accept or store them.

## Machine-readable resources

- LLM summary: https://f9xr.org/llms.txt
- Full LLM description: https://f9xr.org/llms-full.txt
- API catalog: https://f9xr.org/.well-known/api-catalog
- ARD manifest: https://f9xr.org/.well-known/ai-catalog.json
- Security policy: https://f9xr.org/.well-known/security.txt
- Contact: hello@f9xr.org
