---
title: Bug Check 0xEA THREAD_STUCK_IN_DEVICE_DRIVER
description: The THREAD_STUCK_IN_DEVICE_DRIVER bug check has a value of 0x000000EA. This indicates that a thread in a device driver is endlessly spinning.
keywords: ["Bug Check 0xEA THREAD_STUCK_IN_DEVICE_DRIVER", "THREAD_STUCK_IN_DEVICE_DRIVER"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- THREAD_STUCK_IN_DEVICE_DRIVER
api_type:
- NA
---

# Bug Check 0xEA: THREAD\_STUCK\_IN\_DEVICE\_DRIVER


The THREAD\_STUCK\_IN\_DEVICE\_DRIVER bug check has a value of 0x000000EA. This indicates that a thread in a device driver is endlessly spinning.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## THREAD\_STUCK\_IN\_DEVICE\_DRIVER Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>A pointer to the stuck thread object</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>A pointer to the DEFERRED_WATCHDOG object</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>A pointer to the offending driver name</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p><strong>In the kernel debugger:</strong> The number of times the "intercepted" bug check 0xEA was hit</p>
<p><strong>On the blue screen:</strong> 1</p></td>
</tr>
</tbody>
</table>

 

## Cause

A device driver is spinning in an infinite loop, most likely waiting for hardware to become idle.

This usually indicates problem with the hardware itself, or with the device driver programming the hardware incorrectly. Frequently, this is the result of a bad video card or a bad display driver.

## Resolution

The [!analyze](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

Use the [**.thread (Set Register Context)**](../debuggercmds/-thread--set-register-context-.md) command together with Parameter 1. Then use [**kb (Display Stack Backtrace)**](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) to find the location where the thread is stuck.

If the kernel debugger is already connected and running when Windows detects a time-out condition. Then **DbgBreakPoint** will be called instead of **KeBugCheckEx**. A detailed message will be printed to the debugger. See [Sending Output to the Debugge](sending-output-to-the-debugger.md)for more information.

This message will include what would have been the bug check parameters. Because no actual bug check was issued, the [**.bugcheck (Display Bug Check Data)**](../debuggercmds/-bugcheck--display-bug-check-data-.md) command will not be useful. The four parameters can also be retrieved from Watchdog's global variables by using **dd watchdog!g\_WdBugCheckData L5**" on a 32-bit system, or **dq watchdog!g\_WdBugCheckData L5**" on a 64-bit system.

Debugging this error in an interactive manner such as this will enable you to find an offending thread, set breakpoints in it, and then use [**g (Go)**](../debuggercmds/g--go-.md) to return to the spinning code to debug it further.

On multiprocessor machines (OS build 3790 or earlier), you can hit a time out if the spinning thread is interrupted by a hardware interrupt and an ISR or DPC routine is running at the time of the bug check. This is because the time out's work item can be delivered and handled on the second CPU and the same time. If this occurs, you must look deeper at the offending thread's stack to determine the spinning code which caused the time out to occur. Use the [**dds (Display Words and Symbols)**](../debuggercmds/dds--dps--dqs--display-words-and-symbols-.md) command to do this.

 

 




