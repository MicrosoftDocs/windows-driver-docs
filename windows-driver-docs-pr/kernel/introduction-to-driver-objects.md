---
title: Introduction to Driver Objects
author: windows-driver-content
description: Introduction to Driver Objects
ms.assetid: 497ee2dc-671d-408e-b228-16dc24532375
keywords: ["driver objects WDK kernel", "standard driver routines WDK kernel , driver objects", "driver routines WDK kernel , driver objects", "routines WDK kernel , driver objects", "objects WDK driver objects"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Driver Objects


## <a href="" id="ddk-introduction-to-driver-objects-kg"></a>


The I/O manager creates a *driver object* for each driver that has been installed and loaded. Driver objects are defined using [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structures.

When the I/O manager calls a driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, it supplies the address of the driver's driver object. The driver object contains storage for entry points to many of a driver's standard routines. The driver is responsible for filling in these entry points.

## <a href="" id="driver-object-illustration"></a>


The following figure illustrates a driver object, with the set of system-defined standard routines that lowest-level and higher-level drivers can or must have.

Each standard routine with an asterisk beside its name receives an I/O request packet (IRP) as input. Each of these standard routines also receives a pointer to the target device object for the I/O request.

![diagram illustrating a driver object](images/24drvobj.png)

The I/O manager defines the driver object type and uses driver objects to register and track information about the loaded images of drivers. Note that the dispatch entry points (**DDDispatch***Xxx* through **DDDispatch***Yyy*) in the driver object correspond to the major function codes (**IRP\_MJ\_*XXX***) that are passed in the I/O stack locations of IRPs.

The I/O manager routes each IRP first to a driver-supplied dispatch routine. A lowest-level driver's dispatch routine usually calls an I/O support routine ([**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370)) to queue (or pass on) each IRP that has valid arguments to the driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine. The *StartIo* routine starts the requested I/O operation on a particular device. Higher-level drivers usually do not have *StartIo* routines, but they can.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20Driver%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


