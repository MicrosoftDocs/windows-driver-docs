---
title: GPIO Device Contexts
author: windows-driver-content
description: A general-purpose I/O (GPIO) controller device is represented by a framework device object.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4BE99C71-9BA6-44E3-A54F-DE8C3440A474
---

# GPIO Device Contexts


A general-purpose I/O (GPIO) controller device is represented by a framework device object. The GPIO controller driver can associate a device context with this device object. The driver uses this device context to persistently store information about the state of the GPIO controller device.

When the GPIO framework extension (GpioClx) calls an event callback function that is implemented by the driver, GpioClx passes the device context to this function as a parameter. The callback function examines the device context to determine the current state of the device. If the function alters this state, it updates the device context accordingly.

GpioClx allocates the storage for a device object. If a GPIO controller driver has more than one device object, the device context for each of these objects is the same size. During the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, the driver calls the [**GPIO\_CLX\_RegisterClient**](https://msdn.microsoft.com/library/windows/hardware/hh439490) method to register its callback functions and to specify the device context size that it requires. Later, during the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback routine, the driver calls the [**GPIO\_CLX\_ProcessAddDevicePostDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/hh439484) method to pass the new device object to GpioClx, and GpioClx allocates the device context for this object. Thereafter, when GpioClx calls a driver-implemented callback function, this device context is passed to the function as a parameter.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bgpio\parports%5D:%20GPIO%20Device%20Contexts%20%20RELEASE:%20%286/3/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


