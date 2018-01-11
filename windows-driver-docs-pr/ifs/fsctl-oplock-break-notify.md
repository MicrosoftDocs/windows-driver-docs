---
title: FSCTL\_OPLOCK\_BREAK\_NOTIFY control code
description: The FSCTL\_OPLOCK\_BREAK\_NOTIFY control code allows the calling application to wait for completion of an opportunistic lock (oplock) break.
ms.assetid: 80fe4e5f-fb6f-4c11-8574-97d7f0e7cc6b
keywords: ["FSCTL_OPLOCK_BREAK_NOTIFY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_OPLOCK_BREAK_NOTIFY
api_location:
- ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_OPLOCK\_BREAK\_NOTIFY control code


The **FSCTL\_OPLOCK\_BREAK\_NOTIFY** control code allows the calling application to wait for completion of an opportunistic lock (oplock) break.

This operation is useful only for an oplock break that was already initiated when the caller's handle was opened. The handle must have been opened with FILE\_COMPLETE\_IF\_OPLOCKED. This operation is meaningless if an oplock is currently held and the oplock break has not started.

To process this control code, a minifilter calls [**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) with the following parameters. A file system or legacy filter driver calls [**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112).

For more information about opportunistic locking and about the **FSCTL\_OPLOCK\_BREAK\_NOTIFY** control code, see the Microsoft Windows SDK documentation.

**Parameters**

<a href="" id="oplock"></a>*Oplock*  
Opaque oplock object pointer for the file.

<a href="" id="callbackdata"></a>*CallbackData*  
[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) only. Callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_OPLOCK\_BREAK\_NOTIFY.

<a href="" id="irp"></a>*Irp*  
[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112) only. IRP for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_OPLOCK\_BREAK\_NOTIFY.

<a href="" id="opencount"></a>*OpenCount*  
Not used with this operation; set to zero.

Status block
------------

[**FltOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff543398) returns FLT\_PREOP\_PENDING if the oplock break is underway, and the IRP will be completed when the oplock break completes. (In this case, the IRP can eventually complete with either STATUS\_SUCCESS or STATUS\_CANCELLED.) Otherwise, **FltOplockFsctrl** returns FLT\_PREOP\_COMPLETE.

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
<td align="left"><p>No oplock was held by this handle, or an oplock is held and the oplock break has not started.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_OPLOCK_PROTOCOL</strong></p></td>
<td align="left"><p>The IRP was canceled before the FSCTL_OPLOCK_BREAK_NOTIFY operation was completed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_PENDING</strong></p></td>
<td align="left"><p>The oplock break is underway. The IRP will be completed when the oplock break completes. The IRP can eventually complete with either STATUS_SUCCESS or STATUS_CANCELLED. This is a success code.</p></td>
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

[**FSCTL\_REQUEST\_BATCH\_OPLOCK**](fsctl-request-batch-oplock.md)

[**FSCTL\_REQUEST\_FILTER\_OPLOCK**](fsctl-request-filter-oplock.md)

[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1**](fsctl-request-oplock-level-1.md)

[**FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2**](fsctl-request-oplock-level-2.md)

[**FsRtlOplockFsctrl**](https://msdn.microsoft.com/library/windows/hardware/ff547112)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_OPLOCK_BREAK_NOTIFY%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





