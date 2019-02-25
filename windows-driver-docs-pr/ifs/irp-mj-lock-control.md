---
title: IRP_MJ_LOCK_CONTROL
description: IRP\_MJ\_LOCK\_CONTROL
ms.assetid: db21d779-c423-42bd-a94b-4d8c8fd1f7cb
keywords: ["IRP_MJ_LOCK_CONTROL Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_LOCK_CONTROL
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_LOCK\_CONTROL


## When Sent


The IRP\_MJ\_LOCK\_CONTROL request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers.

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine whether the target device object is the file system's control device object. If this is the case, the file system driver should complete the IRP as appropriate without processing the lock request.

Otherwise, if the request has been issued on a handle that represents a user file open, the file system driver should perform the operation indicated by the minor function code and complete the IRP. If not, the driver should fail the IRP.

The following are the valid minor function codes:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_LOCK</p></td>
<td align="left"><p>Indicates a byte-range lock request, possibly on behalf of a user-mode application that has called the Microsoft Win32 <strong>LockFile</strong> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_UNLOCK_ALL</p></td>
<td align="left"><p>Indicates a request to release all byte-range locks for a file, usually because the last outstanding handle to a file object is being closed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MN_UNLOCK_ALL_BY_KEY</p></td>
<td align="left"><p>Indicates a request to release all byte-range locks with a specified key value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_UNLOCK_SINGLE</p></td>
<td align="left"><p>Indicates a request to release a single byte-range lock, possibly on behalf of a user-mode application that has called the Microsoft Win32 <strong>UnlockFile</strong> function.</p></td>
</tr>
</tbody>
</table>

 

## Operation: File System Filter Drivers


File system filter drivers should pass the IRP down to the next-lower driver on the stack after performing any needed processing.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a lock control request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_LOCK\_CONTROL and should not be used.

<a href="" id="irpsp--flags"></a>*IrpSp-&gt;Flags*  
One or more of the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>SL_EXCLUSIVE_LOCK</p></td>
<td align="left"><p>If this flag is set, an exclusive byte-range lock is requested. Otherwise, a shared lock is requested.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SL_FAIL_IMMEDIATELY</p></td>
<td align="left"><p>If this flag is set, the lock request should fail if it cannot be granted immediately.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_LOCK\_CONTROL.

<a href="" id="irpsp--minorfunction"></a>*IrpSp-&gt;MinorFunction*  
Specifies one of the following:

-   IRP\_MN\_LOCK
-   IRP\_MN\_UNLOCK\_ALL
-   IRP\_MN\_UNLOCK\_ALL\_BY\_KEY
-   IRP\_MN\_UNLOCK\_SINGLE

<a href="" id="irpsp--parameters-lockcontrol-byteoffset"></a>*IrpSp-&gt;Parameters.LockControl.ByteOffset*  
Starting byte offset within the file of the byte range to be locked or unlocked.

<a href="" id="irpsp--parameters-lockcontrol-key"></a>*IrpSp-&gt;Parameters.LockControl.Key*  
Key for the byte-range lock.

<a href="" id="irpsp--parameters-lockcontrol-length"></a>*IrpSp-&gt;Parameters.LockControl.Length*  
Length, in bytes, of the byte range to be locked or unlocked.

## See also


[**FltProcessFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff543427)

[**FsRtlProcessFileLock**](https://msdn.microsoft.com/library/windows/hardware/ff547166)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

 

 






