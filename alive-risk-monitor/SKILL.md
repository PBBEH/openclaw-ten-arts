---
name: alive-risk-monitor
description: Monitor inactivity / missed heartbeats and trigger a standard risk-alert email when the protected person may be unresponsive, offline, or in possible danger. Use when the user asks for 我还活着, 生命体征监测, 失联提醒, 安全心跳, inactivity alert, welfare check, or wants a low-friction safety system for daily status confirmation.
---

# Alive Risk Monitor

Run a simple welfare-check system based on heartbeat timeout.

## Workflow

1. Define the protected person, recipient email, and timeout window.
2. Store heartbeat updates in a local heartbeat file.
3. On each scheduled check:
   - read the last heartbeat time
   - compare with timeout threshold
   - if still within threshold, report alive
   - if beyond threshold, send a risk-alert email
4. Use calm, standard language in alert emails.
5. Do not overstate certainty: alert means possible risk, not confirmed danger.

## Rules

- Default timeout: 24 hours unless the user specifies otherwise.
- Default action: email alert.
- Keep wording professional and clear.
- Use one canonical heartbeat file path.
- Prefer recoverable, easy-to-audit local files.

## Minimum Components

- heartbeat file
- monitor config
- check script
- email sender

## Standard Commands

- touch heartbeat
- run one check
- review recipient + timeout config

## References

- Read `references/alert-template.md` for standard alert wording.
- Read `references/operating-notes.md` for setup and usage notes.
