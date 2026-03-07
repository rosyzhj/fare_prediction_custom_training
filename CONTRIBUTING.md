# Contributing Guide

## Branching
- Create feature branches for each milestone/task.
- Keep `main` stable and documented.

## Commit Style
- Use small, focused commits.
- Recommended format: `<type>: <short summary>`
- Example types: `feat`, `fix`, `docs`, `chore`, `refactor`.

## Pull Request Checklist
- Code or notebook changes are scoped to one task.
- README/plan is updated for workflow-impacting changes.
- No credentials, keys, or large raw data files are included.
- Basic run path validated (data prep, train, or inference).

## Project Hygiene
- Keep output artifacts in ignored paths (`artifacts/`, `models/`, `logs/`).
- Keep reproducibility notes in commit messages or project plan.
