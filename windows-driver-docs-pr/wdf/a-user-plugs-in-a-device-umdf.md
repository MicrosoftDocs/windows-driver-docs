---
title: A User Plugs in a Device
description: A User Plugs in a Device
ms.assetid: 1968270b-ce57-4a8c-8b7a-bbd4a972435d
keywords: ["power management scenarios WDK UMDF , plugging in a device", "plugging in a device scenario WDK UMDF"]
---

# A User Plugs in a Device


\[This topic applies to UMDF 1.*x*.\]

When a user plugs in a device, the framework calls a UMDF driver's PnP and Power Management callback methods in the following sequence, starting from the Device Arrived state at the bottom of the figure:

![device enumeration and startup sequence for a umdf driver](images/umdf-powerup-sequence.png)

The framework begins by calling the driver’s [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback so that the driver can create a device callback object and a framework device object to represent the device. The framework continues calling the driver’s callback routines by progressing up through the sequence until the device is operational.

The framework proceeds through this sequence for each UMDF function or filter driver that supports the device, one driver at a time, starting with the driver that is lowest in the driver stack.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20A%20User%20Plugs%20in%20a%20Device%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




