---
title: Bug Check 0x5 INVALID_PROCESS_ATTACH_ATTEMPT
description: The INVALID_PROCESS_ATTACH_ATTEMPT bug check has a value of 0x00000005.
ms.assetid: 72efb88f-1bf7-4552-b44e-4ecb04754b7d
keywords: ["Bug Check 0x5 INVALID_PROCESS_ATTACH_ATTEMPT", "INVALID_PROCESS_ATTACH_ATTEMPT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_PROCESS_ATTACH_ATTEMPT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x5: INVALID\_PROCESS\_ATTACH\_ATTEMPT


The INVALID\_PROCESS\_ATTACH\_ATTEMPT bug check has a value of 0x00000005. This generally indicates that the thread was attached to a process in a situation where that is not allowed. For example, this bug check could occur if **KeAttachProcess** was called when the thread was already attached to a process (which is illegal), or if the thread returned from certain function calls in an attached state (which is invalid),

This bug check appears very infrequently.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

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
<td align="left"><p>The value of the thread&#39;s APC state index.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>A non-zero value indicates that a DPC is running on the current processor.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This bug check can occur if the driver calls the **KeAttachProcess** function and the thread is already attached to another process. It is better to use the **KeStackAttachProcess** function. If the current thread was already attached to another process, the **KeStackAttachProcess** function saves the current APC state before it attaches the current thread to the new process.

 

 




