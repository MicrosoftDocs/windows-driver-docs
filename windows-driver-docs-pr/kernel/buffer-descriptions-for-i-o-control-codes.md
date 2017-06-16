---
title: Buffer Descriptions for I/O Control Codes
author: windows-driver-content
description: Buffer Descriptions for I/O Control Codes
ms.assetid: a458f3fb-a6c7-42ae-870e-1617a96b496f
keywords: ["I/O control codes WDK kernel , buffer descriptions", "control codes WDK IOCTLs , buffer descriptions", "IOCTLs WDK kernel , buffer descriptions", "buffer descriptions WDK IOCTLs"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Buffer Descriptions for I/O Control Codes


## <a href="" id="ddk-buffer-descriptions-for-i-o-control-codes-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Buffer%20Descriptions%20for%20I/O%20Control%20Codes%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


