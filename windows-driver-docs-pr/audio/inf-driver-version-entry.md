---
title: INF Driver-Version Entry
description: INF Driver-Version Entry
ms.assetid: 092cd9ed-8988-4ffd-9958-1267f3c52819
keywords:
- version numbers WDK audio
- INF files WDK audio
- audio miniport drivers WDK , version numbers
- miniport drivers WDK audio , version numbers
- audio drivers WDK , version numbers
- driver version numbers WDK audio
- INF DriverVer Directive
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Driver-Version Entry


## <span id="inf_driver_version_entry"></span><span id="INF_DRIVER_VERSION_ENTRY"></span>


The INF file in a driver package specifies the driver-version information for the drivers that are installed by the INF. The version information in the file identifies the driver package as a whole, in contrast to the [internal and external version numbers](internal-and-external-version-numbers.md) for the individual driver files within the package.

The file specifies each driver's date and version number in an [**INF DriverVer directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394) with the following format:

**DriverVer**= *mm* / *dd* / *yyyy*\[,*x*.*y*.*v*.*z*\]

The date parameter *mm*/*dd*/*yyyy* consists of a two-digit month code *mm*, two-digit day code *dd*, and four-digit year code *yyyy*. This parameter specifies the date of the driver package and applies to all the driver files, including the INF file. A hyphen (-) can be used as the date-field separator in place of the slash (/). The operating system uses the **DriverVer** date to perform driver-version comparisons when selecting between two versions of a driver. This date also appears in the **Driver Date** value displayed by the Device Manager.

The optional version number *x*.*y*.*v*.*z* , which is shown in brackets above, is used for display purposes only (for example, in the **Driver Version** number displayed by the Device Manager). The operating system does not use this value for driver selection. When compiling driver files, make sure that the internal version number that is specified in the *FILEVERSION* parameter in the driver's resource file matches the **DriverVer** version number in the INF file.

When the operating system searches for drivers, it chooses a driver with a more recent **DriverVer** date over a driver with an earlier date. If an INF file has no **DriverVer** entry or is unsigned, the operating system applies the default date of 00/00/0000.

In Windows 2000, Windows XP and later, the INF file for a driver package must provide a **DriverVer** directive.

 

 




