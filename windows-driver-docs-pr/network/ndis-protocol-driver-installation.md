---
title: NDIS Protocol Driver Installation
description: Learn how to install a Network Driver Interface Specification (NDIS) protocol driver.
keywords:
- protocol drivers WDK networking , installation
- NDIS protocol drivers WDK , installation
- installing NDIS protocol drivers WDK networking
ms.date: 12/17/2024
---

# NDIS protocol driver installation

To install a Network Driver Interface Specification (NDIS) protocol driver, you must first provide a setup information (INF) file. The configuration manager reads configuration information about the protocol driver from the INF file and copies it to the registry.

For more information about protocol driver INF files, see [Installation Requirements for Network Protocols](installation-requirements-for-network-protocols.md). For an example protocol driver INF file, see the [ndisprot 630](https://github.com/microsoft/Windows-driver-samples/tree/95037b3f77f3a745f7682f991ac80e81f91f5362/network/ndis/ndisprot/6x/sys/630) sample driver.

After you provide your protocol driver INF file, you must use the `INetCfg` family of [Network Configuration Interfaces](/previous-versions/windows/hardware/network/ff559080(v=vs.85)) to install or uninstall your protocol driver. For example, to install or remove network components, call into the [INetCfgClassSetup](/previous-versions/windows/hardware/network/ff547709(v=vs.85)) interface. You can either call into these interfaces programmatically or you can indirectly call them by using [netcfg.exe](/windows-server/administration/windows-commands/netcfg), which calls `INetCfg` for you. You can't install a driver package through the `INetCfg` and use the [Driver Store](../develop/run-from-driver-store.md) feature on older Windows versions. To successfully install the driver package in this scenario, you need to have a minimum OS build number of 25319. You can't use [SetupAPI](../install/setupapi.md) to install or uninstall an NDIS protocol driver.

For an example of calling into `INetCfg` through code, see the [Bindview Network Configuration Utility sample](https://github.com/microsoft/Windows-driver-samples/tree/95037b3f77f3a745f7682f991ac80e81f91f5362/network/config/bindview) on GitHub.
