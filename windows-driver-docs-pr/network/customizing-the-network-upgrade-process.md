---
title: Customizing the Network Upgrade Process
description: Customizing the Network Upgrade Process
ms.assetid: c754317c-fe31-4a61-9c73-93ae71f64b03
keywords:
- network component upgrades WDK , customizing
- upgrading network components WDK , customizing
- customizing network upgrade process WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customizing the Network Upgrade Process





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

System administrators can customize the network upgrade process.

**To customize the network upgrade process**

1.  Create a directory on the system for each network component to be upgraded.

2.  Copy the vendor-supplied upgrade files for each network component to the appropriate directory that you created in Step 1. These files must include a netmap.inf file. NetSetup uses the netmap.inf file to identify which network components to upgrade.

3.  Create a netupg.inf file that contains an **OemNetUpgradeDirs** section and place it a directory of your choice. Each line in the **OemNetUpgradeDirs** section of the netupg.inf file specifies a path to a directory created in Step 1. Each directory specified in the netupg.inf file must contain the vendor-supplied upgrade files for the network component, including a netmap.inf file.

4.  Set the NET\_UPGRD\_INIT\_FILE\_DIR environment variable to the directory that contains the netupg.inf file.

During the Winnt32 phase of the network upgrade, NetSetup locates the netupg.inf file in the directory specified by the NETUPGRD\_INIT\_FILE\_DIR environment variable. In each directory specified in the netupg.inf file, NetSetup then locates the netmap.inf file and other vendor files for the network component to be upgraded. NetSetup processes these files to upgrade the component. For more information, see [The Network Upgrade Process](the-network-upgrade-process.md).

 

 





