---
title: DispatchDeviceControl and DispatchInternalDeviceControl Routines
author: windows-driver-content
description: DispatchDeviceControl and DispatchInternalDeviceControl Routines
MS-HAID:
- 'DrvComps\_7715ab36-a5d2-4fc8-be6a-1d62e7431696.xml'
- 'kernel.dispatchdevicecontrol\_and\_dispatchinternaldevicecontrol\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0bf8868e-bc5a-4fa7-9ff6-270f7a7bc850
keywords: ["dispatch routines WDK kernel , DispatchDeviceControl routine", "dispatch routines WDK kernel , DispatchInternalDeviceControl routine", "DispatchDeviceControl routine", "DispatchInternalDeviceControl routine", "IRP_MJ_DEVICE_CONTROL I/O function code", "IRP_MJ_INTERNAL_DEVICE_CONTROL I/O function code", "internal device control dispatch routines WDK kernel", "device control dispatch routines WDK kernel"]
---

# DispatchDeviceControl and DispatchInternalDeviceControl Routines


## <a href="" id="ddk-dispatchdevicecontrol-and-dispatchinternaldevicecontrol-routines-k"></a>


A driver's [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) and [*DispatchInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543326) routines handle IRPs with I/O function codes of [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766), respectively.

For every common type of peripheral device, the system defines a set of I/O control codes for **IRP\_MJ\_DEVICE\_CONTROL** requests. New drivers for each type of device must support these requests. In most cases, these public I/O control codes for each type of device are not exported to user-mode applications.

Some of these system-defined I/O control codes are used by higher-level drivers that create IRPs for the underlying device driver by calling [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318). Others are used by Win32 components to communicate with an underlying device driver by calling the Win32 function [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) (described in Microsoft Windows SDK documentation) which, in turn, calls a system service. The I/O manager sets up an IRP, and stores the major function code **IRP\_MJ\_DEVICE\_CONTROL** and the given I/O control code in the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure at **Parameters.DeviceIoControl.IoControlCode**. Then, the I/O manager calls the *DispatchDeviceControl* routine of the highest-level driver in the chain.

For certain system-supplied drivers designed to interoperate with and support new drivers, the operating system also defines a set of I/O control codes for **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests. In most cases, these public I/O control codes allow add-on higher-level drivers to interoperate with an underlying device driver.

As an example, the system-supplied parallel drivers support a set of internal I/O control codes that vendor-supplied drivers send in **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests. For more information, see [Internal Device Control Requests for Parallel Ports](https://msdn.microsoft.com/library/windows/hardware/ff543963) and [Internal Device Control Requests for Parallel Devices](https://msdn.microsoft.com/library/windows/hardware/ff543959).

Almost all operations requested through system-defined I/O control codes use buffered I/O, because this type of request seldom requires the transfer of large amounts of data. That is, even drivers that set up their device objects for direct I/O are sent IRPs for device control requests with data to be transferred into or out of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** (except for certain types of highest-level device drivers with closely coupled Win32 multimedia drivers).

In addition, a driver can define a set of private I/O control codes that other drivers can use to communicate with it. New public I/O control codes can be added to the system only with the cooperation of Microsoft Corporation, because public I/O control codes are built into the operating system itself.

For specific information about the set of public I/O control codes that different kinds of drivers must support and about defining private I/O control codes, see the device-specific reference sections of the Windows Driver Kit (WDK).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchDeviceControl%20and%20DispatchInternalDeviceControl%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


