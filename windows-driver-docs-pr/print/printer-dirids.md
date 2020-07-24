---
title: Printer Dirids
description: Printer Dirids
ms.assetid: 104af180-c739-4733-b21b-448cfe15ab71
keywords:
- INF files WDK print , dirids
- dirids WDK
- directory identifiers WDK printer
- printer dirids WDK
- identifiers WDK printer
ms.date: 06/12/2020
ms.localizationpriority: medium
---

# Printer Dirids

When specifying target directories within INF files, directory identifiers (`dirids`) should be used. For more information, see [Using Dirids](https://docs.microsoft.com/windows-hardware/drivers/install/using-dirids).

The following table lists printer-specific `dirids` and the purpose of each.

| Dirid | Purpose | Directory contents |
|--|--|--|
| 66000 | Represents the directory path returned by the [GetPrinterDriverDirectory](https://docs.microsoft.com/windows/win32/printdocs/getprinterdriverdirectory) function. | Driver files and [dependent files](printer-inf-file-entries.md#ddk-dependent-files-gg) dependent files |
| 66001 | Represents the directory path returned by the [GetPrintProcessorDirectory](https://docs.microsoft.com/windows/win32/printdocs/getprintprocessordirectory) function. | [Print processor](https://docs.microsoft.com/windows-hardware/drivers/#wdkgloss-print-processor) files. |
| 66002 | Represents the directory path to additional files to be copied to \System32 of the local system. See the paragraph following this table. | [Print monitor](https://docs.microsoft.com/windows-hardware/drivers/#wdkgloss-print-monitor) files. |
| 66003 | Represents the directory path returned by the [GetColorDirectory](https://docs.microsoft.com/previous-versions/windows/desktop/wcs/getcolordirectory) function. | ICM color profile files. |
| 66004 | Represents the directory path to which printer type-specific ASP files are copied. | ASP files and associated files. |

Files in the directory assigned to `dirid` 66002 are copied to the System32 subdirectory when printer drivers for the native architecture are being installed on the local system, such as when x86 drivers are installed locally on a x86 system. Files in this directory are ignored if a driver is being installed to a remote system.

A printer driver is installed when the printer class installer calls the spooler's [AddPrinterDriverEx](https://docs.microsoft.com/windows/win32/printdocs/addprinterdriverex) function. This function requires all driver files to be located in the directory that is returned by the **GetPrinterDriverDirectory** function.
