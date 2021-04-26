---
title: IRP_MJ_CREATE (IFS)
description: IRP_MJ_CREATE
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

# IRP_MJ_CREATE (IFS)

## When Sent

The I/O Manager sends an IRP_MJ_CREATE request when a new file or directory is being created, or when an existing file, device, directory, or volume is being opened.

Normally this IRP is sent on behalf of a user-mode application that has called a Microsoft Win32 function such as [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) or on behalf of a kernel-mode component that has called a function such as [**IoCreateFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatefile), [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint), [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile), or [**ZwOpenFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenfile).

If the create request is completed successfully, the application or kernel-mode component receives a handle to the file object.

## Operation: File System Drivers

If the target device object is the file system's control device object, the file system driver's dispatch routine must complete the IRP and return an appropriate NTSTATUS value, after setting *Irp->IoStatus.Status* and *Irp->IoStatus.Information* to appropriate values.

Otherwise, the file system driver should process the create request.

## Operation: File System Filter Drivers

If the target device object is the filter driver's control device object, the filter driver's dispatch routine must complete the IRP and return an appropriate NTSTATUS value, after setting *Irp->IoStatus.Status* and *Irp->IoStatus.Information* to appropriate values.

Otherwise, the filter driver should perform any needed processing and, depending on the nature of the filter, either complete the IRP or pass it down to the next-lower driver on the stack.

Generally, filter drivers should not return **STATUS_PENDING** in response to **IRP_MJ_CREATE**. However, if a lower-level driver returns **STATUS_PENDING**, the filter driver should pass this status value up the driver chain.

File system filter driver writers should note that [**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject) causes an [**IRP_MJ_CLEANUP**](irp-mj-cleanup.md) request to be sent to the file system driver stack for the volume. Because file systems often create stream file objects as a side effect of operations other than **IRP_MJ_CREATE**, it is difficult for filter drivers to reliably detect stream file object creation. Thus a filter driver should expect to receive **IRP_MJ_CLEANUP** and [**IRP_MJ_CLOSE**](../kernel/irp-mj-close.md) requests for previously unseen file objects. In the case of [**IoCreateStreamFileObjectLite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite), an **IRP_MJ_CLEANUP** request is not sent.

> [!NOTE]
> When legacy filter drivers re-issue a create in a post-create callback, they must release and set the buffer that is associated with their reparse point (the auxiliary buffer) to **NULL**. If a legacy filter driver does not free this buffer and set it to **NULL**, the driver will leak memory. Minifilter drivers do not have to do this because the Filter Manager does this for them.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a create request:

* *DeviceObject*: Pointer to the target device object.

* *Irp->AssociatedIrp.SystemBuffer*: Pointer to a [**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)-structured buffer, if the file object represents a file with extended attributes. Otherwise, this member is set to **NULL**.

* *Irp->Flags*: The following flags are set for this request:

  * IRP_CREATE_OPERATION
  * IRP_DEFER_IO_COMPLETION
  * IRP_SYNCHRONOUS_API

* *Irp->RequestorMode*: Indicates the execution mode of the process that requested the operation, either **KernelMode** or **UserMode**. Note that if the SL_FORCE_ACCESS_CHECK flag is set, access checks must be performed, even if *Irp->RequestorMode* is **KernelMode**.

* *Irp->IoStatus*: Pointer to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. The file system sets the **Information** member of this structure to one of the following values:

  * FILE_CREATED
  * FILE_DOES_NOT_EXIST
  * FILE_EXISTS
  * FILE_OPENED
  * FILE_OVERWRITTEN
  * FILE_SUPERSEDED

* *Irp->Overlay.AllocationSize*: Initial allocation size, in bytes, for the file. A nonzero value has no effect unless the file is being created, overwritten, or superseded.

* *IrpSp->FileObject*: Pointer to a file object that the I/O Manager creates to represent the file to be created or opened. When the file system processes the IRP_MJ_CREATE request, it sets the **FsContext** and possibly **FsContext2** fields in this file object to values that are file-system-specific. Thus the values of the **FsContext** and **FsContext2** fields cannot be considered valid until after the file system has processed the create request. For more information, see [File Streams, Stream Contexts, and Per-Stream Contexts](file-streams--stream-contexts--and-per-stream-contexts.md).

  [**FltCancelFileOpen**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcancelfileopen) and [**IoCancelFileOpen**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocancelfileopen) set the FO_FILE_OPEN_CANCELLED flag in the file object's **Flags** field. Setting this flag indicates that the IRP_MJ_CREATE request has been canceled, and an [**IRP_MJ_CLOSE**](irp-mj-close.md) request will be issued for this file object. Once the create request has been canceled, it cannot be reissued.

  The *IrpSp->FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of a FILE_OBJECT structure is used to indicate that a given file has been opened relative to an already open file object. This usually indicates that the relative file is a directory but stream-based files may be opened relative to an already existing stream of a file. The **RelatedFileObject** field of the FILE_OBJECT structure is only valid during the processing of IRP_MJ_CREATE.

