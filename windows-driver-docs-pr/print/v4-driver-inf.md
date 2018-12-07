---
title: V4 Driver INF
description: The v4 print driver setup model continues to use INF files, but also employs a new manifest file to capture the printer specific setup directives.
ms.assetid: 48F19796-43F9-4A69-B042-1305245C9CB9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# V4 Driver INF


The v4 print driver setup model continues to use INF files, but also employs a new manifest file to capture the printer specific setup directives.

## Sample INF


Notice that the sample v4 print driver INF file presented in this topic does not contain any printer-specific directives. The printer-specific instructions are contained in the v4 manifest file, which is always named ending with "–manifest.ini". Each driver within a driver package may specify its own v4 manifest file.

The following sample INF file assumes that a fictional company, Fabrikam, has manufactured print devices that will be installed to run with the v4 print driver.

```INF
[Version]
Signature="$Windows NT$"
Provider="Fabrikam"
ClassGUID={4D36E979-E325-11CE-BFC1-08002BE10318}
Class=Printer
CatalogFile=prnfa999.CAT
DriverVer=09/12/2010,6.2.8060.4
ClassVer=4.0 ;This causes v4 setup to take place

[Manufacturer]
"Fabrikam"=Fabrikam,NTamd64

[Fabrikam.NTamd64] ;Add your models here
"Fabrikam Laser 9000" =        Laser9000,Fabrik9000_sdfjkals                     ;HWID example
"Fabrikam Laser 9100" =        Laser9000,Fabrik9100_sjkasj                       ;HWID example
"Fabrikam Laser 9000 series" = Laser9000,{E0691E8C-F7CC-456E-A7B5-D1FC19BA2279}  ;PrinterDriverID

[Laser9000]
CopyFiles=Laser9000_FILES

[Laser9000_FILES]
faPDL.gpd
faPDL-pipelineconfig.xml
faPDL-manifest.ini
faPDL.dll

[SourceDisksNames.amd64]
1 = %Location%,,,
2 = %Location%,,,amd64

[SourceDisksNames.x86]
1 = %Location%,,,
2 = %Location%,,,x86

[DestinationDirs]
DefaultDestDir=66000

[SourceDisksFiles]
faPDL.gpd=1
faPDL-pipelineconfig.xml=1
faPDL-manifest.ini = 1
faPDL.dll =2

[Strings]
Location="Fabrikam DVD"
```

## INF Directives


The following table shows the list of printer-specific directives that are permitted in v4 print drivers and print class drivers.

| Directive | Description                                         | Restrictions                                                                                                                                           | Usage        |
|-----------|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| ClassVer  | Used to indicate that a printer class driver is v4. | V4 print drivers must specify ClassVer=4.0. V3 print drivers may specify ClassVer=3.0, but it is optional. No other values are supported at this time. | ClassVer=4.0 |

## The DestinationDirs Keyword


The v4 driver INF requires that **DestinationDir** is specified for all files in the package. The supported **DestinationDir** values are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>DestinationDir ID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>66000</td>
<td><p>[This Destination ID has been overloaded for the v4 driver]</p>
<p>V4: This must be set as the DefaultDestDir for a v4 print driver. Specifies that the files should be run from the Driver Store.</p>
<p>V3: This specifies that files should be installed to the \3 directory.</p></td>
</tr>
<tr class="even">
<td>23</td>
<td><p>V4: This must be set as the <strong>DestinationDir</strong> for any color profiles.</p>
<p>V3: Color profiles should be installed using the printer-specific DirID 66003.</p></td>
</tr>
</tbody>
</table>

 

## INF Restrictions


V4 print drivers must not define other printer-specific directives or keywords called out in the following list.

| INF file keyword            | Usage type         |
|-----------------------------|--------------------|
| AddInterface                | Directive          |
| AddReg                      | Directive          |
| AddService                  | Directive          |
| BitReg                      | Directive          |
| ClassInstall32              | Section type       |
| ClassInstall32.Service      | Section type       |
| ConfigFile                  | v3 print Directive |
| CoreDriverDependencies      | v3 Print Directive |
| CoreDriverSections          | v3 Print Directive |
| DataFile                    | v3 Print Directive |
| DDInstall.CoInstallers      | Section type       |
| DDInstall.FactDef           | Section type       |
| DDInstall.HW                | Section type       |
| DDInstall.Interfaces        | Section type       |
| DDInstall.LogConfigOverride | Section type       |
| DDInstall.Services          | Section type       |
| DDInstall.WMI               | Section type       |
| DefaultInstall              | Section type       |
| DefaultInstall.Services     | Section type       |
| DelFiles                    | Directive          |
| DelReg                      | Directive          |
| DelService                  | Directive          |
| DontReflectOffline          | Directive          |
| DriverFile                  | v3 print Directive |
| DriverIsolation             | v3 print Directive |
| FeatureScore                | Directive          |
| HelpFile                    | v3 Print Directive |
| Include                     | Directive          |
| Ini2Reg                     | Directive          |
| InterfaceInstall32          | Section type       |
| LayoutFile                  | Directive          |
| LogConfig                   | Directive          |
| Needs                       | Directive          |
| PackageAware                | v3 Print Directive |
| RenFiles                    | Directive          |
| UpdateIniFields             | Directive          |
| UpdateInis                  | Directive          |

 

**NTPrint References**. NTPrint references are made in the manifest file. The INF file does not require any information about the NTPrint references in its DDInstall, CopyFiles, or SourceDisksFiles sections.

**Configuration Module References**. All print drivers use the same configuration module binary (PrintConfig.dll); there is no mechanism for a driver to select the configuration module.

For information about how to create an INF file for a basic v4 printer driver, see [Building a basic v4 Printer Driver](building-a-basic-v4-printer-driver.md).

 

 




