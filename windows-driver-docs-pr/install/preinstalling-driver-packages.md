---
title: Preinstalling Driver Packages
description: Preinstalling Driver Packages
keywords:
- installation applications WDK , preinstall driver packages
- device installation applications WDK , preinstall driver packages
- preinstalled drivers WDK device installations
ms.date: 03/11/2022
---

# Preinstalling Driver Packages

To preinstall driver package files, your *device installation application* should follow these steps:

1.  On the target system, create a directory for the driver package files. If your device installation application installs an application, the driver package files should be stored in a subdirectory of the application directory.

2.  Copy all files in the [driver package](driver-packages.md) from the distribution media to the directory that is created in step (1). The driver package includes the driver or drivers, the INF file, the catalog file, and other installation files.

3.  Call [SetupCopyOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupcopyoeminfa) specifying the INF file in the directory that was created in step (1). Specify SPOST_PATH for the *OEMSourceMediaType* parameter and specify **NULL** for the *OEMSourceMediaLocation* parameter. [SetupCopyOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupcopyoeminfa) stages the driver package into the [Driver Store](driver-store.md).

When the user plugs in the device, the PnP manager recognizes the device, finds the driver package staged by [SetupCopyOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupcopyoeminfa), and installs the driver package on the device.

 

