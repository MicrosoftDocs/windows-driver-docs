---
title: Preinstalling Driver Packages
description: Preinstalling Driver Packages
ms.assetid: aba794ac-ab24-486a-9f5a-7e8435056bb7
keywords:
- installation applications WDK , preinstall driver packages
- device installation applications WDK , preinstall driver packages
- preinstalled drivers WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preinstalling Driver Packages





To preinstall driver files, your [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) should follow these steps:

1.  On the target system, create a directory for the driver files. If your device installation application installs an application, the driver files should be stored in a subdirectory of the application directory.

2.  Copy all files in the [driver package](driver-packages.md) from the distribution media to the directory that is created in step (1). The driver package includes the driver or drivers, the INF file, the catalog file, and other installation files.

3.  Call [SetupCopyOEMInf](http://go.microsoft.com/fwlink/p/?linkid=98735) specifying the INF file in the directory that was created in step (1). Specify SPOST_PATH for the *OEMSourceMediaType* parameter and specify **NULL** for the *OEMSourceMediaLocation* parameter. [SetupCopyOEMInf](http://go.microsoft.com/fwlink/p/?linkid=194252) copies the INF file for the driver package into the *%SystemRoot%\\Inf* directory on the target system and directs Windows to store the source location of the INF file in its list of preprocessed INF files. [SetupCopyOEMInf](http://go.microsoft.com/fwlink/p/?linkid=194252) also processes the catalog file, so the PnP manager will install the driver the next time that it recognizes a device that is listed in the INF file.

When the user plugs in the device, the PnP manager recognizes the device, finds the INF file copied by [SetupCopyOEMInf](http://go.microsoft.com/fwlink/p/?linkid=194252), and installs the drivers copied in step (2). (For more information about copying INF files, see [Copying INFs](copying-inf-files.md).)

 

 





