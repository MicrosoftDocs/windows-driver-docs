---
title: IRP_MJ_FILE_SYSTEM_CONTROL (FS and filter drivers)
description: IRP_MJ_FILE_SYSTEM_CONTROL
keywords: ["IRP_MJ_FILE_SYSTEM_CONTROL Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_FILE_SYSTEM_CONTROL
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_FILE_SYSTEM_CONTROL (FS and filter drivers)

## When Sent

The I/O Manager, other operating system components, and other kernel-mode drivers send IRP_MJ_FILE_SYSTEM_CONTROL requests. It can be sent, for example, when a user-mode application has called the Win32 [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function to send a file system I/O control (FSCTL) request.

## Operation: File System Drivers

The file system driver or recognizer should check the minor function code to determine which file system control operation is requested.

File system drivers should handle the following minor function codes:

| Code | Description |
| ---- | ----------- |
| IRP_MN_KERNEL_CALL | This request is the same as IRP_MN_USER_FS_REQUEST (described following), except that the source of the request is a trusted kernel component. |
| IRP_MN_MOUNT_VOLUME | Indicates a volume mount request. If a file system driver receives this IRP for a volume whose format doesn't match that of the file system, the file system driver should return STATUS_UNRECOGNIZED_VOLUME. |
| IRP_MN_USER_FS_REQUEST | Indicates an FSCTL request, possibly on behalf of a user-mode application that has called the Microsoft Win32 DeviceIoControl function or on behalf of a kernel-mode component that has called [**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile) or [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest). For detailed information about FSCTL requests, see "Device Input and Output Control Codes" in the Windows SDK documentation. |
| IRP_MN_VERIFY_VOLUME | Indicates a volume verification request. For removable media, the file system must verify the volume when it detects that the media has been removed and returned to ensure that it's still the same known volume. If the volume has changed, the file system should invalidate all outstanding handles. It should also return an error if the file system on this new media has changed. This request is most often used for floppy drives.

File system recognizers must handle the following minor function code:

| Code | Description |
| ---- | ----------- |
| IRP_MN_LOAD_FILE_SYSTEM | Indicates a load-file system request. |

The file system driver or recognizer should perform the requested operation and then complete the IRP.

## Operation: Legacy Files System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information set in the following members of the IRP and IRP stack location to process a file system control request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied input buffer to be passed to the file system or file system filter driver for the target volume. Used for METHOD_BUFFERED or METHOD_DIRECT I/O. Whether this parameter is required depends on the specific file system control code.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **Irp->MdlAddress** is the address of a memory descriptor list (MDL) describing an output buffer to be passed to the file system or file system filter driver for the target volume. Used for METHOD_DIRECT I/O. Whether this parameter is required depends on the specific I/O control code.

- **Irp->UserBuffer** points to a caller-supplied output buffer to be passed to the file system or file system filter driver for the target volume. Used for METHOD_BUFFERED or METHOD_NEITHER I/O. Whether this parameter is optional or required depends on the specific I/O control code.

- **IrpSp->FileObject** points to the file object that is associated with *DeviceObject*.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_FILE_SYSTEM_CONTROL and shouldn't be used.

- **IrpSp->Flags** can be set to SL_ALLOW_RAW_MOUNT for IRP_MN_VERIFY_VOLUME.

- **IrpSp->MajorFunction** is set to IRP_MJ_FILE_SYSTEM_CONTROL.

- **IrpSp->MinorFunction** can be set to one of the following values.

  - IRP_MN_KERNEL_CALL
  - IRP_MN_LOAD_FILE_SYSTEM
  - IRP_MN_MOUNT_VOLUME
  - IRP_MN_USER_FS_REQUEST
  - IRP_MN_VERIFY_VOLUME

- **IrpSp->Parameters.FileSystemControl.FsControlCode** is the FSCTL function code to be passed to the file system or file system filter driver for the target volume. For use with IRP_MN_USER_FS_REQUEST only.

  For detailed information about IOCTL and FSCTL requests, see [Using I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md) and "Device Input and Output Control Codes" in the Windows SDK documentation.

- **IrpSp->Parameters.FileSystemControl.InputBufferLength** is the size in bytes of the buffer pointed to by **Irp->AssociatedIrp.SystemBuffer**.

- **IrpSp->Parameters.FileSystemControl.OutputBufferLength** is the size in bytes of the buffer pointed to by **Irp->UserBuffer**.

- **IrpSp->Parameters.FileSystemControl.Type3InputBuffer** is the input buffer for kernel-mode requests using METHOD_NEITHER.

- **IrpSp->Parameters.MountVolume.DeviceObject** points to the device object for the actual device on which the volume is to be mounted. File system filter drivers shouldn't use this parameter.

- **IrpSp->Parameters.MountVolume.Vpb** points to the volume parameter block (VPB) for the volume to be mounted. File systems that support removable media might substitute a previously used VPB for the one passed in this parameter. On such file systems, after the volume is mounted, this pointer can no longer be assumed to be valid. File system filter drivers that filter these file systems should use this parameter as follows: The filter should save the value of **IrpSp->Parameters.MountVolume.Vpb->RealDevice** before it sends the IRP down to lower-level drivers. After the volume is successfully mounted, the filter can use this pointer to the storage device object to obtain the correct VPB pointer.

- **IrpSp->Parameters.VerifyVolume.DeviceObject** points to the device object for the volume to be verified.

- **IrpSp->Parameters.VerifyVolume.Vpb** points to the VPB for the volume to be verified.

## See also

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoBuildAsynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildasynchronousfsdrequest)

[**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)

[**IoBuildSynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile)
