---
title: Accessing Registry Keys Safely
description: Provides information about accessing registry keys safely.
keywords:
- registry WDK device installations , accessing registry keys safely
- accessing registry keys safely WDK device installations
ms.date: 08/15/2022
---

# Accessing registry keys safely

Customer problems have frequently been traced to external components, such as third-party [device installation applications](writing-a-device-installation-application.md), that do the following:

- Delete critical registry keys.

- Modify the access permissions of critical registry keys.

Many of the problems seen with external components are caused by using the KEY_ALL_ACCESS access permission for registry keys. Starting with Windows Server 2003, [**SetupDiCreateDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya) grants only KEY_READ and KEY_WRITE access permissions and not KEY_ALL_ACCESS. Starting with Windows Vista, additional KEY_ALL_ACCESS restrictions are enforced.

Follow these guidelines to safely access registry keys:

- Use only the [SetupAPI](setupapi.md), [configuration manager](/windows/win32/api/cfgmgr32/) functions, and other supported device related APIs to open device registry keys, especially the [*hardware keys*](opening-a-device-s-hardware-key.md) and [*software keys*](opening-a-device-s-software-key.md) for a device.

    These functions address common problems that result from restrictions on access permissions.

- The location and format of registry keys might change between different versions of Windows. Do not make assumptions about the location, format, or meaning of registry keys or values that are used for device and driver installation.

    For more information about registry keys and trees, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

- Do not use the registry to directly access or modify the internal settings of the device.

- Request only the minimal access permissions that are required for each task, such as the following:

  - KEY_SET_VALUE

  - KEY_CREATE_SUB_KEY

  - KEY_QUERY_VALUE

  - KEY_ENUMERATE_SUB_KEYS

- Do not directly open the device setup class keys in the registry. As with any registry key, the location and name of device setup class keys might change between versions of Windows. For information on how to properly access a device setup class key, see [Opening registry keys for a device setup class](opening-registry-keys-for-a-device-setup-class.md)

- Do not directly open device interface class keys in the registry. As with any registry key, the location and name of device interface class keys might change between versions of Windows.

    To open device interface class keys safely, use [**CM_Open_Class_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_class_keyw) with setting CM_OPEN_CLASS_KEY_INTERFACE in the *ulFlags* parameter or use [**SetupDiOpenClassRegKeyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa) and set DIOCR_INSTALLER in the *Flags* parameter.

- Use only INF directives to modify registry keys that are reserved for use by the operating system. For more information, see [Summary of INF Directives](summary-of-inf-directives.md).

- *Class installers* and *co-installers* cannot call registry functions to create, change, or delete registry values that are reserved for use by the operating system.

For more information about the access permissions of registry keys, see [Registry Key Security and Access Rights](/windows/win32/sysinfo/registry-key-security-and-access-rights).
