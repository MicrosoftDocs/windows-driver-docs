---
title: A User Unplugs a Device
description: A User Unplugs a Device
ms.assetid: d0c8fd6d-b356-4048-aa97-ebe331d23361
keywords: ["power management scenarios WDK UMDF , unplugging a device", "unplugging a device scenario WDK UMDF"]
---

# A User Unplugs a Device


\[This topic applies to UMDF 1.*x*.\]

While a system is running, a user can remove a device in one of the following two ways: by *orderly removal*, which means that the user informs the system that the device is about to be removed (for example, by using the Unplug or Eject Hardware program); or by *surprise removal*, which means that the user unplugs the device without informing the system. If the bus supports surprise removal (for example, USB), the device's drivers must be able to handle the device's sudden disappearance.

<a href="" id="orderly-removal-------"></a>**Orderly Removal**   
The user requests removal by using the system's Unplug or Eject Hardware program, by disabling the device by using Device Manager, or by pushing an ejectable device's eject button. The framework allows the device to be removed or disabled, unless the driver has supplied an [**IPnpCallback::OnQueryRemove**](https://msdn.microsoft.com/library/windows/hardware/ff556808) callback function, and the callback function has vetoed the removal.

The following figure shows the sequence of UMDF callbacks in power-down and removal. The sequence starts at the top of the figure with a device that is in the working power state (D0).

![device power-down and orderly removal sequence for a umdf driver](images/umdf-powerdown-sequence.png)

<a href="" id="surprise-removal-------"></a>**Surprise Removal**   
In this scenario, a user unplugs a device unexpectedly. In the surprise-removal sequence, UMDF calls the [**IPnpCallback::OnSurpriseRemoval**](https://msdn.microsoft.com/library/windows/hardware/ff556812) callback to notify the driver that the device has been unexpectedly removed. This callback is not guaranteed to occur in any particular order with the other callbacks in the removal sequence.

Generally, the driver should avoid accessing the hardware in the remove path. The reflector times out if an attempt to access the hardware waits indefinitely. The following figure shows the surprise-removal sequence for a UMDF driver.

![surprise-removal sequence for a umdf driver](images/umdf-surprise-removal-sequence.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20A%20User%20Unplugs%20a%20Device%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




