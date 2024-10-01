---
title: "Time travel debugging release notes"
description: "This topic provides information on what's new in Time Travel Debugging."
keywords: ["release notes", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 02/12/2024
---

# Time travel debugging release notes

:::image type="content" source="images/ttd-time-travel-debugging-logo.png" alt-text="Time travel debugging logo featuring a clock.":::

This topic provides information on what's new in Time Travel Debugging.

## 1.11.429

This update of TTD contains a few bug fixes along with some internal changes to improve reliability.

Note: 1.11.410 introduced a regression in the emulation of the Intel/AMD LODSD instruction. A fix for this will come in the next release.

Fixes:
- Improve packet reading robustness and other misc changes to improve reliability.
- Fix a regression in emulating the AVX VBROADCAST[I/F]128 instruction.
- Fix the exception record access on ARM64 in newer builds of Windows.

## 1.11.410

Improved accessibility: Progress UI now properly scales with Text Size changes.

The ```@$cursession.TTD.Calls()``` command in the debugger now supports wildcards that match a large number of functions.
It is now possible to query for large numbers of functions (i.e. ```@$cursession.TTD.Calls("kernel32!*")```).

Automation: A new ```-onMonitorReadyEvent``` command-line option indicates when the recording monitor (```-monitor``` switch)
is ready to record new processes.

Fixes:
- Fix some race conditions while initializing the recorder.
- Fix how we record syscalls so that breakpoints work correctly.
- Fix multiple issues related to module selective recording.

ARM64 fixes:
- Fixed a bug preventing TTD recording on plain ARM64v8.0 level CPUs.
- Improved the messaging when attempting to use on ARM64 a trace of an x86 or x64 process.

AMD/Intel fixes (includes some issues reported by Google):
- Fixed incorrect emulation of LODS: Instead of zeroing out the unused bits of RAX they are now correctly preserved.
- Fixed emulation of "pop ax" instruction in x86/x64 processes, which was incorrectly zeroing the upper bits
  of the full register (e.g. "pop ax" cleared the upper bits of rax).
- Direct emulation of the XGETBV instruction (faster).
- Direct emulation of all AVX512 SIMD moves (faster).

## 1.11.316

Fixed a regression that was causing occasional crashes when recording programs with long uninterrupted data-heavy instruction sequences.

ARM64 fixes:
- Recording in ARM64 processes that have the PAC feature enabled is now supported.
- Fixed the ANDS and TST instructions, which were failing to clear the carry and overflow flags.

AMD/Intel fixes:
- Fixed bug where TTD incorrectly emulated "xchg r8,rax" and "xchg r8w,ax" as NOP.

## 1.11.304

TTD now implements and publishes publicly an API to control the recorder from within the live recorded process. Documentation and a sample can be found in [GitHub](https://github.com/microsoft/WinDbg-Samples/tree/HEAD/TTD).

TTD can now inject itself with recording turned off using the new `-recordMode` switch. By default TTD uses `-recordMode Automatic` which causes all threads to be recorded. If `-recordMode Manual` is specified then TTD injects into the target process but does not record anything until told to do so through an API call.

Recording can now be restricted to a specific set of modules using the `-module` switch. In some scenarios this can result in substantially faster recording and smaller trace files. More than one `-module` switch may be specified.

Matching record and replay components are now included in the distribution. In the event of an incompatibility between the debugger and the command line recorder, or a replay bug, the replay components can be copied into the debugger install as a workaround until a new debugger is released.

The installed file location can be found in Powershell by doing the following:

```
ls (Get-AppxPackage | where Name -eq 'Microsoft.TimeTravelDebugging').InstallLocation
```

### Added

- Add -recordmode switch to enable injection without automatic recording (1.11.296)
- Add -module switch and use to create SR config (1.11.291)
- Project custom data recorded by the in-process API to data model (1.11.286)
- Add a new TTDLiveRecorder.dll and wire it up along with TTDRecordCPU.dll (1.11.283)
- Add replay components to MSIX & fix SDK lookup (1.11.265)

### Changed

none

### Fixed

- Work around [a bug](https://github.com/nlohmann/json/issues/4236) in the nlohmann JSON serializer, which is used in some internal tooling (1.11.281)
  - Contributed [a fix](https://github.com/nlohmann/json/pull/4237) to that library that will become available in [a future release](https://github.com/nlohmann/json/milestone/49?closed=1).
- Adjust string alignment to avoid a rare CRT bug (1.11.279)
  - Reported to and fixed in the VS and OS codebases.
- Several small fixes from Watson crash reports (1.11.276)
- Fix a regression that may cause trace file corruption in some cases (1.11.264)

### Known issues

- On ARM64, the compiler is failing to tail-call a number of high-frequency functions which in extreme cases can cause the recorder to run out of stack space and crash.

## 1.11.261

Notable changes in this release include:
- [ARM64] Fixed the behavior of the `SXTL`, `SQXTN2`, `SQXTUN2`, `UQXTN2`, `XTN2` and `TRN1` instructions when the destination register is used as a source.
- [ARM64] Fixed an issue that caused the debugger to show SIMD registers with their lower 64 bits duplicated into the high 64 bits.
- [AMD64] AVX512 emulation fixes for AMD's Zen4 processors (registers were getting corrupted).

### Changed

- Implement a new versioning system specifically for the emulator. (1.11.260)

### Fixed

- Fix faulty ARM64 instructions where the destination register is also used as a source. (1.11.261)
- Fix the Zen4 workaround for direct returns to the emulator. (1.11.222)

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

The new ```-timestampFileName``` switch enables timestamp-based .run file generation. This is useful when you are
recording many instances of the same process, and want to minimize recording startup time.

### Changed

- Choose default injection mode at runtime based on which tracer is used (1.11.156)
- Add switch to enable timestamp-based .run file generation (1.11.155)
- Add EULA and ```-accepteula``` to TTD (1.11.154)
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

