---
title: Bug Check 0x9B UDFS_FILE_SYSTEM
description: The UDFS_FILE_SYSTEM bug check has a value of 0x0000009B. This bug check indicates that a problem occurred in the UDF file system.
ms.assetid: cf20429d-6007-47e7-9faa-db7e1489e96b
keywords: ["Bug Check 0x9B UDFS_FILE_SYSTEM", "UDFS_FILE_SYSTEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- UDFS_FILE_SYSTEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x9B: UDFS\_FILE\_SYSTEM


The UDFS\_FILE\_SYSTEM bug check has a value of 0x0000009B. This bug check indicates that a problem occurred in the UDF file system.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## UDFS\_FILE\_SYSTEM Parameters


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
<td align="left"><p>The source file and line number information. The high 16 bits (the first four hexadecimal digits after the &quot;0x&quot;) identify the source file by its identifier number. The low 16 bits identify the source line in the file where the bug check occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>If <strong>UdfExceptionFilter</strong> is on the stack, this parameter specifies the address of the exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>If <strong>UdfExceptionFilter</strong> is on the stack, this parameter specifies the address of the context record.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The UDFS\_FILE\_SYSTEM bug check might be caused disk corruption. Corruption in the file system or bad blocks (sectors) on the disk can induce this error. Corrupted SCSI and IDE drivers can also adversely affect the system's ability to read and write to the disk and cause the error.

This bug check might also occur if nonpaged pool memory is full. If the nonpaged pool memory is full, this error can stop the system. However, during the indexing process, if the amount of available nonpaged pool memory is very low, another kernel-mode driver that requires nonpaged pool memory can also trigger this error.

Resolution
----------

**To debug this problem:** Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command with Parameter 3, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md).

**To resolve a disk corruption problem:** Check Event Viewer for error messages from SCSI and FASTFAT (System Log) or Autochk (Application Log) that might help identify the device or driver that is causing the error. Disable any virus scanners, backup application, or disk defragmenter tools that continually monitor the system. You should also run hardware diagnostics that the system manufacturer supplies. For more information about these procedures, see the owner's manual for your computer. Run **Chkdsk /f /r** to detect and resolve any file system structural corruption. You must restart the system before the disk scan begins on a system partition.

**To resolve a nonpaged pool memory depletion problem:** Add new physical memory to the computer. This memory increases the quantity of nonpaged pool memory that is available to the kernel.

 

 




