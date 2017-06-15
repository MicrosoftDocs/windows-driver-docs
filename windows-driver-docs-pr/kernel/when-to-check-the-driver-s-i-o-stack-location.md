---
title: When to Check the Driver's I/O Stack Location
author: windows-driver-content
description: When to Check the Driver's I/O Stack Location
MS-HAID:
- 'DrvComps\_bb762bc4-5d2c-4d77-90ce-63522960eea9.xml'
- 'kernel.when\_to\_check\_the\_driver\_s\_i\_o\_stack\_location'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ca084221-7b07-4db0-a987-9dd8a66d169c
keywords: ["dispatch routines WDK kernel , I/O stack locations", "I/O stack locations WDK dispatch routines", "driver I/O stack locations WDK dispatch routines"]
---

# When to Check the Driver's I/O Stack Location


## <a href="" id="ddk-when-to-check-the-driver-s-i-o-stack-location-kg"></a>


A major I/O function code is set in the driver's [I/O stack location](i-o-stack-locations.md) for each incoming IRP.

A driver's dispatch routine must check the driver's I/O stack location for the IRP to determine what to do if any of the following conditions hold:

-   The dispatch routine handles more than one major I/O function code.

-   The dispatch routine must handle a set of minor function codes for certain major function codes. IRPs with minor function codes include [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) and [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784), as well as certain IRPs that the SCSI port driver and file system drivers must handle.

-   The dispatch routine of a device driver or of a closely coupled higher-level driver handles [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests, which have an associated set of I/O control codes.

To get a pointer to a driver's I/O stack location, its dispatch routine calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174).

Higher-level drivers' dispatch routines always call **IoGetCurrentIrpStackLocation** and also call [**IoGetNextIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549266) to get a pointer to the next-lower driver's I/O stack location for IRPs that they set up for the next-lower driver, when [passing IRPs down the driver stack](passing-irps-down-the-driver-stack.md).

The [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine or [*DispatchInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543326) routine of a device driver, or possibly of its closely coupled class driver(s), must determine which I/O control code is set in the driver's I/O stack location at **Parameters.DeviceIoControl.IoControlCode** for each request. The I/O control code is contained in the driver's I/O stack location.

In most cases, the *DispatchDeviceControl* or *DispatchInternalDeviceControl* routine of a higher-level driver simply passes an **IRP\_MJ\_DEVICE\_CONTROL** or **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** request on to the next-lower driver, after setting up its stack location in the IRP. However, SCSI class drivers must check for certain [SCSI Port I/O control codes](https://msdn.microsoft.com/library/windows/hardware/ff565367) so that they can set up the SCSI port driver's I/O stack location correctly before passing on these requests.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20When%20to%20Check%20the%20Driver's%20I/O%20Stack%20Location%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


