# Wisdom DerpFest 17 patches

Compatibility patches for Samsung SM-P205 (`wisdom`), based on the
2026-10-08 DerpFest 17 sync (`04cf624`). `manifest.json` records each
project's base commit, patch SHA-256 and file count.

Sync the Project-Wisdom `17` sources with `repo sync --recurse-submodules`.
Each patched project must be clean and at its recorded base commit.
From this repository, check and apply:

```sh
python3 apply.py --check /path/to/derpfest17
python3 apply.py --apply /path/to/derpfest17
```

Use `--project <path>` to select projects. When upstream changes, rebase
the affected patches and update `manifest.json` before applying them.
