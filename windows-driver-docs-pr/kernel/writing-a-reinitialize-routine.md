---
title: Writing a Reinitialize Routine
author: windows-driver-content
description: Writing a Reinitialize Routine
ms.assetid: 47a7dd3f-e474-49c7-adf2-11f6e788c261
keywords: ["standard driver routines WDK kernel , Reinitialize routine", "driver routines WDK kernel , Reinitialize routine", "routines WDK kernel , Reinitialize routine", "Reinitialize", "reinitializing drivers WDK", "driver reinitialization WDK kernel", "driver initialization WDK kernel", "initializing drivers WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Writing a Reinitialize Routine


## <a href="" id="ddk-writing-a-reinitialize-routine-kg"></a>


Any driver that needs to initialize itself in stages can contain a [*Reinitialize*](https://msdn.microsoft.com/library/windows/hardware/ff561022) routine. A *Reinitialize* routine is called after the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine has returned control and other drivers have initialized themselves. Typically, the *Reinitialize* routine performs tasks that must be done after another driver starts.

For example, the system's keyboard class driver, **kbdclass**, supports both PnP and legacy keyboard ports. If a system includes one or more legacy ports that the PnP manager cannot detect, the keyboard class driver must nevertheless create a device object for each port and layer itself over lower-level drivers for the port. Consequently, the class driver has a *Reinitialize* routine to be called after its **DriverEntry** and [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routines have been called and other drivers have been loaded. The *Reinitialize* routine detects the port, creates a device object for it, and layers the driver over other lower-level drivers for the device.

A driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine calls [**IoRegisterDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549511) to queue a *Reinitialize* routine for execution. The *Reinitialize* routine can also call **IoRegisterDriverReinitialization** itself, which causes the routine to be requeued. One of the parameters to *Reinitialize* indicates the number of times it has been called.

The call to **IoRegisterDriverReinitialization** can include a pointer to driver-defined context data, which the system supplies as input to *Reinitialize*. If the *Reinitialize* routine uses the registry, the context data should include the *RegistryPath* pointer that was passed to the **DriverEntry** routine because this pointer is not an input parameter to the *Reinitialize* routine.

The *Reinitialize* routine will not be called if **DriverEntry** does not return STATUS\_SUCCESS.

Usually, a driver with a *Reinitialize* routine is a higher-level driver that controls both PnP and legacy devices. In addition to creating device objects for the devices that the PnP manager detects (and for which the PnP manager calls the driver's *AddDevice* routine), the driver must also create device objects for legacy devices that the PnP manager does not enumerate. The *Reinitialize* routine creates those device objects and layers the driver over the next-lower driver for the underlying device.

If a driver has a *Reinitialize* routine, it initializes in the same basic steps described in [Writing a DriverEntry Routine](writing-a-driverentry-routine.md), and it also has the same basic requirements as its **DriverEntry** routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20a%20Reinitialize%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


