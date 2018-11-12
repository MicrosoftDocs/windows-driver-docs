---
title: Bug Check 0xF5 FLTMGR_FILE_SYSTEM
description: The FLTMGR_FILE_SYSTEM bug check has a value of 0x000000F5. This indicates that an unrecoverable failure occurred in the Filter Manager.
ms.assetid: 9b008c76-65c8-4de4-b7a0-96d8732c7b7e
keywords: ["Bug Check 0xF5 FLTMGR_FILE_SYSTEM", "FLTMGR_FILE_SYSTEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- FLTMGR_FILE_SYSTEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF5: FLTMGR\_FILE\_SYSTEM


The FLTMGR\_FILE\_SYSTEM bug check has a value of 0x000000F5. This indicates that an unrecoverable failure occurred in the Filter Manager.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## FLTMGR\_FILE\_SYSTEM Parameters


Parameter 1 indicates the type of violation. The meaning of the other parameters depends on the value of Parameter 1.

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
<td align="left"><p>0x66</p></td>
<td align="left"><p>Pointer to the callback data structure for the operation.</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The minifilter returned FLT_PREOP_SUCCESS_WITH_CALLBACK or FLT_PREOP_SYNCHRONIZE from a preoperation callback, but did not register a corresponding postoperation callback.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x67</p></td>
<td align="left"><p>Pointer to the callback data structure for the operation.</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Error NTSTATUS code for the operation</p></td>
<td align="left"><p>An internal object ran out of space, and the system is unable to allocate new space.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x68</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Address of the FLT_FILE_NAME_INFORMATIONN structure</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A FLT_FILE_NAME_INFORMATION structure was dereferenced too many times.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6A</p></td>
<td align="left"><p>File object pointer for the file.</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The file-open or file-create request could not be canceled, because one or more handles have been created for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x6B</p></td>
<td align="left"><p>Frame ID</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Thread</p></td>
<td align="left"><p>Invalid BACKPOCKET IRPCTRL state.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6C</p></td>
<td align="left"><p>Frame ID</p></td>
<td align="left"><p>BackPocket List</p></td>
<td align="left"><p>Thread</p></td>
<td align="left"><p>Too many nested PageFaults for BACKPOCKETED IRPCTR.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x6D</p></td>
<td align="left"><p>Address of the minifilter&#39;s context structure</p></td>
<td align="left"><p>Address of the CONTEXT_NODE structure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The context structure was dereferenced too many times. This means that the reference count on the Filter Manager&#39;s CONTEXT_NODE structure went to zero while it was still attached to its associated object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6E</p></td>
<td align="left"><p>Address of the minifilter&#39;s context structure</p></td>
<td align="left"><p>Address of the CONTEXT_NODE structure</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The context structure was referenced after being freed.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The cause of the problem is indicated by the value of Parameter 1. See the table in the Parameters section.

Resolution
----------

If Parameter 1 equals **0x66**, you can debug this problem by verifying that your minifilter driver has registered a post-operation callback for this operation. The current operation can be found in the callback data structure. (See Parameter 2.) Use the **!fltkd.cbd** debugger extension.

If Parameter 1 equals **0x67**, you should verify that you do not have a nonpaged pool leak somewhere in the system.

If Parameter 1 equals **0x6A**, make sure that your minifilter driver does not reference this file object (see Parameter 2) to get a handle at any point during your minifilter's processing of this operation.

If Parameter 1 equals **0x6B** or **0x6C**, then a non-recoverable internal state error has occurred which will cause the operating system to bug check.

If Parameter 1 equals **0x6D**, make sure that your minifilter driver does not call **FltReleaseContext** too many times for the given context (see Parameter 2).

If Parameter 1 equals 0x6E, make sure that your minifilter driver does not call **FltReferenceContext** after the given context has been deleted (see Parameter 2).

 

 




