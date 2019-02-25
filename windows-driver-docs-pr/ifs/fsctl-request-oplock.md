---
title: FSCTL_REQUEST_OPLOCK control code
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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_REQUEST\_OPLOCK control code


The **FSCTL\_REQUEST\_OPLOCK** control code requests an opportunistic lock (oplock) on a file, or acknowledges that an oplock break has occurred.

For more information about opportunistic locks, see [Opportunistic Locks](https://docs.microsoft.com/windows/desktop/FileIO/opportunistic-locks) in the Windows Desktop documentation. For more information about user mode OPLOCK controls, see [File Management Control Codes](https://docs.microsoft.com/windows/desktop/FileIO/file-management-control-codes) in the Windows Desktop documentation.

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

 

 






