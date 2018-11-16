---
title: Installing a Unidrv Minidriver
description: Installing a Unidrv Minidriver
ms.assetid: 0efead8f-c413-4ec1-b940-89b57f95345e
keywords:
- Unidrv, minidrivers
- minidrivers WDK Unidrv
- INF files WDK print , Unidrv minidrivers
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Unidrv Minidriver





Installation of a Unidrv minidriver requires a [printer INF file](printer-inf-files.md) that identifies the minidriver's files. If a printer model is not supported by Microsoft's printer INF file, ntprint.inf, a vendor-supplied INF file is required. The INF file should reference [printer INF file data sections](printer-inf-file-data-sections.md) and [printer INF file install sections](printer-inf-file-install-sections.md), which are defined in ntprint.inf. For a minidriver named abc100, the following INF file entries are typically needed, if the printer is bidirectional, supports TrueType font substitution, and uses a single resource DLL:

```cpp
[Manufacturer]
"ABC Printers"
 
[ABC Printers]
"ABC Printer 100" = ABC100.GPD, ABC_Printer_100
 
[ABC100.GPD]
CopyFiles=@ABCres.dll,@ABC100.gpd  ;Resource DLL and GPD file
DataSection=UNIDRV_BIDI_DATA       ;Unidrv Data Section
DataFile=ABC100.gpd
Include=NTPRINT.INF                ;Include NTPRINT.INF.
Needs=TTFSUB.OEM,UNIDRV_BIDI.OEM   ;Install TrueType subs, Unidrv,
  ;    and PJL language monitor.
```

If you are providing a [user interface plug-in](user-interface-plug-ins.md) or a [rendering plug-in](rendering-plug-ins.md), you need to include the names of these components within your INF file. For information about installing customized code, see [Installing Customized Driver Components](installing-customized-driver-components.md).

 

 




