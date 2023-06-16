---
title: Using Core Drivers
description: Using Core Drivers
ms.date: 05/08/2023
---

# Using Core Drivers

[!include[Print Support Apps](../includes/print-support-apps.md)]

Print driver writers can use core drivers that they have written by listing the core model GUID in the model section of the INF, and using the **PackageAware** and **CoreDriverSections** keywords.

For example:

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
"My Device Description"  = DriverInstall_Vista, OEM_Company_NameABC_123A
; Core driver definition as discussed in the section Writing Core Drivers
"{GUID1}" = {GUID1}, {GUID1}

[DriverInstall_Vista]
CopyFiles=@file.dll
CoreDriverSections="{D20EA372-DD35-4950-9ED8-A6335AFE79F0},UNIDRV.OEM,UNIDRV_DATA,TTFSUB.OEM", "{GUID1},MANUFACTURER_CORE"
The package install section must also be added, and list all core driver dependencies:
[PrinterPackageInstallation.x86]
PackageAware=TRUE
CoreDriverDependencies={D20EA372-DD35-4950-9ED8-A6335AFE79F0},{GUID1}
```
