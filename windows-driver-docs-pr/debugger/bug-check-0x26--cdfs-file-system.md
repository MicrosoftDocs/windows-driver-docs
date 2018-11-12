---
title: Bug Check 0x26 CDFS_FILE_SYSTEM
description: The CDFS_FILE_SYSTEM bug check has a value of 0x00000026. This indicates that a problem occurred in the CD file system.
ms.assetid: f427c262-f750-4719-a52b-2f00094d2a4e
keywords: ["Bug Check 0x26 CDFS_FILE_SYSTEM", "CDFS_FILE_SYSTEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CDFS_FILE_SYSTEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x26: CDFS\_FILE\_SYSTEM


The CDFS\_FILE\_SYSTEM bug check has a value of 0x00000026. This indicates that a problem occurred in the CD file system.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## CDFS\_FILE\_SYSTEM Parameters


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
<td align="left"><p>Specifies source file and line number information. The high 16 bits (the first four hexadecimal digits after the &quot;0x&quot;) identify the source file by its identifier number. The low 16 bits identify the source line in the file where the bug check occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>If <strong>CdExceptionFilter</strong> is on the stack, this parameter specifies the address of the exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>If <strong>CdExceptionFilter</strong> is on the stack, this parameter specifies the address of the context record.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

One possible cause of this bug check is disk corruption. Corruption in the file system or bad blocks (sectors) on the disk can induce this error. Corrupted SCSI and IDE drivers can also adversely affect the system's ability to read and write to the disk, thus causing the error.

Another possible cause is depletion of nonpaged pool memory. If the nonpaged pool memory is completely depleted, this error can stop the system. However, during the indexing process, if the amount of available nonpaged pool memory is very low, another kernel-mode driver requiring nonpaged pool memory can also trigger this error.

Resolution
----------

**To debug this problem:** Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command with Parameter 3, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md).

**To resolve a disk corruption problem:** Check Event Viewer for error messages from SCSI and FASTFAT (System Log) or Autochk (Application Log) that might help pinpoint the device or driver that is causing the error. Try disabling any virus scanners, backup programs, or disk defragmenter tools that continually monitor the system. You should also run hardware diagnostics supplied by the system manufacturer. For details on these procedures, see the owner's manual for your computer. Run **Chkdsk /f /r** to detect and resolve any file system structural corruption. You must restart the system before the disk scan begins on a system partition.

**To resolve a nonpaged pool memory depletion problem:** Add new physical memory to the computer. This will increase the quantity of nonpaged pool memory available to the kernel.

 

 




