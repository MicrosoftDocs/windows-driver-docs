---
title: FSCTL\_REQUEST\_OPLOCK control code
description: The FSCTL\_REQUEST\_OPLOCK control code requests an opportunistic lock (oplock) on a file, or acknowledges that an oplock break has occurred.
ms.assetid: a36f2a13-d450-4903-b999-6ba574ab3f6e
keywords: ["FSCTL_REQUEST_OPLOCK control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_REQUEST_OPLOCK
api_location:
- Ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_REQUEST\_OPLOCK control code


The **FSCTL\_REQUEST\_OPLOCK** control code requests an opportunistic lock (oplock) on a file, or acknowledges that an oplock break has occurred.

For more information about opportunistic locks and about the **FSCTL\_REQUEST\_OPLOCK** control code, see the Microsoft Windows SDK documentation.

To process this control code, a file system or filter driver calls [**FsRtlOplockFsctrlEx**](https://msdn.microsoft.com/library/windows/hardware/ff547113) with the following parameters.

**Parameters**

<a href="" id="oplock"></a>*Oplock*  
Opaque oplock object pointer for the file.

<a href="" id="irp"></a>*Irp*  
A pointer to the IRP for an IRP\_MJ\_FILE\_SYSTEM\_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL\_REQUEST\_OPLOCK.

<a href="" id="opencount"></a>*OpenCount*  
The number of user handles for the file if the request is for an exclusive oplock. If the request is for an oplock that can be shared, *OpenCount* is zero if no byte-range locks exist on the file. Otherwise, *OpenCount* is nonzero. The caller can call the [**FsRtlOplockIsSharedRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547128) routine on the IRP to determine if the request is for an oplock that can be shared.

<a href="" id="flags"></a>*Flags*  
A bitmask for the associated oplock operations. A file system or filter driver sets bits to specify the behavior of [**FsRtlOplockFsctrlEx**](https://msdn.microsoft.com/library/windows/hardware/ff547113). The *Flags* parameter has the following options:

<a href="" id="oplock-fsctrl-flag-all-keys-match--0x00000001-"></a>OPLOCK\_FSCTRL\_FLAG\_ALL\_KEYS\_MATCH (0x00000001)  
Specifies that the file system has verified that all opportunistic lock keys match on any handle that is currently open. By specifying this flag, the oplock package can grant an oplock of level RW or RWH when more than one open handle to the file exists. For more information about oplock types, see [Overview](https://msdn.microsoft.com/library/windows/hardware/ff551011).

Status block
------------

[**FsRtlOplockFsctrlEx**](https://msdn.microsoft.com/library/windows/hardware/ff547113) returns one of the following NTSTATUS values for this operation:

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
<td align="left"><p>The IRP was canceled before the FSCTL_REQUEST_OPLOCK operation was completed. This is an error code.</p></td>
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


[**FsRtlOplockFsctrlEx**](https://msdn.microsoft.com/library/windows/hardware/ff547113)

[**FsRtlOplockIsSharedRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547128)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_REQUEST_OPLOCK%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





