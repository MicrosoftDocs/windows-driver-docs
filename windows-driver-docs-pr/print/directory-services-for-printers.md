---
title: Directory Services for Printers
description: Directory Services for Printers
ms.assetid: 4b368602-67d9-4d26-a82b-8d14d8da2625
keywords:
- Directory Services WDK printer
- printer Directory Services support WDK
- print queues WDK , Directory Services
- queues WDK printer , Directory Services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Directory Services for Printers





When a user installs a network-shared printer, the Windows 2000 and later print folder, by default, also publishes the printer to the Windows 2000 (or later) Directory Services. Publication is accomplished by calling the spooler's **SetPrinter** function with an input structure of PRINTER\_INFO\_7, as described in the Microsoft Windows SDK documentation.

Publishing a print queue makes it visible to users through the **Search** option on the task bar's **Start** menu.

The following topics provide more information about printer support for Directory Services:

[Print Spooler Support for Printer Directory Services](print-spooler-support-for-printer-directory-services.md)

[Printer Driver Support for Printer Directory Services](printer-driver-support-for-printer-directory-services.md)

 

 




