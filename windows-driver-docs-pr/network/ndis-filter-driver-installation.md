---
title: NDIS Filter Driver Installation
description: Learn how to install an NDIS filter driver using a setup information (INF) file.
ms.date: 01/31/2025
---

# NDIS filter driver installation

This article explains how to install Network Driver Interface Specification (NDIS) filter drivers. Lightweight filter drivers are different from filter intermediate drivers. The configuration manager supplies NDIS with a list of filter modules for each miniport adapter. There's no virtual device (or virtual miniport) that's associated with a filter driver as there is with an NDIS filter intermediate driver.

To install a filter driver, you must provide a setup information (INF) file. The configuration manager reads configuration information about the filter driver from the INF file and copies it to the registry.

The filter driver INF file defines a network service. Filter drivers don't have a miniport INF file. For an example filter driver INF file, see the [ndislwf](https://github.com/microsoft/Windows-driver-samples/tree/95037b3f77f3a745f7682f991ac80e81f91f5362/network/ndis/filter) sample driver.

Once you have provided your filter driver INF file, to install or uninstall your filter driver you must use the `INetCfg` family of [Network Configuration Interfaces](/previous-versions/windows/hardware/network/ff559080(v=vs.85)). For example, to install or remove network components, call into the [INetCfgClassSetup](/previous-versions/windows/hardware/network/ff547709(v=vs.85)) interface. You can either call into these interfaces programmatically or you can indirectly call them with [netcfg](/windows-server/administration/windows-commands/netcfg), which calls `INetCfg` for you. You can't install a driver package through the `INetCfg` and use the [Driver Store](../develop/run-from-driver-store.md) feature on older Windows versions. To successfully install the driver package in this scenario, you need to have a minimum OS build number of 25319. You can't use [SetupAPI](../install/setupapi.md) to install or uninstall an NDIS filter driver.

For an example of calling into `INetCfg` through code, see the [Bindview Network Configuration Utility sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/network/config/bindview).

## Related content

- [Specifying Filter Driver Binding Relationships](specifying-filter-driver-binding-relationships.md)
- [INF File Settings for Filter Drivers](inf-file-settings-for-filter-drivers.md)
- [Accessing Configuration Information for a Filter Driver](accessing-configuration-information-for-a-filter-driver.md)
