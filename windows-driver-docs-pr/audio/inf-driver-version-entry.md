---
title: INF Driver-Version Entry
description: INF Driver-Version Entry
keywords:
- version numbers WDK audio
- INF files WDK audio
- audio miniport drivers WDK , version numbers
- miniport drivers WDK audio , version numbers
- audio drivers WDK , version numbers
- driver version numbers WDK audio
- INF DriverVer Directive
ms.date: 04/28/2021
ms.localizationpriority: medium
---

# INF Driver-Version Entry


## <span id="inf_driver_version_entry"></span><span id="INF_DRIVER_VERSION_ENTRY"></span>


The INF file in a driver package specifies the driver-version information for the drivers that are installed by the INF. The version information in the file identifies the driver package as a whole, in contrast to the [internal and external version numbers](internal-and-external-version-numbers.md) for the individual driver files within the package.

The file specifies each driver's date and version number in an [**INF DriverVer directive**](../install/inf-driverver-directive.md) with the following format:

**DriverVer**= *mm* / *dd* / *yyyy*\[,*x*.*y*.*v*.*z*\]

The date parameter *mm*/*dd*/*yyyy* consists of a two-digit month code *mm*, two-digit day code *dd*, and four-digit year code *yyyy*. This parameter specifies the date of the driver package and applies to all the driver files, including the INF file. A hyphen (-) can be used as the date-field separator in place of the slash (/). The operating system uses the **DriverVer** date to perform driver-version comparisons when selecting between two versions of a driver. This date also appears in the **Driver Date** value displayed by the Device Manager.

The version parameter *w.x.y.z* specifies a version number.

Each of *w*, *x*, *y*, and *z* must be an integer that is greater than or equal to zero and less than 65535.

For Windows XP SP1, Windows Server 2003 and later versions of Windows, this value is also *used* by Setup, in combination with the driver rank and date, to select a driver for a device. For more information, see [How Windows Selects Drivers](../install/how-windows-selects-a-driver-for-a-device.md).

In Windows 2000, Windows XP and later, the INF file for a driver package must provide a **DriverVer** directive.

