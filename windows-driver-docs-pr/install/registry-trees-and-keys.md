---
title: Registry Trees and Keys for Devices and Drivers
description: Registry Trees and Keys for Devices and Drivers
ms.date: 05/20/2022
---

# Registry Trees and Keys for Devices and Drivers

The operating system, drivers, and device installation components store information about drivers and devices in the registry. In general, drivers and device installation components should use the registry to store data that must be maintained across restarts of the system. For information about how a driver accesses registry information, see [Using the Registry in a Driver](../kernel/registry-key-object-routines.md).

Registry contents should always be treated as untrusted, modifiable information. If one of your driver components writes information to the registry and another component reads it later, do not assume that the information has not been modified in the meantime. After reading information from the registry, your driver components should always validate the information before using it.

For more information about the registry in general, see the Microsoft Windows SDK documentation.

This section contains the following topics which describe the use of registry keys to store information about drivers and devices:

- [Registry Trees for Devices and Drivers](overview-of-registry-trees-and-keys.md)

- [RunOnce Registry Key](runonce-registry-key.md)

- [DeviceOverrides Registry Key](deviceoverrides-registry-key.md)

Drivers must access Plug and Play (PnP) keys in the registry using system routines such as [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty) or [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey). User-mode setup components should use device installation functions such as [**CM_Get_DevNode_Registry_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_registry_propertyw) or [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key). The registry can be accessed from INF files by using [**INF AddReg directives**](inf-addreg-directive.md). See the [registry state section of the driver package isolation page](../develop/driver-isolation.md#registry-state) for more information.

> [!IMPORTANT]
> Drivers must not access these registry trees and keys directly. This discussion of registry information in this section is solely for debugging a device installation or configuration problem.

 

