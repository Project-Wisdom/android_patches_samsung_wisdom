# Wisdom source and validation record — 2026-10-05

The patch set targets DerpFest 17 manifest `04cf624bec963ac042c1487f1b529f5f5ad44203`. Each upstream project must match its exact `base_commit` in `manifest.json`. Combine these patches with the following Project-Wisdom source revisions on branch `17`:

| Repository | Source commit |
| --- | --- |
| [Device](https://github.com/Project-Wisdom/android_device_samsung_wisdom) | `5638bfa039091e6d5268b4940b81cf76df2d5db0` |
| [Kernel](https://github.com/Project-Wisdom/android_kernel_samsung_wisdom) | `217ea2d1a413343f7777cde73272fb806ff77b5c` |
| [Vendor](https://github.com/Project-Wisdom/proprietary_vendor_samsung_wisdom) | `8bf42c68606c9fbdb6e09778b34786bc2e8f1dad` |
| [Local manifest](https://github.com/Project-Wisdom/android_manifest_samsung_wisdom) | `40d05c4f39a583cce54310e839b54c82abde14b5` |

PhhIms (`xuanyayi/ims-for-wisdom`, branch `derpfest-17`) is at `353a65bae702eb73fed5955f0cbfa5bfe99e5087`. Initialize its recursive submodules when syncing.

## Changes included

- Rebase the compatibility set onto the 2026-10-05 upstream baseline, preserving the upstream verified-boot and certification changes.
- Add the system dark-animation fallback in frameworks/base.
- Install Monet animation modules and Fossify Gallery in system, retain Gallery2, select the dark animation by default through the device configuration, and fit the authored 1080×2160 animation to a centered 960×1920 rectangle on the 1200×1920 display. PNG content is unchanged.
- The device source adds the sw600dp portrait full-width shade override. Landscape retains the upstream split shade.
- The kernel source selectively adapts xxKSU 32657 / UAPI v5, with Linux 4.4 helper and AVTAB/XPERMS fixes. Pair it with Manager/ksud v3.3.0-59 / UAPI v5.

## Verified

All 17 patch hashes, base commits, and file counts were checked. `apply.py --check` and `--apply` passed on isolated clean Git mirrors. Every resulting tree matches the active modified upstream source tree, and reversing each patch restores the recorded base tree. The mirrors used temporary indexes and shared local Git objects; the active source files were not reverted.

The full `m derp -j8` build passed in rom-builder, including VINTF compatibility and OTA ZIP integrity checks. The package was Recovery-sideloaded successfully without clearing user data. Boot completed with SELinux Enforcing; System Server/SystemUI remained alive, and the crash buffer was empty. The installed boot partition matches the candidate image over its image length.

Portrait resolves `config_isFullWidthShade=true`, `shadeMode=Single`; landscape resolves `false`, `shadeMode=Split`. Both layouts were inspected on SM-P205. Root shell, ksud v59, OverlayFS mounting, and OpenEUICC privileged-activity startup passed.

## Installed package identity

- ROM: `DerpFest-v17-20261005-wisdom-Community-Stable.zip`, 1,224,400,857 bytes, SHA-256 `bb354584c46735b6af6307f6535bcdfb19b5d1f048163c61cb4b96c142d37107`.
- boot.img: 27,299,856 bytes, SHA-256 `6df27c2bc8263aa49ea2bd6b920e834b3d35bac6690966169a946a5e8e8320d9`, runtime kernel `#79`. A later intermediate vmlinux was `#80`; it is not the installed image.

These hashes identify the tested package; later builds may differ because of timestamps and kernel build counters.

## Remaining validation

This is a boot and focused functionality check, not full release acceptance. Camera, S-Pen, audio, Wi-Fi/IMS, charging, suspend/resume, app-level root grant/deny/revoke and persistence, general module lifecycle, safe mode, and soft reboot still need regression testing. Actual eSIM operations were not tested.

The existing three Samsung camera section mismatches require a separate lifetime-annotation correction and deferred-probe/rebind testing. The missing `modules.builtin.modinfo` warning comes from the old 4.4 build; the tested configuration has no loadable `.ko` modules. Neither warning was introduced by the shade or animation changes.

ROM binaries, recovery/boot backups, device screenshots, raw logs, and user data are retained locally and are not included in this repository.
