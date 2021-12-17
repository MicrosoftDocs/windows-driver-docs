---
title: Downloading Driver-Specific Files
description: Downloading Driver-Specific Files
keywords:
- Point and Print WDK , driver-specific files
- driver-specific files WDK printer
- downloading driver-specific printer files
ms.date: 12/16/2021
ms.custom: contperf-fy22q2
---

# Downloading Driver-Specific Files

A client system creates a connection to a print server by calling [**AddPrinterConnection**](/windows/win32/printdocs/addprinterconnection).

This call results in a call to [**GetPrinterDriver**](/windows/win32/printdocs/getprinterdriver) on the server, which reads the [printer's INF file](printer-inf-files.md) in order to fill in a DRIVER_INFO_3 structure, followed by a call to [**AddPrinterDriver**](/windows/win32/printdocs/addprinterdriver), with the [**DRIVER_INFO_3**](/windows/win32/printdocs/driver-info-3) structure as input.

The **AddPrinterDriver** function causes all files listed in the **DRIVER_INFO_3** structure to be sent to the client.

## See also

[**AddPrinterConnection**](/windows/win32/printdocs/addprinterconnection)

[**AddPrinterDriver**](/windows/win32/printdocs/addprinterdriver)

[**GetPrinterDriver**](/windows/win32/printdocs/getprinterdriver)

[**DRIVER_INFO_3**](/windows/win32/printdocs/driver-info-3)
