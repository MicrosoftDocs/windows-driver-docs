---
title: NDIS Filter Driver Installation
description: NDIS Filter Driver Installation
keywords:
- filter drivers WDK networking , installation
- NDIS filter drivers WDK , installation
- installing NDIS filter drivers WDK networking
ms.date: 01/16/2019
ms.localizationpriority: medium
---

# NDIS Filter Driver Installation

This section provides information about installing NDIS filter drivers. Lightweight Filter drivers are different from filter intermediate drivers. The configuration manager supplies NDIS with a list of filter modules for each miniport adapter. There is no virtual device (or virtual miniport) that is associated with a filter driver as there is with an NDIS filter intermediate driver.

To install a filter driver, you must provide a single INF file. The configuration manager reads configuration information about the filter driver from the INF file and copies it to the registry.

The filter driver INF file defines a network service. Filter drivers do not have a miniport INF file. For an example filter driver INF file, see the [ndislwf](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/ndis/filter) sample driver.

Once you have provided your filter driver INF file, to install or uninstall your filter driver you must use the `INetCfg` family of [Network Configuration Interfaces](/previous-versions/windows/hardware/network/ff559080(v=vs.85)). For example, to install or remove network components, call into the [INetCfgClassSetup](/previous-versions/windows/hardware/network/ff547709(v=vs.85)) interface. You can either call into these interfaces programmatically or you can indirectly call them with [netcfg.exe](/windows-server/administration/windows-commands/netcfg), which calls `INetCfg` for you. You cannot use [SetupAPI](../install/setupapi.md) to install or uninstall an NDIS filter driver.

For an example of calling into `INetCfg` through code, see the [Bindview Network Configuration Utility sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/config/bindview).

This section includes:

[Specifying Filter Driver Binding Relationships](specifying-filter-driver-binding-relationships.md)

[INF File Settings for Filter Drivers](inf-file-settings-for-filter-drivers.md)

[Accessing Configuration Information for a Filter Driver](accessing-configuration-information-for-a-filter-driver.md)
