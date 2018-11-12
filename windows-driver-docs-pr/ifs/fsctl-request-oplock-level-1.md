---
title: FSCTL_REQUEST_OPLOCK_LEVEL_1 control code
description: The FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1 control code requests a level 1 opportunistic lock (oplock) on a file.
ms.assetid: 67ffb92c-d638-46fc-9afb-9f1322db2f3b
keywords: ["FSCTL_REQUEST_OPLOCK_LEVEL_1 control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_REQUEST_OPLOCK_LEVEL_1
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1 control code


The **FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1** control code requests a level 1 opportunistic lock (oplock) on a file.

To process this control code, a minifilter calls [**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) with the following parameters. A file system or legacy filter driver calls [**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112).

For more information about opportunistic locking and about the **FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1** control code, see the Microsoft Windows SDK documentation.

**Parameters**

<a href="" id="oplock"></a>*Oplock*  
Opaque oplock object pointer for the file.

<a href="" id="callbackdata"></a>*CallbackData*  
[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) only. Callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1.

<a href="" id="irp"></a>*Irp*  
[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112) only. IRP for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1.

<a href="" id="opencount"></a>*OpenCount*  
Number of user handles for the file.

Status block
------------

[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) returns FLT\_PREOP\_PENDING for this operation if the oplock was granted. Otherwise, it returns FLT\_PREOP\_COMPLETE.

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
<td align="left"><p><strong>STATUS_PENDING</strong></p></td>
<td align="left"><p>The oplock was granted. This is a success code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_CANCELLED</strong></p></td>
<td align="left"><p>The IRP was canceled before the FSCTL_REQUEST_OPLOCK_LEVEL_1 operation was completed. This is an error code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_OPLOCK_NOT_GRANTED</strong></p></td>
<td align="left"><p>The oplock could not be granted. This is an error code.</p></td>
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

[**FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2**](fsctl-oplock-break-ack-no-2.md)

[**FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE**](fsctl-oplock-break-acknowledge.md)

[**FSCTL\_OPLOCK\_BREAK\_NOTIFY**](fsctl-oplock-break-notify.md)

[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](fsctl-request-batch-oplock.md)

[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](fsctl-request-filter-oplock.md)

[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](fsctl-request-oplock-level-2.md)

[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

 

 






