---
title: Package-Aware Print Drivers that Share Files
description: Package-Aware Print Drivers that Share Files
ms.assetid: dcf4e7b4-f0f4-4644-9f5c-c01c1b6c4221
keywords:
- package-aware print drivers WDK
- core drivers WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Package-Aware Print Drivers that Share Files


When more than one print driver package shares driver files, the shared files must be isolated into a core driver. For example, Unidrv is a collection of files that many print drivers use, so Unidrv is a core driver.

Unidrv print drivers use the Needs and Include INF-file directives, as shown in the following section of an INF file for Windows XP:

```cpp
[UniDrvInstall]
CopyFiles=@OEMRES.DLL,@OEMABC.GPD
DataFile=OEMABC.GPD
DataSection=UNIDRV_DATA
Include=NTPRINT.INF
Needs=UNIDRV.OEM,TTFSUB.OEM
```

In Windows Vista, package-aware drivers should use the new **CoreDriverSections** keyword when referring to Unidrv files, as shown in the following section of an INF file for Windows Vista:

```cpp
[UniDrvInstall_Vista]
CopyFiles=@OEMRES.DLL,@OEMABC.GPD
DataFile=OEMABC.GPD
CoreDriverSections="{D20EA372-DD35-4950-9ED8-A6335AFE79F0}, 
 UNIDRV.OEM, UNIDRV_DATA, TTFSUB.OEM"
```

In Windows Vista, the reference to Ntprint.inf is no longer necessary because Unidrv is packaged as a core driver and is referred to by its globally unique identifier (GUID). When using core drivers, do not use the **DataSection** keyword, but instead refer to this section from the **CoreDriverSections** keyword.

Core print package files are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Core File</th>
<th>GUID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>UNIDRV</p></td>
<td><p>{D20EA372-DD35-4950-9ED8-A6335AFE79F0}</p></td>
</tr>
<tr class="even">
<td><p>PSCRIPT</p></td>
<td><p>{D20EA372-DD35-4950-9ED8-A6335AFE79F1}</p></td>
</tr>
<tr class="odd">
<td><p>PCLXL</p></td>
<td><p>{D20EA372-DD35-4950-9ED8-A6335AFE79F2}</p></td>
</tr>
<tr class="even">
<td><p>PLOTTER</p></td>
<td><p>{D20EA372-DD35-4950-9ED8-A6335AFE79F4}</p></td>
</tr>
<tr class="odd">
<td><p>XPSDRV</p></td>
<td><p>{D20EA372-DD35-4950-9ED8-A6335AFE79F5}</p></td>
</tr>
</tbody>
</table>

 

More than one core driver section can be referenced; for example:

```cpp
CoreDriverSections="{GUID1}, SectionName1, SectionName2", "{GUID2}, SectionName3"
```

When installing a driver that depends on a core driver, the print installer will look for the latest version of that core driver in the driver store and will install the newest version.

This section includes the following topics:

[Writing Core Drivers](writing-core-drivers.md)

[Using Core Drivers](using-core-drivers.md)

[Core Driver Sample](core-driver-sample.md)

 

 




