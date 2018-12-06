---
title: Components of a Driver Package
description: Components of a Driver Package
ms.assetid: 3e09b17f-9a62-43fd-be00-29fe2e6140c5
keywords:
- components WDK
- driver packages WDK , components
- packages WDK , components
- files WDK driver packages
- co-installers WDK device installations , driver packages
- installation files WDK
- .sys files
- SYS files
- .cat files
ms.date: 05/09/2018
ms.localizationpriority: medium
---

# Components of a Driver Package





The following components are necessary to install and support a device on a Windows operating system:

<a href="" id="the-device-itself"></a>**The device itself**  
If you plan to design and build a new device, follow industry hardware standards. When you follow these standards, you are more likely to have a streamlined development process as well as lower your support costs. Not only do test suites exist for such devices, but, in many cases, generic drivers exist for standard types. Therefore, you might not have to write a new driver.

<a href="" id="the-driver-package-for-the-device"></a>**The driver package for the device**  
A driver package includes all the software components that you must supply to ensure that your device is supported with Windows. Typically, a driver package contains the following components:

-   Driver files

-   Installation files

-   Other files

A brief description of each component of a driver package follows.

### Driver Files

The driver is the part of the package that provides the I/O interface for a device. Typically, a driver is a dynamic-link library (DLL) with the .*sys* file name extension. Long file names are allowed, except for [*boot-start drivers*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver). When a device is installed, Windows copies the *.sys* file to the *%SystemRoot%\\system32\\drivers* directory.

The software that is required to support a particular device depends on the features of the device and the bus or port to which it connects. Microsoft ships drivers for many common devices and nearly all buses with the operating system. If your device can be serviced by one of these drivers, you might have to write only a device-specific [*minidriver*](https://msdn.microsoft.com/library/windows/hardware/ff556308#wdkgloss-minidriver). A minidriver handles device-specific features on behalf of a system-supplied driver. For some types of devices, even a minidriver is not necessary. For example, modems can typically be supported with just installation files.

### Installation Files

In addition to the device and the driver, a driver package also contains one or more of the following files that provide driver installation:

-   A device setup information (INF) file

    An INF file contains information that the [system-provided device installation components](system-provided-device-installation-components.md) use to install support for the device. Windows copies this file to the %*SystemRoot*%\\*inf* directory when it installs the device. Every device must have an INF file.

    For more information, see [Supplying an INF File](supplying-an-inf-file.md).

-   A driver [catalog (.cat) file](catalog-files.md)

    A driver catalog file contains a cryptographic hash of each file in the driver package. Windows uses these hashes to verify that the package was not altered after it was published. To ensure that the catalog file is not altered, it should be [digitally signed](digital-signatures.md).

    For information about how to sign drivers, see [Signing Drivers for Public Release](signing-drivers-for-public-release.md) and [Signing Drivers during Development and Test](signing-drivers-during-development-and-test.md).

### Other Files

A driver package can also contain other files, such as a device installation application, a device icon, device property pages, and so forth. For more information, see the following topics:

[Providing Device Property Pages](providing-device-property-pages.md)

[Installing a Boot-Start Driver](installing-a-boot-start-driver.md)

 

 





