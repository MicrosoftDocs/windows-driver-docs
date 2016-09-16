---
title: Package-Aware Print Drivers that Share Files
author: windows-driver-content
description: Package-Aware Print Drivers that Share Files
MS-HAID:
- 'prtinst\_bbf49b33-893a-4c72-9998-de8c334a8380.xml'
- 'print.package\_aware\_print\_drivers\_that\_share\_files'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dcf4e7b4-f0f4-4644-9f5c-c01c1b6c4221
keywords: ["package-aware print drivers WDK", "core drivers WDK printer"]
---

# Package-Aware Print Drivers that Share Files


When more than one print driver package shares driver files, the shared files must be isolated into a core driver. For example, Unidrv is a collection of files that many print drivers use, so Unidrv is a core driver.

Unidrv print drivers use the Needs and Include INF-file directives, as shown in the following section of an INF file for Windows XP:

```
[UniDrvInstall]
CopyFiles=@OEMRES.DLL,@OEMABC.GPD
DataFile=OEMABC.GPD
DataSection=UNIDRV_DATA
Include=NTPRINT.INF
Needs=UNIDRV.OEM,TTFSUB.OEM
```

In Windows Vista, package-aware drivers should use the new **CoreDriverSections** keyword when referring to Unidrv files, as shown in the following section of an INF file for Windows Vista:

```
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

```
CoreDriverSections="{GUID1}, SectionName1, SectionName2", "{GUID2}, SectionName3"
```

When installing a driver that depends on a core driver, the print installer will look for the latest version of that core driver in the driver store and will install the newest version.

This section includes the following topics:

[Writing Core Drivers](writing-core-drivers.md)

[Using Core Drivers](using-core-drivers.md)

[Core Driver Sample](core-driver-sample.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Package-Aware%20Print%20Drivers%20that%20Share%20Files%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


