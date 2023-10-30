---
title: Package-Aware Print Drivers that Share Files
description: Package-Aware Print Drivers that Share Files
keywords:
- package-aware print drivers WDK
- core drivers WDK printer
ms.date: 07/18/2023
---

# Package-Aware Print Drivers that Share Files

[!include[Print Support Apps](../includes/print-support-apps.md)]

When more than one print driver package shares driver files, the shared files must be isolated into a core driver. For example, Unidrv is a collection of files that many print drivers use, so Unidrv is a core driver.

Unidrv print drivers use the Needs and Include INF-file directives, as shown in the following section of an INF file for Windows XP:

```inf
[UniDrvInstall]
CopyFiles=@OEMRES.DLL,@OEMABC.GPD
DataFile=OEMABC.GPD
DataSection=UNIDRV_DATA
Include=NTPRINT.INF
Needs=UNIDRV.OEM,TTFSUB.OEM
```

In Windows Vista, package-aware drivers should use the new **CoreDriverSections** keyword when referring to Unidrv files, as shown in the following section of an INF file for Windows Vista:

```inf
[UniDrvInstall_Vista]
CopyFiles=@OEMRES.DLL,@OEMABC.GPD
DataFile=OEMABC.GPD
CoreDriverSections="{D20EA372-DD35-4950-9ED8-A6335AFE79F0}, 
 UNIDRV.OEM, UNIDRV_DATA, TTFSUB.OEM"
```

As of Windows Vista, do not include Ntprint.inf because Unidrv is packaged as a core driver and is referred to by its globally unique identifier (GUID). When using core drivers, do not use the **DataSection** keyword, but instead refer to this section from the **CoreDriverSections** keyword.

Core print package files are listed in the following table.

| Core File | GUID |
|--|--|
| UNIDRV | {D20EA372-DD35-4950-9ED8-A6335AFE79F0} |
| PSCRIPT | {D20EA372-DD35-4950-9ED8-A6335AFE79F1} |
| PCLXL | {D20EA372-DD35-4950-9ED8-A6335AFE79F2} |
| PLOTTER | {D20EA372-DD35-4950-9ED8-A6335AFE79F4} |
| XPSDRV | {D20EA372-DD35-4950-9ED8-A6335AFE79F5} |

More than one core driver section can be referenced; for example:

```inf
CoreDriverSections="{GUID1}, SectionName1, SectionName2", "{GUID2}, SectionName3"
```

When installing a driver that depends on a core driver, the print installer will look for the latest version of that core driver in the driver store and will install the newest version.

This section includes the following topics:

[Writing Core Drivers](writing-core-drivers.md)

[Using Core Drivers](using-core-drivers.md)

[Core Driver Sample](core-driver-sample.md)
