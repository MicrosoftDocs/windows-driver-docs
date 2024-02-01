---
title: Opening a Device'S Software Key
description: Provides information about opening a device's software key.
keywords:
- software keys WDK device installations
- opening software keys WDK device installations
- modifying registry values in a device's software key
- modifying registry values WDK device installations , device software key
ms.date: 08/15/2022
---

# Opening a device's software key

You must not directly open a device's *software key*. As with any registry key, the location or format of these keys might change between different versions of Windows.

> [!NOTE]
> You should open a device's software key only after the corresponding device has been found. For more information about this procedure, see [Enumerating Installed Devices](enumerating-installed-devices.md).

To open or create a device's software key, follow these guidelines:

> [!NOTE]
> You must set the parameter where you provide the requested security access to the minimal access permissions that are required. You must not set this parameter to KEY_ALL_ACCESS. For more information about how to specify access permissions for registry access, see [Accessing Registry Keys Safely](accessing-registry-keys-safely.md).

- To open an existing software key, use [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) with a *Disposition* of *RegDisposition_OpenExisting* and *ulFlags* containing *CM_REGISTRY_SOFTWARE* or use [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) and *KeyType* parameter of *DIREG_DRV*.

- To create a software key, use [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) with a *Disposition* of *RegDisposition_OpenAlways* and *ulFlags* containing *CM_REGISTRY_SOFTWARE* or use [**SetupDiCreateDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya) and *KeyType* parameter of *DIREG_DRV*.

- Kernel-mode callers should use [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey) and set the *DevInstKeyType* parameter to PLUGPLAY_REGKEY_DRIVER.

## Modifying Registry Values in a Device's Software Key

You must not modify the values of the following registry entries (*device properties*) in a device's [*software key*](opening-a-device-s-software-key.md):

- DriverDate

- DriverDateData

- DriverDesc

- DriverVersion

- InfPath

- InfSection

- InfSectionExt

- MatchingDeviceId

- ProviderName

- EnumPropPages32

These device properties represent a device's installation state. Direct modification of these properties might invalidate the device's installation state. For example, changing information related to the [INF file](overview-of-inf-files.md) invalidates information about driver files that are associated with such properties as device and driver signing information. Changing driver version or driver date might break Windows Update functionality.

> [!NOTE]
> Starting with Windows Vista, the operating system imposes "installation-time only" access restrictions for these properties. Values can be replicated for compatibility, and direct modification of values during device installation does not affect internal state.
