# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This repo holds two unrelated projects. Each one has a path-scoped rule in `.claude/rules/`, which loads only while you work on that project's files:

- `nutrition-research/`: Chinese-language research notes on public nutrition and healthy diets in China and abroad. Rule: `.claude/rules/nutrition-research.md`
- `promo-video/`: a 60-second, 1080×1920 promo video built from HTML pages and rendered frame by frame with Playwright. Rule: `.claude/rules/promo-video.md`

Don't mix changes to the two projects in one commit.
