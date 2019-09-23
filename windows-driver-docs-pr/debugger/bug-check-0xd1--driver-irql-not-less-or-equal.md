---
title: Bug Check 0xD1 DRIVER_IRQL_NOT_LESS_OR_EQUAL
description: The DRIVER_IRQL_NOT_LESS_OR_EQUAL bug check has a value of 0x000000D1. This indicates that a kernel-mode driver attempted to access pageable memory at a process IRQL that was too high.
ms.assetid: 26cfd881-cc6e-4cc3-b464-e67d75700b96
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


## DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL Parameters


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
<td align="left"><p>Memory referenced.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>IRQL at time of reference.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p><strong>0:</strong> Read</p>
<p><strong>1:</strong> Write</p>
<p><strong>2:</strong> Execute</p>
<p><strong>8:</strong> Execute</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Address that referenced memory. Use `ln' on this address to see the name of the function.</p></td>
</tr>
</tbody>
</table>

Cause
-----

Typically, a driver tried to access an address that is pageable (or that is completely invalid) while the IRQL was too high.

This can be caused by:

1. Dereferencing a bad pointer (such as a NULL or freed pointer) while executing at or above DISPATCH_LEVEL.
2. Accessing pageable data at or above DISPATCH_LEVEL.
3. Executing pageable code at or above DISPATCH_LEVEL.

If a driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**. You can use the debugger dx command to display this - `dx KiBugCheckDriver`.

This bug check is usually caused by drivers that have used improper memory addresses.

Possible causes for the page fault include the following:

- The function was marked as pageable and was running at an elevated IRQL (which includes obtaining a lock).

- The function call was made to a function in another driver, and that driver was unloaded.

- The function was called by using a function pointer that was an invalid pointer.

Resolution
----------

If the problem is caused by the driver that you are developing, make sure that the function that was executing at the time of the bug check is not marked as pageable or does not call any other inline functions that could be paged out.

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

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

If a trap frame is available in the dump file use the `.trap` command to set your context to the provided address.

To start, examine the stack trace using the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command.

Use the `!IRQL` command to display information about the interrupt request level (IRQL) of a processor on the target computer before the debugger break.

```dbgcmd
0: kd> !irql
Debugger saved IRQL for processor 0x0 -- 2 (DISPATCH_LEVEL)
```

The majority of the time the issue is not the IRQL level, but rather the memory that is being accessed.

Because this bug check is usually caused by drivers that have used improper memory addresses, use parameters 1,3  and 4 to invesitgate further.

Use [ln (List Nearest Symbols)](ln--list-nearest-symbols-.md) with parameter 4 to see the name of the function that was called. Also examine the !analyze output to see if faulting code is identified.

Use [!pool](-pool.md) on the parameter 1 address to see whether it's paged pool. Use [!address](-address.md) and the advanced [!pte](-pte.md) command to learn more about this area of memory.

Use the [display memory](-db---dc---dd---dp---dq---du---dw.md) commands to examine the memory referenced in command in parameter 1.

Use the [Unassemble](u--unassemble-.md) command to look at the code in the address which referenced the memory in parameter 4.

Use the `lm t n` to list modules that are loaded in the memory. Use [!memusage](-memusage.md) and to examine the general state of the system memory. 

**Driver Verifier**

Driver Verifier is a tool that runs in real time to examine the behavior of drivers. For example, Driver Verifier checks the use of memory resources, such as memory pools. If it sees errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, type *Verifer* at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try and verify the smallest number of drivers as possible. For more information, see [Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier).

Remarks
-------

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

- Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

- If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

- Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

- For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).
