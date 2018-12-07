---
title: DispatchDeviceControl and DispatchInternalDeviceControl Routines
description: DispatchDeviceControl and DispatchInternalDeviceControl Routines
ms.assetid: 0bf8868e-bc5a-4fa7-9ff6-270f7a7bc850
keywords: ["dispatch routines WDK kernel , DispatchDeviceControl routine", "dispatch routines WDK kernel , DispatchInternalDeviceControl routine", "DispatchDeviceControl routine", "DispatchInternalDeviceControl routine", "IRP_MJ_DEVICE_CONTROL I/O function code", "IRP_MJ_INTERNAL_DEVICE_CONTROL I/O function code", "internal device control dispatch routines WDK kernel", "device control dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchDeviceControl and DispatchInternalDeviceControl Routines


A driver's dispatch routines (see [**DRIVER_DISPATCH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch)) handle IRPs with I/O function codes of [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766), respectively.

For every common type of peripheral device, the system defines a set of I/O control codes for **IRP\_MJ\_DEVICE\_CONTROL** requests. New drivers for each type of device must support these requests. In most cases, these public I/O control codes for each type of device are not exported to user-mode applications. 


Some of these system-defined I/O control codes are used by higher-level drivers that create IRPs for the underlying device driver by calling [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318). Others are used by Win32 components to communicate with an underlying device driver by calling the Win32 function [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) (described in Microsoft Windows SDK documentation) which, in turn, calls a system service. The I/O manager sets up an IRP, and stores the major function code **IRP\_MJ\_DEVICE\_CONTROL** and the given I/O control code in the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure at **Parameters.DeviceIoControl.IoControlCode**. Then, the I/O manager calls the *DispatchDeviceControl* routine of the highest-level driver in the chain.

For certain system-supplied drivers designed to interoperate with and support new drivers, the operating system also defines a set of I/O control codes for **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests. In most cases, these public I/O control codes allow add-on higher-level drivers to interoperate with an underlying device driver.

As an example, the system-supplied parallel drivers support a set of internal I/O control codes that vendor-supplied drivers send in **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests. For more information, see [Internal Device Control Requests for Parallel Ports](https://msdn.microsoft.com/library/windows/hardware/ff543963) and [Internal Device Control Requests for Parallel Devices](https://msdn.microsoft.com/library/windows/hardware/ff543959).

Almost all operations requested through system-defined I/O control codes use buffered I/O, because this type of request seldom requires the transfer of large amounts of data. That is, even drivers that set up their device objects for direct I/O are sent IRPs for device control requests with data to be transferred into or out of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** (except for certain types of highest-level device drivers with closely coupled Win32 multimedia drivers).

In addition, a driver can define a set of private I/O control codes that other drivers can use to communicate with it. New public I/O control codes can be added to the system only with the cooperation of Microsoft Corporation, because public I/O control codes are built into the operating system itself.

For specific information about the set of public I/O control codes that different kinds of drivers must support and about defining private I/O control codes, see the device-specific reference sections of the Windows Driver Kit (WDK).

 

 




