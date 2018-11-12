---
title: Bug Check 0x133 DPC_WATCHDOG_VIOLATION
description: The DPC_WATCHDOG_VIOLATION bug check has a value of 0x00000133.
ms.assetid: CE9A4CBF-0016-42F7-A9EE-56DF6E61593A
keywords: ["Bug Check 0x133 DPC_WATCHDOG_VIOLATION", "DPC_WATCHDOG_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DPC_WATCHDOG_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x133 DPC\_WATCHDOG\_VIOLATION


The DPC\_WATCHDOG\_VIOLATION bug check has a value of 0x00000133. This bug check indicates that the DPC watchdog executed, either because it detected a single long-running deferred procedure call (DPC), or because the system spent a prolonged time at an interrupt request level (IRQL) of DISPATCH\_LEVEL or above. The value of Parameter 1 indicates whether a single DPC exceeded a timeout, or whether the system cumulatively spent an extended period of time at IRQL DISPATCH\_LEVEL or above. DPCs should not run longer than 100 microseconds and ISRs should not run longer than 25 microseconds, however the actual timeout values on the system are set much higher.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DPC\_WATCHDOG\_VIOLATION Parameters


*Parameter 1* indicates the type of violation. The meaning of the other parameters depends on the value of *Parameter 1*.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>The DPC time count (in ticks)</p></td>
<td align="left"><p>The DPC time allotment (in ticks).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A single DPC or ISR exceeded its time allotment. The offending component can usually be identified with a stack trace.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>The watchdog period</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The system cumulatively spent an extended period of time at IRQL DISPATCH_LEVEL or above. The offending component can usually be identified with a stack trace.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

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

[**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) to look at what code was running when the stop code occurred.

You may want to use the u, ub, uu (Unassemble) command to look deeper into the specifics of a the code that was running.

The [**!pcr**](-pcr.md) extension displays the current status of the Processor Control Region (PCR) on a specific processor. In the output will be the address of the Prcb

```dbgcmd
                     Prcb: fffff80309974180
```

You can use the [**dt (Display Type)**](dt--display-type-.md) command to display additional information about the DPCs and the DPC Watchdog. For the address use the Prcb listed in the !pcr output:

```dbgcmd
dt nt!_KPRCB fffff80309974180 Dpc* 
```

**Parameter 1 = 1**

For parameter of 1, the code may not stop in the offending area of code. In this case one approach is to use the event tracing to attempt to track down which driver is exceeding it's normal execution duration.

For more information see the following topics:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Using the !analyze Extension](using-the--analyze-extension.md) and [!analyze](-analyze.md)

Remarks
-------

In general this stop code is caused by faulty driver code that under certain conditions, does not complete its work within the allotted time frame.

If you are not equipped to use the Windows debugger to this problem, you should use some basic troubleshooting techniques.

-   If a driver is identified in the bug check message, to isolate the issue, disable the driver. Check with the manufacturer for driver updates.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing bug check 0x133.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

 

 




