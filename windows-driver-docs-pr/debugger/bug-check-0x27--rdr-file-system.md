---
title: Bug Check 0x27 RDR_FILE_SYSTEM
description: The RDR_FILE_SYSTEM bug check has a value of 0x00000027. This indicates that a problem occurred in the SMB redirector file system.
ms.assetid: 1294022d-7281-45d2-89c8-40d11ce202f0
keywords: ["Bug Check 0x27 RDR_FILE_SYSTEM", "RDR_FILE_SYSTEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- RDR_FILE_SYSTEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x27: RDR\_FILE\_SYSTEM


The RDR\_FILE\_SYSTEM bug check has a value of 0x00000027. This indicates that a problem occurred in the SMB redirector file system.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## RDR\_FILE\_SYSTEM Parameters


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
<td align="left"><p>The high 16 bits (the first four hexadecimal digits after the &quot;0x&quot;) identify the type of problem. Possible values include:</p>
<p>0xCA550000 RDBSS_BUG_CHECK_CACHESUP</p>
<p>0xC1EE0000 RDBSS_BUG_CHECK_CLEANUP</p>
<p>0xC10E0000 RDBSS_BUG_CHECK_CLOSE</p>
<p>0xBAAD0000 RDBSS_BUG_CHECK_NTEXCEPT</p>
<p></p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>If <strong>RxExceptionFilter</strong> is on the stack, this parameter specifies the address of the exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>If <strong>RxExceptionFilter</strong> is on the stack, this parameter specifies the address of the context record.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

One possible cause of this bug check is depletion of nonpaged pool memory. If the nonpaged pool memory is completely depleted, this error can stop the system. However, during the indexing process, if the amount of available nonpaged pool memory is very low, another kernel-mode driver requiring nonpaged pool memory can also trigger this error.

Resolution
----------

**To debug this problem:** Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command with Parameter 3, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md).

**To resolve a nonpaged pool memory depletion problem:** Add new physical memory to the computer. This will increase the quantity of nonpaged pool memory available to the kernel.

 

 




