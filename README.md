# Project-Wisdom DerpFest 17 compatibility patches

These patches record the **16 modified upstream projects** for the Samsung SM-P205 (`wisdom`) Android 17 / DerpFest build. The 2026-09-28 legacy fscrypt permission change has passed source and compile checks; device validation remains pending. The `build/soong` patch ignores the NDK-only `Android.mk` files in libjxl's sjpeg submodule, which otherwise stop Android 17 product configuration after recursive submodule sync. Project-Wisdom-owned device, kernel and vendor changes belong in their own source repositories and are intentionally excluded. OTA ZIPs, device logs and user data are also excluded.

Each patch is a binary-safe `git diff` from the exact `base_commit` in `manifest.json`. The manifest records the upstream URL, SHA-256 and file count. Applying a patch requires that project's HEAD to match its recorded base and its worktree to be clean. Apply Project-Wisdom-owned source repositories through their normal branches first.

Sync the Project-Wisdom `17` local manifest with `repo sync --recurse-submodules` so PhhIms receives rnnoise, AEC3, and nested Abseil. If those submodules were not checked out, run `git -C packages/apps/PhhIms submodule update --init --recursive` from the Android tree; the pinned AEC3 commit can be fetched directly from its upstream by full SHA. From the patch repository root, check a clean synced tree and then apply:

```sh
python3 apply.py --check /path/to/derpfest17
python3 apply.py --apply /path/to/derpfest17
```

Use `--project packages/modules/Bluetooth` (repeatable) to limit the operation. `--apply` first checks every selected project, then applies the patches. Review the resulting diff and build before release. When upstream commits move, rebase each patch deliberately and update its base commit and checksum; do not force it onto an unrelated revision.

Run `--apply` only after `--check` succeeds on a clean synced workspace.
