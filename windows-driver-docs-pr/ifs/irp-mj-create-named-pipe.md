---
title: IRP_MJ_CREATE_NAMED_PIPE (FS and Filter Drivers)
description: IRP_MJ_CREATE_NAMED_PIPE
keywords: ["IRP_MJ_CREATE_NAMED_PIPE File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_CREATE_NAMED_PIPE
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_CREATE_NAMED_PIPE (FS and filter drivers)

## When Sent

The I/O Manager sends the IRP_MJ_CREATE_NAMED_PIPE request when a new named pipe is being created or opened. Normally this IRP is sent:

- On behalf of a user-mode application that has called a Microsoft Win32 function such as [**CreateNamedPipe**](/windows/win32/api/winbase/nf-winbase-createnamedpipea).
- Or, on behalf of a kernel-mode component that has called [**IoCreateFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatefile) or [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

If the named pipe create request is completed successfully, the application or kernel-mode component receives a handle to the server end of the named pipe file instance.

The handling of IRP_MJ_CREATE_NAMED_PIPE is much the same as [IRP_MJ_CREATE](irp-mj-create.md).

## Operation: File System Drivers

If the target device object is the file system's control device object, the file system driver's dispatch routine must do the following operations:

- Set **Irp->IoStatus.Status** and **Irp->IoStatus.Information** to appropriate values.
- Complete the IRP and return an appropriate NTSTATUS value.

Otherwise, the file system driver should process the create request.

## Operation: Legacy File System Filter Drivers

If the target device object is the legacy filter driver's control device object, that driver's dispatch routine must complete the IRP and return an appropriate NTSTATUS value, after setting **Irp->IoStatus.Status** and **Irp->IoStatus.Information** to appropriate values.

Otherwise, the legacy filter driver should perform any needed processing. Then, depending on the nature of the filter, the driver should either complete the IRP or pass it down to the next-lower driver on the stack.

Generally, legacy filter drivers shouldn't return **STATUS_PENDING** in response to IRP_MJ_CREATE_NAMED_PIPE. However, if a lower-level driver returns **STATUS_PENDING**, the legacy filter driver should pass this status value up the driver chain.

## Parameters

A file system or legacy filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a create named pipe request.

- **DeviceObject** is a pointer to the target device object.

- **Irp->Flags** is set to the following flags for this request:
  - IRP_CREATE_OPERATION
  - IRP_DEFER_IO_COMPLETION
  - IRP_SYNCHRONOUS_API

- **Irp->IoStatus** points to an [IO_STATUS_BLOCK](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. The file system sets the **Information** member of this structure to one of the following values:
  - FILE_CREATED
  - FILE_OPENED

- **Irp->RequestorMode** indicates the execution mode of the process that requested the operation, either **KernelMode** or **UserMode**. If the SL_FORCE_ACCESS_CHECK flag is set, access checks must be performed, even if **Irp->RequestorMode** is **KernelMode**.

- **IrpSp->MajorFunction** is set to IRP_MJ_CREATE_NAMED_PIPE.
  
- **IrpSp->Flags** can be set to SL_FORCE_ACCESS_CHECK. If this flag is set, access checks must be performed even if the value of **Irp->RequestorMode** is **KernelMode**.

- **IrpSp->Parameters.CreatePipe.SecurityContext->AccessState** is a pointer to an [ACCESS_STATE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state) structure containing the object's subject context, granted access types, and remaining desired access types.

- **IrpSp->Parameters.CreatePipe.SecurityContext->DesiredAccess** is an ACCESS_MASK structure specifying access rights requested for the named pipe. For more information, see the description of the **DesiredAccess** parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

- **IrpSp->Parameters.CreatePipe.Options** is a bitmask of flags that specify the options to be applied when creating or opening the named pipe, and the action to be taken if the named pipe already exists.

  The high 8 bits of this parameter correspond to the **Disposition** parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

  The low 24 bits of this member correspond to the **CreateOptions** parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

- **IrpSp->Parameters.CreatePipe.ShareAccess** is a bitmask of share access rights requested for the named pipe. If this member is zero, exclusive access is being requested. For more information, see the description of the **ShareAccess** parameter to [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

- **IrpSp->Parameters.CreatePipe.Parameters** is a pointer to a [NAMED_PIPE_CREATE_PARAMETERS](/windows-hardware/drivers/ddi/wdm/ns-wdm-_named_pipe_create_parameters) structure that contains the create parameters for when the named pipe is being created.

- **IrpSp->FileObject** is a pointer to a file object that the I/O Manager creates to represent the named pipe to be created or opened. When the file system processes the IRP_MJ_CREATE_NAMED_PIPE request, it sets the **FsContext** and possibly **FsContext2** fields in this file object to values that are file-system-specific. Thus the values of the **FsContext** and **FsContext2** fields can't be considered valid until after the file system has processed the create request. For more information, see [File Streams, Stream Contexts, and Per-Stream Contexts](./file-streams--stream-contexts--and-per-stream-contexts.md).

  [**IoCancelFileOpen**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocancelfileopen) (and [**FltCancelFileOpen**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcancelfileopen)) set the FO_FILE_OPEN_CANCELLED flag in the file object's **Flags** field. Setting this flag indicates that the IRP_MJ_CREATE_NAMED_PIPE request has been canceled, and an [**IRP_MJ_CLOSE**](irp-mj-close.md) request will be issued for this file object. Once the create request has been canceled, it can't be reissued.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of a FILE_OBJECT structure is used to indicate that a given named pipe has been opened relative to an already open file object. This usually indicates that the relative file is a directory but stream-based files may be opened relative to an already existing stream of a file. The **RelatedFileObject** field of the FILE_OBJECT structure is only valid during the processing of IRP_MJ_CREATE_NAMED_PIPE.

## See also

[ACCESS_MASK](../kernel/access-mask.md)

[ACCESS_STATE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state)

[FLT_PARAMETERS](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[FLT_PARAMETERS for IRP_MJ_CREATE_NAMED_PIPE](flt-parameters-for-irp-mj-create-named-pipe.md)

[**FltCancelFileOpen**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcancelfileopen)

[IO_STACK_LOCATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[IO_STATUS_BLOCK](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCancelFileOpen**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocancelfileopen)

[**IoCreateFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatefile)

[**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint)

[**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject)

[**IoCreateStreamFileObjectLite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[IRP](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[IRP_MJ_CLEANUP](irp-mj-cleanup.md)

[IRP_MJ_CLOSE](irp-mj-close.md)

[IRP_MJ_CREATE (WDK Kernel Reference)](../kernel/irp-mj-create.md)

[NAMED_PIPE_CREATE_PARAMETERS](/windows-hardware/drivers/ddi/wdm/ns-wdm-_named_pipe_create_parameters)
