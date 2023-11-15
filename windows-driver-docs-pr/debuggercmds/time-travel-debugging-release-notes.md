---
title: Time travel debugging release notes
description: This topic provides information on what's new in Time Travel Debugging.
ms.date: 10/30/2023
---

# Time travel debugging release notes

:::image type="content" source="images/ttd-time-travel-debugging-logo.png" alt-text="Time travel debugging logo featuring a clock.":::

This topic provides information on what's new in Time Travel Debugging.

## 1.11.202

This release fixes a number of issues encountered while recording services or monitoring process launch via the `-monitor` switch. It also removes ARM32 recording support from the product.

### Changed

- Reduce binary size by linking TTD components to UCRT as a DLL. (1.11.191)

### Fixed

- Fix recording of services. (1.11.193)
- Fix several issues when using -monitor. (1.11.189)
- Fix the stack frame of the function that preserves non-volatiles when running fallbacks on x64 (1.11.188)
- Re-enabled output buffering for TTD (1.11.187)
- Fix the handling of the GPO's handle in the ProcessMonitorServer (1.11.179)

### Removed

- Remove ARM32 recording code from the repo (1.11.198)

## 1.11.173

This release increases visibility of certain error messages by extracting them from the .out file and printing them to the console. It also fixes a rare crash during trace replay.

### Changed

- Extract and print error messages from .out file (1.11.173)

### Fixed

- Fix file conflict while reading .out file from seperate process. (1.11.171)
- Fix rare crash during trace replay. (1.11.166)

## 1.11.163

This release adds support for recording x86 processes on x64 machines.

### Changed

- Fix x86 recording with x64 TTD installation (1.11.163)

### Fixed

- EULA cleanup (1.11.161)

## 1.11.159

This release is the first public release of the command line recorder. Along with several changes required to
enable public release of the command line recorder, this release also includes a number of bug fixes, including
a couple of fixes to the CPU emulator.

The new `-timestampFileName` switch enables timestamp-based .run file generation. This is useful when you are
recording many instances of the same process, and want to minimize recording startup time.

### Changed

- Choose default injection mode at runtime based on which tracer is used (1.11.156)
- Add switch to enable timestamp-based .run file generation (1.11.155)
- Add EULA and -accepteula to TTD (1.11.154)
- Add ProcLaunchMon.sys to MSIX (1.11.153)
- Create per-arch MSIX and MSIXBUNDLE (1.11.152)
- Fix a number of issues that came up when testing TTD built with Clang. (1.11.146)
- Clang fixes for TTDAnalyze (1.11.144)

### Fixed

- Review feedback on appinstaller / public release (1.11.159)
- RC feedback (1.11.157)
- Avoid trashing the Zero register by initializing RegisterInfo to point to Sink. (1.11.149)
- Fix TST instruction with immediate and enhance the unit test to cover it and more. (1.11.148)
- Consolidate protected process decision and disable protected process use (1.11.147)

## 1.11.138

### Changed

- Create recorder MSIX (1.11.138)
- Fix all issues so Clang can build TTD. (1.11.137)
- Introduce -monitor X as way to record a process when it launches (1.11.116)

### Fixed

- Fix "CMP ZR" ARM64 emulation (1.11.128)
- Fix AVX512 emulation on AMD's Zen4 processors (1.11.127)
- Fix the mechanism TTD uses to find files for a specific CPU (1.11.121)
- Fix x86 TTD regression (TTDRecordCPU.dll fails to load) (1.11.110)
- Fix the return to native path on ARM64 to not trash X28 (1.11.109)

## See Also

[Time Travel Debugging – Overview](time-travel-debugging-overview.md)

[Time Travel Debugging – Command line recorder](time-travel-debugging-ttd-exe-command-line-util.md)
