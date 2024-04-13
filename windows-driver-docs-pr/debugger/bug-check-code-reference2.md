---
title: Bug Check Code Reference
description: This section contains descriptions of the common bug checks, including the parameters passed to the blue screen.
ms.date: 10/28/2022
---

# Bug Check Code Reference

This section contains descriptions of common bug check codes that are displayed on the blue bug check screen. This section also describes how you can use the [**!analyze**](../debuggercmds/-analyze.md) extension in the Windows Debugger to display information about a bug check code.

> [!NOTE]
> This topic is for programmers. If you are a customer whose system has displayed a blue screen with a bug check code, see [Troubleshoot blue screen errors](https://support.microsoft.com/help/14238/windows-10-troubleshoot-blue-screen-errors).

## Using WinDbg to display stop code information

If a specific bug check code does not appear in this topic, use the [**!analyze**](../debuggercmds/-analyze.md) extension in the Windows Debugger (WinDbg) with the following syntax (in kernel mode), replacing `<code>` with a bug check code:

`!analyze -show <code>`

Entering this command causes WinDbg to display information about the specified bug check code. If your default number base (radix) is not 16, prefix `<code>` with **0x**.

Provide the stop code parameters to the !analyze command to display any available parameter information. For example, to display information on [Bug Check 0x9F: DRIVER_POWER_STATE_FAILURE](bug-check-0x9f--driver-power-state-failure.md), with a parameter 1 value of 0x3, use `!analyze -show 0x9F 0x3` as shown here.  

```dbgcmd
1: kd> !analyze -show 0x9F 0x3
DRIVER_POWER_STATE_FAILURE (9f)
A driver has failed to complete a power IRP within a specific time.
Arguments:
Arg1: 0000000000000003, A device object has been blocking an Irp for too long a time
Arg2: 0000000000000000, Physical Device Object of the stack
Arg3: 0000000000000000, nt!_TRIAGE_9F_POWER on Win7 and higher, otherwise the Functional Device Object of the stack
Arg4: 0000000000000000, The blocked IRP
```

To download WinDbg, see [Debugging Tools for Windows](debugger-download-tools.md). To learn more about the WinDbg development tools, see [Getting Started with Windows Debugging](getting-started-with-windows-debugging.md).

## Bug check dump files

When a bug check occurs, a dump file may be available that contains additional information about the contents of memory when the stop code occurred. To understand the contents of memory during a failure, knowledge of processor memory registers and assembly is required.

For more information, see:

- [Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

- [!analyze](../debuggercmds/-analyze.md)

- [Processor Architecture](processor-architecture.md)

## Live Dumps

 Live Dump stop codes to not reset the OS, but allow for the capture of memory information for abnormal situations where the operating system can continue. For information about live dumps, see [Bug Check Code Reference - Live Dump](bug-check-code-reference-live-dump.md).

## Bug Check Codes

The following table provides links to bug check codes.

| Code       | Name                                                                                                                                              |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000001 | [**APC\_INDEX\_MISMATCH**](bug-check-0x1--apc-index-mismatch.md)                                                                                  |
| 0x00000002 | [**DEVICE\_QUEUE\_NOT\_BUSY**](bug-check-0x2--device-queue-not-busy.md)                                                                           |
| 0x00000003 | [**INVALID\_AFFINITY\_SET**](bug-check-0x3--invalid-affinity-set.md)                                                                              |
| 0x00000004 | [**INVALID\_DATA\_ACCESS\_TRAP**](bug-check-0x4--invalid-data-access-trap.md)                                                                     |
| 0x00000005 | [**INVALID\_PROCESS\_ATTACH\_ATTEMPT**](bug-check-0x5--invalid-process-attach-attempt.md)                                                         |
| 0x00000006 | [**INVALID\_PROCESS\_DETACH\_ATTEMPT**](bug-check-0x6--invalid-process-detach-attempt.md)                                                         |
| 0x00000007 | [**INVALID\_SOFTWARE\_INTERRUPT**](bug-check-0x7--invalid-software-interrupt.md)                                                                  |
| 0x00000008 | [**IRQL\_NOT\_DISPATCH\_LEVEL**](bug-check-0x8--irql-not-dispatch-level.md)                                                                       |
| 0x00000009 | [**IRQL\_NOT\_GREATER\_OR\_EQUAL**](bug-check-0x9--irql-not-greater-or-equal.md)                                                                  |
| 0x0000000A | [**IRQL\_NOT\_LESS\_OR\_EQUAL**](bug-check-0xa--irql-not-less-or-equal.md)                                                                        |
| 0x0000000B | [**NO\_EXCEPTION\_HANDLING\_SUPPORT**](bug-check-0xb--no-exception-handling-support.md)                                                           |
| 0x0000000C | [**MAXIMUM\_WAIT\_OBJECTS\_EXCEEDED**](bug-check-0xc--maximum-wait-objects-exceeded.md)                                                           |
| 0x0000000D | [**MUTEX\_LEVEL\_NUMBER\_VIOLATION**](bug-check-0xd--mutex-level-number-violation.md)                                                             |
| 0x0000000E | [**NO\_USER\_MODE\_CONTEXT**](bug-check-0xe--no-user-mode-context.md)                                                                             |
| 0x0000000F | [**SPIN\_LOCK\_ALREADY\_OWNED**](bug-check-0xf--spin-lock-already-owned.md)                                                                       |
| 0x00000010 | [**SPIN\_LOCK\_NOT\_OWNED**](bug-check-0x10--spin-lock-not-owned.md)                                                                              |
| 0x00000011 | [**THREAD\_NOT\_MUTEX\_OWNER**](bug-check-0x11--thread-not-mutex-owner.md)                                                                        |
| 0x00000012 | [**TRAP\_CAUSE\_UNKNOWN**](bug-check-0x12--trap-cause-unknown.md)                                                                                 |
| 0x00000013 | [**EMPTY\_THREAD\_REAPER\_LIST**](bug-check-0x13--empty-thread-reaper-list.md)                                                                    |
| 0x00000014 | [**CREATE\_DELETE\_LOCK\_NOT\_LOCKED**](bug-check-0x14--create-delete-lock-not-locked.md)                                                         |
| 0x00000015 | [**LAST\_CHANCE\_CALLED\_FROM\_KMODE**](bug-check-0x15--last-chance-called-from-kmode.md)                                                         |
| 0x00000016 | [**CID\_HANDLE\_CREATION**](bug-check-0x16--cid-handle-creation.md)                                                                               |
| 0x00000017 | [**CID\_HANDLE\_DELETION**](bug-check-0x17--cid-handle-deletion.md)                                                                               |
| 0x00000018 | [**REFERENCE\_BY\_POINTER**](bug-check-0x18--reference-by-pointer.md)                                                                             |
| 0x00000019 | [**BAD\_POOL\_HEADER**](bug-check-0x19--bad-pool-header.md)                                                                                       |
| 0x0000001A | [**MEMORY\_MANAGEMENT**](bug-check-0x1a--memory-management.md)                                                                                    |
| 0x0000001B | [**PFN\_SHARE\_COUNT**](bug-check-0x1b--pfn-share-count.md)                                                                                       |
| 0x0000001C | [**PFN\_REFERENCE\_COUNT**](bug-check-0x1c--pfn-reference-count.md)                                                                               |
| 0x0000001D | [**NO\_SPIN\_LOCK\_AVAILABLE**](bug-check-0x1d--no-spin-lock-available.md)                                                                        |
| 0x0000001E | [**KMODE\_EXCEPTION\_NOT\_HANDLED**](bug-check-0x1e--kmode-exception-not-handled.md)                                                              |
| 0x0000001F | [**SHARED\_RESOURCE\_CONV\_ERROR**](bug-check-0x1f--shared-resource-conv-error.md)                                                                |
| 0x00000020 | [**KERNEL\_APC\_PENDING\_DURING\_EXIT**](bug-check-0x20--kernel-apc-pending-during-exit.md)                                                       |
| 0x00000021 | [**QUOTA\_UNDERFLOW**](bug-check-0x21--quota-underflow.md)                                                                                        |
| 0x00000022 | [**FILE\_SYSTEM**](bug-check-0x22--file-system.md)                                                                                                |
| 0x00000023 | [**FAT\_FILE\_SYSTEM**](bug-check-0x23--fat-file-system.md)                                                                                       |
| 0x00000024 | [**NTFS\_FILE\_SYSTEM**](bug-check-0x24--ntfs-file-system.md)                                                                                     |
| 0x00000025 | [**NPFS\_FILE\_SYSTEM**](bug-check-0x25--npfs-file-system.md)                                                                                     |
| 0x00000026 | [**CDFS\_FILE\_SYSTEM**](bug-check-0x26--cdfs-file-system.md)                                                                                     |
| 0x00000027 | [**RDR\_FILE\_SYSTEM**](bug-check-0x27--rdr-file-system.md)                                                                                       |
| 0x00000028 | [**CORRUPT\_ACCESS\_TOKEN**](bug-check-0x28--corrupt-access-token.md)                                                                             |
| 0x00000029 | [**SECURITY\_SYSTEM**](bug-check-0x29--security-system.md)                                                                                        |
| 0x0000002A | [**INCONSISTENT\_IRP**](bug-check-0x2a--inconsistent-irp.md)                                                                                      |
| 0x0000002B | [**PANIC\_STACK\_SWITCH**](bug-check-0x2b--panic-stack-switch.md)                                                                                 |
| 0x0000002C | [**PORT\_DRIVER\_INTERNAL**](bug-check-0x2c--port-driver-internal.md)                                                                             |
| 0x0000002D | [**SCSI\_DISK\_DRIVER\_INTERNAL**](bug-check-0x2d--scsi-disk-driver-internal.md)                                                                  |
| 0x0000002E | [**DATA\_BUS\_ERROR**](bug-check-0x2e--data-bus-error.md)                                                                                         |
| 0x0000002F | [**INSTRUCTION\_BUS\_ERROR**](bug-check-0x2f--instruction-bus-error.md)                                                                           |
| 0x00000030 | [**SET\_OF\_INVALID\_CONTEXT**](bug-check-0x30--set-of-invalid-context.md)                                                                        |
| 0x00000031 | [**PHASE0\_INITIALIZATION\_FAILED**](bug-check-0x31--phase0-initialization-failed.md)                                                             |
| 0x00000032 | [**PHASE1\_INITIALIZATION\_FAILED**](bug-check-0x32--phase1-initialization-failed.md)                                                             |
| 0x00000033 | [**UNEXPECTED\_INITIALIZATION\_CALL**](bug-check-0x33--unexpected-initialization-call.md)                                                         |
| 0x00000034 | [**CACHE\_MANAGER**](bug-check-0x34--cache-manager.md)                                                                                            |
| 0x00000035 | [**NO\_MORE\_IRP\_STACK\_LOCATIONS**](bug-check-0x35--no-more-irp-stack-locations.md)                                                             |
| 0x00000036 | [**DEVICE\_REFERENCE\_COUNT\_NOT\_ZERO**](bug-check-0x36--device-reference-count-not-zero.md)                                                     |
| 0x00000037 | [**FLOPPY\_INTERNAL\_ERROR**](bug-check-0x37--floppy-internal-error.md)                                                                           |
| 0x00000038 | [**SERIAL\_DRIVER\_INTERNAL**](bug-check-0x38--serial-driver-internal.md)                                                                         |
| 0x00000039 | [**SYSTEM\_EXIT\_OWNED\_MUTEX**](bug-check-0x39--system-exit-owned-mutex.md)                                                                      |
| 0x0000003A | [**SYSTEM\_UNWIND\_PREVIOUS\_USER**](bug-check-0x3a--system-unwind-previous-user.md)                                                              |
| 0x0000003B | [**SYSTEM\_SERVICE\_EXCEPTION**](bug-check-0x3b--system-service-exception.md)                                                                     |
| 0x0000003C | [**INTERRUPT\_UNWIND\_ATTEMPTED**](bug-check-0x3c--interrupt-unwind-attempted.md)                                                                 |
| 0x0000003D | [**INTERRUPT\_EXCEPTION\_NOT\_HANDLED**](bug-check-0x3d--interrupt-exception-not-handled.md)                                                      |
| 0x0000003E | [**MULTIPROCESSOR\_CONFIGURATION\_NOT\_SUPPORTED**](bug-check-0x3e--multiprocessor-configuration-not-supported.md)                                |
| 0x0000003F | [**NO\_MORE\_SYSTEM\_PTES**](bug-check-0x3f--no-more-system-ptes.md)                                                                              |
| 0x00000040 | [**TARGET\_MDL\_TOO\_SMALL**](bug-check-0x40--target-mdl-too-small.md)                                                                            |
| 0x00000041 | [**MUST\_SUCCEED\_POOL\_EMPTY**](bug-check-0x41--must-succeed-pool-empty.md)                                                                      |
| 0x00000042 | [**ATDISK\_DRIVER\_INTERNAL**](bug-check-0x42--atdisk-driver-internal.md)                                                                         |
| 0x00000043 | [**NO\_SUCH\_PARTITION**](bug-check-0x43--no-such-partition.md)                                                                                   |
| 0x00000044 | [**MULTIPLE\_IRP\_COMPLETE\_REQUESTS**](bug-check-0x44--multiple-irp-complete-requests.md)                                                        |
| 0x00000045 | [**INSUFFICIENT\_SYSTEM\_MAP\_REGS**](bug-check-0x45--insufficient-system-map-regs.md)                                                            |
| 0x00000046 | [**DEREF\_UNKNOWN\_LOGON\_SESSION**](bug-check-0x46--deref-unknown-logon-session.md)                                                              |
| 0x00000047 | [**REF\_UNKNOWN\_LOGON\_SESSION**](bug-check-0x47--ref-unknown-logon-session.md)                                                                  |
| 0x00000048 | [**CANCEL\_STATE\_IN\_COMPLETED\_IRP**](bug-check-0x48--cancel-state-in-completed-irp.md)                                                         |
| 0x00000049 | [**PAGE\_FAULT\_WITH\_INTERRUPTS\_OFF**](bug-check-0x49--page-fault-with-interrupts-off.md)                                                       |
| 0x0000004A | [**IRQL\_GT\_ZERO\_AT\_SYSTEM\_SERVICE**](bug-check-0x4a--irql-gt-zero-at-system-service.md)                                                      |
| 0x0000004B | [**STREAMS\_INTERNAL\_ERROR**](bug-check-0x4b--streams-internal-error.md)                                                                         |
| 0x0000004C | [**FATAL\_UNHANDLED\_HARD\_ERROR**](bug-check-0x4c--fatal-unhandled-hard-error.md)                                                                |
| 0x0000004D | [**NO\_PAGES\_AVAILABLE**](bug-check-0x4d--no-pages-available.md)                                                                                 |
| 0x0000004E | [**PFN\_LIST\_CORRUPT**](bug-check-0x4e--pfn-list-corrupt.md)                                                                                     |
| 0x0000004F | [**NDIS\_INTERNAL\_ERROR**](bug-check-0x4f--ndis-internal-error.md)                                                                               |
| 0x00000050 | [**PAGE\_FAULT\_IN\_NONPAGED\_AREA**](bug-check-0x50--page-fault-in-nonpaged-area.md)                                                             |
| 0x00000051 | [**REGISTRY\_ERROR**](bug-check-0x51--registry-error.md)                                                                                          |
| 0x00000052 | [**MAILSLOT\_FILE\_SYSTEM**](bug-check-0x52--mailslot-file-system.md)                                                                             |
| 0x00000053 | [**NO\_BOOT\_DEVICE**](bug-check-0x53--no-boot-device.md)                                                                                         |
| 0x00000054 | [**LM\_SERVER\_INTERNAL\_ERROR**](bug-check-0x54--lm-server-internal-error.md)                                                                    |
| 0x00000055 | [**DATA\_COHERENCY\_EXCEPTION**](bug-check-0x55--data-coherency-exception.md)                                                                     |
| 0x00000056 | [**INSTRUCTION\_COHERENCY\_EXCEPTION**](bug-check-0x56--instruction-coherency-exception.md)                                                       |
| 0x00000057 | [**XNS\_INTERNAL\_ERROR**](bug-check-0x57--xns-internal-error.md)                                                                                 |
| 0x00000058 | [**FTDISK\_INTERNAL\_ERROR**](bug-check-0x58--ftdisk-internal-error.md)                                                                           |
| 0x00000059 | [**PINBALL\_FILE\_SYSTEM**](bug-check-0x59--pinball-file-system.md)                                                                               |
| 0x0000005A | [**CRITICAL\_SERVICE\_FAILED**](bug-check-0x5a--critical-service-failed.md)                                                                       |
| 0x0000005B | [**SET\_ENV\_VAR\_FAILED**](bug-check-0x5b--set-env-var-failed.md)                                                                                |
| 0x0000005C | [**HAL\_INITIALIZATION\_FAILED**](bug-check-0x5c--hal-initialization-failed.md)                                                                   |
| 0x0000005D | [**UNSUPPORTED\_PROCESSOR**](bug-check-0x5d--unsupported-processor.md)                                                                            |
| 0x0000005E | [**OBJECT\_INITIALIZATION\_FAILED**](bug-check-0x5e--object-initialization-failed.md)                                                             |
| 0x0000005F | [**SECURITY\_INITIALIZATION\_FAILED**](bug-check-0x5f--security-initialization-failed.md)                                                         |
| 0x00000060 | [**PROCESS\_INITIALIZATION\_FAILED**](bug-check-0x60--process-initialization-failed.md)                                                           |
| 0x00000061 | [**HAL1\_INITIALIZATION\_FAILED**](bug-check-0x61--hal1-initialization-failed.md)                                                                 |
| 0x00000062 | [**OBJECT1\_INITIALIZATION\_FAILED**](bug-check-0x62--object1-initialization-failed.md)                                                           |
| 0x00000063 | [**SECURITY1\_INITIALIZATION\_FAILED**](bug-check-0x63--security1-initialization-failed.md)                                                       |
| 0x00000064 | [**SYMBOLIC\_INITIALIZATION\_FAILED**](bug-check-0x64--symbolic-initialization-failed.md)                                                         |
| 0x00000065 | [**MEMORY1\_INITIALIZATION\_FAILED**](bug-check-0x65--memory1-initialization-failed.md)                                                           |
| 0x00000066 | [**CACHE\_INITIALIZATION\_FAILED**](bug-check-0x66--cache-initialization-failed.md)                                                               |
| 0x00000067 | [**CONFIG\_INITIALIZATION\_FAILED**](bug-check-0x67--config-initialization-failed.md)                                                             |
| 0x00000068 | [**FILE\_INITIALIZATION\_FAILED**](bug-check-0x68--file-initialization-failed.md)                                                                 |
| 0x00000069 | [**IO1\_INITIALIZATION\_FAILED**](bug-check-0x69--io1-initialization-failed.md)                                                                   |
| 0x0000006A | [**LPC\_INITIALIZATION\_FAILED**](bug-check-0x6a--lpc-initialization-failed.md)                                                                   |
| 0x0000006B | [**PROCESS1\_INITIALIZATION\_FAILED**](bug-check-0x6b--process1-initialization-failed.md)                                                         |
| 0x0000006C | [**REFMON\_INITIALIZATION\_FAILED**](bug-check-0x6c--refmon-initialization-failed.md)                                                             |
| 0x0000006D | [**SESSION1\_INITIALIZATION\_FAILED**](bug-check-0x6d--session1-initialization-failed.md)                                                         |
| 0x0000006E | [**SESSION2\_INITIALIZATION\_FAILED**](bug-check-0x6e--session2-initialization-failed.md)                                                         |
| 0x0000006F | [**SESSION3\_INITIALIZATION\_FAILED**](bug-check-0x6f--session3-initialization-failed.md)                                                         |
| 0x00000070 | [**SESSION4\_INITIALIZATION\_FAILED**](bug-check-0x70--session4-initialization-failed.md)                                                         |
| 0x00000071 | [**SESSION5\_INITIALIZATION\_FAILED**](bug-check-0x71--session5-initialization-failed.md)                                                         |
| 0x00000072 | [**ASSIGN\_DRIVE\_LETTERS\_FAILED**](bug-check-0x72--assign-drive-letters-failed.md)                                                              |
| 0x00000073 | [**CONFIG\_LIST\_FAILED**](bug-check-0x73--config-list-failed.md)                                                                                 |
| 0x00000074 | [**BAD\_SYSTEM\_CONFIG\_INFO**](bug-check-0x74--bad-system-config-info.md)                                                                        |
| 0x00000075 | [**CANNOT\_WRITE\_CONFIGURATION**](bug-check-0x75--cannot-write-configuration.md)                                                                 |
| 0x00000076 | [**PROCESS\_HAS\_LOCKED\_PAGES**](bug-check-0x76--process-has-locked-pages.md)                                                                    |
| 0x00000077 | [**KERNEL\_STACK\_INPAGE\_ERROR**](bug-check-0x77--kernel-stack-inpage-error.md)                                                                  |
| 0x00000078 | [**PHASE0\_EXCEPTION**](bug-check-0x78--phase0-exception.md)                                                                                      |
| 0x00000079 | [**MISMATCHED\_HAL**](bug-check-0x79--mismatched-hal.md)                                                                                          |
| 0x0000007A | [**KERNEL\_DATA\_INPAGE\_ERROR**](bug-check-0x7a--kernel-data-inpage-error.md)                                                                    |
| 0x0000007B | [**INACCESSIBLE\_BOOT\_DEVICE**](bug-check-0x7b--inaccessible-boot-device.md)                                                                     |
| 0x0000007C | [**BUGCODE\_NDIS\_DRIVER**](bug-check-0x7c--bugcode-ndis-driver.md)                                                                               |
| 0x0000007D | [**INSTALL\_MORE\_MEMORY**](bug-check-0x7d--install-more-memory.md)                                                                               |
| 0x0000007E | [**SYSTEM\_THREAD\_EXCEPTION\_NOT\_HANDLED**](bug-check-0x7e--system-thread-exception-not-handled.md)                                             |
| 0x0000007F | [**UNEXPECTED\_KERNEL\_MODE\_TRAP**](bug-check-0x7f--unexpected-kernel-mode-trap.md)                                                              |
| 0x00000080 | [**NMI\_HARDWARE\_FAILURE**](bug-check-0x80--nmi-hardware-failure.md)                                                                             |
| 0x00000081 | [**SPIN\_LOCK\_INIT\_FAILURE**](bug-check-0x81--spin-lock-init-failure.md)                                                                        |
| 0x00000082 | [**DFS\_FILE\_SYSTEM**](bug-check-0x82--dfs-file-system.md)                                                                                       |
| 0x00000085 | [**SETUP\_FAILURE**](bug-check-0x85--setup-failure.md)                                                                                            |
| 0x0000008B | [**MBR\_CHECKSUM\_MISMATCH**](bug-check-0x8b--mbr-checksum-mismatch.md)                                                                           |
| 0x0000008E | [**KERNEL\_MODE\_EXCEPTION\_NOT\_HANDLED**](bug-check-0x8e--kernel-mode-exception-not-handled.md)                                                 |
| 0x0000008F | [**PP0\_INITIALIZATION\_FAILED**](bug-check-0x8f--pp0-initialization-failed.md)                                                                   |
| 0x00000090 | [**PP1\_INITIALIZATION\_FAILED**](bug-check-0x90--pp1-initialization-failed.md)                                                                   |
| 0x00000092 | [**UP\_DRIVER\_ON\_MP\_SYSTEM**](bug-check-0x92--up-driver-on-mp-system.md)                                                                       |
| 0x00000093 | [**INVALID\_KERNEL\_HANDLE**](bug-check-0x93--invalid-kernel-handle.md)                                                                           |
| 0x00000094 | [**KERNEL\_STACK\_LOCKED\_AT\_EXIT**](bug-check-0x94--kernel-stack-locked-at-exit.md)                                                             |
| 0x00000096 | [**INVALID\_WORK\_QUEUE\_ITEM**](bug-check-0x96--invalid-work-queue-item.md)                                                                      |
| 0x00000097 | [**BOUND\_IMAGE\_UNSUPPORTED**](bug-check-0x97--bound-image-unsupported.md)                                                                       |
| 0x00000098 | [**END\_OF\_NT\_EVALUATION\_PERIOD**](bug-check-0x98--end-of-nt-evaluation-period.md)                                                             |
| 0x00000099 | [**INVALID\_REGION\_OR\_SEGMENT**](bug-check-0x99--invalid-region-or-segment.md)                                                                  |
| 0x0000009A | [**SYSTEM\_LICENSE\_VIOLATION**](bug-check-0x9a--system-license-violation.md)                                                                     |
| 0x0000009B | [**UDFS\_FILE\_SYSTEM**](bug-check-0x9b--udfs-file-system.md)                                                                                     |
| 0x0000009C | [**MACHINE\_CHECK\_EXCEPTION**](bug-check-0x9c--machine-check-exception.md)                                                                       |
| 0x0000009E | [**USER\_MODE\_HEALTH\_MONITOR**](bug-check-0x9e--user-mode-health-monitor.md)                                                                    |
| 0x0000009F | [**DRIVER\_POWER\_STATE\_FAILURE**](bug-check-0x9f--driver-power-state-failure.md)                                                                |
| 0x000000A0 | [**INTERNAL\_POWER\_ERROR**](bug-check-0xa0--internal-power-error.md)                                                                             |
| 0x000000A1 | [**PCI\_BUS\_DRIVER\_INTERNAL**](bug-check-0xa1--pci-bus-driver-internal.md)                                                                      |
| 0x000000A2 | [**MEMORY\_IMAGE\_CORRUPT**](bug-check-0xa2--memory-image-corrupt.md)                                                                             |
| 0x000000A3 | [**ACPI\_DRIVER\_INTERNAL**](bug-check-0xa3--acpi-driver-internal.md)                                                                             |
| 0x000000A4 | [**CNSS\_FILE\_SYSTEM\_FILTER**](bug-check-0xa4--cnss-file-system-filter.md)                                                                      |
| 0x000000A5 | [**ACPI\_BIOS\_ERROR**](bug-check-0xa5--acpi-bios-error.md)                                                                                       |
| 0x000000A7 | [**BAD\_EXHANDLE**](bug-check-0xa7--bad-exhandle.md)                                                                                              |
| 0x000000AC | [**HAL\_MEMORY\_ALLOCATION**](bug-check-0xac--hal-memory-allocation.md)                                                                           |
| 0x000000AD | [**VIDEO\_DRIVER\_DEBUG\_REPORT\_REQUEST**](bug-check-0xad--video-driver-debug-report-request.md)                                                 |
| 0x000000B1 | [**BGI\_DETECTED\_VIOLATION**](bug-check-0xb1--bgi-detected-violation.md)                                                                         |
| 0x000000B4 | [**VIDEO\_DRIVER\_INIT\_FAILURE**](bug-check-0xb4--video-driver-init-failure.md)                                                                  |
| 0x000000B8 | [**ATTEMPTED\_SWITCH\_FROM\_DPC**](bug-check-0xb8--attempted-switch-from-dpc.md)                                                                  |
| 0x000000B9 | [**CHIPSET\_DETECTED\_ERROR**](bug-check-0xb9--chipset-detected-error.md)                                                                         |
| 0x000000BA | [**SESSION\_HAS\_VALID\_VIEWS\_ON\_EXIT**](bug-check-0xba--session-has-valid-views-on-exit.md)                                                    |
| 0x000000BB | [**NETWORK\_BOOT\_INITIALIZATION\_FAILED**](bug-check-0xbb--network-boot-initialization-failed.md)                                                |
| 0x000000BC | [**NETWORK\_BOOT\_DUPLICATE\_ADDRESS**](bug-check-0xbc--network-boot-duplicate-address.md)                                                        |
| 0x000000BD | [**INVALID\_HIBERNATED\_STATE**](bug-check-0xbd--invalid-hibernated-state.md)                                                                     |
| 0x000000BE | [**ATTEMPTED\_WRITE\_TO\_READONLY\_MEMORY**](bug-check-0xbe--attempted-write-to-readonly-memory.md)                                               |
| 0x000000BF | [**MUTEX\_ALREADY\_OWNED**](bug-check-0xbf--mutex-already-owned.md)                                                                               |
| 0x000000C1 | [**SPECIAL\_POOL\_DETECTED\_MEMORY\_CORRUPTION**](bug-check-0xc1--special-pool-detected-memory-corruption.md)                                     |
| 0x000000C2 | [**BAD\_POOL\_CALLER**](bug-check-0xc2--bad-pool-caller.md)                                                                                       |
| 0x000000C4 | [**DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](bug-check-0xc4--driver-verifier-detected-violation.md)                                                |
| 0x000000C5 | [**DRIVER\_CORRUPTED\_EXPOOL**](bug-check-0xc5--driver-corrupted-expool.md)                                                                       |
| 0x000000C6 | [**DRIVER\_CAUGHT\_MODIFYING\_FREED\_POOL**](bug-check-0xc6--driver-caught-modifying-freed-pool.md)                                               |
| 0x000000C7 | [**TIMER\_OR\_DPC\_INVALID**](bug-check-0xc7--timer-or-dpc-invalid.md)                                                                            |
| 0x000000C8 | [**IRQL\_UNEXPECTED\_VALUE**](bug-check-0xc8--irql-unexpected-value.md)                                                                           |
| 0x000000C9 | [**DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION**](bug-check-0xc9--driver-verifier-iomanager-violation.md)                                              |
| 0x000000CA | [**PNP\_DETECTED\_FATAL\_ERROR**](bug-check-0xca--pnp-detected-fatal-error.md)                                                                    |
| 0x000000CB | [**DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS**](bug-check-0xcb--driver-left-locked-pages-in-process.md)                                            |
| 0x000000CC | [**PAGE\_FAULT\_IN\_FREED\_SPECIAL\_POOL**](bug-check-0xcc--page-fault-in-freed-special-pool.md)                                                  |
| 0x000000CD | [**PAGE\_FAULT\_BEYOND\_END\_OF\_ALLOCATION**](bug-check-0xcd--page-fault-beyond-end-of-allocation.md)                                            |
| 0x000000CE | [**DRIVER\_UNLOADED\_WITHOUT\_CANCELLING\_PENDING\_OPERATIONS**](bug-check-0xce--driver-unloaded-without-cancelling-pending-operations.md)        |
| 0x000000CF | [**TERMINAL\_SERVER\_DRIVER\_MADE\_INCORRECT\_MEMORY\_REFERENCE**](bug-check-0xcf--terminal-server-driver-made-incorrect-memory-reference.md)     |
| 0x000000D0 | [**DRIVER\_CORRUPTED\_MMPOOL**](bug-check-0xd0--driver-corrupted-mmpool.md)                                                                       |
| 0x000000D1 | [**DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL**](bug-check-0xd1--driver-irql-not-less-or-equal.md)                                                        |
| 0x000000D2 | [**BUGCODE\_ID\_DRIVER**](bug-check-0xd2--bugcode-id-driver.md)                                                                                   |
| 0x000000D3 | [**DRIVER\_PORTION\_MUST\_BE\_NONPAGED**](bug-check-0xd3--driver-portion-must-be-nonpaged.md)                                                     |
| 0x000000D4 | [**SYSTEM\_SCAN\_AT\_RAISED\_IRQL\_CAUGHT\_IMPROPER\_DRIVER\_UNLOAD**](bug-check-0xd4--system-scan-at-raised-irql-caught-improper-driver-unlo.md) |
| 0x000000D5 | [**DRIVER\_PAGE\_FAULT\_IN\_FREED\_SPECIAL\_POOL**](bug-check-0xd5--driver-page-fault-in-freed-special-pool.md)                                   |
| 0x000000D6 | [**DRIVER\_PAGE\_FAULT\_BEYOND\_END\_OF\_ALLOCATION**](bug-check-0xd6--driver-page-fault-beyond-end-of-allocation.md)                             |
| 0x000000D7 | [**DRIVER\_UNMAPPING\_INVALID\_VIEW**](bug-check-0xd7--driver-unmapping-invalid-view.md)                                                          |
| 0x000000D8 | [**DRIVER\_USED\_EXCESSIVE\_PTES**](bug-check-0xd8--driver-used-excessive-ptes.md)                                                                |
| 0x000000D9 | [**LOCKED\_PAGES\_TRACKER\_CORRUPTION**](bug-check-0xd9--locked-pages-tracker-corruption.md)                                                      |
| 0x000000DA | [**SYSTEM\_PTE\_MISUSE**](bug-check-0xda--system-pte-misuse.md)                                                                                   |
| 0x000000DB | [**DRIVER\_CORRUPTED\_SYSPTES**](bug-check-0xdb--driver-corrupted-sysptes.md)                                                                     |
| 0x000000DC | [**DRIVER\_INVALID\_STACK\_ACCESS**](bug-check-0xdc--driver-invalid-stack-access.md)                                                              |
| 0x000000DE | [**POOL\_CORRUPTION\_IN\_FILE\_AREA**](bug-check-0xde--pool-corruption-in-file-area.md)                                                           |
| 0x000000DF | I[**MPERSONATING\_WORKER\_THREAD**](bug-check-0xdf--impersonating-worker-thread.md)                                                               |
| 0x000000E0 | [**ACPI\_BIOS\_FATAL\_ERROR**](bug-check-0xe0--acpi-bios-fatal-error.md)                                                                          |
| 0x000000E1 | [**WORKER\_THREAD\_RETURNED\_AT\_BAD\_IRQL**](bug-check-0xe1--worker-thread-returned-at-bad-irql.md)                                              |
| 0x000000E2 | [**MANUALLY\_INITIATED\_CRASH**](bug-check-0xe2--manually-initiated-crash.md)                                                                     |
| 0x000000E3 | [**RESOURCE\_NOT\_OWNED**](bug-check-0xe3--resource-not-owned.md)                                                                                 |
| 0x000000E4 | [**WORKER\_INVALID**](bug-check-0xe4--worker-invalid.md)                                                                                          |
| 0x000000E6 | [**DRIVER\_VERIFIER\_DMA\_VIOLATION**](bug-check-0xe6--driver-verifier-dma-violation.md)                                                          |
| 0x000000E7 | [**INVALID\_FLOATING\_POINT\_STATE**](bug-check-0xe7--invalid-floating-point-state.md)                                                            |
| 0x000000E8 | [**INVALID\_CANCEL\_OF\_FILE\_OPEN**](bug-check-0xe8--invalid-cancel-of-file-open.md)                                                             |
| 0x000000E9 | [**ACTIVE\_EX\_WORKER\_THREAD\_TERMINATION**](bug-check-0xe9--active-ex-worker-thread-termination.md)                                             |
| 0x000000EA | [**THREAD\_STUCK\_IN\_DEVICE\_DRIVER**](bug-check-0xea--thread-stuck-in-device-driver.md)                                                         |
| 0x000000EB | [**DIRTY\_MAPPED\_PAGES\_CONGESTION**](bug-check-0xeb--dirty-mapped-pages-congestion.md)                                                          |
| 0x000000EC | [**SESSION\_HAS\_VALID\_SPECIAL\_POOL\_ON\_EXIT**](bug-check-0xec--session-has-valid-special-pool-on-exit.md)                                     |
| 0x000000ED | [**UNMOUNTABLE\_BOOT\_VOLUME**](bug-check-0xed--unmountable-boot-volume.md)                                                                       |
| 0x000000EF | [**CRITICAL\_PROCESS\_DIED**](bug-check-0xef--critical-process-died.md)                                                                           |
| 0x000000F0 | [**STORAGE\_MINIPORT\_ERROR**](bug-check-0xf0--storage-miniport-error.md)                                                                         |
| 0x000000F1 | [**SCSI\_VERIFIER\_DETECTED\_VIOLATION**](bug-check-0xf1--scsi-verifier-detected-violation.md)                                                    |
| 0x000000F2 | [**HARDWARE\_INTERRUPT\_STORM**](bug-check-0xf2--hardware-interrupt-storm.md)                                                                     |
| 0x000000F3 | [**DISORDERLY\_SHUTDOWN**](bug-check-0xf3--disorderly-shutdown.md)                                                                                |
| 0x000000F4 | [**CRITICAL\_OBJECT\_TERMINATION**](bug-check-0xf4--critical-object-termination.md)                                                               |
| 0x000000F5 | [**FLTMGR\_FILE\_SYSTEM**](bug-check-0xf5--fltmgr-file-system.md)                                                                                 |
| 0x000000F6 | [**PCI\_VERIFIER\_DETECTED\_VIOLATION**](bug-check-0xf6--pci-verifier-detected-violation.md)                                                      |
| 0x000000F7 | [**DRIVER\_OVERRAN\_STACK\_BUFFER**](bug-check-0xf7--driver-overran-stack-buffer.md)                                                              |
| 0x000000F8 | [**RAMDISK\_BOOT\_INITIALIZATION\_FAILED**](bug-check-0xf8--ramdisk-boot-initialization-failed.md)                                                |
| 0x000000F9 | [**DRIVER\_RETURNED\_STATUS\_REPARSE\_FOR\_VOLUME\_OPEN**](bug-check-0xf9--driver-returned-status-reparse-for-volume-open.md)                     |
| 0x000000FA | [**HTTP\_DRIVER\_CORRUPTED**](bug-check-0xfa---http-driver-corrupted.md)                                                                          |
| 0x000000FC | [**ATTEMPTED\_EXECUTE\_OF\_NOEXECUTE\_MEMORY**](bug-check-0xfc---attempted-execute-of-noexecute-memory.md)                                        |
| 0x000000FD | [**DIRTY\_NOWRITE\_PAGES\_CONGESTION**](bug-check-0xfd---dirty-nowrite-pages-congestion.md)                                                       |
| 0x000000FE | [**BUGCODE\_USB\_DRIVER**](bug-check-0xfe--bugcode-usb-driver.md)                                                                                 |
| 0x000000FF | [**RESERVE\_QUEUE\_OVERFLOW**](bug-check-0xff---reserve-queue-overflow.md)                                                                        |
| 0x00000100 | [**LOADER\_BLOCK\_MISMATCH**](bug-check-0x100---loader-block-mismatch.md)                                                                         |
| 0x00000101 | [**CLOCK\_WATCHDOG\_TIMEOUT**](bug-check-0x101---clock-watchdog-timeout.md)                                                                       |
| 0x00000102 | [**DPC\_WATCHDOG\_TIMEOUT**](bug-check-0x102--dpc-watchdog-timeout.md)                                                                            |
| 0x00000103 | [**MUP\_FILE\_SYSTEM**](bug-check-0x103---mup-file-system.md)                                                                                     |
| 0x00000104 | [**AGP\_INVALID\_ACCESS**](bug-check-0x104---agp-invalid-access.md)                                                                               |
| 0x00000105 | [**AGP\_GART\_CORRUPTION**](bug-check-0x105---agp-gart-corruption.md)                                                                             |
| 0x00000106 | [**AGP\_ILLEGALLY\_REPROGRAMMED**](bug-check-0x106---agp-illegally-reprogrammed.md)                                                               |
| 0x00000108 | [**THIRD\_PARTY\_FILE\_SYSTEM\_FAILURE**](bug-check-0x108--third-party-file-system-failure.md)                                                    |
| 0x00000109 | [**CRITICAL\_STRUCTURE\_CORRUPTION**](bug-check-0x109---critical-structure-corruption.md)                                                         |
| 0x0000010A | [**APP\_TAGGING\_INITIALIZATION\_FAILED**](bug-check-0x10a---app-tagging-initialization-failed.md)                                                |
| 0x0000010C | [**FSRTL\_EXTRA\_CREATE\_PARAMETER\_VIOLATION**](bug-check-0x10c---fsrtl-extra-create-parameter-violation.md)                                     |
| 0x0000010D | [**WDF\_VIOLATION**](bug-check-0x10d---wdf-violation.md)                                                                                          |
| 0x0000010E | [**VIDEO\_MEMORY\_MANAGEMENT\_INTERNAL**](bug-check-0x10e---video-memory-management-internal.md)                                                  |
| 0x0000010F | [**RESOURCE\_MANAGER\_EXCEPTION\_NOT\_HANDLED**](bug-check-0x10f---resource-manager-exception-not-handled.md)                                     |
| 0x00000111 | [**RECURSIVE\_NMI**](bug-check-0x111---recursive-nmi.md)                                                                                          |
| 0x00000112 | [**MSRPC\_STATE\_VIOLATION**](bug-check-0x112---msrpc-state-violation.md)                                                                         |
| 0x00000113 | [**VIDEO\_DXGKRNL\_FATAL\_ERROR**](bug-check-0x113---video-dxgkrnl-fatal-error.md)                                                                |
| 0x00000114 | [**VIDEO\_SHADOW\_DRIVER\_FATAL\_ERROR**](bug-check-0x114---video-shadow-driver-fatal-error.md)                                                   |
| 0x00000115 | [**AGP\_INTERNAL**](bug-check-0x115---agp-internal.md)                                                                                            |
| 0x00000116 | [**VIDEO\_TDR\_FAILURE**](bug-check-0x116---video-tdr-failure.md)                                                                                     |
| 0x00000117 | [**VIDEO\_TDR\_TIMEOUT\_DETECTED**](bug-check-0x117---video-tdr-timeout-detected.md)                                                              |
| 0x00000119 | [**VIDEO\_SCHEDULER\_INTERNAL\_ERROR**](bug-check-0x119---video-scheduler-internal-error.md)                                                      |
| 0x0000011A | [**EM\_INITIALIZATION\_FAILURE**](bug-check-0x11a---em-initialization-failure.md)                                                                 |
| 0x0000011B | [**DRIVER\_RETURNED\_HOLDING\_CANCEL\_LOCK**](bug-check-0x11b---driver-returned-holding-cancel-lock.md)                                           |
| 0x0000011C | [**ATTEMPTED\_WRITE\_TO\_CM\_PROTECTED\_STORAGE**](bug-check-0x11c--attempted-write-to-cm-protected-storage.md)                                   |
| 0x0000011D | [**EVENT\_TRACING\_FATAL\_ERROR**](bug-check-0x11d---event-tracing-fatal-error.md)                                                                |
| 0x0000011E | [**TOO\_MANY\_RECURSIVE\_FAULTS**](bug-check-0x11e--too-many-recursive-faults.md)                                                                 |
| 0x0000011F | [**INVALID\_DRIVER\_HANDLE**](bug-check-0x11f--invalid-driver-handle.md)                                                                          |
| 0x00000120 | [**BITLOCKER\_FATAL\_ERROR**](bug-check-0x120--bitlocker-fatal-error-.md)                                                                         |
| 0x00000121 | [**DRIVER\_VIOLATION**](bug-check-0x121---driver-violation.md)                                                                                    |
| 0x00000122 | [**WHEA\_INTERNAL\_ERROR**](bug-check-0x122---whea-internal-error.md)                                                                             |
| 0x00000123 | [**CRYPTO\_SELF\_TEST\_FAILURE**](bug-check-0x123--crypto-self-test-failure-.md)                                                                  |
| 0x00000124 | [**WHEA\_UNCORRECTABLE\_ERROR**](bug-check-0x124---whea-uncorrectable-error.md)                                                                   |
| 0x00000125 | [**NMR\_INVALID\_STATE**](bug-check-0x125--nmr-invalid-state.md)                                                                                  |
| 0x00000126 | [**NETIO\_INVALID\_POOL\_CALLER**](bug-check-0x126--netio-invalid-pool-caller.md)                                                                 |
| 0x00000127 | [**PAGE\_NOT\_ZERO**](bug-check-0x127---page-not-zero.md)                                                                                         |
| 0x00000128 | [**WORKER\_THREAD\_RETURNED\_WITH\_BAD\_IO\_PRIORITY**](bug-check-0x128--worker-thread-returned-with-bad-io-priority.md)                          |
| 0x00000129 | [**WORKER\_THREAD\_RETURNED\_WITH\_BAD\_PAGING\_IO\_PRIORITY**](bug-check-0x129--worker-thread-returned-with-bad-paging-io-priority.md)           |
| 0x0000012A | [**MUI\_NO\_VALID\_SYSTEM\_LANGUAGE**](bug-check-0x12a--mui-no-valid-system-language.md)                                                          |
| 0x0000012B | [**FAULTY\_HARDWARE\_CORRUPTED\_PAGE**](bug-check-0x12b---faulty-hardware-corrupted-page.md)                                                      |
| 0x0000012C | [**EXFAT\_FILE\_SYSTEM**](bug-check-0x12c---exfat-file-system.md)                                                                                 |
| 0x0000012D | [**VOLSNAP\_OVERLAPPED\_TABLE\_ACCESS**](bug-check-0x12d--volsnap-overlapped-table-access.md)                                                     |
| 0x0000012E | [**INVALID\_MDL\_RANGE**](bug-check-0x12e--invalid-mdl-range.md)                                                                                  |
| 0x0000012F | [**VHD\_BOOT\_INITIALIZATION\_FAILED**](bug-check-0x12f--vhd-boot-initialization-failed.md)                                                       |
| 0x00000130 | [**DYNAMIC\_ADD\_PROCESSOR\_MISMATCH**](bug-check-0x130--dynamic-add-processor-mismatch.md)                                                       |
| 0x00000131 | [**INVALID\_EXTENDED\_PROCESSOR\_STATE**](bug-check-0x131--invalid-extended-processor-state.md)                                                   |
| 0x00000132 | [**RESOURCE\_OWNER\_POINTER\_INVALID**](bug-check-0x132--resource-owner-pointer-invalid.md)                                                       |
| 0x00000133 | [**DPC\_WATCHDOG\_VIOLATION**](bug-check-0x133-dpc-watchdog-violation.md)                                                                         |
| 0x00000134 | [**DRIVE\_EXTENDER**](bug-check-0x134--drive-extender.md)                                                                                         |
| 0x00000135 | [**REGISTRY\_FILTER\_DRIVER\_EXCEPTION**](bug-check-0x135--registry-filter-driver-exception.md)                                                   |
| 0x00000136 | [**VHD\_BOOT\_HOST\_VOLUME\_NOT\_ENOUGH\_SPACE**](bug-check-0x136--vhd-boot-host-volume-not-enough-space.md)                                      |
| 0x00000137 | [**WIN32K\_HANDLE\_MANAGER**](bug-check-0x137--win32k-handle-manager.md)                                                                          |
| 0x00000138 | [**GPIO\_CONTROLLER\_DRIVER\_ERROR**](bug-check-0x138-gpio-controller-driver-error.md)                                                            |
| 0x00000139 | [**KERNEL\_SECURITY\_CHECK\_FAILURE**](bug-check-0x139--kernel-security-check-failure.md)                                                         |
| 0x0000013A | [**KERNEL\_MODE\_HEAP\_CORRUPTION**](bug-check-0x13a--kernel-mode-heap-corruption.md)                                                             |
| 0x0000013B | [**PASSIVE\_INTERRUPT\_ERROR**](bug-check-0x13b--passive-interrupt-error.md)                                                                      |
| 0x0000013C | [**INVALID\_IO\_BOOST\_STATE**](bug-check-0x13c--invalid-io-boost-state.md)                                                                       |
| 0x0000013D | [**CRITICAL\_INITIALIZATION\_FAILURE**](bug-check-0x13d--critical-initialization-failure.md)                                                      |
| 0x00000140 | [**STORAGE\_DEVICE\_ABNORMALITY\_DETECTED**](bug-check-0x140--storage-device-abnormality-detected.md)                                             |
| 0x00000143 | [**PROCESSOR\_DRIVER\_INTERNAL**](bug-check-0x143--processor-driver-internal.md)                                                                  |
| 0x00000144 | [**BUGCODE\_USB3\_DRIVER**](bug-check-0x144--bugcode-usb3-driver.md)                                                                              |
| 0x00000145 | [**SECURE\_BOOT\_VIOLATION**](bug-check-0x145--secure-boot-violation-.md)                                                                         |
| 0x00000147 | [**ABNORMAL\_RESET\_DETECTED**](bug-check-0x147--abnormal-reset-detected.md)                                                                      |
| 0x00000149 | [**REFS\_FILE\_SYSTEM**](bug-check-0x149--refs-file-system.md)                                                                                    |
| 0x0000014A | [**KERNEL\_WMI\_INTERNAL**](bug-check-0x14a--kernel-wmi-internal.md)                                                                              |
| 0x0000014B | [**SOC\_SUBSYSTEM\_FAILURE**](bug-check-0x14b--soc-subsystem-failure.md)                                                                          |
| 0x0000014C | [**FATAL\_ABNORMAL\_RESET\_ERROR**](bug-check-0x14c--fatal-abnormal-reset-error.md)                                                               |
| 0x0000014D | [**EXCEPTION\_SCOPE\_INVALID**](bug-check-0x14d--exception-scope-invalid.md)                                                                      |
| 0x0000014E | [**SOC\_CRITICAL\_DEVICE\_REMOVED**](bug-check-0x14e--soc-critical-device-removed.md)                                                             |
| 0x0000014F | [**PDC\_WATCHDOG\_TIMEOUT**](bug-check-0x14f--pdc-watchdog-timeout.md)                                                                            |
| 0x00000150 | [**TCPIP\_AOAC\_NIC\_ACTIVE\_REFERENCE\_LEAK**](bug-check-0x150--tcpip-aoac-nic-active-reference-leak.md)                                         |
| 0x00000151 | [**UNSUPPORTED\_INSTRUCTION\_MODE**](bug-check-0x151--unsupported-instruction-mode.md)                                                            |
| 0x00000152 | [**INVALID\_PUSH\_LOCK\_FLAGS**](bug-check-0x152--invalid-push-lock-flags.md)                                                                     |
| 0x00000153 | [**KERNEL\_LOCK\_ENTRY\_LEAKED\_ON\_THREAD\_TERMINATION**](bug-check-0x153--kernel-lock-entry-leaked-on-thread-termination.md)                    |
| 0x00000154 | [**UNEXPECTED\_STORE\_EXCEPTION**](bug-check-0x154--unexpected-store-exception.md)                                                                |
| 0x00000155 | [**OS\_DATA\_TAMPERING**](bug-check-0x155--os-data-tampering.md)                                                                                  |
| 0x00000157 | [**KERNEL\_THREAD\_PRIORITY\_FLOOR\_VIOLATION**](bug-check-0x157--kernel-thread-priority-floor-violation.md)                                      |
| 0x00000158 | [**ILLEGAL\_IOMMU\_PAGE\_FAULT**](bug-check-0x158--illegal-iommu-page-fault.md)                                                                   |
| 0x00000159 | [**HAL\_ILLEGAL\_IOMMU\_PAGE\_FAULT**](bug-check-0x159--hal-illegal-iommu-page-fault.md)                                                          |
| 0x0000015A | [**SDBUS\_INTERNAL\_ERROR**](bug-check-0x15a--sdbus-internal-error.md)                                                                            |
| 0x0000015B | [**WORKER\_THREAD\_RETURNED\_WITH\_SYSTEM\_PAGE\_PRIORITY\_ACTIVE**](bug-check-0x15b--worker-thread-returned-with-system-page-priority-active.md) |
| 0x00000160 | [**WIN32K\_ATOMIC\_CHECK\_FAILURE**](bug-check-0x160--win32k-atomic-check-failure.md)                                                             |
| 0x00000162 | [**KERNEL\_AUTO\_BOOST\_INVALID\_LOCK\_RELEASE**](bug-check-0x162--kernel-auto-boost-invalid-lock-release.md)                                     |
| 0x00000163 | [**WORKER\_THREAD\_TEST\_CONDITION**](bug-check-0x162--worker-thread-test-condition.md)                                                           |
| 0x00000164 | [**WIN32K\_CRITICAL\_FAILURE**](bug-check-0x164--win32k-critical-failure.md)                                                                      |
| 0x0000016C | [**INVALID\_RUNDOWN\_PROTECTION\_FLAGS**](bug-check-0x16c--invalid-rundown-protection-flags.md)                                                   |
| 0x0000016D | [**INVALID\_SLOT\_ALLOCATOR\_FLAGS**](bug-check-0x16d--invalid-slot-allocator-flags.md)                                                           |
| 0x0000016E | [**ERESOURCE\_INVALID\_RELEASE**](bug-check-0x16e--eresource-invalid-release.md)                                                                  |
| 0x00000170 | [**CLUSTER\_CSV\_CLUSSVC\_DISCONNECT\_WATCHDOG**](bug-check-0x170--cluster-csv-clussvc-disconnect-watchdog.md)                                    |
| 0x00000171 | [**CRYPTO\_LIBRARY\_INTERNAL\_ERROR**](bug-check-0x171--crypto-library-internal-error.md)                                                         |
| 0x00000173 | [**COREMSGCALL\_INTERNAL\_ERROR**](bug-check-0x173--coremsgcall-internal-error.md)                                                                |
| 0x00000174 | [**COREMSG\_INTERNAL\_ERROR**](bug-check-0x174--coremsg-internal-error.md)                                                                        |
| 0x00000178 | [**ELAM\_DRIVER\_DETECTED\_FATAL\_ERROR**](bug-check-0x178--elam-driver-detected-fatal-error.md)                                                  |
| 0x0000017B | [**PROFILER\_CONFIGURATION\_ILLEGAL**](bug-check-0x17b--profiler-configuration-illegal.md)                                                        |
| 0x0000017E | [**MICROCODE\_REVISION\_MISMATCH**](bug-check-0x17e--microcode-revision-mismatch.md)                                                              |
| 0x00000187 | [**VIDEO\_DWMINIT\_TIMEOUT\_FALLBACK\_BDD**](bug-check-0x187--video-dwminit-timeout-fallback-bdd.md)                                              |
| 0x00000189 | [**BAD\_OBJECT\_HEADER**](bug-check-0x189--bad-object-header.md)                                                                                  |
| 0x0000018B | [**SECURE\_KERNEL\_ERROR**](bug-check-0x18b--secure-kernel-error.md)                                                                              |
| 0x0000018C | [**HYPERGUARD\_VIOLATION**](bug-check-0x18c--hyperguard-violation.md)                                                                             |
| 0x0000018D | [**SECURE\_FAULT\_UNHANDLED**](bug-check-0x18d--secure-fault-unhandled.md)                                                                        |
| 0x0000018E | [**KERNEL\_PARTITION\_REFERENCE\_VIOLATION**](bug-check-0x18e--kernel-partition-reference-violation.md)                                           |
| 0x00000191 | [**PF\_DETECTED\_CORRUPTION**](bug-check-0x191--pf-detected-corruption.md)                                                                        |
| 0x00000192 | [**KERNEL\_AUTO\_BOOST\_LOCK\_ACQUISITION\_WITH\_RAISED\_IRQL**](bug-check-0x192--kernel-auto-boost-lock-acquisition-with-raised-irql.md)         |
| 0x00000196 | [**LOADER\_ROLLBACK\_DETECTED**](bug-check-0x196--loader-rollback-detected.md)                                                                    |
| 0x00000197 | [**WIN32K\_SECURITY\_FAILURE**](bug-check-0x197--win32k-security-failure.md)                                                                      |
| 0x00000199 | [**KERNEL\_STORAGE\_SLOT\_IN\_USE**](bug-check-0x199--kernel-storage-slot-in-use.md)                                                              |
| 0x0000019A | [**WORKER\_THREAD\_RETURNED\_WHILE\_ATTACHED\_TO\_SILO**](bug-check-0x19a--worker-thread-returned-while-attached-to-silo.md)                      |
| 0x0000019B | [**TTM\_FATAL\_ERROR**](bug-check-0x19b--ttm-fatal-error.md)                                                                                      |
| 0x0000019C | [**WIN32K\_POWER\_WATCHDOG\_TIMEOUT**](bug-check-0x19c--win32k-power-watchdog-timeout.md)                                                         |
| 0x000001A0 | [**TTM\_WATCHDOG\_TIMEOUT**](bug-check-0x1a0--ttm-watchdog-timeout.md)                                                                            |
| 0x000001A2 | [**WIN32K\_CALLOUT\_WATCHDOG\_BUGCHECK**](bug-check-0x1a2--win32k-callout-watchdog-bugcheck.md)                                                   |
| 0x000001AA | [**EXCEPTION\_ON\_INVALID\_STACK**](bug-check-0x1aa-exception-on-invalid-stack.md)                                                                |
| 0x000001AB | [**UNWIND\_ON\_INVALID\_STACK**](bug-check-0x1ab-unwind-on-invalid-stack.md)                                                                      |
| 0x000001C6 | [**FAST\_ERESOURCE\_PRECONDITION\_VIOLATION**](bug-check-0x1c6--fast-eresource-precondition-violation.md)                                         |
| 0x000001C7 | [**STORE\_DATA\_STRUCTURE\_CORRUPTION**](bug-check-0x1c7--store-data-structure-corruption.md)                                                     |
| 0x000001C8 | [**MANUALLY\_INITIATED\_POWER\_BUTTON\_HOLD**](bug-check-0x1c8--manually-initiated-power-button-hold.md)                                          |
| 0x000001CA | [**SYNTHETIC\_WATCHDOG\_TIMEOUT**](bug-check-0x1ca--synthetic-watchdog-timeout.md)                                                                |
| 0x000001CB | [**INVALID\_SILO\_DETACH**](bug-check-0x1cb--invalid-silo-detach.md)                                                                              |
| 0x000001CD | [**INVALID\_CALLBACK\_STACK_ADDRESS**](bug-check-0x1cd--invalid-callback-stack-address.md)                                                        |
| 0x000001CE | [**INVALID\_KERNEL\_STACK\_ADDRESS**](bug-check-0x1ce--invalid-kernel-stack-address.md)                                                           |
| 0x000001CF | [**HARDWARE\_WATCHDOG\_TIMEOUT**](bug-check-0x1cf--hardware-watchdog-timeout.md)                                                                  |  
| 0x000001D0 | [**CPI\_FIRMWARE\_WATCHDOG\_TIMEOUT**](bug-check-0x1d0--acpi-firmware-watchdog-timeout.md)                                                        |
| 0x000001D2 | [**WORKER\_THREAD\_INVALID\_STATE**](bug-check-0x1d2--worker-thread-invalid-state.md)                                                             |
| 0x000001D3 | [**WFP\_INVALID\_OPERATION**](bug-check-0x1d3--wfp-invalid-operation.md)                                                                          |
| 0x000001D5 | [**DRIVER_PNP_WATCHDOG**](bug-check-0x1d5--driver-pnp-watchdog.md)                                                                                |
| 0x000001D6 | [**WORKER\_THREAD\_RETURNED\_WITH\_NON\_DEFAULT\_WORKLOAD\_CLASS**](bug-check-0x1d6--worker-thread-returned-with-non-default-workload-class.md)   |
| 0x000001D7 | [**EFS\_FATAL\_ERROR**](bug-check-0x1d7--efs-fatal-error.md)                                                                                      |
| 0x000001D8 | [**UCMUCSI\_FAILURE**](bug-check-0x1d8--ucmucsi-failure.md)                                                                                       |
| 0x000001D9 | [**HAL\_IOMMU\_INTERNAL\_ERROR**](bug-check-0x1d8--ucmucsi-failure.md)                                                                            |  
| 0x000001DA | [**HAL\_BLOCKED\_PROCESSOR\_INTERNAL\_ERROR**](bug-check-0x1da--hal-blocked-processor-internal-error.md)                                          |
| 0x000001DB | [**IPI\_WATCHDOG\_TIMEOUT**](bug-check-0x1db--ipi-watchdog-timeout.md)                                                                            |
| 0x000001DC | [**DMA_COMMON_BUFFER_VECTOR_ERROR**](bug-check-0x1dc--dma-common-buffer-vector-error.md)                                                          |
| 0x000001DD | [**BUGCODE\_MBBADAPTER\_DRIVER**](bug-check-0x1dd--bugcode-mbbadapter-driver.md)                                                                  |
| 0x000001DE | [**BUGCODE\_WIFIADAPTER\_DRIVER**](bug-check-0x1de--bugcode-wifiadapter-driver.md)                                                                |
| 0x000001DF | [**PROCESSOR\_START\_TIMEOUT**](bug-check-0x1df--processor-start-timeout.md)                                                                      |
| 0x000001E4 | [**VIDEO\_DXGKRNL\_SYSMM_FATAL_ERROR**](bug-check-0x1e4--video-dxgkrnl-sysmm-fatal-error.md)                                                      |
| 0x000001E9 | [**ILLEGAL\_ATS\_INITIALIZATION**](bug-check-0x1e9--illegal-ats-initialization.md)                                                                |
| 0x000001EA | [**SECURE\_PCI\_CONFIG\_SPACE\_ACCESS\_VIOLATION**](bug-check-0x1ea--secure-pci-config-space-access-violation.md)                                 |
| 0x000001EB | [**DAM\_WATCHDOG\_TIMEOUT**](bug-check-0x1eb--dam-watchdog-timeout.md)                                                                            |
| 0x000001ED | [**HANDLE\_ERROR\_ON\_CRITICAL\_THREAD**](bug-check-0x1ed--handle-error-on-critical-thread.md)                                                    |
| 0x00000356 | [**XBOX\_ERACTRL\_CS\_TIMEOUT**](bug-check-0x356--xbox-eractrl-cs-timeout.md)                                                                     |
| 0x00000BFE | [**BC\_BLUETOOTH\_VERIFIER\_FAULT**](bug-check-0xbfe--bc-bluetooth-verifier-fault.md)                                                             |
| 0x00000BFF | [**BC\_BTHMINI\_VERIFIER\_FAULT**](bug-check-0xbff--bc-bthmini-verifier-fault.md)                                                                 |
| 0x00020001 | [**HYPERVISOR\_ERROR**](bug-check-0x20001--hypervisor-error.md)                                                                                   |
| 0x1000007E | [**SYSTEM\_THREAD\_EXCEPTION\_NOT\_HANDLED\_M**](bug-check-0x1000007e--system-thread-exception-not-handled-m.md)                                  |
| 0x1000007F | [**UNEXPECTED\_KERNEL\_MODE\_TRAP\_M**](bug-check-0x1000007f--unexpected-kernel-mode-trap-m.md)                                                   |
| 0x1000008E | [**KERNEL\_MODE\_EXCEPTION\_NOT\_HANDLED\_M**](bug-check-0x1000008e--kernel-mode-exception-not-handled-m.md)                                      |
| 0x100000EA | [**THREAD\_STUCK\_IN\_DEVICE\_DRIVER\_M**](bug-check-0x100000ea--thread-stuck-in-device-driver-m.md)                                              |
| 0x4000008A | [**THREAD\_TERMINATE\_HELD\_MUTEX**](bug-check-0x4000008a--thread-terminate-held-mutex.md)                                                        |
| 0xC0000218 | [**STATUS\_CANNOT\_LOAD\_REGISTRY\_FILE**](bug-check-0xc0000218--status-cannot-load-registry-file.md)                                             |
| 0xC000021A | [**WINLOGON\_FATAL\_ERROR**](bug-check-0xc000021a--winlogin-fatal-error.md)                                                                       |
| 0xC0000221 | [**STATUS\_IMAGE\_CHECKSUM\_MISMATCH**](bug-check-0xc0000221--status-image-checksum-mismatch.md)                                                  |
| 0xDEADDEAD | [**MANUALLY\_INITIATED\_CRASH1**](bug-check-0xdeaddead--manually-initiated-crash1.md)                                                             |

## See also

[General Tips for Blue Screens](general-troubleshooting-tips.md)

[Blue Screen Data](blue-screen-data.md)
