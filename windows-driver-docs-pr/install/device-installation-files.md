---
title: Device Installation Files
description: Device Installation Files
ms.assetid: a4a53040-ff53-49ba-a4a5-aba5f13119ef
keywords:
- Device setup WDK device installations , files
- device installations WDK , files
- installing devices WDK , files
- files WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Installation Files





The software that is required to support a particular device depends on the kind of device and the ways in which the device is used. Typically, a vendor provides the following software in a [driver package](driver-packages.md) to support a device:

<a href="" id="a-device-setup-information-file--inf-file-"></a>A device setup information file (INF file)  
An INF file contains information that the system Windows components use to install support for the device. Windows copies this file to the %*SystemRoot*%\\*inf* directory when it installs the driver. This file is required.

For more information, see [Creating an INF File](overview-of-inf-files.md).

<a href="" id="one-or-more-drivers-for-the-device"></a>One or more drivers for the device  
A .*sys* file is the driver's image file. Windows copies this file to the *%SystemRoot%\\system32\\drivers* directory when the driver is installed. Drivers are required for most devices.

For more information, see [Choosing a Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff554652).

<a href="" id="digital-signatures-for-the-driver-package--a-driver-catalog-file-"></a>Digital signatures for the [driver package](driver-packages.md) (a driver catalog file)  
A driver catalog file contains digital signatures. All driver packages should be signed.

A vendor obtains digital signatures by submitting its driver package to the Windows Hardware Quality Lab (WHQL) for testing and signing. WHQL returns the package with a catalog file (.*cat* file).

For more information, see [WHQL release signatures](whql-release-signature.md).

<a href="" id="other-files"></a>Other files  
A [driver package](driver-packages.md) can contain other files, such as a custom device installation application, a device icon, or a driver library file (such as for video drivers).

For more information, see [Providing Device Property Pages](providing-device-property-pages.md) and [Drivers with Special Installation Requirements](drivers-with-special-installation-requirements.md).

Also, see the device-type-specific documentation in the WDK.

The WDK includes various sample installation files. For more information, see [Sample Device Installation Files](sample-device-installation-files.md)

 

 





