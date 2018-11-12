---
title: Bug Check 0x103 MUP_FILE_SYSTEM
description: The MUP_FILE_SYSTEM bug check has a value of 0x00000103.
ms.assetid: 2756bdcc-5b10-481e-99ec-17b00c4f459d
keywords: ["Bug Check 0x103 MUP_FILE_SYSTEM", "MUP_FILE_SYSTEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MUP_FILE_SYSTEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x103: MUP\_FILE\_SYSTEM


The MUP\_FILE\_SYSTEM bug check has a value of 0x00000103. This bug check indicates that the multiple UNC provider (MUP) has encountered invalid or unexpected data. As a result, the MUP cannot channel a remote file system request to a network redirector, the Universal Naming Convention (UNC) provider.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MUP\_FILE\_SYSTEM Parameters


Parameter 1 identifies the type of violation.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The address of the pending IRP.</p></td>
<td align="left"><p>The address of the file object whose file context could not be found.</p></td>
<td align="left"><p>The address of the device object.</p></td>
<td align="left"><p>The MUP could not locate the file context that corresponds to a file object. This typically indicates that the MUP is seeing an I/O request for a file object for which MUP did not see a corresponding IRP_MJ_CREATE request. The likely cause of this bug check is a filter driver error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>The address of the expected file context.</p></td>
<td align="left"><p>The address that was actually retrieved from the file object.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A file context is known to exist for the file object, but was not what was expected (for example, it might be <strong>NULL</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The address of the IRP context.</p></td>
<td align="left"><p>The IRP completion status code.</p></td>
<td align="left"><p>The driver object of the UNC provider that completed the IRP (might be <strong>NULL</strong>).</p></td>
<td align="left"><p>The IRP completion status was unexpected or invalid.</p>
<p>This bug check occurs only when you are using a Checked Build of Windows and should only be caused by file system filter drivers that are attached to legacy network redirectors. Legacy redirectors use <strong>FsRtlRegisterUncProvider</strong> to register with MUP. This bug check detects filter drivers that return an NTSTATUS that is not STATUS_SUCCESS in IRP_MJ_CLEANUP or IRP_MJ_CLOSE requests.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>Address of the IRP</p></td>
<td align="left"><p>Address of the file object</p></td>
<td align="left"><p>The file context for the file object</p></td>
<td align="left"><p>An I/O operation was started on a file object before the create request for the file object was completed.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The MUP maintains context information on a per-file object basis for all file objects it handles.

 

 




