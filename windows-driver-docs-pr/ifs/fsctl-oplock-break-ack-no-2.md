---
title: FSCTL\_OPLOCK\_BREAK\_ACK\_NO\_2 control code
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_OPLOCK_BREAK_ACK_NO_2%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





