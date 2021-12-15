---
title: Overview of the Driver Package Selection Process
description: Overview of the Driver Package Selection Process
ms.date: 12/03/2021
---

# Overview of the Driver Package Selection Process


Windows represents a [driver package](driver-packages.md) as a *driver node*, which includes all the software support for a device, such as any file, services, and registry entries. The services for a device include a function driver and any upper-level and lower-level device filter drivers.

Some devices require a vendor-supplied driver package that is designed specifically for that device or one that is designed to support a family of devices. However, other devices can be driven by a system-supplied driver package that supports a family of devices or all the devices of a given [device setup class](./overview-of-device-setup-classes.md). Windows selects the driver package that most closely matches the device. If Windows does not find such a driver package, it selects from increasingly more general driver packages.

### <a href="" id="how-setup-searches-for-drivers"></a> How Windows Searches for Driver Packages

Windows searches in specific locations for [driver packages](driver-packages.md) that match a device. A driver package matches a device if the following are true:

-   One of the [hardware identifiers (IDs)](hardware-ids.md) or [compatible IDs](compatible-ids.md) that is reported by the bus driver for the device matches a *hw-id* or *compatible-id* string in an [**INF *Models* section**](inf-models-section.md) entry of the driver package's [INF file](overview-of-inf-files.md).

-   The *TargetOSVersion* decoration of the [**INF *Models* section**](inf-models-section.md) that contains the matching entry applies to the operating system version on which the device is to be installed.

    For more information about the *TargetOSVersion* decoration, see [Combining Platform Extensions with Operating System Versions](combining-platform-extensions-with-operating-system-versions.md).

For more information about where Windows searches for matching drivers, see [Where Windows Searches for Drivers](./how-windows-selects-a-driver-for-a-device.md).

### <a href="" id="how-setup-ranks-drivers"></a> How Windows Ranks Driver Packages

Windows creates a list of all the matches within each applicable [driver package](driver-packages.md) and assigns each match a rank. A single driver package may contain multiple matches for a device if the driver package has multiple lines in its [**INF *Models* section**](inf-models-section.md) entries that match on the device. Windows represents each driver package matches' rank with an integer value that is greater than or equal to zero.

For more information about the ranking process, see [How Windows Ranks Driver Packages](how-setup-ranks-drivers--windows-vista-and-later-.md).

Starting with Windows Vista, Windows also ranks driver packages based on whether the driver package is digitally signed. Windows ranks driver packages based on a digital signature as follows:

-   If the [**AllSignersEqual** Group Policy](./allsigningequal-group-policy.md) is disabled, Windows ranks driver packages that are signed with a Microsoft signature higher than driver packages that are signed with an [Authenticode](authenticode.md) signature. This ranking occurs even if a driver package that is signed with an Authenticode signature is, in all other aspects, a better match for a device.

-   If the [**AllSignersEqual** Group Policy](./allsigningequal-group-policy.md) is enabled, Windows ranks all digitally signed driver packages equally.

**Note**  Starting with Windows 7, the [AllSignersEqual Group Policy](./allsigningequal-group-policy.md) is enabled by default. In Windows Vista and Windows Server 2008, the **AllSignersEqual** Group Policy is disabled by default. IT departments can override the default ranking behavior by enabling or disabling the **AllSignersEqual** Group Policy.

Signatures from a Windows signing authority include the following:

-   Premium Windows Hardware Quality Labs (WHQL) signatures and standard WHQL signatures

-   Signatures for inbox driver packages

-   Windows Sustained Engineering (Windows SE) signatures

-   A WHQL signature for a Windows version that is the same or later than the [LowerLogoVersion](lowerlogoversion.md) value of the driver package's device setup class

### <a href="" id="how-setup-selects-drivers"></a> How Windows Selects Driver Packages

Windows selects the [driver package](driver-packages.md) match with the lowest rank value as the best match for the device.

However, if there are multiple equally ranked driver package matches that are a best match for a device, Windows uses the driver package's date and version to select a driver. The driver's date and version are specified by the [**INF DriverVer directive**](inf-driverver-directive.md) that is contained in the driver package's [INF file](overview-of-inf-files.md).

Windows uses the following criteria to select a driver package match for a device:

-   Windows selects the driver package match that has the lowest rank value as the best match for the device.

-   For driver package matches that have equal rank, Windows selects the driver package that has the most recent date.

-   For the driver packages that have equal rank and date, Windows selects the driver package that has the highest version.

-   For driver packages that have equal rank, date, and version, Windows can select any driver package.
