---
title: INF DDInstall.MigrateToDevNode Section
author: windows-driver-content
description: INF DDInstall.MigrateToDevNode Section
ms.assetid: a4edbc9e-a2d0-4012-aca9-0b357939a881
keywords:
- INF files WDK non-HID keyboard/mouse
- DDInstall.MigrateToDevNode section
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF DDInstall.MigrateToDevNode Section





**\[***install-section-name***.MigrateToDevNode\]** |
**\[***install-section-name***.nt.MigrateToDevNode\]** |
**\[***install-section-name***.ntx86.MigrateToDevNode\]** |
**\[***install-section-name***.ntia64.MigrateToDevNode\]**

*ServiceName***=***value-name*\[**,***value-name*\],...
The keyboard and mouse class installers copy the entry values specified by the list of *value-name* strings from the registry key **HKLM\\System\\CurrentControlSet\\Services\\***ServiceName***\\Parameters** to the device node of the device being installed.

### Entries and Values

<a href="" id="servicename"></a>*ServiceName*  
Specifies the service name associated with a device port (for example, **i8042prt**, **sermouse**, and so on).

<a href="" id="value-name"></a>*value-name*  
Specifies an entry value under the registry key **HKLM\\System\\CurrentControlSet\\Services\\***ServiceName***\\Parameters**.

### <a href="" id="comments"></a>Remarks

Microsoft supports INF *DDinstall***.MigratetoDevNode** sections primarily to facilitate porting Windows NT 4.0 legacy devices to Windows 2000 and later.

The keyboard and mouse class installers copy all the *value-name* entry values before the system starts the device stack. The specified entry values can be any valid registry entry values. The *value-name* entry values are not deleted from the **...\\***ServiceName***\\Parameters** registry key.

 

 




