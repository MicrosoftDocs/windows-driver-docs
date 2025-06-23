---
title: "Time travel debugging release notes"
description: "This topic provides information on what's new in Time Travel Debugging."
keywords: ["release notes", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 06/23/2024
ms.topic: release-notes
---

# Time travel debugging release notes

:::image type="content" source="images/ttd-time-travel-debugging-logo.png" alt-text="Time travel debugging logo featuring a clock.":::

This topic provides information on what's new in Time Travel Debugging.

## 1.11.532

This is a maintenance release that makes some improvements to recording robustness and coincides with the June 2025 release of Windbg. One customer-facing feature is the Position data model object now reports percentage into the trace.

### Changed

- Miscellaneous infrastructure maintenance.
- Use the ISO standard implementation of C++ volatile. (1.11.518)
- Add Percent to Position data model projection. (1.11.514)

### Fixed

- Increase the robustness of TTD's handling of decoded instructions. (1.11.530)
- Remove uses of XSAVE in the emulator and optimize internal register transfer. (1.11.509)

## 1.11.506

This is a minor release to coincide with the April 2025 release of WinDbg.

### Changed

- Clicking on a TTD position in the data model (i.e. in the Modules list) navigates to that position in the trace. (1.11.492)

  Note: The command window will not show the updated TTD position until the next step or run command is executed.

### Fixed

- Add process name to .out file when attaching to a PID to aid troubleshooting. (1.11.486)

## 1.11.481

We have revamped the !tt command to give you more powerful ways to navigate through your trace:
- Fractional percentages can be used to narrow down the search space (!tt 23.65)
- Find the previous/next time a register changes value (!tt br ebx)
- Find the previous/next time a memory range is accessed (!tt ba- [addr] [range])
- Find the previous/next time execution moves to a different module (!tt bm)
- Find the previous/next time execution moves to a specific module (!tt bm ntdll)

For more details see the [documentation](time-travel-debugging-extension-tt.md).

Some notable fixes:
- "Error: 64 bit value loses precision on conversion to number" messages when using `@$cursession.TTD.Data.Heap()` on 32-bit trace are gone.
- Help option parsing (`-?`, `-help`) is now correctly detected anywhere in the command line.
- `dx @$cursession.TTD.Calls()` no longer requires addresses to match the start of a function. Instead, the address will be mapped to the start of the closest matching function.
- TTD correctly reports target OS version from vertarget command.
- Using "-monitor" with a hosted service name no longer records unrelated hosted services.

### Added

- Register change breakpoints in TTD traces (1.11.431)

### Changed

- Fix recording of services by name using monitor mode (1.11.477)
- Capture actual target system's OS information for use by debugger (1.11.473)
- Fix the transfer of XMM registers between the emulator and CONTEXT (1.11.469)
- Allow call queries against addresses inside a function (1.11.459)
- Support symbols as addresses/sizes in !tt command line (1.11.454)
- Improve the consistency and extend the capabilities of TTD navigation commands (1.11.453)
- Improve module DB consistency in the face of corrupted data (1.11.430)

### Fixed

- Add process name to output when attaching to PID (1.11.486)
- TTD.Data.Heap() reports "Error: 64 bit value loses precision on conversion to number" in some cases (1.11.471)
- Improve the reliability of recording a process with shadow stacks enabled (1.11.466)
- Add module navigation via !tt bm and data model (1.11.462)
- Fix Some issues with command-line parsing. (1.11.444)
- Fix lodsd, load doubleword at address (zero out upper part of rax) (1.11.434)
- Fix some libfuzzer bugs (1.11.433)

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
It is now possible to query for large numbers of functions (```@$cursession.TTD.Calls("kernel32!*")```).

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

TTD can now inject itself with recording turned off using the new `-recordMode` switch. By default TTD uses `-recordMode Automatic` which causes all threads to be recorded. If `-recordMode Manual` is specified then TTD injects into the target process but doesn't record anything until told to do so through an API call.

Recording can now be restricted to a specific set of modules using the `-module` switch. In some scenarios this can result in substantially faster recording and smaller trace files. More than one `-module` switch may be specified.

Matching record and replay components are now included in the distribution. In the event of an incompatibility between the debugger and the command line recorder, or a replay bug, the replay components can be copied into the debugger install as a workaround until a new debugger is released.

The installed file location can be found in PowerShell by doing the following:

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

