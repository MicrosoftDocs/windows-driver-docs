---
title: Creating a Netmap.inf File
description: Creating a Netmap.inf File
ms.assetid: 0f9b4f57-717c-4f11-b0c6-d117a949ab38
keywords:
- network component upgrades WDK , netmap.inf files
- upgrading network components WDK , netmap.inf files
- netmap.inf files WDK
- vendor-supplied files WDK netmap.inf file
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Netmap.inf File





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

The netmap.inf file is a vendor-supplied file that resides either in a directory specified by an entry in the **OemNetUpgradeDirs** section of a [netupg.inf](creating-a-netupg-inf-file.md) file or in the directory that contains netupgrd.dll. The netmap.inf file:

-   Maps a network component's preupgrade device ID to the component's Microsoft Windows 2000 or later device ID

-   Specifies the network migration DLL that NetSetup loads

-   Optionally specifies an alternative Help message file

A network component that has built-in upgrade support in Windows 2000 or later operating systems does not require a vendor-supplied netmap.inf file because these components are automatically upgraded during the installation of Windows 2000 and later operating systems.

This section includes the following topics:

-   [Mapping IDs in a Netmap.inf File](mapping-ids-in-a-netmap-inf-file.md)
-   [Specifying the Upgrade DLL in a Netmap.inf File](specifying-the-upgrade-dll-in-a-netmap-inf-file.md)
-   [Specifying Alternative Help Message Files in a Netmap.inf File](specifying-alternative-help-message-files-in-a-netmap-inf-file.md)

 

 





