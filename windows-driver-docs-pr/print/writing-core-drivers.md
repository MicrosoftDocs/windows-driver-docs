---
title: Writing Core Drivers
description: Writing Core Drivers
ms.assetid: 3a41a91b-3cc3-462a-8836-448203ccb4c2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing Core Drivers


Print driver writers can use the core driver functionality that Windows Vista provides. To make a core driver, generate a GUID that other driver packages can use to refer to the set of files that makes up the core driver. For example, in Ntprint.inf, the Unidrv core driver file definition is shown in the following example:

```cpp
[Microsoft.NTx86]
"{D20EA372-DD35-4950-9ED8-A6335AFE79F0}" =  
  {D20EA372-DD35-4950-9ED8-A6335AFE79F0}, 
  {D20EA372-DD35-4950-9ED8-A6335AFE79F0}
[{D20EA372-DD35-4950-9ED8-A6335AFE79F0}]
CopyFiles=UNIDRV,PJLMON.DLL,@TTFSUB.GPD,@LOCALE.GPD,@MSXPSINC.GPD
[UNIDRV]
; Unidrv files and pjlmon sections follow...
```

With this definition, a print driver INF file can refer to core driver files by using the **CoreDriverSections** keyword as shown in the previous sample.

It is important to note that a core driver must retain compatibility with earlier versions. Because more than one driver may use the core driver, it must continue to work with existing drivers that depend on it when it is updated. The core driver must ship as part of the driver package.

The core driver is defined with a Model section, which includes a device description that is the core driver GUID. For example:

```cpp
; Model section
[Company.NTx86]
"{GUID1}" = {GUID1}, {GUID1}

; Install section - must list all files in the core printer driver
[{GUID1}]
DriverVer = MM/DD/YYYY,1.1.1.1
CopyFiles=MANUFACTURER_CORE_FILESET

; Core Driver Section, can use print-specific INF keywords here
[MANUFACTURER_CORE]
CopyFiles=MANUFACTURER_CORE_FILESET

[MANUFACTURER_CORE_FILESET]
File1.dll
File2.dll
File3.dll

[ControlFlags]
AlwaysExcludeFromSelect = {GUID1}
```

The core driver must include version information in the install section, by using the **DriverVer** keyword. The install section must also list all the files that the core driver requires. Use the new **AlwaysExcludeFromSelect** keyword to ensure that the core driver is not displayed to the user in the UI.

 

 




