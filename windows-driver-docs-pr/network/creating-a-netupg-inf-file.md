---
title: Creating a Netupg.inf File
description: Creating a Netupg.inf File
ms.assetid: 8ee000e0-abd1-4a06-9f38-2a7971bc2c97
keywords:
- netupg.inf files WDK
- network component upgrades WDK , customizing
- upgrading network components WDK , customizing
- customizing network upgrade process WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Netupg.inf File





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

The netupg.inf file contains a single section called **OemNetUpgradeDirs**. Each entry in this section specifies the complete path to a directory that contains the vendor-supplied upgrade files for a non-Microsoft-supported network component. Every network component being upgraded must have a corresponding entry in the **OemNetUpgradeDirs** section.

The following is an example of a netupg.inf file:

```INF
[OemNetUpgradeDirs]
c:\temp\adapter1
c:\temp\adapter2
c:\temp\protocol1
c:\temp\netclient1
c:\temp\netservice1
```

Each directory specified in the **OemNetUpgradeDirs** section must contain a netmap.inf file. This file, which is provided by the vendor of the network component, maps the preupgrade device, hardware or compatible ID of a network component to the corresponding ID in the upgraded operating system.

 

 





