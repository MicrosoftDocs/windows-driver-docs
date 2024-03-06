---
title: Bug Check 0x133 DPC_WATCHDOG_VIOLATION
description: The DPC_WATCHDOG_VIOLATION bug check has a value of 0x00000133.
keywords: ["Bug Check 0x133 DPC_WATCHDOG_VIOLATION", "DPC_WATCHDOG_VIOLATION"]
ms.date: 03/14/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- DPC_WATCHDOG_VIOLATION
api_type:
- NA
---

# Bug Check 0x133: DPC\_WATCHDOG\_VIOLATION

The DPC\_WATCHDOG\_VIOLATION bug check has a value of 0x00000133. This bug check indicates that the DPC watchdog executed, either because it detected a single long-running deferred procedure call (DPC), or because the system spent a prolonged time at an interrupt request level (IRQL) of DISPATCH\_LEVEL or above. 

The value of Parameter 1 indicates whether a single DPC exceeded a timeout, or whether the system cumulatively spent an extended period of time at IRQL DISPATCH\_LEVEL or above. DPCs should not run longer than 100 microseconds and ISRs should not run longer than 25 microseconds, however the actual timeout values on the system are set much higher.

For more information about DPCs, see [Introduction to DPC Objects](../kernel/introduction-to-dpc-objects.md) and [Windows Internals 7th Edition Part 1](/sysinternals/resources/windows-internals) by  Pavel Yosifovich, Mark E. Russinovich, David A. Solomon and Alex Ionescu.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## DPC\_WATCHDOG\_VIOLATION Parameters

*Parameter 1* indicates the type of violation. The meaning of the other parameters depends on the value of *Parameter 1*.

|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Cause of Error|
|---------- |---------- |---------- |---------- |------------- |
|0|The DPC time count (in ticks)|The DPC time allotment (in ticks).|cast to nt!DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK, which contains additional information regarding this single DPC timeout|A single DPC or ISR exceeded its time allotment. The offending component can usually be identified with a stack trace.|
|1|The watchdog period|cast to nt!DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK, which contains additional information regarding this single DPC timeout|Reserved|The system cumulatively spent an extended period of time at IRQL DISPATCH_LEVEL or above. The offending component can usually be identified with a stack trace.|

## Cause

To determine the cause requires the Windows debugger, programming experience and access to the source code for the faulting module.

For more information see the following topics:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Using the !analyze Extension](using-the--analyze-extension.md) and [!analyze](../debuggercmds/-analyze.md)

For more information on Windows DPC, see [Windows Internals 7th Edition Part 1](/sysinternals/resources/windows-internals) by  Pavel Yosifovich, Mark E. Russinovich, David A. Solomon and Alex Ionescu.

### Example 1

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

**Parameter 1 = 0**

In this example, the tick count of 501 exceeds the DPC time allotment of 500. The image name indicates that this code was executing when the bug check occurred.

```dbgcmd
0: kd> !analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

DPC_WATCHDOG_VIOLATION (133)
The DPC watchdog detected a prolonged run time at an IRQL of DISPATCH_LEVEL
or above.
Arguments:
Arg1: 0000000000000000, A single DPC or ISR exceeded its time allotment. The offending
    component can usually be identified with a stack trace.
Arg2: 0000000000000501, The DPC time count (in ticks).
Arg3: 0000000000000500, The DPC time allotment (in ticks).
Arg4: 0000000000000000

...

IMAGE_NAME:  BthA2DP.sys
...
```

Use the following debugger commands to gather more information for failures with a parameter of 0:

[**k (Display Stack Backtrace)**](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) to look at what code was running when the stop code occurred.

You may want to use the u, ub, uu (Unassemble) command to look deeper into the specifics of a the code that was running.

The [**!pcr**](../debuggercmds/-pcr.md) extension displays the current status of the Processor Control Region (PCR) on a specific processor. In the output will be the address of the Prcb

