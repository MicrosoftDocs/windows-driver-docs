---
title: Failure to Validate Device Objects
author: windows-driver-content
description: Failure to Validate Device Objects
ms.assetid: aa4abc20-0b87-44d7-8987-a5b2be397bb1
keywords: ["reliability WDK kernel , device object validations", "device objects WDK kernel , validation failures", "validation failures WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Failure to Validate Device Objects


## <a href="" id="ddk-failure-to-validate-device-objects-kg"></a>


Many drivers create more than one kind of device object by calling [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397). Some drivers create control device objects in their **DriverEntry** routines to allow applications to communicate with the driver, even before the driver creates an FDO. For example, file system drivers create device objects to handle file system notifications when they register themselves as file systems with **IoRegisterFileSystem**.

A driver should be ready for [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) requests for any device object it creates. After completing the request with a success status, the driver should expect to receive any user-accessible I/O requests on the created file object. Consequently, any driver that creates more than one device object must check which device object each I/O request specifies.

For example, suppose a driver creates overall control device objects in [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113), and then creates another set of device objects in its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. Suppose the *AddDevice* routine initializes the device extension with information about lower-level drivers, but the control device objects do not contain this information. In this case, all dispatch routines must be careful to check each device object that they receive. Otherwise, the driver might crash when trying to use device extension information.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Failure%20to%20Validate%20Device%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


