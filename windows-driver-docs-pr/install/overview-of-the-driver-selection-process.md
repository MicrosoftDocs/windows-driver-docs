---
title: Overview of the Driver Selection Process
description: Overview of the Driver Selection Process
ms.assetid: 120ab9f9-6ac5-4b76-bee1-2e975d0c38f2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of the Driver Selection Process


Windows represents a driver as a [*driver node*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-node), which includes all the software support for a device, such as any services, device-specific co-installers, and registry entries. The services for a device include a function driver and any upper-level and lower-level device filter drivers.

Some devices require a vendor-supplied driver that is designed specifically for that device or one that is designed to support a family of devices. However, other devices can be driven by a system-supplied driver that supports all the devices of a given [device setup class](device-setup-classes.md). Windows selects the driver that most closely matches the device. If Windows does not find such a driver, it selects from increasingly more general drivers.

### <a href="" id="how-setup-searches-for-drivers"></a> How Windows Searches for Drivers

Windows searches in specific locations for drivers that match a device. A driver matches a device if the following are true:

-   One of the Plug and Play (PnP) [device identification strings](device-identification-strings.md) that is reported by the bus driver for the device matches a device identification string in an [**INF *Models* section**](inf-models-section.md) entry of the driver's [INF file](inf-files.md).

-   If the matching device identification string in an [**INF *Models* section**](inf-models-section.md) entry specifies a *TargetOSVersion* decoration, the decoration matches the operating system version on which the device is to be installed.

    For more information about the *TargetOSVersion* decoration, see [Combining Platform Extensions with Operating System Versions](combining-platform-extensions-with-operating-system-versions.md).

For more information about where Windows searches for matching drivers, see [Where Windows Searches for Drivers](where-setup-searches-for-drivers.md).

### <a href="" id="how-setup-ranks-drivers"></a> How Windows Ranks Drivers

Windows creates a list of all the matching drivers and assigns each driver a rank. Windows represents each driver's rank with an integer value that is greater than or equal to zero.

For more information about the ranking process, see [How Windows Ranks Drivers](how-setup-ranks-drivers.md).

Starting with Windows Vista, Windows also ranks drivers based on whether the driver is digitally signed. Windows ranks drivers based on a digital signature as follows:

-   If the [**AllSignersEqual** Group Policy](allsignersequal-group-policy--windows-vista-and-later-.md) is disabled, Windows ranks drivers that are signed with a Microsoft signature higher than drivers that are signed with an [Authenticode](authenticode.md) signature. This ranking occurs even if a driver that is signed with an Authenticode signature is, in all other aspects, a better match for a device.

-   If the [**AllSignersEqual** Group Policy](allsignersequal-group-policy--windows-vista-and-later-.md) is enabled, Windows ranks all digitally signed drivers equally.

**Note**  Starting with Windows 7, the [AllSignersEqual Group Policy](allsignersequal-group-policy--windows-vista-and-later-.md) is enabled by default. In Windows Vista and Windows Server 2008, the **AllSignersEqual** Group Policy is disabled by default. IT departments can override the default ranking behavior by enabling or disabling the **AllSignersEqual** Group Policy.

 

Signatures from a Windows signing authority include the following:

-   Premium Windows Hardware Quality Labs (WHQL) signatures and standard WHQL signatures

-   Signatures for inbox drivers

-   Windows Sustained Engineering (Windows SE) signatures

-   A WHQL signature for a Windows version that is the same or later than the [LowerLogoVersion](lowerlogoversion.md) value of the driver's device setup class

### <a href="" id="how-setup-selects-drivers"></a> How Windows Selects Drivers

Windows selects the driver with the lowest rank value as the best match for the device.

However, if there are multiple equally ranked drivers that are a best match for a device, Windows uses the driver's date and version to select a driver. The driver's date and version are specified by the [**INF DriverVer directive**](inf-driverver-directive.md) that is contained in the driver's [INF file](inf-files.md).

Windows uses the following criteria to select a driver for a device:

-   Windows selects the driver that has the lowest rank value as the best match for the device.

-   For drivers that have equal rank, Windows selects the driver that has the most recent date.

-   For the drivers that have equal rank and date, Windows selects the driver that has the highest version.

-   For drivers that have equal rank, date, and version, Windows can select any driver.

 

 





