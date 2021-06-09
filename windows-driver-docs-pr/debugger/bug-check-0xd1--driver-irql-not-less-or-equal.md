---
title: Bug Check 0xD1 DRIVER_IRQL_NOT_LESS_OR_EQUAL
description: The DRIVER_IRQL_NOT_LESS_OR_EQUAL bug check has a value of 0x000000D1. This indicates that a kernel-mode driver attempted to access pageable memory at a process IRQL that was too high.
keywords: ["Bug Check 0xD1 DRIVER_IRQL_NOT_LESS_OR_EQUAL", "DRIVER_IRQL_NOT_LESS_OR_EQUAL"]
ms.date: 03/28/2019
topic_type:
- apiref
api_name:
- DRIVER_IRQL_NOT_LESS_OR_EQUAL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xD1: DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL


The DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL bug check has a value of 0x000000D1. This indicates that a kernel-mode driver attempted to access pageable memory while the process IRQL that was too high. 

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL parameters

<table>
<colgroup>
<col width="20%" />
<col width="80%" />
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
<td align="left"><p>Memory referenced.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>IRQL at time of reference.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><ul>
<li>0 - Read</li>
<li>1 - Write</li>
<li>2 - Execute</li>
<li>8 - Execute</li>
</td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Address that referenced memory. Use <a href="./ln--list-nearest-symbols-.md"><strong>ln</strong> (list nearest symbols)</a> on this address to see the name of the function.</p></td>
</tr>
</tbody>
</table>


## Cause

Typically, when this error occurs, a driver has tried to access an address that is pageable (or that is completely invalid) while the interrupt request level (IRQL) was too high. This can be caused by:

 - Dereferencing a bad pointer (such as a NULL or freed pointer) while executing at or above DISPATCH_LEVEL.

 - Accessing pageable data at or above DISPATCH_LEVEL.

 - Executing pageable code at or above DISPATCH_LEVEL.

If a driver that is responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**. You can use [**dx** (display debugger object model expression)](dx--display-visualizer-variables-.md), a debugger command, to display this: **dx KiBugCheckDriver**.

This bug check is usually caused by drivers that have used improper memory addresses.

Possible causes for the page fault include the following events:

- The function was marked as pageable and was running at an elevated IRQL (which includes obtaining a lock).

- The function call was made to a function in another driver, and that driver was unloaded.

- The function was called by using a function pointer that was an invalid pointer.


## Resolution

If the problem is caused by the driver that you are developing, make sure that the function that was executing at the time of the bug check is (1) not marked as pageable or (2) does not call any other inline functions that could be paged out.

The [**!analyze**](-analyze.md) debugger extension displays information about the bug check and can be helpful in determining the root cause. The following example is output from **!analyze**.

```dbgcmd
DRIVER_IRQL_NOT_LESS_OR_EQUAL (d1)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.  This is usually
caused by drivers using improper addresses.
If kernel debugger is available get stack backtrace.
Arguments:
Arg1: fffff808add27150, memory referenced
Arg2: 0000000000000002, IRQL
Arg3: 0000000000000000, value 0 = read operation, 1 = write operation
Arg4: fffff808adc386a6, address which referenced memory
```

If a trap frame is available in the dump file, use the [**.trap**](-trap--display-trap-frame-.md) command to set your context to the provided address.

To start debugging this type of bug check, examine the stack trace by using the [**k**, **kb**, **kc**, **kd**, **kp**, **kP**, **kv** (display stack backtrace)](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands.

In the debugger, run the [**!irql**](-irql.md) command to display information about the IRQL of a processor on the target computer before the debugger break. For example:

```dbgcmd
0: kd> !irql
Debugger saved IRQL for processor 0x0 -- 2 (DISPATCH_LEVEL)
```

In the majority of cases of this type of bug check, the issue is not the IRQL level, but rather the memory that is being accessed.

Because this bug check is usually caused by drivers that have used improper memory addresses, use parameters 1, 3, and 4 to investigate further.

Use [**ln** (list nearest symbols)](ln--list-nearest-symbols-.md) with parameter 4 to see the name of the function that was called. Also examine the **!analyze** output to see if faulting code is identified.

Use [**!pool**](-pool.md) on the parameter 1 address to see whether it is paged pool. Use [**!address**](-address.md) and the advanced [**!pte**](-pte.md) command to learn more about this area of memory.

Use the [display memory](-db---dc---dd---dp---dq---du---dw.md) commands to examine the memory referenced in command in parameter 1.

Use the [**u**, **ub**, **uu** (unassemble)](u--unassemble-.md) commands to look at the code in the address which referenced the memory in parameter 4.

Use the command `lm t n` to list modules that are loaded in the memory. Use [**!memusage**](-memusage.md) and to examine the general state of the system memory. 


### Driver Verifier

Driver Verifier is a tool that runs in real time to examine the behavior of drivers. For example, Driver Verifier checks the use of memory resources, such as memory pools. If it identifies errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. Driver Verifier Manager is built into Windows and is available on all Windows PCs.

To start Driver Verifier Manager, type **verifier** at a command prompt. You can configure which drivers to verify. The code that verifies drivers adds overhead as it runs, so try to verify the smallest number of drivers possible. For more information, see [Driver Verifier](../devtest/driver-verifier.md).


## Remarks

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

- Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

- If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

- Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

For additional general troubleshooting information, see [Blue screen data](blue-screen-data.md).
