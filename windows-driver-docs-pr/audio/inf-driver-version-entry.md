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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20INF%20Driver-Version%20Entry%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


