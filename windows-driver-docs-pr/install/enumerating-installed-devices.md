---
title: Enumerating Installed Devices
description: Enumerating Installed Devices
ms.assetid: 98EF9A16-6415-4778-BB5D-C0B7160C1509
keywords: ["enumerating installed devices WDK", "installed devices WDK , enumerating"]
---

# Enumerating Installed Devices


You should not enumerate devices by using registry keys directly. Registry keys do not contain the required information to enumerate installed devices on the system. This information, such as whether the device is actually present or is a phantom device (one that is not plugged in), is held by the [Plug and Play (PnP) manager](pnp-manager.md). The PnP manager also performs additional filtering of registry information.

To enumerate installed devices safely, follow these steps:

1.  Use [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) or [**SetupDiGetClassDevsEx**](https://msdn.microsoft.com/library/windows/hardware/ff551072) to retrieve information for a set of devices that belong to a specified device setup class. To retrieve information only for devices that are present in the system, set DIGCF\_PRESENT in the *Flags* parameter.

2.  Use [**SetupDiEnumDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551010) to enumerate the devices in the set.

3.  Use [**SetupDiGetDeviceInstanceId**](https://msdn.microsoft.com/library/windows/hardware/ff551106) to retrieve unique [device instance identifiers (IDs)](device-instance-ids.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Enumerating%20Installed%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




