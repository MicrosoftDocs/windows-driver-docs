---
title: Components of a Driver Package
description: Components of a Driver Package
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
ms.date: 12/09/2021
---

# Components of a Driver Package

A driver package includes all the software components that you must supply to ensure that your device is supported with Windows. Typically, a driver package contains the following components:

-   INF file

-   Catalog file

-   Driver files

-   Other files

A brief description of each component of a driver package follows.

The WDK includes various sample driver packages. For more information, see [Sample Device Installation Files](sample-device-installation-files.md)


## INF file

Every driver package must include an INF file, which the device installation components read when installing the device. An INF file is not an installation script. It is an ASCII or Unicode (UTF-16 only) text file that provides device and driver information, including the driver files, registry entries, device IDs, [catalog files](catalog-files.md), and version information that is required to install driver package on a device.

The exact contents and format of the INF file depend on the [device setup class](./overview-of-device-setup-classes.md) that the INF declares itself as being in. [Summary of INF Sections](summary-of-inf-sections.md) describes the information that is required in each type of INF. In general, per-manufacturer information is located in an [**INF *Models* section**](inf-models-section.md). Entries in the **Models** section refer to [**INF *DDInstall* sections**](inf-ddinstall-section.md) that contain model-specific details.

The [InfVerif](../devtest/infverif.md) tool, which is provided in the *\\tools* directory of the Microsoft Windows Driver Kit (WDK), checks the syntax and structure of all cross-class INF sections and directives, together with the class-specific extensions for all setup classes except for Printers.

Starting with Windows 2000, you can use a single INF file for installation on all versions of the Windows operating system. For more information, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md). If your device will be sold in the international market, you should [create an international INF file](creating-international-inf-files.md). Depending on the localities involved, an international INF file might have to be a Unicode (UTF-16) file instead of ASCII.

A good way to create an INF file for your driver is to modify one of the samples that the WDK provides. Most of the WDK sample drivers include INF files in the same directory as the sample driver.

For more information about INF files, see [Creating an INF File](overview-of-inf-files.md), the documentation for [InfVerif](../devtest/infverif.md), the device-specific documentation in the WDK, and the INF files that are supplied with sample drivers for devices similar to yours.

## Catalog file

A driver catalog file contains a cryptographic hash of each file in the driver package. Windows uses these hashes to verify that the package was not altered after it was published. To ensure that the catalog file is not altered, it must be [digitally signed](digital-signatures.md) with a digital signature that would be trusted by the systems that should use this driver package.

A vendor obtains release digital signatures by submitting its driver package to the Windows Hardware Quality Lab (WHQL) for testing and signing. WHQL returns the package with a catalog file (.*cat* file). For more information, see [WHQL release signatures](whql-release-signature.md).

For information about how to sign drivers, see [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md) and [Signing Drivers during Development and Test](./introduction-to-test-signing.md).

The INF file must reference the catalog file with a *CatalogFile* directive in the [**INF *Version* section**](inf-version-section.md) of the INF.

## Driver Files

In most cases, a driver package will contain one or more driver services that should be part of the [device stack](../gettingstarted/device-nodes-and-device-stacks.md) for the device the driver package is installed on. For more information on driver services, see [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md). The driver service is the part of the package that provides the I/O interface for a device. Typically, a driver is a dynamic-link library (DLL) with the .*sys* file name extension. Long file names are allowed, except for *boot-start drivers*.

The software that is required to support a particular device depends on the features of the device and the bus or port to which it connects. Microsoft ships drivers for many common devices. If your device can be serviced by one of these drivers, you might have to write only a device-specific *minidriver*. A minidriver handles device-specific features on behalf of a system-supplied driver. For some types of devices, even a minidriver is not necessary. For example, modems can typically be supported with just installation files.

## Other Files

A driver package can also contain other files, such as hardware calibration settings, a Win32 service, a device icon, or a driver library file (such as for video drivers). For more information, see the following topic:

[Providing Icons for a Device](providing-vendor-icons-for-the-shell-and-autoplay.md)
