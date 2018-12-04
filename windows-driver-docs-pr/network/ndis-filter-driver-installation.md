---
title: NDIS Filter Driver Installation
description: NDIS Filter Driver Installation
ms.assetid: 8e0c47bf-6b63-4be5-98b7-7a99e9efe283
keywords:
- filter drivers WDK networking , installation
- NDIS filter drivers WDK , installation
- installing NDIS filter drivers WDK networking
ms.date: 12/03/2018
ms.localizationpriority: medium
---

# NDIS Filter Driver Installation

This section provides information about installing NDIS filter drivers. Lightweight Filter drivers are different from filter intermediate drivers. The configuration manager supplies NDIS with a list of filter modules for each miniport adapter. There is no virtual device (or virtual miniport) that is associated with a filter driver as there is with an NDIS filter intermediate driver.

To install a filter driver, you must provide a single INF file. The configuration manager reads configuration information about the filter driver from the INF file and copies it to the registry.

The filter driver INF file defines a network service. Filter drivers do not have a miniport INF file. For an example filter driver INF file, see the [ndislwf](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/ndis/filter) sample driver.

Once you have provided your filter driver INF file, to install or uninstall your filter driver you must use [INetCfg](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff547694%28v%3dvs.85%29). You can either call into this interface programmatically or you can indirectly call it with [netcfg.exe](https://docs.microsoft.com/windows-server/administration/windows-commands/netcfg), which calls `INetCfg` for you. You cannot use [SetupAPI](../install/setupapi.md) to install or uninstall an NDIS filter driver.

For an example of calling into `INetCfg` through code, see the [Bindview Network Configuration Utility sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/config/bindview).

This section includes:

[Specifying Filter Driver Binding Relationships](specifying-filter-driver-binding-relationships.md)

[INF File Settings for Filter Drivers](inf-file-settings-for-filter-drivers.md)

[Accessing Configuration Information for a Filter Driver](accessing-configuration-information-for-a-filter-driver.md)