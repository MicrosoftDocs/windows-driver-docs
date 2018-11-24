---
title: GPIO Device Contexts
description: A general-purpose I/O (GPIO) controller device is represented by a framework device object.
ms.assetid: 4BE99C71-9BA6-44E3-A54F-DE8C3440A474
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPIO Device Contexts


A general-purpose I/O (GPIO) controller device is represented by a framework device object. The GPIO controller driver can associate a device context with this device object. The driver uses this device context to persistently store information about the state of the GPIO controller device.

When the GPIO framework extension (GpioClx) calls an event callback function that is implemented by the driver, GpioClx passes the device context to this function as a parameter. The callback function examines the device context to determine the current state of the device. If the function alters this state, it updates the device context accordingly.

GpioClx allocates the storage for a device object. If a GPIO controller driver has more than one device object, the device context for each of these objects is the same size. During the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, the driver calls the [**GPIO\_CLX\_RegisterClient**](https://msdn.microsoft.com/library/windows/hardware/hh439490) method to register its callback functions and to specify the device context size that it requires. Later, during the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback routine, the driver calls the [**GPIO\_CLX\_ProcessAddDevicePostDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/hh439484) method to pass the new device object to GpioClx, and GpioClx allocates the device context for this object. Thereafter, when GpioClx calls a driver-implemented callback function, this device context is passed to the function as a parameter.

 

 




