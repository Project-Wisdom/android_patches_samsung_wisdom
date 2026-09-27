# Project-Wisdom DerpFest 17 compatibility patches

These patches record the **15 modified upstream projects** used by the Samsung SM-P205 (`wisdom`) Android 17 / DerpFest #55 build. Project-Wisdom-owned device, kernel and vendor changes belong in their own source repositories and are intentionally excluded. OTA ZIPs, device logs and user data are also excluded.

Each patch is a binary-safe `git diff` from the exact `base_commit` in `manifest.json`. The manifest records the upstream URL, SHA-256 and file count. Applying a patch requires that project's HEAD to match its recorded base and its worktree to be clean. Apply Project-Wisdom-owned source repositories through their normal branches first.

From the patch repository root, check a clean synced tree and then apply:

```sh
python3 apply.py --check /path/to/derpfest17
python3 apply.py --apply /path/to/derpfest17
```

Use `--project packages/modules/Bluetooth` (repeatable) to limit the operation. `--apply` first checks every selected project, then applies the patches. Review the resulting diff and build before release. When upstream commits move, rebase each patch deliberately and update its base commit and checksum; do not force it onto an unrelated revision.

The current checkout already contains these changes. `--apply` is intended for a **fresh** workspace.
