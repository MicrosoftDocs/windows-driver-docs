---
title: NDIS protocol driver installation
description: NDIS protocol driver installation
keywords:
- protocol drivers WDK networking , installation
- NDIS protocol drivers WDK , installation
- installing NDIS protocol drivers WDK networking
ms.date: 01/16/2019
---

# NDIS protocol driver installation

To install a protocol driver, you must first provide a single INF file. The configuration manager reads configuration information about the protocol driver from the INF file and copies it to the registry. 

For more information about protocol driver INF files, see [Installation Requirements for Network Protocols](installation-requirements-for-network-protocols.md). For an example protocol driver INF file, see the [ndisprot 630](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/ndis/ndisprot/6x/sys/630) sample driver.

Once you have provided your protocol driver INF file, to install or uninstall your protocol driver you must use the `INetCfg` family of [Network Configuration Interfaces](/previous-versions/windows/hardware/network/ff559080(v=vs.85)). For example, to install or remove network components, call into the [INetCfgClassSetup](/previous-versions/windows/hardware/network/ff547709(v=vs.85)) interface. You can either call into these interfaces programmatically or you can indirectly call them with [netcfg.exe](/windows-server/administration/windows-commands/netcfg), which calls `INetCfg` for you. You cannot use [SetupAPI](../install/setupapi.md) to install or uninstall an NDIS protocol driver.

For an example of calling into `INetCfg` through code, see the [Bindview Network Configuration Utility sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/config/bindview).
