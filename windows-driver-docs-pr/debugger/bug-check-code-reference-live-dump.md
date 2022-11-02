---
title: Kernel Live Dump Code Reference
description: This section contains descriptions of the common kernel live dumps, and describes how they are different from traditional bug checks.
ms.date: 11/01/2022
---

# Kernel Live Dump Code Reference

This section contains descriptions of common kernel live dump codes that may occur. Live dumps do not reset the OS, but allow for the capture of memory information for abnormal situations where the operating system can continue.

> [!NOTE]
> This topic is for programmers. If you are a customer whose system has displayed a blue screen with a bug check code, see [Troubleshoot blue screen errors](https://support.microsoft.com/help/14238/windows-10-troubleshoot-blue-screen-errors).

## Kernel live dump compared to bug check

With a traditional bug check, the PC resets and the user's work is disrupted. The goal of kernel live dump is to gather data to trouble shoot an abnormal situation, but allow the OS to continue operation. This reduces downtime when compared to a bug check for “non-fatal” but high-impact failures and hangs. Kernel live dumps are used when it is possible to recover the OS to a known good state. For example a hardware reset of a subsystem, such as video/display, USB3 or Wi-Fi can allow those systems to return to a known good state, with minimal user impact.

A kernel live dump creates a consistent snapshot of kernel memory and saves it to a dump file for the future analysis. To minimize impact on the performance, memory copy techniques are used to create the dump file in a short period of time. In addition, the collection of live dumps is throttled, so that user impact is minimized.

A kernel live dump is effective for a category of problems where something is taking a long time, and yet nothing is technically failing. A watchdog timer can be initialized when an operation is started. If the watchdog expires before operation completes with in the expected time, a live dump of the system can be taken. Then the dump can be analyzed by traversing the call stack and related wait chain for that operation to investigate why it is not completing with the expected time frame.

System logs work well when something fails and the code owner has recorded the cause of the failure and can identify the cause. Live dumps that use watchdog timers attempt to catch failure paths that were not anticipated and logged. But as with every failure, the system logs may identify other issues that may provide clues to the specific root cause of the failure.

## Kernel live dump file contents

Similar to regular dump files, live dump files may contain minidumps (with secondary data), and full kernel dumps, which may also include user mode memory, similar to active dumps. For general information about dump file contents, see [Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md). Some live dumps only attempt to capture minidumps, as they are designed to capture specific hardware-related data, while others may attempt to capture a larger kernel live dump.

For performance, file size and for the reliability of dump captures, some information is not included, such as pages from the stand by list and file caches.

Live dump files typically contain memory pages such as:

- KdDebuggerBlock
- Loaded Module List

For each processor the following information is captured in kernel dumps:

- KiProcessorBlock
- PRCBs
- Current stack
- Current page directory table
- KI_USER_SHARED_DATA
- NTOS Kernel Image
- HAL Image

Additional information in kernel dumps may include:

- Thread / memory state
- In-memory logging

Some live dumps may contain user-mode process pages.

Additional domain specific data, for example USB specific data for USB failures, may be included for some live dumps.

## Partial kernel live dump file

A partial kernel live dump file may be generated in situations when live dump cannot reliably capture all intended memory pages. The information that is captured in a partial dump is filtered and prioritized, by capturing pages that contain important data required to generate a valid dump before other pages. For instance, the kernel pages are prioritized over user pages, when the live dump includes user pages.  In some situations there are not enough resources available to capture all intended optional memory pages, so memory may be missing from the dump file. The dump file should still be recognized by the WinDbg debugger but may show errors when trying to dump memory.  If the debugger shows an error when attempting to dump memory at an address, you can use the [!pte](-pte.md) extension to check whether the PTE for an address is valid or not. This can help to determine if the memory address is really invalid, or if the page is valid but just not available in the dump file.

## Analyzing live dump files

When a live dump occurs, the dump file can be analyzed using the same techniques used for other memory dump files. To understand the contents of memory during a failure, knowledge of processor memory registers and assembly programming is required.

For more information, see:

- [Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

- [!analyze](-analyze.md)

- [Processor Architecture](processor-architecture.md)

## Using WinDbg to display live dump stop code information

If a specific live dump code does not appear in this topic, use the [**!analyze**](-analyze.md) extension in the Windows Debugger (WinDbg) with the following syntax (in kernel mode), replacing `<code>` with a live dump code:

`!analyze -show <code>`

Entering this command causes WinDbg to display information about the specified live dump code. If your default number base (radix) is not 16, prefix `<code>` with **0x**.

Provide the live dump code parameters to the !analyze command to display any available parameter information. For example, to display information on [Bug Check 0x144 BUGCODE_USB3_DRIVER](bug-check-0x144--bugcode-usb3-driver.md), with a parameter 1 value of 0x3003, use `!analyze -show 0x144 0x3003` as shown here.  

```dbgcmd
0: kd> !analyze -show 0x144 0x3003
BUGCODE_USB3_DRIVER (144)
This bugcheck usually happens when the USB3 core stack detects an invalid
operation being performed by a USB client. This bugcheck may also occur
due to hardware failure on a USB Boot Device.
Arguments:
Arg1: 0000000000003003, USB3_WER_BUGCODE_USBHUB3_DEVICE_ENUMERATION_FAILURE
	A USB device failed enumeration.
Arg2: 0000000000000000, USBHUB3_LIVEDUMP_CONTEXT
Arg3: 0000000000000000, 0
Arg4: 0000000000000000, 0
```

To download WinDbg, see [Download Debugging Tools for Windows](debugger-download-tools.md). To learn more about the WinDbg development tools, see [Getting Started with Windows Debugging](getting-started-with-windows-debugging.md).

## Live dump file locations

The live dumps by default are stored in the 'C:\WINDOWS\LiveKernelReports' directory.

Full dumps:  `%systemroot%\LiveKernelReports\*.dmp`

Minidumps: `%systemroot%\LiveKernelReports\<ComponentName>\*.dmp`

A directory structure is used to store live dumps for different components.

```dos
NDIS
PDCRevocation
PoW32kWatchdog
USBHUB3
WATCHDOG
```

## Live dump registry keys

For more information on configuration options for system-generated live kernel reports, see [WER Settings](/windows/win32/wer/wer-settings#crashcontrolfulllivekernelreports-subkey).

## Use PowerShell to manually trigger a live dump

1. Open and Administrator PowerShell prompt.

2. Get the StorageSubsystem friendly name by using [Get-StorageSubSystem](/powershell/module/storage/get-storagesubsystem) PowerShell command.

```powershell
 C:\> Get-StorageSubSystem
 FriendlyName                     HealthStatus OperationalStatus
 ------------                     ------------ -----------------
 Windows Storage on 10-2411-PC    Healthy      OK
```

3. Use Get-StorageDiagnosticInfo to generate a live dump for the above subsystem (along with other diagnostic logs). For more information see [Get-StorageDiagnosticInfo](/powershell/module/storage/get-storagediagnosticinfo).

```powershell
 C:\> Get-StorageDiagnosticInfo -StorageSubSystemFriendlyName "Windows Storage on 10-2411-PC" -IncludeLiveDump -DestinationPath C:\destinationfolder
```

4. The output will indicate that the requested information is being generated.

```powershell
Gathering storage subsystem diagnostic information                                                                         
Running                                                                                                                 
[oooooooooooo                                                                                              ] 
```

5. The dump will be inside `[DestinationPath]\localhost`.

```powershell
 C:\> dir C:\destinationfolder\localhost\*.dmp
   Directory: C:\destinationfolder\localhost
 Mode                LastWriteTime         Length Name
 ----                -------------         ------ ----
 -a----         5/5/2016   1:08 PM      867135488 LiveDump.dmp
```

6. Using the debugger to run [!analyze](-analyze.md) on the dump file will indicate that this is a live dump code of [LIVE_SYSTEM_DUMP (161)](bug-check-0x161--live-system-dump.md).

## Kernel live dump codes

The following table provides links to kernel live dumps codes.

| Code       | Name                                                                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x000000AB | [**SESSION\_HAS\_VALID\_POOL\_ON\_EXIT**](bug-check-0xab--session-has-valid-pool-on-exit.md)                                                      |
| 0x00000117 | [**VIDEO\_TDR\_TIMEOUT\_DETECTED**](bug-check-0x117---video-tdr-timeout-detected.md)                                                              |
| 0x00000141 | [**VIDEO\_ENGINE\_TIMEOUT\_DETECTED**](bug-check-0x141---video-engine-timeout-detected.md)                                                        |
| 0x00000142 | [**VIDEO\_TDR\_APPLICATION\_BLOCKED**](bug-check-0x142--video-tdr-application-blocked.md)                                                         |
| 0x00000156 | [**WINSOCK\_DETECTED\_HUNG\_CLOSESOCKET\_LIVEDUMP**](bug-check-0x156--winsock-detected-hung-closesocket-livedump.md)                              |
| 0x0000015C | [**PDC\_WATCHDOG\_TIMEOUT\_LIVEDUMP**](bug-check-0x15c--pdc-watchdog-timeout-livedump.md)                                                         |  
| 0x0000015D | [**SOC\_SUBSYSTEM\_FAILURE\_LIVEDUMP**](bug-check-0x15d-soc-subsystem-failure-livedump.md)                                                        |
| 0x0000015E | [**BUGCODE\_NDIS\_DRIVER\_LIVE\_DUMP**](bug-check-0x15e-bugcode-ndis-driver-live-dump.md)                                                         |
| 0x0000015F | [**CONNECTED\_STANDBY\_WATCHDOG\_TIMEOUT\_LIVEDUMP**](bug-check-0x15f--connected-standby-watchdog-timeout-livedump.md)                            |
| 0x00000161 | [**LIVE\_SYSTEM\_DUMP**](bug-check-0x161--live-system-dump.md)                                                                                    |
| 0x00000165 | [**CLUSTER\_CSV\_STATUS\_IO\_TIMEOUT\_LIVEDUMP**](bug-check-0x165--cluster-csv-staus-io-timeout-livedump.md)                                      |
| 0x00000166 | [**CLUSTER\_RESOURCE\_CALL\_TIMEOUT\_LIVEDUMP**](bug-check-0x166--cluster-resource-call-timeout-livedump.md)                                      |
| 0x00000167 | [**CLUSTER\_CSV\_SNAPSHOT\_DEVICE\_INFO\_TIMEOUT\_LIVEDUMP**](bug-check-0x167--cluster-csv-snapshot-device-info-timeout-livedump.md)              |
| 0x00000168 | [**CLUSTER\_CSV\_STATE\_TRANSITION\_TIMEOUT\_LIVEDUMP**](bug-check-0x168--cluster-csv-state-transition-timeout-livedump.md)                       |   
| 0x00000169 | [**CLUSTER\_CSV\_VOLUME\_ARRIVAL\_LIVEDUMP**](bug-check-0x169--cluster-csv-volume-arival-livedump.md)                                             |      
| 0x0000016A | [**CLUSTER\_CSV\_VOLUME\_REMOVAL\_LIVEDUMP**](bug-check-0x16a--cluster-csv-volume-removal-livedump.md)                                            |    
| 0x0000016B | [**CLUSTER\_CSV\_CLUSTER\_WATCHDOG\_LIVEDUMP**](bug-check-0x16b--cluster-csv-cluster-watchdog-livedump.md)                                        |   
| 0x0000016F | [**CLUSTER\_CSV\_STATE\_TRANSITION\_INTERVAL\_TIMEOUT\_LIVEDUMP**](bug-check-0x16f--cluster-csv-state-transistion-interval-livedump.md)           |
| 0x00000175 | [**PREVIOUS\_FATAL\_ABNORMAL\_RESET\_ERROR**](bug-check-0x175--previous-fatal-abnormal-reset-error.md)                                            |
| 0x00000179 | [**CLUSTER\_CLUSPORT\_STATUS\_IO\_TIMEOUT\_LIVEDUMP**](bug-check-0x179--cluster-clusport-status-io-timeout-livedump.md)                           |
| 0x0000017C | [**PDC\_LOCK\_WATCHDOG\_LIVEDUMP**](bug-check-0x17c--pdc-lock-watchdog-livedump.md)                                                               | 
| 0x0000017D | [**PDC\_UNEXPECTED\_REVOCATION\_LIVEDUMP**](bug-check-0x17d-unexpected-revocation-livedump.md)                                                    | 
| 0x00000187 | [**VIDEO\_DWMINIT\_TIMEOUT\_FALLBACK\_BDD**](bug-check-0x187--video-dwminit-timeout-fallback-bdd.md)                                              |
| 0x00000188 | [**CLUSTER\_CSVFS\_LIVEDUMP**](bug-check-0x188--cluster-csvfs-livedump.md)                                                                        |
| 0x00000190 | [**WIN32K\_CRITICAL\_FAILURE\_LIVEDUMP**](bug-check-0x190--win32k-critical-failure-livedump.md)                                                   |
| 0x00000193 | [**VIDEO\_DXGKRNL\_LIVEDUMP**](bug-check-0x192--video-dxgkrnl-livedump.md)                                                                        |
| 0x00000195 | [**SMB\_SERVER\_LIVEDUMP**](bug-check-0x195--smb-server-livedump.md)                                                                              |
| 0x00000198 | [**UFX\_LIVEDUMP**](bug-check-0x198--ufx-livedump.md)                                                                                             |
| 0x0000019D | [**CLUSTER\_SVHDX\_LIVEDUMP**](bug-check-0x19d--cluster-svhdx-livedump.md)                                                                        |
| 0x000001A1 | [**WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP**](bug-check-0x1a1--win32k-callout-watchdog-livedump.md)                                                   |
| 0x000001A3 | [**CALL\_HAS\_NOT\_RETURNED\_WATCHDOG\_TIMEOUT\_LIVEDUMP**](bug-check-0x1a3--call-has-not-returned-watchdog-timeout-livedump.md)                  |
| 0x000001A4 | [**DRIPS\_SW\_HW\_DIVERGENCE\_LIVEDUMP**](bug-check-0x1a4--drips-sw-hw-divergence-livedump.md)                                                    |
| 0x000001A5 | [**USB\_DRIPS\_BLOCKER\_SURPRISE\_REMOVAL\_LIVEDUMP**](bug-check-0x1a5--usb-drips-blocker-surprise-removal-livedump.md)                           |
| 0x000001A6 | [**BLUETOOTH\_ERROR\_RECOVERY\_LIVEDUMP**](bug-check-0x1a6--bluetooth-error-recovery-livedump.md)                                                 |
| 0x000001A7 | [**SMB\_REDIRECTOR\_LIVEDUMP**](bug-check-0x1A7--smb-redirector-livedump.md)                                                                      |
| 0x000001A8 | [**VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP**](bug-check-0x1a8--video-dxgkrnl-black-screen-livedump.md)                                            |
| 0x000001A9 | [**DIRECTED\_FX\_TRANSITION\_LIVEDUMP**](bug-check-0x1a9--directed-fx-transition-livedump.md)                                                     |
| 0x000001B0 | [**VIDEO_MINIPORT_FAILED_LIVEDUMP**](bug-check-0x1b0--video-miniport-failed-livedump.md)                                                          |
| 0x000001B8 | [**VIDEO_MINIPORT_BLACK_SCREEN_LIVEDUMP**](bug-check-0x1b8--video-miniport-black-screen-livedump.md)                                              |
| 0x000001C4 | [**DRIVER\_VERIFIER\_DETECTED\_VIOLATION\_LIVEDUMP**](bug-check-0x1c4--driver-verifier-detected-violation-livedump.md)                            |
| 0x000001C5 | [**IO\_THREADPOOL\_DEADLOCK\_LIVEDUMP**](bug-check-0x1c5--io-threadpool-deadlock-livedump.md)                                                     |
| 0x000001C9 | [**USER\_MODE\_HEALTH\_MONITOR\_LIVEDUMP**](bug-check-0x1c9--user-mode-health-monitor-livedump.md)                                                |
| 0x000001CC | [**EXRESOURCE_TIMEOUT_LIVEDUMP**](bug-check-0x1cc--exresource-timeout-livedump.md)                                                                |
| 0x000001D1 | [**TELEMETRY\_ASSERTS\_LIVEDUMP**](bug-check-0x1d1--telemetry-asserts-livedump.md)                                                                |
| 0x000001D4 | [**UCMUCSI\_LIVEDUMP**](bug-check-0x1d4--ucmusci-livedump.md)                                                                                     |
| 0x000001E1 | [**DEVICE\_DIAGNOSTIC\_LOG\_LIVEDUMP**](bug-check-0x1e1--device-diagnostic-log-livedump.md)                                                       |
| 0x000001F5 | [**APPLICATION\_HANG\_KERNEL\_LIVEDUMP**](bug-check-0x1f5--application-hang-kernel-livedump.md)                                                   |
| 0x000021C8 | [**MANUALLY\_INITIATED\_BLACKSCREEN\_HOTKEY\_LIVE\_DUMP**](bug-check-0x21c8--manually-initiated-blackscreen-hotkey-live-dump.md)                  |        

These stop codes can be used for live dumps or to bug check the device.

| Code       | Name                                                                            |
|------------|---------------------------------------------------------------------------------|
| 0x00000124 | [**WHEA\_UNCORRECTABLE\_ERROR**](bug-check-0x124---whea-uncorrectable-error.md) |
| 0x00000144 | [**BUGCODE\_USB3\_DRIVER**](bug-check-0x144--bugcode-usb3-driver.md)            |
| 0x00000164 | [**WIN32K\_CRITICAL\_FAILURE**](bug-check-0x164--win32k-critical-failure.md)    |
