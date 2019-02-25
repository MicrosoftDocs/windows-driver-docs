---
title: INF DDInstall.MigrateToDevNode Section
description: INF DDInstall.MigrateToDevNode Section
ms.assetid: a4edbc9e-a2d0-4012-aca9-0b357939a881
keywords:
- INF files WDK non-HID keyboard/mouse
- DDInstall.MigrateToDevNode section
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall.MigrateToDevNode Section





**\[**<em>install-section-name</em>**.MigrateToDevNode\]** |
**\[**<em>install-section-name</em>**.nt.MigrateToDevNode\]** |
**\[**<em>install-section-name</em>**.ntx86.MigrateToDevNode\]** |
**\[**<em>install-section-name</em>**.ntia64.MigrateToDevNode\]**

<em>ServiceName</em>**=**<em>value-name</em>\[**,**<em>value-name</em>\],...
The keyboard and mouse class installers copy the entry values specified by the list of *value-name* strings from the registry key **HKLM\\System\\CurrentControlSet\\Services\\**<em>ServiceName</em>**\\Parameters** to the device node of the device being installed.

### Entries and Values

<a href="" id="servicename"></a>*ServiceName*  
Specifies the service name associated with a device port (for example, **i8042prt**, **sermouse**, and so on).

<a href="" id="value-name"></a>*value-name*  
Specifies an entry value under the registry key **HKLM\\System\\CurrentControlSet\\Services\\**<em>ServiceName</em>**\\Parameters**.

### <a href="" id="comments"></a>Remarks

Microsoft supports INF <em>DDinstall</em>**.MigratetoDevNode** sections primarily to facilitate porting Windows NT 4.0 legacy devices to Windows 2000 and later.

The keyboard and mouse class installers copy all the *value-name* entry values before the system starts the device stack. The specified entry values can be any valid registry entry values. The *value-name* entry values are not deleted from the **...\\**<em>ServiceName</em>**\\Parameters** registry key.

 

 




