---
title: IRP_MJ_CREATE
description: IRP\_MJ\_CREATE
ms.assetid: fdcc81f0-e571-4194-88cd-d0956ca1577e
keywords: ["IRP_MJ_CREATE Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_CREATE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_CREATE


## When Sent


The I/O Manager sends the IRP\_MJ\_CREATE request when a new file or directory is being created, or when an existing file, device, directory, or volume is being opened. Normally this IRP is sent on behalf of a user-mode application that has called a Microsoft Win32 function such as [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) or on behalf of a kernel-mode component that has called [**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418), [**IoCreateFileSpecifyDeviceObjectHint**](https://msdn.microsoft.com/library/windows/hardware/ff548289), [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), or [**ZwOpenFile**](https://msdn.microsoft.com/library/windows/hardware/ff567011). If the create request is completed successfully, the application or kernel-mode component receives a handle to the file object.

## Operation: File System Drivers


If the target device object is the file system's control device object, the file system driver's dispatch routine must complete the IRP and return an appropriate NTSTATUS value, after setting *Irp-&gt;IoStatus.Status* and *Irp-&gt;IoStatus.Information* to appropriate values.

Otherwise, the file system driver should process the create request.

## Operation: File System Filter Drivers


If the target device object is the filter driver's control device object, the filter driver's dispatch routine must complete the IRP and return an appropriate NTSTATUS value, after setting *Irp-&gt;IoStatus.Status* and *Irp-&gt;IoStatus.Information* to appropriate values.

Otherwise, the filter driver should perform any needed processing and, depending on the nature of the filter, either complete the IRP or pass it down to the next-lower driver on the stack.

Generally, filter drivers should not return **STATUS\_PENDING** in response to **IRP\_MJ\_CREATE**. However, if a lower-level driver returns **STATUS\_PENDING**, the filter driver should pass this status value up the driver chain.

File system filter driver writers should note that [**IoCreateStreamFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548296) causes an [**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md) request to be sent to the file system driver stack for the volume. Because file systems often create stream file objects as a side effect of operations other than **IRP\_MJ\_CREATE**, it is difficult for filter drivers to reliably detect stream file object creation. Thus a filter driver should expect to receive **IRP\_MJ\_CLEANUP** and [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720) requests for previously unseen file objects. In the case of [**IoCreateStreamFileObjectLite**](https://msdn.microsoft.com/library/windows/hardware/ff548306), an **IRP\_MJ\_CLEANUP** request is not sent.

&gt; \[!Note\]
&gt;  When legacy filter drivers re-issue a create in a post-create callback, they must release and set the buffer that is associated with their reparse point (the auxiliary buffer) to **NULL**. If a legacy filter driver does not free this buffer and set it to **NULL**, the driver will leak memory. Minifilter drivers do not have to do this because the Filter Manager does this for them.

 

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a create request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to a [**FILE\_FULL\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545793)-structured buffer, if the file object represents a file with extended attributes. Otherwise, this member is set to **NULL**.

<a href="" id="irp--flags"></a>*Irp-&gt;Flags*  
The following flags are set for this request:

IRP\_CREATE\_OPERATION

IRP\_DEFER\_IO\_COMPLETION

IRP\_SYNCHRONOUS\_API

<a href="" id="irp--requestormode"></a>*Irp-&gt;RequestorMode*
Indicates the execution mode of the process that requested the operation, either **KernelMode** or **UserMode**. Note that if the SL\_FORCE\_ACCESS\_CHECK flag is set, access checks must be performed, even if *Irp-&gt;RequestorMode* is KernelMode.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation. The file system sets the **Information** member of this structure to one of the following values:

FILE\_CREATED

FILE\_DOES\_NOT\_EXIST

FILE\_EXISTS

FILE\_OPENED

FILE\_OVERWRITTEN

FILE\_SUPERSEDED

<a href="" id="irp--overlay-allocationsize"></a>*Irp-&gt;Overlay.AllocationSize*
Initial allocation size, in bytes, for the file. A nonzero value has no effect unless the file is being created, overwritten, or superseded.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*
Pointer to a file object that the I/O Manager creates to represent the file to be created or opened. When the file system processes the IRP\_MJ\_CREATE request, it sets the **FsContext** and possibly **FsContext2** fields in this file object to values that are file-system-specific. Thus the values of the **FsContext** and **FsContext2** fields cannot be considered valid until after the file system has processed the create request. For more information, see [File Streams, Stream Contexts, and Per-Stream Contexts](https://msdn.microsoft.com/library/windows/hardware/ff540359).

[**FltCancelFileOpen**](https://msdn.microsoft.com/library/windows/hardware/ff541784) and [**IoCancelFileOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548246) set the FO\_FILE\_OPEN\_CANCELLED flag in the file object's **Flags** field. Setting this flag indicates that the IRP\_MJ\_CREATE request has been canceled, and an [**IRP\_MJ\_CLOSE**](irp-mj-close.md) request will be issued for this file object. Once the create request has been canceled, it cannot be reissued.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of a FILE\_OBJECT structure is used to indicate that a given file has been opened relative to an already open file object. This usually indicates that the relative file is a directory but stream-based files may be opened relative to an already existing stream of a file. The **RelatedFileObject** field of the FILE\_OBJECT structure is only valid during the processing of IRP\_MJ\_CREATE.

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
<td align="left"><p>SL_CASE_SENSITIVE</p></td>
<td align="left"><p>If this flag is set, file name comparisons should be case-sensitive.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SL_FORCE_ACCESS_CHECK</p></td>
<td align="left"><p>If this flag is set, access checks must be performed even if the value of <em>IRP-&gt;RequestorMode</em> is <strong>KernelMode</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SL_OPEN_PAGING_FILE</p></td>
<td align="left"><p>If this flag is set, the file is a paging file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SL_OPEN_TARGET_DIRECTORY</p></td>
<td align="left"><p>If this flag is set, the file&#39;s parent directory should be opened.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*
Specifies IRP\_MJ\_CREATE.

<a href="" id="irpsp--parameters-create-ealength"></a>*IrpSp-&gt;Parameters.Create.EaLength*
Size in bytes of the buffer at *Irp-&gt;AssociatedIrp.SystemBuffer*. If the value of *Irp-&gt;AssociatedIrp.SystemBuffer* is **NULL**, this member must be zero.

<a href="" id="irpsp--parameters-create-fileattributes"></a>*IrpSp-&gt;Parameters.Create.FileAttributes*
Bitmask of attribute flags to be applied when creating or opening the file. Explicitly specified attributes are applied only when the file is created, superseded, or, in some cases, overwritten. By default, this value is FILE\_ATTRIBUTE\_NORMAL, which can be overridden by any other flag or by an ORed combination of compatible flags. This member corresponds to the *FileAttributes* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://msdn.microsoft.com/library/windows/hardware/ff548289).

<a href="" id="irpsp--parameters-create-options"></a>*IrpSp-&gt;Parameters.Create.Options*
Bitmask of flags that specify the options to be applied when creating or opening the file, as well as the action to be taken if the file already exists.

The high 8 bits of this parameter correspond to the *Disposition* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://msdn.microsoft.com/library/windows/hardware/ff548289).

The low 24 bits of this member correspond to the *CreateOptions* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://msdn.microsoft.com/library/windows/hardware/ff548289). File system filter and minifilter drivers that perform file scanning (such as antivirus programs) should pay particular attention to the FILE\_COMPLETE\_IF\_OPLOCKED flag. If this flag is set, the filter must not block or otherwise delay the IRP\_MJ\_CREATE operation.

If the FILE\_COMPLETE\_IF\_OPLOCKED flag is set in the pre-create (create dispatch) path, the filter must not initiate any of the following types of operations, because they can cause oplock breaks:

IRP\_MJ\_CLEANUP
IRP\_MJ\_CREATE
IRP\_MJ\_FILE\_SYSTEM\_CONTROL
IRP\_MJ\_FLUSH\_BUFFERS
IRP\_MJ\_LOCK\_CONTROL
IRP\_MJ\_READ
IRP\_MJ\_SET\_INFORMATION
IRP\_MJ\_WRITE
If a filter or minifilter cannot honor the FILE\_COMPLETE\_IF\_OPLOCKED flag, it must complete the IRP\_MJ\_CREATE request with STATUS\_SHARING\_VIOLATION.

If the FILE\_COMPLETE\_IF\_OPLOCKED flag is set in the completion (post-create) path, the filter should check whether the file system has set *Irp-&gt;IoStatus.Status* to the STATUS\_OPLOCK\_BREAK\_IN\_PROGRESS status value. If this status value is not set, it is safe for the filter to initiate one of the above operations on the file. If this status value is set, the oplock has not yet been broken, and the filter must not initiate any operation that can cause an oplock break. Thus the filter must postpone all of the above operations on the file until one of the following conditions is true:

-   The owner of the oplock sends an FSCTL\_OPLOCK\_BREAK\_ACKNOWLEDGE request to the file system.
-   A system component other than the filter or minifilter sends the file system an I/O request that must wait until the oplock break is complete (such as IRP\_MJ\_READ or IRP\_MJ\_WRITE). The filter or minifilter can initiate one of the above operations from its dispatch (or preoperation callback) routine for this new operation, because the dispatch or preoperation callback routine is put into a wait state until the oplock break is complete.

<a href="" id="irpsp--parameters-create-securitycontext--accessstate"></a>*IrpSp-&gt;Parameters.Create.SecurityContext-&gt;AccessState*
Pointer to an [**ACCESS\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff538840) structure containing the object's subject context, granted access types, and remaining desired access types.

<a href="" id="irpsp--parameters-create-securitycontext--desiredaccess"></a>*IrpSp-&gt;Parameters.Create.SecurityContext-&gt;DesiredAccess*
ACCESS\_MASK structure specifying access rights requested for the file. For more information, see the description of the *DesiredAccess* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://msdn.microsoft.com/library/windows/hardware/ff548289).

<a href="" id="irpsp--parameters-create-shareaccess"></a>*IrpSp-&gt;Parameters.Create.ShareAccess*
Bitmask of share access rights requested for the file. If this member is zero, exclusive access is being requested. For more information, see the description of the *ShareAccess* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://msdn.microsoft.com/library/windows/hardware/ff548289).

## See also


[**ACCESS\_MASK**](https://msdn.microsoft.com/library/windows/hardware/ff540466)

[**ACCESS\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff538840)

[**FILE\_FULL\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545793)

[**FltCancelFileOpen**](https://msdn.microsoft.com/library/windows/hardware/ff541784)

[**FltReissueSynchronousIo**](https://msdn.microsoft.com/library/windows/hardware/ff544311)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoCancelFileOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548246)

[**IoCheckEaBufferValidity**](https://msdn.microsoft.com/library/windows/hardware/ff548252)

[**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418)

[**IoCreateFileSpecifyDeviceObjectHint**](https://msdn.microsoft.com/library/windows/hardware/ff548289)

[**IoCreateStreamFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548296)

[**IoCreateStreamFileObjectLite**](https://msdn.microsoft.com/library/windows/hardware/ff548306)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md)

[**IRP\_MJ\_CLOSE**](irp-mj-close.md)

[**IRP\_MJ\_CREATE (WDK Kernel Reference)**](https://msdn.microsoft.com/library/windows/hardware/ff550729)

[**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424)

[**ZwOpenFile**](https://msdn.microsoft.com/library/windows/hardware/ff567011)

 

 






