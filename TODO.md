# ./TODO.md

## Next Version

- [ ] **Containerize the app.** Replaces the per-OS virtual environment setup. Add a `Dockerfile` that installs the `tesseract-ocr` system package plus `requirements.txt`, exposes port 5000, and runs `app.py`. Add a `compose.yaml` that mounts `uploads/` as a volume so extracted files survive container restarts. Once this works, the Windows-only `launcher/OCR_app_Launcher.bat` and the host `venv/` become optional, and the README setup section reduces to a single `docker compose up`. (Raised 2026-08-17)

## Open Questions

- [ ] **Reconcile the Version 1.0.1 entry in `change_log.md` with the code.** The entry dated 2026-04-14 claims "bug fix: web browser IP;port fails" and "update: UI enhancements", but `app.py`, `templates/index.html`, and `static/style.css` are byte-identical to the 1.0.0 code tagged `v1.0`. Either the 1.0.1 work was never written, or it exists in a copy not present in this folder. `README.md` also still reports `## Version 1.0.0 - June 2025`. Decide whether to implement the two items, or drop the 1.0.1 entry and keep the changelog at 1.0.0. (Raised 2026-08-17)
