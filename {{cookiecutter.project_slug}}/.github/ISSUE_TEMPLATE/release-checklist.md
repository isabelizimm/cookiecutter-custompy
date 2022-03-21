---
name: Release checklist
about: prepare for relase
title: Release X.X.X
labels: release
assignees: ''

---

Prepare for release:

- [ ] `pre-commit run`
- [ ] `pytest {{cookiecutter.project_slug}}/tests` 
- [ ] bump release number

Submit to PyPI:
- [ ] submit 🎉
