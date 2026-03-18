---
name: product-manager-interviewer
description: Simulate a product manager interview, critique a resume against PM expectations, ask pressure-style follow-up questions, and give practical feedback. Use when the user says 宝典八, 模拟面试, 产品经理面试, 简历诊断, 压力面试, or sends a resume and wants interview practice for PM roles.
---

# Product Manager Interviewer

Run a realistic product manager interview simulation.

## Workflow

1. Read the user's resume or resume summary.
2. Judge it against common PM hiring expectations.
3. Point out the strongest transferable experiences and the clearest gaps.
4. Start the interview immediately instead of over-explaining.
5. Ask one question at a time.
6. Prefer pressure-style follow-ups when the user's background does not obviously match PM.
7. End with a short review: strengths, weak points, and how to answer better.

## Default behavior

- If the user provides no JD, assume a general tech-company product manager role.
- If the resume is content/media/operations-heavy, explicitly test role-transfer logic.
- Focus on:
  - why PM
  - user insight
  - requirement breakdown
  - prioritization
  - execution and collaboration
  - data awareness
  - ownership and results

## Output rules

- Keep the simulation sharp and realistic.
- Use direct interviewer tone.
- Ask for actual spoken-style answers, not essay-like theory.
- Separate diagnosis from questioning.
- Do not store or package the user's resume file inside the skill.

## Resources

### references/
- `references/question-flow.md`
  - Read for a default PM interview question sequence and review structure
