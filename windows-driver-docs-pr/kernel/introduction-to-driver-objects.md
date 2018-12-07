---
title: Introduction to Driver Objects
description: Introduction to Driver Objects
ms.assetid: 497ee2dc-671d-408e-b228-16dc24532375
keywords: ["driver objects WDK kernel", "standard driver routines WDK kernel , driver objects", "driver routines WDK kernel , driver objects", "routines WDK kernel , driver objects", "objects WDK driver objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
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

 

 




