---
title: Installing a Pscript Minidriver
description: Installing a Pscript Minidriver
keywords:
- minidrivers WDK Pscript , installing
- INF files WDK print , Pscript
ms.date: 01/27/2023
---

# Installing a Pscript Minidriver

[!include[Print Support Apps](../includes/print-support-apps.md)]

Installation of a Pscript minidriver requires a [printer INF file](printer-inf-files.md) that identifies the minidriver's files. If a printer model isn't supported by Microsoft's printer INF file, ntprint.inf, a vendor-supplied INF file is required. The INF file should reference [printer INF file data sections](printer-inf-file-data-sections.md) and [printer INF file install sections](printer-inf-file-install-sections.md), which are defined in ntprint.inf. For a minidriver named abc100, the following INF file entries are typically needed:

```inf
[Manufacturer]
"ABC Printers"
 
[ABC Printers]
"ABC Printer 100 PS" = ABC100.PPD, ABC_Printer_100_PS
 
[ABC100.PPD]
CopyFiles=@ABC100.ppd       ; PPD file.
DataSection=PSCRIPT_DATA    ; PSCRIPT Data Section
DataFile=ABC100.ppd
Include=NTPRINT.INF         ; Include NTPRINT.INF.
Needs=PSCRIPT.OEM           ; Install PSCRIPT.
```

If you're providing a [user interface plug-in](user-interface-plug-ins.md) or a [rendering plug-in](rendering-plug-ins.md), you need to include the names of these components within your INF file. For information about installing customized code, see [Installing Customized Driver Components](installing-customized-driver-components.md).
