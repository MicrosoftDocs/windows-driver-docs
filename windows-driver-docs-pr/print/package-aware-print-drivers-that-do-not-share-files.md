---
title: Package-Aware Print Drivers that Do Not Share Files
description: Package-Aware Print Drivers that Do Not Share Files
keywords:
- package-aware print drivers WDK
ms.date: 05/08/2023
---

# Package-Aware Print Drivers that Do Not Share Files

[!include[Print Support Apps](../includes/print-support-apps.md)]

When the files in the driver package are uniquely named and do not occur in any other driver package, add a PrinterPackageInstallation section to the INF file. In that section, add the **PackageAware**=TRUE keyword as shown in line 23 of the following example:

```inf
[Version]
Signature="$Windows NT$"
Class=Printer
ClassGUID={4D36E979-E325-11CE-BFC1-08002BE10318}
Provider="OEM Company"
CatalogFile=PackageAware.cat     ; Single Catalog file for all OS versions
DriverVer=10/10/2005, 1.2.3.4
PnpLockdown=1

[Manufacturer]
"OEM Company" = Company, NTx86.6.0

;Models section for installation of x86 driver on
; Windows Vista and later
[Company.NTx86.6.0]
"My Device Description"
   = DriverInstall_Vista, OEM_Company_NameABC_640A

[DriverInstall_Vista]
CopyFiles=@OEMRES.DLL,@OEMABC.GPD
DataFile=OEMABC.GPD

[PrinterPackageInstallation.x86]
PackageAware=TRUE

; Source Media Information Sections
[DestinationDirs]
DefaultDestDir=66000

[SourceDisksNames.x86]
1   = %MediaDescription%,,,"I386"

[SourceDisksFiles]
OEMRES.DLL  = 1
OEMABC.GPD  = 1
OEMCORE.DLL = 1

[Strings]
MediaDescription = "Description for Vendor provided media"
```
