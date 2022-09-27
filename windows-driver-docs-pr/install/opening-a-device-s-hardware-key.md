---
title: Opening a device's hardware key
description: Provides information about opening a device's hardware key.
keywords:
- hardware keys WDK device installations , opening
- opening hardware keys WDK device installations
ms.date: 08/15/2022
---

# Opening a device's hardware key

A *hardware key* is device-specific registry subkey that contains information about the device. You must not directly open a device's hardware key. As with any registry key, the location or format of these keys might change between different versions of Windows.

> [!NOTE]
> You should open a device's hardware key only after the corresponding device has been found. For more information about this procedure, see [Enumerating Installed Devices](enumerating-installed-devices.md).

To open or create a device's hardware key, follow these guidelines:

> [!NOTE]
> You must set the parameter where you provide the requested security access to the minimal access permissions that are required. You must not set this parameter to KEY_ALL_ACCESS. For more information about how to specify access permissions for registry access, see [Accessing Registry Keys Safely](accessing-registry-keys-safely.md).

- To open an existing hardware key, use [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) with a *Disposition* of *RegDisposition_OpenExisting* and *ulFlags* containing *CM_REGISTRY_HARDWARE* or use [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) and *KeyType* parameter of *DIREG_DEV*.

- To create a hardware key, use [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) with a *Disposition* of *RegDisposition_OpenAlways* and *ulFlags* containing *CM_REGISTRY_HARDWARE* or use [**SetupDiCreateDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya) and *KeyType* parameter of *DIREG_DEV*.

- Kernel-mode callers should use [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey) and set the *DevInstKeyType* parameter to PLUGPLAY_REGKEY_DEVICE.
