---
title: Opening a Device's Software Key
description: Opening a Device's Software Key
ms.assetid: CA9EC186-7991-4cc5-B49E-DFE87A13BCFA
keywords:
- software keys WDK device installations , opening
- opening software keys WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening a Device's Software Key


You must not directly open a device's [*software key*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key). As with any registry key, the location or format of these keys might change between different versions of Windows.

**Note**  You should open a device's software key only after the corresponding device has been found. For more information about this procedure, see [Enumerating Installed Devices](enumerating-installed-devices.md).

 

To open a device's software key, follow these guidelines:

-   To open an existing software key, use [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079). To create a software key, use [**SetupDiCreateDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550973). In either case, you must set the *KeyType* parameter to DIREG_DRV.

    **Note**  You must set the *samDesired* parameter to the minimal access permissions that are required. You must not set this parameter to KEY_ALL_ACCESS. For more information about how to specify access permissions for registry access, see [Accessing Registry Keys Safely](accessing-registry-keys-safely.md).

     

-   Kernel-mode callers should use [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443) and set the *DevInstKeyType* parameter to PLUGPLAY_REGKEY_DRIVER.

 

 





