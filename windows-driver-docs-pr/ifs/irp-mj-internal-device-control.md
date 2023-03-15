---
title: IRP_MJ_INTERNAL_DEVICE_CONTROL (FS and filter drivers)
description: IRP_MJ_INTERNAL_DEVICE_CONTROL
keywords: ["IRP_MJ_INTERNAL_DEVICE_CONTROL Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_INTERNAL_DEVICE_CONTROL
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_INTERNAL_DEVICE_CONTROL (FS and filter drivers)

## When Sent

The I/O Manager, other operating system components, and other kernel-mode drivers send IRP_MJ_INTERNAL_DEVICE_CONTROL requests.

Unlike [**IRP_MJ_DEVICE_CONTROL**](irp-mj-device-control.md) requests, IRP_MJ_INTERNAL_DEVICE_CONTROL requests are used only for communication among kernel-mode components. While an IRP_MJ_DEVICE_CONTROL request usually originates with a call to **DeviceIoControl** or [**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile), these routines can't create IRP_MJ_INTERNAL_DEVICE_CONTROL requests. However, both types of IRP can be created by calling [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest).

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine whether the request has been issued on a handle that represents a volume open. If so, the file system driver should pass the IRP to the device driver for the storage device on which the volume is mounted. If not, the driver should fail the IRP.

## Operation: Legacy File System Filter Drivers

The filter driver should perform any needed processing and, depending on the nature of the filter, either complete the IRP or pass it down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a device control request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied input buffer to be passed to the device driver for the target device. Used for METHOD_BUFFERED or METHOD_DIRECT I/O. Whether this parameter is required depends on the specific I/O control code.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. For more information, see the description of the **IoStatusBlock** parameter to [**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile).

- **Irp->MdlAddress** is the address of a memory descriptor list (MDL) that describes an output buffer to be passed to the device driver for the target device. Used for METHOD_DIRECT I/O. Whether this parameter is required depends on the specific I/O control code.

- **Irp->RequestorMode** indicates the execution mode of the process that requested the operation, either **KernelMode** or **UserMode**.

- **Irp->UserBuffer** points to a caller-supplied output buffer to be passed to the device driver for the target device. This parameter is used for METHOD_BUFFERED or METHOD_NEITHER I/O. Whether this parameter is optional or required depends on the specific I/O control code.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_INTERNAL_DEVICE_CONTROL and shouldn't be used.

- **IrpSp->MajorFunction** is set to IRP_MJ_INTERNAL_DEVICE_CONTROL.

- **IrpSp->Parameters.DeviceIoControl.InputBufferLength** is the size in bytes of the buffer pointed to by **Irp->AssociatedIrp.SystemBuffer**.

- **IrpSp->Parameters.DeviceIoControl.IoControlCode** is the IOCTL function code to be passed to the device driver for the target device.

  For detailed information about IOCTL requests, see [Using I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md) and "Device Input and Output Control Codes" in the Windows SDK documentation.

- **IrpSp->Parameters.DeviceIoControl.OutputBufferLength** is the size in bytes of the buffer pointed to by **Irp->UserBuffer**.

- **IrpSp->Parameters.DeviceIoControl.Type3InputBuffer** is the input buffer for kernel-mode requests using METHOD_NEITHER.

## See also

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IoGetFunctionCodeFromCtlCode**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetfunctioncodefromctlcode)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_DEVICE_CONTROL**](irp-mj-device-control.md)

[**IRP_MJ_INTERNAL_DEVICE_CONTROL (WDK Kernel Reference)**](../kernel/irp-mj-internal-device-control.md)

[Using I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md)

[**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile)
