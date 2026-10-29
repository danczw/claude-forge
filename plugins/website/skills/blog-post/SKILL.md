---
name: blog-post
description: Write a ~400-word blog post for danczw.com (architecture deep dive, hot take, or lessons learned) in the site's voice, saved as a draft in the current project's posts collection. Use when the user wants to write or draft a blog post for their website.
---

# Blog post for danczw.com

The site of Daniel Czw, an ML infrastructure engineer: building production ML systems: how data moves, how models ship, how both stay secure.

## 1. Input and questions
Get: **post type** (architecture deep dive | hot take | lessons learned), **topic** (one sentence), **core claim** (never invent it), **notes**.
Then ask one batch of ≤ 4 clarifying questions on what's still open (angle, lead example, how punchy, unverifiable facts, whether a snippet earns its place), each with 2–4 options and a recommendation. Write nothing until answered.

## 2. Write
- First person, conversational expert with conviction; take a position. Broad tech audience: explain jargon on first use.
- ~400 words, hard cap 450. One idea. Open with the claim; 2–4 short paragraphs of concrete examples, stories or numbers; close with one decisive line (implication, recommendation or prediction).
- Body may use sparse `##` headings, fenced code with a language tag, one blockquote for the key claim, inline links.
- Banned: hype ("revolutionize", "game-changer", "10x", "unleash"), buzzword stacking, intro filler, rhetorical questions, "in conclusion"/recap paragraphs, hedging chains, em-dash overload.

## 3. Save
```markdown
---
title: '<short title>'
description: '<one-sentence summary>'
publishedAt: <today, YYYY-MM-DD>
tags: ['<2–4 lowercase tags>']
draft: true
---
```
Check word count and banned list. Find the posts dir from the content config (`src/content.config.ts` or `src/content/config.ts`), match its schema and existing tag style, and save `<slug>.md` there. No posts collection in the current dir → return the file content and suggested filename.
