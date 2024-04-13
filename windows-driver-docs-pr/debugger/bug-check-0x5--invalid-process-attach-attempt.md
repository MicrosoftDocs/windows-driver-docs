---
title: Bug Check 0x5 INVALID_PROCESS_ATTACH_ATTEMPT
description: The INVALID_PROCESS_ATTACH_ATTEMPT bug check has a value of 0x00000005.
keywords: ["Bug Check 0x5 INVALID_PROCESS_ATTACH_ATTEMPT", "INVALID_PROCESS_ATTACH_ATTEMPT"]
ms.date: 09/04/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- INVALID_PROCESS_ATTACH_ATTEMPT
api_type:
- NA
---

# Bug Check 0x5: INVALID\_PROCESS\_ATTACH\_ATTEMPT


The INVALID\_PROCESS\_ATTACH\_ATTEMPT bug check has a value of 0x00000005. This generally indicates that the thread was attached to a process in a situation where that is not allowed. For example, this bug check could occur if **KeAttachProcess** was called when the thread was already attached to a process (which is illegal), or if the thread returned from certain function calls in an attached state (which is invalid),

This bug check appears very infrequently.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## INVALID\_PROCESS\_ATTACH\_ATTEMPT Parameters


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
<td align="left"><p>The pointer to the dispatcher object for the target process, or if the thread is already attached, the pointer to the object for the original process.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The pointer to the dispatcher object of the process that the current thread is currently attached to.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The value of the thread's APC state index.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>A non-zero value indicates that a DPC is running on the current processor.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

This bug check can occur if the driver calls the [KeAttachProcess](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-keattachprocess)  function and the thread is already attached to another process. It is better to use the [KeStackAttachProcess](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-kestackattachprocess) function. If the current thread was already attached to another process, the **KeStackAttachProcess** function saves the current APC state before it attaches the current thread to the new process. Calling **KeStackAttachProcess** incorrectly can also cause this bug check, for example if a DPC is running on the current processor.

For general information about this area, see working with [Windows Kernel-Mode Process and Thread Manager](../kernel/windows-kernel-mode-process-and-thread-manager.md) and [Introduction to Kernel Dispatcher Objects](../kernel/managing-interlocked-queues-with-a-driver-created-thread.md).

 

