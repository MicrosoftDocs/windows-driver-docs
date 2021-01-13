---
title: IRP_MJ_INTERNAL_DEVICE_CONTROL (IFS)
description: IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL
keywords: ["IRP_MJ_INTERNAL_DEVICE_CONTROL Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_INTERNAL_DEVICE_CONTROL
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL (IFS)


## When Sent


The IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers.

Unlike [**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md) requests, IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL requests are used only for communication among kernel-mode components. While an IRP\_MJ\_DEVICE\_CONTROL request usually originates with a call to **DeviceIoControl** or [**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile), these routines cannot create IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL requests. However, both types of IRP can be created by calling [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest).

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine whether the request has been issued on a handle that represents a volume open. If this is the case, the file system driver should pass the IRP to the device driver for the storage device on which the volume is mounted. If not, the driver should fail the IRP.

## Operation: File System Filter Drivers


The filter driver should perform any needed processing and, depending on the nature of the filter, either complete the IRP or pass it down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a device control request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to a system-supplied input buffer to be passed to the device driver for the target device. Used for METHOD\_BUFFERED or METHOD\_DIRECT I/O. Whether this parameter is required depends on the specific I/O control code.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. For more information, see the description of the *IoStatusBlock* parameter to [**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile).

<a href="" id="irp--mdladdress"></a>*Irp-&gt;MdlAddress*  
Address of a memory descriptor list (MDL) that describes an output buffer to be passed to the device driver for the target device. Used for METHOD\_DIRECT I/O. Whether this parameter is required depends on the specific I/O control code.

<a href="" id="irp--requestormode"></a>*Irp-&gt;RequestorMode*  
Indicates the execution mode of the process that requested the operation, either **KernelMode** or **UserMode**.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
Pointer to a caller-supplied output buffer to be passed to the device driver for the target device. This parameter is used for METHOD\_BUFFERED or METHOD\_NEITHER I/O. Whether this parameter is optional or required depends on the specific I/O control code.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBJECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL.

<a href="" id="irpsp--parameters-deviceiocontrol-inputbufferlength"></a>*IrpSp-&gt;Parameters.DeviceIoControl.InputBufferLength*  
Size in bytes of the buffer pointed to by *Irp-&gt;AssociatedIrp.SystemBuffer*.

<a href="" id="irpsp--parameters-deviceiocontrol-iocontrolcode"></a>*IrpSp-&gt;Parameters.DeviceIoControl.IoControlCode*  
IOCTL function code to be passed to the device driver for the target device.

For detailed information about IOCTL requests, see [Using I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md) in the *Kernel Mode Architecture Guide* and "Device Input and Output Control Codes" in the Microsoft Windows SDK documentation.

<a href="" id="irpsp--parameters-deviceiocontrol-outputbufferlength"></a>*IrpSp-&gt;Parameters.DeviceIoControl.OutputBufferLength*  
Size in bytes of the buffer pointed to by *Irp-&gt;UserBuffer*.

<a href="" id="irpsp--parameters-deviceiocontrol-type3inputbuffer"></a>*IrpSp-&gt;Parameters.DeviceIoControl.Type3InputBuffer*  
Input buffer for kernel-mode requests using METHOD\_NEITHER.

## See also


[**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IoGetFunctionCodeFromCtlCode**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetfunctioncodefromctlcode)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md)

[**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL (WDK Kernel Reference)**](../kernel/irp-mj-internal-device-control.md)

[Using I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md)

[**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile)

