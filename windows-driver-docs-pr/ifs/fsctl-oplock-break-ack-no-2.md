---
title: FSCTL_OPLOCK_BREAK_ACK_NO_2 control code
description: The FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2 control code responds to notification that an exclusive (level 1, batch, or filter) opportunistic lock (oplock) on a file has been broken.
ms.assetid: f76c98ba-e0bf-4b86-bda4-92f233ea5839
keywords: ["FSCTL_OPLOCK_BREAK_ACK_NO_2 control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_OPLOCK_BREAK_ACK_NO_2
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2 control code


The **FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2** control code responds to notification that an exclusive (level 1, batch, or filter) opportunistic lock (oplock) on a file has been broken.

A client application sends this control code to indicate that it acknowledges the oplock break and that, if the oplock is a level 1 oplock that was broken to level 2, it does not want the level 2 oplock.

To process this control code, a minifilter calls [**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) with the following parameters. A file system or legacy filter driver calls [**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112).

For more information about opportunistic locking and about the FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2 control code, see the Microsoft Windows SDK documentation.

**Parameters**

<a href="" id="oplock"></a>*Oplock*  
Opaque oplock object pointer for the file.

<a href="" id="callbackdata"></a>*CallbackData*  
[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) only. Callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2.

<a href="" id="irp"></a>*Irp*  
[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112) only. IRP for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2.

<a href="" id="opencount"></a>*OpenCount*  
Not used with this operation; set to zero.

Status block
------------

[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) always returns FLT\_PREOP\_COMPLETE for this operation.

[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112) returns one of the following NTSTATUS values for this operation:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>STATUS_SUCCESS</strong></p></td>
<td align="left"><p>The oplock break is acknowledged. No remaining oplocks are held.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_OPLOCK_PROTOCOL</strong></p></td>
<td align="left"><p>No oplock was held by this handle, or the oplock break is not currently in progress. This is an error code.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**FLT\_PARAMETERS for IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398)

[**FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING**](fsctl-opbatch-ack-close-pending.md)

[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](fsctl-oplock-break-acknowledge.md)

[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](fsctl-oplock-break-notify.md)

[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](fsctl-request-batch-oplock.md)

[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](fsctl-request-filter-oplock.md)

[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](fsctl-request-oplock-level-1.md)

[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](fsctl-request-oplock-level-2.md)

[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

 

 






