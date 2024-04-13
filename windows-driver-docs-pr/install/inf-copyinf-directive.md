---
title: INF CopyINF Directive
description: A CopyINF directive causes specified INF files to be copied to the target system. The CopyINF directive is supported in Windows XP and later versions of Windows.
keywords:
- INF CopyINF Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF CopyINF directive
api_type:
- NA
ms.date: 07/08/2022
---

# INF CopyINF directive

A **CopyINF** directive causes specified INF files to be copied to the target system. The **CopyINF** directive is supported in Windows XP and later versions of Windows.

```inf
[DDInstall]
  
CopyINF=filename1.inf[,filename2.inf]...
```

## Remarks

System support for the **CopyINF** directive is available in Microsoft Windows XP and later versions of Windows.

This directive is typically used when installing multifunction devices. If the installation of a multifunction device requires multiple INF files (for multiple functions that belong to multiple setup classes), using this directive ensures that Windows will find the INF files when it installs the functions. Use the following rules:

- If the functions that are supplied by a multifunction device are enumerated as children of a parent device (such as an IEEE 1284.4 device), the INF file for the parent device should have a **CopyINF** directive to copy the INF files for the device's individual functions.

- If all the functions that are supplied by a multifunction device (such as a PCI card) are enumerated as peers of one another, the INF file for each function should have a **CopyINF** directive to copy the INF files for all peer functions.

If you follow these rules, Windows can install drivers for each function without prompting the user for an installation disk for each function.

The following points apply to the **CopyINF** directive:

- Before Windows Vista, Windows copies the specified INF files as part of the default processing for [**DIF_INSTALLDEVICE**](./dif-installdevice.md) (see [**SetupDiInstallDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldevice)) after the device is installed successfully.

    Windows copies the specified INF files into a system directory path that it will search during device installations.

- The INF files that are specified in the **CopyINF** directive must reside in the same directory as the INF file that contains the **CopyINF** directive or in a subdirectory of that directory. If the INF file resides in a subdirectory, the **CopyINF** directive should include the full relative path to that INF file. For example, `CopyINF=SubDir1\SubDir2\Example.inf`.

- You must include all INF files on each disk of a multidisk installation.

Starting with Windows Vista, the following points also apply to the **CopyINF** directive:

- The **CopyINF** directive causes the complete [driver package](driver-packages.md) that is referenced by the specified INF file to be copied into the [driver store](driver-store.md). This is required in order to support the deployment of multifunction driver packages, because the original source media might not be available when the device is actually installed. If the driver package that is referenced by the specified INF file already exists in the driver store, the INF file specified in the **CopyINF** directive is ignored.

- The **CopyINF** directive is processed during driver store import instead of during device installation. This means that a call to [SetupCopyOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupcopyoeminfa) on Windows Vista and later versions of Windows causes all the **CopyINF** directives in the specified INF file to be processed at that time. This occurs recursively for each **CopyINF** directive that is contained within the specified INF file until all referenced driver packages are copied into the driver store.

Starting with Windows 10, version 1511, under certain circumstances (for example, running Windows Update or some calls to [**DiInstallDevice**](/windows/win32/api/newdev/nf-newdev-diinstalldevice)), INFs copied with **CopyINF** will also be installed on applicable devices.

For more information about how to copy INF files, see [Copying INFs](copying-inf-files.md).

## Examples

```inf
[MyMfDevice.NTx86]
CopyINF = Sound.INF
```