* *IrpSp->Flags*: One or more of the following values:

  | Flag | Meaning |
  | ---- | ------- |
  | SL_FORCE_ACCESS_CHECK 0x01 | If this flag is set, access checks must be performed even if the value of *IRP->RequestorMode* is **KernelMode**. |
  | SL_OPEN_PAGING_FILE 0x02 | If this flag is set, the file is a paging file. |
  | SL_OPEN_TARGET_DIRECTORY 0x04 | If this flag is set, the file's parent directory should be opened. |
  | SL_STOP_ON_SYMLINK 0x08 | If this flag is set, the I/O Manager's automatic traversal of junctions and symbolic links is suppressed, causing opens of junctions and symbolic links to return STATUS_REPARSE. |
  | SL_IGNORE_READONLY_ATTRIBUTE 0x40 | If this flag is set, it allows the creation of a read-only file in conjunction with the FILE_DELETE_ON_CLOSE option, which causes the file to be deleted when the handle is closed. |
  | SL_CASE_SENSITIVE 0x80 | If set, file name comparisons should be case-sensitive. |
  
* *IrpSp->MajorFunction*: Specifies IRP_MJ_CREATE.

* *IrpSp->Parameters.Create.EaLength*: Size in bytes of the buffer at *Irp->AssociatedIrp.SystemBuffer*. If the value of *Irp->AssociatedIrp.SystemBuffer* is **NULL**, this member must be zero.

* *IrpSp->Parameters.Create.FileAttributes*: Bitmask of attribute flags to be applied when creating or opening the file. Explicitly specified attributes are applied only when the file is created, superseded, or, in some cases, overwritten. By default, this value is FILE_ATTRIBUTE_NORMAL, which can be overridden by any other flag or by an ORed combination of compatible flags. This member corresponds to the *FileAttributes* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

* *IrpSp->Parameters.Create.Options*: Bitmask of flags that specify the options to be applied when creating or opening the file, as well as the action to be taken if the file already exists.

  The high 8 bits of this parameter correspond to the *Disposition* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

  The low 24 bits of this member correspond to the *CreateOptions* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint). File system filter and minifilter drivers that perform file scanning (such as antivirus programs) should pay particular attention to the FILE_COMPLETE_IF_OPLOCKED flag. If this flag is set, the filter must not block or otherwise delay the IRP_MJ_CREATE operation.

  If the FILE_COMPLETE_IF_OPLOCKED flag is set in the pre-create (create dispatch) path, the filter must not initiate any of the following types of operations, because they can cause oplock breaks:

  * IRP_MJ_CLEANUP
  * IRP_MJ_CREATE
  * IRP_MJ_FILE_SYSTEM_CONTROL
  * IRP_MJ_FLUSH_BUFFERS
  * IRP_MJ_LOCK_CONTROL
  * IRP_MJ_READ
  * IRP_MJ_SET_INFORMATION
  * IRP_MJ_WRITE

  If a filter or minifilter cannot honor the FILE_COMPLETE_IF_OPLOCKED flag, it must complete the IRP_MJ_CREATE request with STATUS_SHARING_VIOLATION.

  If the FILE_COMPLETE_IF_OPLOCKED flag is set in the completion (post-create) path, the filter should check whether the file system has set *Irp->IoStatus.Status* to the STATUS_OPLOCK_BREAK_IN_PROGRESS status value. If this status value is not set, it is safe for the filter to initiate one of the above operations on the file. If this status value is set, the oplock has not yet been broken, and the filter must not initiate any operation that can cause an oplock break. Thus the filter must postpone all of the above operations on the file until one of the following conditions is true:

  * The owner of the oplock sends an FSCTL_OPLOCK_BREAK_ACKNOWLEDGE request to the file system.
  * A system component other than the filter or minifilter sends the file system an I/O request that must wait until the oplock break is complete (such as IRP_MJ_READ or IRP_MJ_WRITE). The filter or minifilter can initiate one of the above operations from its dispatch (or preoperation callback) routine for this new operation, because the dispatch or preoperation callback routine is put into a wait state until the oplock break is complete.

* *IrpSp->Parameters.Create.SecurityContext->AccessState*: Pointer to an [**ACCESS_STATE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state) structure containing the object's subject context, granted access types, and remaining desired access types.

* *IrpSp->Parameters.Create.SecurityContext->DesiredAccess*: ACCESS_MASK structure specifying access rights requested for the file. For more information, see the description of the *DesiredAccess* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

* *IrpSp->Parameters.Create.ShareAccess*: Bitmask of share access rights requested for the file. If this member is zero, exclusive access is being requested. For more information, see the description of the *ShareAccess* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

## See also

[**ACCESS_MASK**](../kernel/access-mask.md)

[**ACCESS_STATE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state)

[**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)

[**FltCancelFileOpen**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcancelfileopen)

[**FltReissueSynchronousIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreissuesynchronousio)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCancelFileOpen**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocancelfileopen)

[**IoCheckEaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckeabuffervalidity)

[**IoCreateFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatefile)

[**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint)

[**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject)

[**IoCreateStreamFileObjectLite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_CLEANUP**](irp-mj-cleanup.md)

[**IRP_MJ_CLOSE**](irp-mj-close.md)

[**IRP_MJ_CREATE (WDK Kernel Reference)**](../kernel/irp-mj-create.md)

[**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)

[**ZwOpenFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenfile)
