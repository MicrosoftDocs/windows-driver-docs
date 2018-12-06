---
title: FSCTL_OPBATCH_ACK_CLOSE_PENDING control code
description: The FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING control code responds to notification that an exclusive (level 1, batch, or filter) opportunistic lock (oplock) on a file has been broken.
ms.assetid: 310cd778-5a1c-46e2-8c05-127fc754ecfe
keywords: ["FSCTL_OPBATCH_ACK_CLOSE_PENDING control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_OPBATCH_ACK_CLOSE_PENDING
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING control code


The **FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING** control code responds to notification that an exclusive (level 1, batch, or filter) opportunistic lock (oplock) on a file has been broken. A client application sends this control code to indicate that it acknowledges the oplock break and it is about to close the file handle.

For a batch or filter oplock break, the caller must close its file handle after sending this control code. Otherwise, the system will block waiting for the file handle to be closed.

This control code is not intended to be used with level 1 oplocks. Nevertheless, for a level 1 oplock break, the system treats this control code as a complete acknowledgment of the break, and the caller is not required to close the file handle.

This control code is rarely used. When a client application is notified of an oplock break for a file, and it closes its handle for the file, the system treats the file handle close as a complete acknowledgment of the oplock break. Thus it is never necessary to send this control code.

To process this control code, a minifilter calls [**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) with the following parameters. A file system or legacy filter driver calls [**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112).

For more information about opportunistic locking and about the FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING control code, see the Microsoft Windows SDK documentation.

**Parameters**

<a href="" id="oplock"></a>*Oplock*  
Opaque oplock object pointer for the file.

<a href="" id="callbackdata"></a>*CallbackData*  
[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) only. Callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING.

<a href="" id="irp"></a>*Irp*  
[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112) only. IRP for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_OPBATCH\_ACK\_CLOSE\_PENDING.

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
<td align="left"><p>The oplock held by this handle was in the process of being broken.</p></td>
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

[**FLT\_PARAMETERS for IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398)

[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](fsctl-oplock-break-ack-no-2.md)

[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](fsctl-oplock-break-acknowledge.md)

[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](fsctl-oplock-break-notify.md)

[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](fsctl-request-batch-oplock.md)

[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](fsctl-request-filter-oplock.md)

[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](fsctl-request-oplock-level-1.md)

[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](fsctl-request-oplock-level-2.md)

[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

 

 






