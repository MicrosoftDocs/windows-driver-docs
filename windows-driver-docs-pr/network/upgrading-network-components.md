---
title: Process for upgrading network components
description: Process for upgrading network components
ms.assetid: ddd1eda0-7bed-44e7-8636-8db3508825f5
keywords:
- network component upgrades WDK
- upgrading network components WDK
- network component upgrades WDK , about upgrading network components
- upgrading network components WDK , about upgrading network components
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Process for upgrading network components





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (Service Pack 1 \[SP1\] and later), Microsoft Windows Server 2003, and later operating systems.

 

The network upgrade process migrates parameter values for network components during an operating system upgrade. The network upgrade process thus eliminates the need to reconfigure upgraded network components after the new operating system is installed.

The network upgrade process upgrades network components from Microsoft Windows NT 3.51 or Windows NT 4.0 to Microsoft Windows 2000 or later versions of the operating system. The network upgrade process does not upgrade network components from Windows 2000 to later versions of the operating system.

Vendors whose network components are not released as part of Windows 2000 or later should provide upgrade support for these components by supplying the following:

-   A network migration DLL that migrates the preupgrade parameter values for one or more network components.

-   A netmap.inf file that maps the preupgrade device, hardware, or compatible ID of one or more network components, to the corresponding ID in the new operating system.

-   Optional custom Help message files that provide information about upgrading network components.

The network upgrade process is described in the following topics:

[Customizing the Network Upgrade Process](customizing-the-network-upgrade-process.md)

[The Network Upgrade Process](the-network-upgrade-process.md)

[Writing a Network Migration DLL](writing-a-network-migration-dll.md)

[Creating a Netmap.inf File](creating-a-netmap-inf-file.md)

[Testing the Upgrade of Network Components](testing-the-upgrade-of-network-components.md)

Network components whose drivers are released as part of Windows 2000 or later operating systems are automatically upgraded when the operating system is installed. No additional upgrade support is required for such components.

 

 





