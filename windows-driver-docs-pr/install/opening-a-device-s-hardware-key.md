---
title: Opening a Device's Hardware Key
description: Opening a Device's Hardware Key
ms.assetid: FED22F37-D09C-4207-8C2C-FB6484A8D19D
keywords:
- hardware keys WDK device installations , opening
- opening hardware keys WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening a Device's Hardware Key


A *hardware key* is device-specific registry subkey that contains information about the device. You must not directly open a device's hardware key. As with any registry key, the location or format of these keys might change between different versions of Windows. 

**Note**  You should open a device's hardware key only after the corresponding device has been found. For more information about this procedure, see [Enumerating Installed Devices](enumerating-installed-devices.md).

 

To open or create a device's hardware key, follow these guidelines:

-   To open an existing hardware key, use [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079). To create a hardware key, use [**SetupDiCreateDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550973). In either case, you must set the *KeyType* parameter to DIREG_DEV.

    **Note**  You must set the *samDesired* parameter to the minimal access permissions that are required. You must not set this parameter to KEY_ALL_ACCESS. For more information about how to specify access permissions for registry access, see [Accessing Registry Keys Safely](accessing-registry-keys-safely.md).

     

-   Kernel-mode callers should use [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443) and set the *DevInstKeyType* parameter to PLUGPLAY_REGKEY_DEVICE.

 

 





