---
title: Running the Upgrade Test and Examining the Results
description: Running the Upgrade Test and Examining the Results
ms.assetid: 82a2427e-94ed-4f7e-93e7-7952ca0d98e8
keywords:
- testing network component upgrades WDK
- upgrade tests WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Running the Upgrade Test and Examining the Results





**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

Before you upgrade the system to Windows 2000 or later, note the parameter values in the registry for each network component to be upgraded.

**To run the upgrade test**

1.  Make sure that the CD-ROM that contains the checked build of Windows 2000 or later is in the CD-ROM drive.

2.  Run winnt32.exe on the test system. For example, use the following command to run winnt32.exe on an Intel-based system with the CD-ROM in drive O:
    ```CMD
    winnt32.exe /s:o\i386
    ```

3.  After Windows 2000 or later is installed, verify that the upgraded network component's parameters have been correctly migrated to the new operating system.

 

 





