---
title: Opening a Device's Software Key
description: Opening a Device's Software Key
keywords:
- software keys WDK device installations , opening
- opening software keys WDK device installations
ms.date: 04/20/2017
---

# Opening a Device's Software Key


You must not directly open a device's *software key*. As with any registry key, the location or format of these keys might change between different versions of Windows.

**Note**  You should open a device's software key only after the corresponding device has been found. For more information about this procedure, see [Enumerating Installed Devices](enumerating-installed-devices.md).

 

To open a device's software key, follow these guidelines:

-   To open an existing software key, use [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey). To create a software key, use [**SetupDiCreateDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya). In either case, you must set the *KeyType* parameter to DIREG_DRV.

    **Note**  You must set the *samDesired* parameter to the minimal access permissions that are required. You must not set this parameter to KEY_ALL_ACCESS. For more information about how to specify access permissions for registry access, see [Accessing Registry Keys Safely](accessing-registry-keys-safely.md).

     

-   Kernel-mode callers should use [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey) and set the *DevInstKeyType* parameter to PLUGPLAY_REGKEY_DRIVER.

 

