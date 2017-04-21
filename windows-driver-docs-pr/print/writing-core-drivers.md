---
title: Writing Core Drivers
author: windows-driver-content
description: Writing Core Drivers
ms.assetid: 3a41a91b-3cc3-462a-8836-448203ccb4c2
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Writing Core Drivers


Print driver writers can use the core driver functionality that Windows Vista provides. To make a core driver, generate a GUID that other driver packages can use to refer to the set of files that makes up the core driver. For example, in Ntprint.inf, the Unidrv core driver file definition is shown in the following example:

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Writing%20Core%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


