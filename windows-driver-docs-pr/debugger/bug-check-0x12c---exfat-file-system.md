---
title: Bug Check 0x12C EXFAT_FILE_SYSTEM
description: The EXFAT_FILE_SYSTEM bug check has a value of 0x0000012C. This bug check indicates that a problem occurred in the Extended File Allocation Table (exFAT) file system.
ms.assetid: f55bbe88-d96f-494f-b84b-eda7c4e6bdfc
keywords: ["Bug Check 0x12C EXFAT_FILE_SYSTEM", "EXFAT_FILE_SYSTEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- EXFAT_FILE_SYSTEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x12C: EXFAT\_FILE\_SYSTEM


The EXFAT\_FILE\_SYSTEM bug check has a value of 0x0000012C. This bug check indicates that a problem occurred in the Extended File Allocation Table (exFAT) file system.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## EXFAT\_FILE\_SYSTEM Parameters


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
<td align="left"><p>Specifies source file and line number information. The high 16 bits (the first four hexadecimal digits after the &quot;0x&quot;) determine the source file by its identifier number. The low 16 bits determine the source line in the file where the bug check occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>If <strong>FppExceptionFilter</strong> is on the stack, this parameter specifies the address of the exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>If <strong>FppExceptionFilter</strong> is on the stack, this parameter specifies the address of the context record.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This bug check is caused by the file system as a last resort when its internal accounting is in an unsupportable state and to continue poses a large risk of data loss. The file system never causes this bug check when the on disk structures are corrupted, the disk sectors go bad, or a memory allocation fails. Bad sectors could lead to a bug check, for example, when a page fault occurs in kernel code or data and the memory manager cannot read the pages. However, for this bug check, the file system is not the cause.

Resolution
----------

**To debug this problem:** Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command together with Parameter 3, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md).

 

 




