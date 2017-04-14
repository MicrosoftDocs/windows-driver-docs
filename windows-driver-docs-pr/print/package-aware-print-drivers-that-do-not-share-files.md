---
title: Package-Aware Print Drivers that Do Not Share Files
author: windows-driver-content
description: Package-Aware Print Drivers that Do Not Share Files
ms.assetid: cd114766-37f4-43b5-8e2a-d85f95c973ab
keywords: ["package-aware print drivers WDK"]
---

# Package-Aware Print Drivers that Do Not Share Files


When the files in the driver package are uniquely named and do not occur in any other driver package, add a PrinterPackageInstallation section to the INF file. In that section, add the **PackageAware**=TRUE keyword as shown in line 23 of the following example:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Package-Aware%20Print%20Drivers%20that%20Do%20Not%20Share%20Files%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


