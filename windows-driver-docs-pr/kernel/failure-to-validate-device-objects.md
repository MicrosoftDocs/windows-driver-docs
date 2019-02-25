---
title: Failure to Validate Device Objects
description: Failure to Validate Device Objects
ms.assetid: aa4abc20-0b87-44d7-8987-a5b2be397bb1
keywords: ["reliability WDK kernel , device object validations", "device objects WDK kernel , validation failures", "validation failures WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Failure to Validate Device Objects





Many drivers create more than one kind of device object by calling [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397). Some drivers create control device objects in their **DriverEntry** routines to allow applications to communicate with the driver, even before the driver creates an FDO. For example, file system drivers create device objects to handle file system notifications when they register themselves as file systems with **IoRegisterFileSystem**.

A driver should be ready for [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) requests for any device object it creates. After completing the request with a success status, the driver should expect to receive any user-accessible I/O requests on the created file object. Consequently, any driver that creates more than one device object must check which device object each I/O request specifies.

For example, suppose a driver creates overall control device objects in [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113), and then creates another set of device objects in its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. Suppose the *AddDevice* routine initializes the device extension with information about lower-level drivers, but the control device objects do not contain this information. In this case, all dispatch routines must be careful to check each device object that they receive. Otherwise, the driver might crash when trying to use device extension information.

 

 




