---
title: Opening Software Keys for All Devices in a Setup Class
description: Opening Software Keys for All Devices in a Setup Class
ms.assetid: B601982E-FCD6-4932-813C-A68B2F15FC5C
keywords: ["software keys WDK device installations , opening for all devices in a setup class", "setup classes WDK device installations , opening software keys for devices"]
---

# Opening Software Keys for All Devices in a Setup Class


When a user-mode application opens the [*software keys*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key) for all devices in a device setup class, it must not directly access the registry to enumerate the subkeys of a device setup class. As with any registry key, the location and name of this key might change between different versions of Windows.

To safely enumerate and open the subkeys of a device setup class, follow these steps:

1.  Use [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) or [**SetupDiGetClassDevsEx**](https://msdn.microsoft.com/library/windows/hardware/ff551072) to retrieve a set of information about all devices for a specified device setup class.

2.  Use [**SetupDiEnumDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551010) to enumerate all devices in the set.

3.  Use [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) to open the software key for each device. The *KeyType* parameter must be set to DIREG\_DRV.

**Note**  Some devices might not have software keys, such as when a device is present and enumerated by the [Plug and Play (PnP) manager](pnp-manager.md) but has not been installed.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Opening%20Software%20Keys%20for%20All%20Devices%20in%20a%20Setup%20Class%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




