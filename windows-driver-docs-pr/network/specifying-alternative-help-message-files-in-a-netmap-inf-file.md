---
title: Specifying Alternative Help Message Files in a Netmap.inf File
description: Specifying Alternative Help Message Files in a Netmap.inf File
ms.assetid: 66ab7124-803a-4497-b5e0-98b47006dfb6
keywords:
- network component upgrades WDK , netmap.inf files
- upgrading network components WDK , netmap.inf files
- netmap.inf files WDK
- device IDs WDK netmap.inf
- Help message files WDK netmap.inf
- alternate Help message files WDK netmap.inf
- vendor-supplied files WDK netmap.inf file
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Alternative Help Message Files in a Netmap.inf File





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

If NetSetup fails to find the device ID mapping for a network component in any of the netmap.inf files, it lists this component on the Compatibility Report page in the wizard. Associated with each such component is a Help message file.

By default, NetSetup displays a Help message contained in the \\winntupg\\unsupmsg.txt file or, if an HTML browser is installed on the system, in the \\winntupg\\unsupmsg.htm file. You can optionally supply a custom message file that overrides the unsupmsg.txt and unsupmsg.txt message files. For example, if a vendor provides upgrade support for only some of its network components, the vendor could supply a custom Help message file that indicates that upgrade support is not provided for certain components.

An optional **OemUpgradeHelpFiles** section in a netmap.inf file specifies one or more custom Help message files. Each entry in this section has the following format:

*postupgrade-ID* = *text-name*, *htm-file*

where:

*postupgrade-ID* is the Windows 2000 or later device ID of network component

*text-name* is the path and name of the text version of the custom Help message file

*htm-file* is the path and name of the HTML version of the custom Help message file.

If a full path name is not specified in *text-name* or *htm-file*, the specified path is appended to the i386 directory--for example: \\i386\\mydirectory\\myfile.txt.

The following example of a netmap.inf file contains an **OemUpgradeHelpFiles** section.

```INF
[Version]
signature="$WindowsNT$

[OemNetProtocols]
Protocol1=Protoco1_2000
Protocol2=Protocol2_2000

[OemUpgradeSupport]
Protocol1=NotSupported
Protocol2=abc_upgrade.dll, abc.inf

[OemUpgradeHelpFiles]
Protoco11=helpmsg.txt, helpmsg.htm
```

Even though this sample netmap.inf file does not provide upgrade support for Protocol1, it provides a device ID mapping for Protocol1 in the **OemNetProtocols** section. This mapping specifies a Windows 2000 device ID for Protocol1. The Windows 2000 device ID is required to associate custom Help message files with a network component.

Notice that the keyword **NotSupported** is assigned to Protocol1 in the **OemUpgradeHelpFiles** section. This keyword indicates that there is no need to load a migration DLL to upgrade Protocol1.

In the **OemUpgradeHelpFiles** section of the previous example, the Protoco11=helpmsg.txt, helpmsg.htm entry specifies two custom Help message files for Protocol1. The custom Help message contained in these files could indicate, for example, that the vendor does not support the upgrade of Protocol1 and that the user must separately upgrade Protocol1 to Protocol2 before attempting to upgrade the system to Windows 2000 or later.

 

 





