---
title: Package-Aware Print Drivers that Do Not Share Files
description: Package-Aware Print Drivers that Do Not Share Files
ms.assetid: cd114766-37f4-43b5-8e2a-d85f95c973ab
keywords:
- package-aware print drivers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Package-Aware Print Drivers that Do Not Share Files


When the files in the driver package are uniquely named and do not occur in any other driver package, add a PrinterPackageInstallation section to the INF file. In that section, add the **PackageAware**=TRUE keyword as shown in line 23 of the following example:

```cpp
[Version]
Signature="$Windows NT$"
ClassGUID={4D36E979-E325-11CE-BFC1-08002BE10318}
Class=Printer
Provider="OEM Company"
CatalogFile=PackageAware.cat     ; Single Catalog file for all OS versions
DriverVer=10/10/2005, 1.2.3.4

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

 

 




