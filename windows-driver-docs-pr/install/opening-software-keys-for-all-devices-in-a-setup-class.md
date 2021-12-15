---
title: Opening Software Keys for All Devices in a Setup Class
description: Opening Software Keys for All Devices in a Setup Class
keywords:
- software keys WDK device installations , opening for all devices in a setup class
- setup classes WDK device installations , opening software keys for devices
ms.date: 04/20/2017
---

# Opening Software Keys for All Devices in a Setup Class


When a user-mode application opens the *software keys* for all devices in a device setup class, it must not directly access the registry to enumerate the subkeys of a device setup class. As with any registry key, the location and name of this key might change between different versions of Windows.

To safely enumerate and open the subkeys of a device setup class, follow these steps:

1.  Use [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) or [**SetupDiGetClassDevsEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa) to retrieve a set of information about all devices for a specified device setup class.

2.  Use [**SetupDiEnumDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo) to enumerate all devices in the set.

3.  Use [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) to open the software key for each device. The *KeyType* parameter must be set to DIREG_DRV.

**Note**  Some devices might not have software keys, such as when a device is present and enumerated by the [Plug and Play (PnP) manager](pnp-manager.md) but has not been installed.

 

 

