---
title: Device Installation Files
description: Device Installation Files
keywords:
- Device setup WDK device installations , files
- device installations WDK , files
- installing devices WDK , files
- files WDK device installations
ms.date: 12/01/2021
ms.localizationpriority: medium
---

# Device Installation Files

The software that is required to support a particular device depends on the kind of device and the ways in which the device is used. Typically, a vendor provides the following software in a [driver package](driver-packages.md) to support a device:

* <a href="" id="a-device-setup-information-file--inf-file-"></a>A device setup information file (INF file)  
    An INF file contains information that the device installation components use to install the [driver package](driver-packages.md) on a device. This file is required. For more information, see [Creating an INF File](overview-of-inf-files.md).

* <a href="" id="digital-signatures-for-the-driver-package--a-driver-catalog-file-"></a>Digital signatures for the [driver package](driver-packages.md) (a driver catalog file)  
    A driver catalog file contains hashes of all of the files in the driver package and is signed with a digital signature that would be trusted by the systems that should use this driver package. All driver packages should include a catalog file that is signed.

    A vendor obtains release digital signatures by submitting its driver package to the Windows Hardware Quality Lab (WHQL) for testing and signing. WHQL returns the package with a catalog file (.*cat* file). For more information, see [WHQL release signatures](whql-release-signature.md).

* <a href="" id="one-or-more-drivers-for-the-device"></a>One or more drivers for the device  
    In most cases, a driver package will contain one or more driver services that should be part of the [device stack](../gettingstarted/device-nodes-and-device-stacks.md) for the device the driver package is installed on. For more information on driver services, see [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md).

* <a href="" id="other-files"></a>Other files  
    A [driver package](driver-packages.md) can contain other files, such as hardware calibration settings, a Win32 service, a device icon, or a driver library file (such as for video drivers).

Also, see the device-type-specific documentation in the WDK.

The WDK includes various sample installation files. For more information, see [Sample Device Installation Files](sample-device-installation-files.md)

