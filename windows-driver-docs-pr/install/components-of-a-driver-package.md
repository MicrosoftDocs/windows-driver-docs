---
title: Components of a Driver Package
description: A driver package includes all the software components that you must supply to ensure that your device is supported with Windows.
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
ms.date: 04/22/2025
---

# Components of a Driver Package

A driver package includes all the software components that you must supply to ensure that your device is supported with Windows. Typically, a driver package contains the following components:

- Setup information (INF) file
- Catalog file
- Driver files
- Other files

A brief description of each component of a driver package follows.

The Windows Driver Kit (WDK) includes sample driver packages. For more information, see [Sample Device Installation Files](sample-device-installation-files.md)

## INF file

Every driver package must include a setup information (INF) file, which the device installation components read when installing the device. An INF file isn't an installation script. It's an ASCII or Unicode (UTF-16 only) text file that provides device and driver information. Setup information includes the driver files, registry entries, device IDs, [catalog files](catalog-files.md), and version information required to install driver package on a device.

The exact contents and format of the INF file depend on the [device setup class](./overview-of-device-setup-classes.md) that the INF declares itself as being in. [Summary of INF Sections](summary-of-inf-sections.md) describes the information that is required in each type of INF. In general, per-manufacturer information is located in an [**INF *Models* section**](inf-models-section.md). Entries in the **Models** section refer to [**INF *DDInstall* sections**](inf-ddinstall-section.md) that contain model-specific details.

The [InfVerif](../devtest/infverif.md) tool checks the syntax and structure of all cross-class INF sections and directives, together with the class-specific extensions for all setup classes except for printers. The **InfVerif** tool resides in the *\\tools* directory of the WDK.

You can use a single INF file for installation on all versions of the Windows operating system. For more information, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md). If your device is sold in the international market, [create an international INF file](creating-international-inf-files.md). Depending on the localities involved, an international INF file might have to be a Unicode (UTF-16) file instead of ASCII.

A good way to create an INF file for your driver is to modify one of the samples that the WDK provides. Most of the WDK sample drivers include INF files in the same directory as the sample driver.

The INF file for the device must contain the following information at minimum:

- Information about what versions of the operating system the driver package is supported on
- The setup class GUID and setup class for the driver package
- Driver package version information
- The names of the driver files together with their source and destination locations
- Device-specific information, including [hardware ID](hardware-ids.md) and [compatible IDs](compatible-ids.md), that determines applicability of the driver package
- The name of a [catalog (.cat) file](catalog-files.md)
- Information about how and when to load the services that are provided by each driver package

If your device is involved in booting the system, installation requirements differ. See [Installing a Boot Driver](installing-a-boot-start-driver.md).

For more information about INF files, see [Creating an INF File](overview-of-inf-files.md). Also, see the documentation for [InfVerif](../devtest/infverif.md), the device-specific documentation in the WDK, and the INF files supplied with sample drivers for devices similar to yours.

## Catalog file

A driver catalog file contains a cryptographic hash of each file in the driver package. Windows uses these hashes to verify that the package wasn't altered after it was published. To ensure that the catalog file isn't altered, it must have a [digital signature](digital-signatures.md) trusted by the systems using this driver package.

A vendor obtains release digital signatures by submitting its driver package to the Windows Hardware Quality Lab (WHQL) for testing and signing. WHQL returns the package with a catalog file (.*cat* file). For more information, see [WHQL release signatures](whql-release-signature.md).

For information about how to sign drivers, see [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md) and [Signing Drivers during Development and Test](./introduction-to-test-signing.md).

The INF file must reference the catalog file with a *CatalogFile* directive in the [**INF *Version* section**](inf-version-section.md) of the INF.

## Driver Files

In most cases, a driver package contains one or more driver services that should be part of the [device stack](../gettingstarted/device-nodes-and-device-stacks.md) for the device the driver package is installed on. For more information on driver services, see [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md). The driver service is the part of the package that provides the I/O interface for a device. Typically, a driver is a dynamic-link library (DLL) with the .*sys* file name extension. Long file names are allowed, except for *boot-start drivers*.

The software that is required to support a particular device depends on the features of the device and the bus or port to which it connects. Microsoft ships drivers for many common devices. If one of these drivers can service your device, you might only have to write a device-specific *minidriver*. A minidriver handles device-specific features on behalf of a system-supplied driver. For some types of devices, even a minidriver isn't necessary. For example, modems can typically be supported with just installation files.

## Other Files

A driver package can contain other files, such as hardware calibration settings, a Win32 service, a device icon, or a driver library file. For more information, see:

- [Providing Icons for a Device](providing-vendor-icons-for-the-shell-and-autoplay.md)
