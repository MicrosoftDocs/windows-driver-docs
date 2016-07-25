---
title: Overview of Device Setup Classes
description: Overview of Device Setup Classes
ms.assetid: 318ec3f4-f2c2-437c-a767-494ac240cb89
---

# Overview of Device Setup Classes


To facilitate device installation, devices that are set up and configured in the same manner are grouped into a device setup class. For example, SCSI media changer devices are grouped into the MediumChanger device setup class. The device setup class defines the class installer and class co-installers that are involved in installing the device.

Microsoft defines setup classes for most devices. IHVs and OEMs can define new device setup classes, but only if none of the existing classes apply. For example, a camera vendor does not have to define a new setup class because cameras fall under the Image setup class. Similarly, uninterruptible power supply (UPS) devices fall under the Battery class.

There is a GUID associated with each device setup class. System-defined setup class GUIDs are defined in *Devguid.h* and typically have symbolic names of the form GUID\_DEVCLASS\_*Xxx*.

The device setup class GUID defines the **..\\CurrentControlSet\\Control\\Class\\***ClassGuid* registry key under which to create a new subkey for any particular device of a standard setup class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Overview%20of%20Device%20Setup%20Classes%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




