---
title: Introduction to Printer Interface DLLs
description: Introduction to Printer Interface DLLs
ms.assetid: 1993d818-9761-418e-96c3-e3c46965bef1
keywords:
- printer interface DLL WDK , about printer interface DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Printer Interface DLLs





Printers typically provide users with a large number of modifiable configuration options that can be changed for each document that is printed. Options such as paper, tray and font selection, along with image resolution, size, color, and so on, must be accessible through user interfaces that can be invoked by applications.

A printer driver's *printer interface DLL*, which executes in user mode, is responsible for exporting a user interface to the printer's configuration options. Providing this interface involves [creating property sheet pages for printers](creating-property-sheet-pages-for-printers.md). Applications (such as the print folder) display the interface by calling Win32 functions exported by the print spooler, and the spooler, in turn, calls [functions defined by printer interface DLLs](functions-defined-by-printer-interface-dlls.md).

Providing a user interface to configuration options is not a printer interface DLL's only responsibility. The DLL also exports functions that the spooler can call to notify the driver of print-related system events, such as driver installations and upgrades, or printer additions and connections.

 

 