```dbgcmd
0: kd> !pcr
KPCR for Processor 0 at fffff8035f5a4000:
    Major 1 Minor 1
	NtTib.ExceptionList: fffff80368e77fb0
	    NtTib.StackBase: fffff80368e76000
	   NtTib.StackLimit: 0000000000000000
	 NtTib.SubSystemTib: fffff8035f5a4000
	      NtTib.Version: 000000005f5a4180
	  NtTib.UserPointer: fffff8035f5a4870
	      NtTib.SelfTib: 000000b6d3086000

	            SelfPcr: 0000000000000000
	               Prcb: fffff8035f5a4180
	               Irql: 0000000000000000
	                IRR: 0000000000000000
	                IDR: 0000000000000000
	      InterruptMode: 0000000000000000
	                IDT: 0000000000000000
	                GDT: 0000000000000000
	                TSS: 0000000000000000

	      CurrentThread: fffff80364926a00
	         NextThread: ffffe40b77c12040
	         IdleThread: fffff80364926a00
```

You can use the [**dt (Display Type)**](../debuggercmds/dt--display-type-.md) command to display additional information about the DPCs and the DPC Watchdog. For the address use the Prcb listed in the !pcr output:

```dbgcmd
dt nt!_KPRCB fffff80309974180 Dpc* 
```

```dbgcmd
0: kd> dt nt!DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK fffff803648fa320
   +0x000 Signature        : 0xaebecede
   +0x004 Revision         : 1
   +0x006 Size             : 0x10
   +0x008 DpcWatchdogProfileOffset : 0x84a8
   +0x00c DpcWatchdogProfileLength : 0x8200
```

## Example 2

**Parameter 1 = 1**

For parameter of 1, the code may not stop in the offending area of code. In this case one approach is to use the event tracing to attempt to track down which driver is exceeding it's normal execution duration.

Use the [**!analyze**](../debuggercmds/-analyze.md) debug extension to display information about the bug check.

```dbgcmd
0: kd> !analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

DPC_WATCHDOG_VIOLATION (133)
The DPC watchdog detected a prolonged run time at an IRQL of DISPATCH_LEVEL
or above.
Arguments:
Arg1: 0000000000000001, The system cumulatively spent an extended period of time at
	DISPATCH_LEVEL or above. The offending component can usually be
	identified with a stack trace.
Arg2: 0000000000001e00, The watchdog period.
Arg3: fffff803648fa320, cast to nt!DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK, which contains
	additional information regarding the cumulative timeout
Arg4: 0000000000000000
```

Cast the address of the nt!DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK to display information about it.

```dbgcmd
0: kd> dt nt!DPC_WATCHDOG_GLOBAL_TRIAGE_BLOCK fffff803648fa320
   +0x000 Signature        : 0xaebecede
   +0x004 Revision         : 1
   +0x006 Size             : 0x10
   +0x008 DpcWatchdogProfileOffset : 0x84a8
   +0x00c DpcWatchdogProfileLength : 0x8200
```

Use the [!dpcs](../debuggercmds/-dpcs.md) command to display the queued DPCs.

```dbgcmd
3: kd> !dpcs
CPU Type      KDPC       Function
 0: Normal  : 0xfffff8035f5ac290 0xfffff80363e15630 nt!PpmPerfAction
Failed to read DPC at 0xffffe40b77190dd8
 0: Threaded: 0xfffff8035f5ac3d8 0xfffff80363f27d70 nt!KiDpcWatchdog
```

## Resolution

To determine the specific cause and to create a code fix, programming experience and access to the source code of the faulting module, is required. 


## Remarks

In general this stop code is caused by faulty driver code that under certain conditions, does not complete its work within the allotted time frame.

If you are not equipped to use the Windows debugger to this problem, you should use some basic troubleshooting techniques.

-   If a driver is identified in the bug check message, to isolate the issue, disable the driver. Check with the manufacturer for driver updates.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing bug check 0x133.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example for Windows 10, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

## See also
 
[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
