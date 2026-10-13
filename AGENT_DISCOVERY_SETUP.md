# Agent Discovery Setup (RFC 8288 / DNS-AID / Markdown for Agents)

This document tracks the `isitagentready.com` audit goals for `https://f9xr.org`
and what each one requires. Some goals are satisfied by files in this repo
(served by GitHub Pages); three require changes in the **Cloudflare dashboard**
(the site is GitHub Pages origin, proxied by Cloudflare).

## Status

| Goal | In-repo artifact | Still required |
|---|---|---|
| Link response headers | `_headers` (for header-capable hosts) | Cloudflare Transform Rule — see §1 |
| DNS-AID records | — | Cloudflare DNS records + DNSSEC — see §2 |
| Markdown for Agents | — | Enable Cloudflare feature — see §3 |
| OAuth/OIDC discovery | *intentionally omitted* (no auth backend) | — |
| OAuth Protected Resource | *intentionally omitted* (no auth backend) | — |
| auth.md | `/auth.md` ✅ self-contained | — |
| MCP Server Card | `/.well-known/mcp/server-card.json` ✅ | Deploy a live `/mcp` endpoint — see §4 |
| Agent Skills index | `/.well-known/agent-skills/index.json` ✅ | — |
| ARD manifest | `/.well-known/ai-catalog.json` ✅ | — |

Also updated: `robots.txt` (`Agentmap:` directive) and `index.html` `<link>` hints.

> **Note:** GitHub Pages ignores the `_headers` file. It is kept as the source of
> truth for header values and works as-is if the site is ever moved to
> Cloudflare Pages or Netlify. On GitHub Pages, apply the values via Cloudflare
> Transform Rules below.

---

## 1. Link response headers (RFC 8288)

Cloudflare dashboard → `f9xr.org` zone → **Rules → Transform Rules → Modify
Response Header** → **Create rule**.

- **Rule name**: `Link headers for agent discovery`
- **When incoming requests match** (Custom filter expression):

  ```
  (http.host eq "f9xr.org" and http.request.uri.path eq "/")
  ```

- **Then**: **Set static** header
  - **Header name**: `Link`
  - **Value**:

    ```
    </.well-known/api-catalog>; rel="api-catalog"; type="application/linkset+json", </.well-known/ai-catalog.json>; rel="service-desc"; type="application/json", </llms.txt>; rel="service-desc"; type="text/plain", </.well-known/mcp/server-card.json>; rel="service-desc"; type="application/json", </auth.md>; rel="describedby"; type="text/markdown"
    ```

- **Deploy**.

Verify:

```bash
curl -sI https://f9xr.org/ | findstr /I "link"
```

---

## 2. DNS-AID records (RFC 9460 SVCB/HTTPS)

Cloudflare dashboard → `f9xr.org` zone → **DNS → Records → Add record**. Add
the following records (Cloudflare's DNS editor accepts `SVCB`/`HTTPS` types):

```dns
_index._agents.f9xr.org.   3600 IN HTTPS 1 . alpn="agents" port=443
_a2a._agents.f9xr.org.     3600 IN SVCB  1 f9xr.org. alpn="a2a" port=443 mandatory=alpn,port
_catalog._agents.f9xr.org. 3600 IN TXT   "url=https://f9xr.org/.well-known/ai-catalog.json"
```

`_catalog._agents` is the ARD spec's DNS pointer to the ai-catalog manifest
(reported only). Use numeric `keyNNNNN` names for any experimental parameters
until they are registered.

**DNSSEC** — Go to the zone → **DNS → Settings → DNSSEC** → **Enable DNSSEC**,
then add the generated **DS record** at your registrar so validating resolvers
return authenticated data.

Verify (DNS-over-HTTPS, as the scanner does):

```bash
curl -s "https://cloudflare-dns.com/dns-query?name=_a2a._agents.f9xr.org&type=SVCB" -H "accept: application/dns-json"
```

---

## 3. Markdown for Agents

Requires a **Pro or Business** Cloudflare plan.

Cloudflare dashboard → `f9xr.org` zone → **AI Crawl Control** → enable
**Markdown for Agents**.

Or via API:

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{zone_tag}/settings/content_converter" \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer {api_token}" \
  --data-raw '{"value":"on"}'
```

Verify — the response should be `Content-Type: text/markdown`:

```bash
curl -sI https://f9xr.org/ -H "Accept: text/markdown"
```

---

## 4. MCP Server Card endpoint

`/.well-known/mcp/server-card.json` advertises a Streamable HTTP MCP transport at
`https://f9xr.org/mcp`. GitHub Pages is static and cannot serve the MCP
handshake, so that endpoint must be provided by a Worker (or other host) before
agents can connect. Until then the card is a valid discovery document but the
transport will not respond.

---

## 5. OAuth goals — intentionally not published

`ai.txt` and `/auth.md` state that F9XR runs no authenticated APIs. Publishing
`oauth-authorization-server`, `openid-configuration`, or
`oauth-protected-resource` would advertise endpoints that do not exist, so they
are deliberately omitted. If a real identity provider is ever added (e.g.
Cloudflare Access), publish the matching metadata and set the issuer in
`/auth.md`.
