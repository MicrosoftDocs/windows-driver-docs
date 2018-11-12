---
title: Bug Check 0x108 THIRD_PARTY_FILE_SYSTEM_FAILURE
description: The THIRD_PARTY_FILE_SYSTEM_FAILURE bug check has a value of 0x00000108. This indicates that an unrecoverable problem has occurred in a third-party file system or file system filter.
ms.assetid: 1ed82617-b0f0-4b41-9af9-b309b6b75dfd
keywords: ["Bug Check 0x108 THIRD_PARTY_FILE_SYSTEM_FAILURE", "THIRD_PARTY_FILE_SYSTEM_FAILURE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- THIRD_PARTY_FILE_SYSTEM_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x108: THIRD\_PARTY\_FILE\_SYSTEM\_FAILURE


The THIRD\_PARTY\_FILE\_SYSTEM\_FAILURE bug check has a value of 0x00000108. This indicates that an unrecoverable problem has occurred in a third-party file system or file system filter.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## THIRD\_PARTY\_FILE\_SYSTEM\_FAILURE Parameters


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
<td align="left"><p>Identifies the file system that failed. Possible values include:</p>
<p><strong>1:</strong> Polyserve (Psfs.sys)</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address of the exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the context record.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

One possible cause of this bug check is disk corruption. Corruption in the third-party file system or bad blocks (sectors) on the hard disk can induce this error. Corrupted SCSI and IDE drivers can also adversely affect the Windows operating system's ability to read and write to disk, thus causing the error.

Another possible cause is depletion of nonpaged pool memory. If the nonpaged pool is completely depleted, this error can stop the system.

Resolution
----------

**To debug this problem:** Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command with Parameter 3, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md).

**To resolve a disk corruption problem:** Check Event Viewer for error messages from SCSI, IDE, or other disk controllers in the system that might help pinpoint the device or driver that is causing the error. Try disabling any virus scanners, backup programs, or disk defragmenter tools that continually monitor the system. You should also run hardware diagnostics supplied by the file system or the file system filter manufacturer.

**To resolve a nonpaged pool memory depletion problem:** Add new physical memory to the computer. This will increase the quantity of nonpaged pool memory available to the kernel.

 

 




