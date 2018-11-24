---
title: Opening Software Keys for All Devices in a Setup Class
description: Opening Software Keys for All Devices in a Setup Class
ms.assetid: B601982E-FCD6-4932-813C-A68B2F15FC5C
keywords:
- software keys WDK device installations , opening for all devices in a setup class
- setup classes WDK device installations , opening software keys for devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening Software Keys for All Devices in a Setup Class


When a user-mode application opens the [*software keys*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key) for all devices in a device setup class, it must not directly access the registry to enumerate the subkeys of a device setup class. As with any registry key, the location and name of this key might change between different versions of Windows.

To safely enumerate and open the subkeys of a device setup class, follow these steps:

1.  Use [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) or [**SetupDiGetClassDevsEx**](https://msdn.microsoft.com/library/windows/hardware/ff551072) to retrieve a set of information about all devices for a specified device setup class.

2.  Use [**SetupDiEnumDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551010) to enumerate all devices in the set.

3.  Use [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) to open the software key for each device. The *KeyType* parameter must be set to DIREG_DRV.

**Note**  Some devices might not have software keys, such as when a device is present and enumerated by the [Plug and Play (PnP) manager](pnp-manager.md) but has not been installed.

 

 

 





