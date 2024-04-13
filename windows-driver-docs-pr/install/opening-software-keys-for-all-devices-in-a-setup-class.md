---
title: Opening Software Keys for All Devices in a Setup Class
description: Provides information about opening software keys for all devices in a setup class.
keywords:
- software keys WDK device installations , opening for all devices in a setup class
- setup classes WDK device installations , opening software keys for devices
ms.date: 08/15/2022
---

# Opening software keys for all devices in a setup class

When a user-mode application opens the [*software keys*](opening-a-device-s-software-key.md) for all devices in a [device setup class](overview-of-device-setup-classes.md), it must not directly access the registry to enumerate the subkeys of a device setup class. As with any registry key, the location and name of this key might change between different versions of Windows.

To safely enumerate and open the subkeys of a device setup class, follow these steps:

> [!NOTE]
> Some devices might not have software keys, such as when a device is present and enumerated by the [Plug and Play (PnP) manager](pnp-manager.md) but has not been installed.

Using [configuration manager](/windows/win32/api/cfgmgr32/) functions:

1. Use [**CM_Get_Device_ID_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_listw) with a *ulFlags* of *CM_GETIDLIST_FILTER_CLASS* and a *pszFilter* with the GUID of the desired device setup class to retrieve a list of device instance paths for all devices in the specified device setup class.

1. For each returned device instance path, use [**CM_Locate_DevNode**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_locate_devnodew) to retrieve a **DEVINST** representing the device.

1. Use [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) with *ulFlags* containing *CM_REGISTRY_SOFTWARE* to open the software key for each device. See [Opening a device's software key](opening-a-device-s-software-key.md) for more information.

Using [SetupApi](setupapi.md) functions:

1. Use [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) or [**SetupDiGetClassDevsEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa) to retrieve a set of information about all devices for a specified device setup class.

1. Use [**SetupDiEnumDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo) to enumerate all devices in the set.

1. Use [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) to open the software key for each device. The *KeyType* parameter must be set to DIREG_DRV.
