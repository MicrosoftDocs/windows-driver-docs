---
title: Printer Dirids
description: Printer Dirids
keywords:
- INF files WDK print , dirids
- dirids WDK
- directory identifiers WDK printer
- printer dirids WDK
- identifiers WDK printer
ms.date: 02/16/2021
ms.localizationpriority: medium
---

# Printer Dirids

When specifying target directories within INF files, directory identifiers (`dirids`) should be used. For more information, see [Using Dirids](../install/using-dirids.md).

The following table lists printer-specific `dirids` and the purpose of each.

| Dirid | Purpose | Directory contents |
|--|--|--|
| 66000 | Represents the directory path returned by the **GetPrinterDriverDirectory** function. | Driver files and dependent files dependent files |
| 66001 | Represents the directory path returned by the **GetPrintProcessorDirectory** function. | Print processor files |
| 66002 | Represents the directory path to additional files to be copied to \System32 of the local system. See the paragraph following this table. | Print monitor files |
| 66003 | Represents the directory path returned by the [GetColorDirectory](/windows/win32/api/icm/nf-icm-getcolordirectoryw) function. | ICM color profile files |
| 66004 | Represents the directory path to which printer type-specific ASP files are copied. | ASP files and associated files |

Files in the directory assigned to `dirid` 66002 are copied to the System32 subdirectory when printer drivers for the native architecture are being installed on the local system, such as when x86 drivers are installed locally on a x86 system. Files in this directory are ignored if a driver is being installed to a remote system.

A printer driver is installed when the printer class installer calls the spooler's **AddPrinterDriverEx** function. This function requires all driver files to be located in the directory that is returned by the **GetPrinterDriverDirectory** function.
