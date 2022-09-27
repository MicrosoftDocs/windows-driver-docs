---
title: Directory Services for printers
description: Provides information about Directory Services for printers.
keywords:
- Directory Services WDK printer
- printer Directory Services support WDK
- print queues WDK, Directory Services
- queues WDK printer, Directory Services
ms.date: 09/12/2022
---

# Directory Services for printers

When a user installs a network-shared printer, the print folder, by default, also publishes the printer to Directory Services. Publication is accomplished by calling the spooler's **SetPrinter** function with an input structure of [**PRINTER_INFO_7**](/windows/win32/printdocs/printer-info-7).

Publishing a print queue makes it visible to users through the **Search** option on the task bar's **Start** menu.

The following topics provide more information about printer support for Directory Services:

[Print spooler support for printer Directory Services](print-spooler-support-for-printer-directory-services.md)

[Printer driver support for printer Directory Services](printer-driver-support-for-printer-directory-services.md)
