---
title: DispatchDeviceControl and DispatchInternalDeviceControl Routines
description: DispatchDeviceControl and DispatchInternalDeviceControl Routines
keywords: ["dispatch routines WDK kernel , DispatchDeviceControl routine", "dispatch routines WDK kernel , DispatchInternalDeviceControl routine", "DispatchDeviceControl routine", "DispatchInternalDeviceControl routine", "IRP_MJ_DEVICE_CONTROL I/O function code", "IRP_MJ_INTERNAL_DEVICE_CONTROL I/O function code", "internal device control dispatch routines WDK kernel", "device control dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchDeviceControl and DispatchInternalDeviceControl Routines


A driver's dispatch routines (see [**DRIVER_DISPATCH**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)) handle IRPs with I/O function codes of [**IRP\_MJ\_DEVICE\_CONTROL**](./irp-mj-device-control.md) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](./irp-mj-internal-device-control.md), respectively.

For every common type of peripheral device, the system defines a set of I/O control codes for **IRP\_MJ\_DEVICE\_CONTROL** requests. New drivers for each type of device must support these requests. In most cases, these public I/O control codes for each type of device are not exported to user-mode applications. 


Some of these system-defined I/O control codes are used by higher-level drivers that create IRPs for the underlying device driver by calling [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest). Others are used by Win32 components to communicate with an underlying device driver by calling the Win32 function [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) (described in Microsoft Windows SDK documentation) which, in turn, calls a system service. The I/O manager sets up an IRP, and stores the major function code **IRP\_MJ\_DEVICE\_CONTROL** and the given I/O control code in the [**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure at **Parameters.DeviceIoControl.IoControlCode**. Then, the I/O manager calls the *DispatchDeviceControl* routine of the highest-level driver in the chain.

For certain system-supplied drivers designed to interoperate with and support new drivers, the operating system also defines a set of I/O control codes for **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests. In most cases, these public I/O control codes allow add-on higher-level drivers to interoperate with an underlying device driver.

As an example, the system-supplied parallel drivers support a set of internal I/O control codes that vendor-supplied drivers send in **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests. For more information, see [Internal Device Control Requests for Parallel Ports](/windows-hardware/drivers/ddi/parallel) and [Internal Device Control Requests for Parallel Devices](/windows-hardware/drivers/ddi/index).

Almost all operations requested through system-defined I/O control codes use buffered I/O, because this type of request seldom requires the transfer of large amounts of data. That is, even drivers that set up their device objects for direct I/O are sent IRPs for device control requests with data to be transferred into or out of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** (except for certain types of highest-level device drivers with closely coupled Win32 multimedia drivers).

In addition, a driver can define a set of private I/O control codes that other drivers can use to communicate with it. New public I/O control codes can be added to the system only with the cooperation of Microsoft Corporation, because public I/O control codes are built into the operating system itself.

For specific information about the set of public I/O control codes that different kinds of drivers must support and about defining private I/O control codes, see the device-specific reference sections of the Windows Driver Kit (WDK).

 

