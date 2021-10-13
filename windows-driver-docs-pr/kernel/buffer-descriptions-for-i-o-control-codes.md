---
title: Buffer Descriptions for I/O Control Codes
description: Buffer Descriptions for I/O Control Codes
keywords: ["I/O control codes WDK kernel , buffer descriptions", "control codes WDK IOCTLs , buffer descriptions", "IOCTLs WDK kernel , buffer descriptions", "buffer descriptions WDK IOCTLs"]
ms.date: 07/29/2021
ms.localizationpriority: medium
---

# Buffer Descriptions for I/O Control Codes

I/O control codes are contained in [**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md) and [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](./irp-mj-internal-device-control.md) requests.
The I/O manager creates these requests as a result of calls to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) and [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest).

Because [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) and **IoBuildDeviceIoControlRequest** accept both an input buffer and an output buffer as arguments, all **IRP_MJ_DEVICE_CONTROL** and **IRP_MJ_INTERNAL_DEVICE_CONTROL** requests supply both an input buffer and an output buffer.
The way the system describes these buffers is dependent on the data transfer type.
The transfer type is specified by the *TransferType* value in the [**CTL_CODE**](defining-i-o-control-codes.md) macro that creates IOCTL code values.

The system describes buffers for each *TransferType* value as follows.

## METHOD_BUFFERED

For this transfer type, IRPs supply a pointer to a buffer at **Irp->AssociatedIrp.SystemBuffer**. This buffer represents both the input buffer and the output buffer that are specified in calls to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) and **IoBuildDeviceIoControlRequest**. The driver transfers data out of, and then into, this buffer.

For input data, the buffer size is specified by **Parameters.DeviceIoControl.InputBufferLength** in the driver's [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure. For output data, the buffer size is specified by **Parameters.DeviceIoControl.OutputBufferLength** in the driver's **IO_STACK_LOCATION** structure.

The size of the space that the system allocates for the single input/output buffer is the larger of the two length values.

## METHOD_IN_DIRECT or METHOD_OUT_DIRECT

For these transfer types, IRPs supply a pointer to a buffer at **Irp->AssociatedIrp.SystemBuffer**.
This represents the first buffer that is specified in calls to **DeviceIoControl** and **IoBuildDeviceIoControlRequest**.
The buffer size is specified by **Parameters.DeviceIoControl.InputBufferLength** in the driver's **IO_STACK_LOCATION** structure.

For these transfer types, IRPs also supply a pointer to an MDL at **Irp->MdlAddress**.
This represents the second buffer that is specified in calls to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) and **IoBuildDeviceIoControlRequest**.
This buffer can be used as either an input buffer or an output buffer, as follows:

-   METHOD_IN_DIRECT is specified if the driver that handles the IRP receives data in the buffer when it is called. The MDL describes an input buffer, and specifying METHOD_IN_DIRECT ensures that the executing thread has read-access to the buffer.

-   METHOD_OUT_DIRECT is specified if the driver that handles the IRP will write data into the buffer before completing the IRP. The MDL describes an output buffer, and specifying METHOD_OUT_DIRECT ensures that the executing thread has write-access to the buffer.

For both of these transfer types, **Parameters.DeviceIoControl.OutputBufferLength** specifies the size of the buffer that is described by the MDL.

## METHOD_NEITHER

The I/O manager does not provide any system buffers or MDLs.
The IRP supplies the user-mode virtual addresses of the input and output buffers that were specified to **DeviceIoControl** or **IoBuildDeviceIoControlRequest**, without validating or mapping them.

The input buffer's address is supplied by **Parameters.DeviceIoControl.Type3InputBuffer** in the driver's **IO_STACK_LOCATION** structure, and the output buffer's address is specified by **Irp->UserBuffer**.

Buffer sizes are supplied by **Parameters.DeviceIoControl.InputBufferLength** and **Parameters.DeviceIoControl.OutputBufferLength** in the driver's **IO_STACK_LOCATION** structure.

For more information about the **CTL_CODE** macro and the transfer types listed above, see [Defining I/O Control Codes](defining-i-o-control-codes.md).
