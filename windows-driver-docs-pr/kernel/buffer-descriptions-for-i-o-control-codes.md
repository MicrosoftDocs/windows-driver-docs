---
title: Buffer Descriptions for I/O Control Codes
description: Buffer Descriptions for I/O Control Codes
ms.assetid: a458f3fb-a6c7-42ae-870e-1617a96b496f
keywords: ["I/O control codes WDK kernel , buffer descriptions", "control codes WDK IOCTLs , buffer descriptions", "IOCTLs WDK kernel , buffer descriptions", "buffer descriptions WDK IOCTLs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Buffer Descriptions for I/O Control Codes





I/O control codes are contained in [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests. The I/O manager creates these requests as a result of calls to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) (described in the Microsoft Windows SDK documentation) and [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318).

Because [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) and **IoBuildDeviceIoControlRequest** accept both an input buffer and an output buffer as arguments, all **IRP\_MJ\_DEVICE\_CONTROL** and **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests supply both an input buffer and an output buffer. The way the system describes these buffers is dependent on the data transfer type. The transfer type is specified by the *TransferType* value in the [**CTL\_CODE**](defining-i-o-control-codes.md) macro that creates IOCTL code values.

The system describes buffers for each *TransferType* value as follows:

<a href="" id="method-buffered"></a>METHOD\_BUFFERED  
For this transfer type, IRPs supply a pointer to a buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. This buffer represents both the input buffer and the output buffer that are specified in calls to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) and **IoBuildDeviceIoControlRequest**. The driver transfers data out of, and then into, this buffer.

For input data, the buffer size is specified by **Parameters.DeviceIoControl.InputBufferLength** in the driver's [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure. For output data, the buffer size is specified by **Parameters.DeviceIoControl.OutputBufferLength** in the driver's **IO\_STACK\_LOCATION** structure.

The size of the space that the system allocates for the single input/output buffer is the larger of the two length values.

<a href="" id="method-in-direct-or-method-out-direct"></a>METHOD\_IN\_DIRECT or METHOD\_OUT\_DIRECT  
For these transfer types, IRPs supply a pointer to a buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. This represents the input buffer that is specified in calls to **DeviceIoControl** and **IoBuildDeviceIoControlRequest**. The buffer size is specified by **Parameters.DeviceIoControl.InputBufferLength** in the driver's **IO\_STACK\_LOCATION** structure.

For these transfer types, IRPs also supply a pointer to an MDL at **Irp-&gt;MdlAddress**. This represents the output buffer that is specified in calls to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) and **IoBuildDeviceIoControlRequest**. However, this buffer can actually be used as either an input buffer or an output buffer, as follows:

-   METHOD\_IN\_DIRECT is specified if the driver that handles the IRP receives data in the buffer when it is called. The MDL describes an input buffer, and specifying METHOD\_IN\_DIRECT ensures that the executing thread has read-access to the buffer.

-   METHOD\_OUT\_DIRECT is specified if the driver that handles the IRP will write data into the buffer before completing the IRP. The MDL describes an output buffer, and specifying METHOD\_OUT\_DIRECT ensures that the executing thread has write-access to the buffer.

For both of these transfer types, **Parameters.DeviceIoControl.OutputBufferLength** specifies the size of the buffer that is described by the MDL.

<a href="" id="method-neither"></a>METHOD\_NEITHER  
The I/O manager does not provide any system buffers or MDLs. The IRP supplies the user-mode virtual addresses of the input and output buffers that were specified to **DeviceIoControl** or **IoBuildDeviceIoControlRequest**, without validating or mapping them.

The input buffer's address is supplied by **Parameters.DeviceIoControl.Type3InputBuffer** in the driver's **IO\_STACK\_LOCATION** structure, and the output buffer's address is specified by **Irp-&gt;UserBuffer**.

Buffer sizes are supplied by **Parameters.DeviceIoControl.InputBufferLength** and **Parameters.DeviceIoControl.OutputBufferLength** in the driver's **IO\_STACK\_LOCATION** structure.

For more information about the **CTL\_CODE** macro and the transfer types listed above, see [Defining I/O Control Codes](defining-i-o-control-codes.md).

 

 




