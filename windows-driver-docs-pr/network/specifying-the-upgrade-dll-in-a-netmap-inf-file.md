---
title: Specifying the Upgrade DLL in a Netmap.inf File
description: Specifying the Upgrade DLL in a Netmap.inf File
ms.assetid: 01735a7d-ee33-427d-befa-7429fd64353b
keywords:
- network component upgrades WDK , netmap.inf files
- upgrading network components WDK , netmap.inf files
- netmap.inf files WDK
- upgrade DLL WDK netmap.inf
- device IDs WDK netmap.inf
- network-migration-DLL WDK netmap.inf
- DLLs WDK network upgrades
- vendor-supplied files WDK netmap.inf file
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying the Upgrade DLL in a Netmap.inf File





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

A netmap.inf file must have an **OemUpgradeSupport** section. For each network component to be upgraded, the **OemUpgradeSupport** section must contain an entry that has the following format:

*postupgrade-ID* = *network-migration-DLL*\[ , *Inf-file-name*\]

where:

*postupgrade-ID* is the network component's Windows 2000 or later device ID, which was obtained by NetSetup, as described in [Winnt32 Phase of the Network Upgrade Process](winnt32-phase-of-the-network-upgrade-process.md).

*network-migration-DLL* is the name of the network migration DLL that NetSetup must load to upgrade the network component. Only one migration DLL can be specified in a netmap.inf file. If the netmap.inf file contains device ID mappings for more than one component, then all such components must be upgraded by the same migration DLL.

*Inf-file-name* is the name of the INF file that installs the network component.

 

 





