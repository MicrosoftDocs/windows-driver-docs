---
title: IRP_MJ_CREATE_MAILSLOT
description: IRP_MJ_CREATE_MAILSLOT
ms.assetid: 6cd04fd0-ee36-421f-8877-f409aba31b17
keywords: ["IRP_MJ_CREATE_MAILSLOT File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_CREATE_MAILSLOT
api_type:
- NA
ms.date: 11/04/2019
ms.localizationpriority: medium
---

# IRP_MJ_CREATE_MAILSLOT

## When Sent

The I/O Manager sends the IRP_MJ_CREATE_MAILSLOT request when a new mailslot is being created or opened. Normally this IRP is sent:

- On behalf of a user-mode application that has called a Microsoft Win32 function such as [**CreateMailslot**](https://docs.microsoft.com/windows/win32/api/winbase/nf-winbase-createmailslota).
- Or, on behalf of a kernel-mode component that has called [**IoCreateFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatefile), [**IoCreateFileSpecifyDeviceObjectHint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint), [**ZwCreateFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile), or [**ZwOpenFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenfile).

If the create request is completed successfully, the application or kernel-mode component receives a handle to the mailslot file instance.

The handling of IRP_MJ_CREATE_MAILSLOT is much the same as [IRP_MJ_CREATE](irp-mj-create.md).

## Operation: File System Drivers

If the target device object is the file system's control device object, the file system driver's dispatch routine must complete the IRP and return an appropriate NTSTATUS value, after setting *Irp->IoStatus.Status* and *Irp->IoStatus.Information* to appropriate values.

Otherwise, the file system driver should process the create request.

## Operation: File System Filter Drivers

If the target device object is the filter driver's control device object, the filter driver's dispatch routine must complete the IRP and return an appropriate NTSTATUS value, after setting *Irp->IoStatus.Status* and *Irp->IoStatus.Information* to appropriate values.

Otherwise, the filter driver should perform any needed processing and, depending on the nature of the filter, either complete the IRP or pass it down to the next-lower driver on the stack.

Generally, filter drivers should not return **STATUS_PENDING** in response to **IRP_MJ_CREATE_MAILSLOT**. However, if a lower-level driver returns **STATUS_PENDING**, the filter driver should pass this status value up the driver chain.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a create request:

- *DeviceObject*

  Pointer to the target device object.

- *Irp->Flags*  
  The following flags are set for this request:
  - IRP_CREATE_OPERATION
  - IRP_DEFER_IO_COMPLETION
  - IRP_SYNCHRONOUS_API

- *Irp->RequestorMode*
  Indicates the execution mode of the process that requested the operation, either **KernelMode** or **UserMode**. Note that if the SL_FORCE_ACCESS_CHECK flag is set, access checks must be performed, even if *Irp->RequestorMode* is **KernelMode**.

- *Irp->IoStatus*
  Pointer to an [IO_STATUS_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. The file system sets the **Information** member of this structure to one of the following values:
  - FILE_CREATED
  - FILE_DOES_NOT_EXIST
  - FILE_EXISTS
  - FILE_OPENED
  - FILE_OVERWRITTEN
  - FILE_SUPERSEDED

- *Irp->Overlay.AllocationSize*
  Initial allocation size, in bytes, for the mailslot. A nonzero value has no effect unless the mailslot is being created, overwritten, or superseded.

- *IrpSp->FileObject*
  Pointer to a file object that the I/O Manager creates to represent the mailslot to be created or opened. When the file system processes the IRP_MJ_CREATE_MAILSLOT request, it sets the **FsContext** and possibly **FsContext2** fields in this file object to values that are file-system-specific. Thus the values of the **FsContext** and **FsContext2** fields cannot be considered valid until after the file system has processed the create request. For more information, see [File Streams, Stream Contexts, and Per-Stream Contexts](https://docs.microsoft.com/windows-hardware/drivers/ifs/file-streams--stream-contexts--and-per-stream-contexts).

  [**FltCancelFileOpen**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcancelfileopen) and [**IoCancelFileOpen**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocancelfileopen) set the FO_FILE_OPEN_CANCELLED flag in the file object's **Flags** field. Setting this flag indicates that the IRP_MJ_CREATE_MAILSLOT request has been canceled, and an [**IRP_MJ_CLOSE**](irp-mj-close.md) request will be issued for this file object. Once the create request has been canceled, it cannot be reissued.

  The *IrpSp->FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of a FILE_OBJECT structure is used to indicate that a given mailslot has been opened relative to an already open file object. This usually indicates that the relative file is a directory but stream-based files may be opened relative to an already existing stream of a file. The **RelatedFileObject** field of the FILE_OBJECT structure is only valid during the processing of IRP_MJ_CREATE_MAILSLOT.

- *IrpSp->Flags*

  One or more of the following:

| Flag | Meaning |
| ---- | ------- |
| SL_CASE_SENSITIVE | If this flag is set, mailslot name comparisons should be case-sensitive. |
| SL_FORCE_ACCESS_CHECK | If this flag is set, access checks must be performed even if the value of *Irp->RequestorMode* is **KernelMode**. |
| SL_OPEN_PAGING_FILE | If this flag is set, the mailslot is a paging file. |
| SL_OPEN_TARGET_DIRECTORY | If this flag is set, the mailslot's parent directory should be opened. |

- *IrpSp->MajorFunction*

  Specifies IRP_MJ_CREATE_MAILSLOT.

- *IrpSp->Parameters.CreateMailslot.SecurityContext->AccessState*

  Pointer to an [ACCESS_STATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state) structure containing the object's subject context, granted access types, and remaining desired access types.

- *IrpSp->Parameters.CreateMailslot.SecurityContext->DesiredAccess*

  ACCESS_MASK structure specifying access rights requested for the mailslot. For more information, see the description of the *DesiredAccess* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

- *IrpSp->Parameters.CreateMailslot.Options*

  Bitmask of flags that specify the options to be applied when creating or opening the mailslot, as well as the action to be taken if the mailslot already exists.

  The high 8 bits of this parameter correspond to the *Disposition* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

  The low 24 bits of this member correspond to the *CreateOptions* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint). File system minifilter drivers that perform file scanning (such as antivirus programs) should pay particular attention to the FILE_COMPLETE_IF_OPLOCKED flag. If this flag is set, the minifilter must not block or otherwise delay the IRP_MJ_CREATE_MAILSLOT operation.

  If the FILE_COMPLETE_IF_OPLOCKED flag is set in the pre-create (create dispatch) path, the minifilter must not initiate any of the following types of operations, because they can cause oplock breaks:
  - IRP_MJ_CLEANUP
  - IRP_MJ_CREATE
  - IRP_MJ_FILE_SYSTEM_CONTROL
  - IRP_MJ_FLUSH_BUFFERS
  - IRP_MJ_LOCK_CONTROL
  - IRP_MJ_READ
  - IRP_MJ_SET_INFORMATION
  - IRP_MJ_WRITE

  If a minifilter cannot honor the FILE_COMPLETE_IF_OPLOCKED flag, it must complete the IRP_MJ_CREATE_MAILSLOT request with STATUS_SHARING_VIOLATION.

- *IrpSp->Parameters.CreateMailslot.ShareAccess*

  Bitmask of share access rights requested for the mailslot. If this member is zero, exclusive access is being requested. For more information, see the description of the *ShareAccess* parameter to [**IoCreateFileSpecifyDeviceObjectHint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

- *IrpSp->Parameters.CreateMailslot.Parameters*

  Pointer to a [MAILSLOT_CREATE_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_mailslot_create_parameters) structure that contains the create parameters for when the mailslot is being created.

## See also

[ACCESS_MASK](https://docs.microsoft.com/windows-hardware/drivers/kernel/access-mask)

[ACCESS_STATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state)

[FLT_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[FLT_PARAMETERS for IRP_MJ_CREATE_MAILSLOT](flt-parameters-for-irp-mj-create-mailslot.md)

[**FltCancelFileOpen**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcancelfileopen)

[**FltCreateNamedPipeFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatenamedpipefile)

[IO_STACK_LOCATION](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[IO_STATUS_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCancelFileOpen**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocancelfileopen)

[**IoCreateFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatefile)

[**IoCreateFileSpecifyDeviceObjectHint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint)

[**IoCreateStreamFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject)

[**IoCreateStreamFileObjectLite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite)

[**IoGetCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[IRP](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[IRP_MJ_CLEANUP](irp-mj-cleanup.md)

[IRP_MJ_CLOSE](irp-mj-close.md)

[IRP_MJ_CREATE (WDK Kernel Reference)](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-create)

[MAILSLOT_CREATE_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_mailslot_create_parameters)
