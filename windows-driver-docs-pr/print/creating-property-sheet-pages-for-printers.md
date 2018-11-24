---
title: Creating Property Sheet Pages for Printers
description: Creating Property Sheet Pages for Printers
ms.assetid: b9b7aa52-39b7-4809-acdf-e72293da37e1
keywords:
- printer interface DLL WDK , property sheet pages
- property sheet pages WDK print , creating
- property sheet pages WDK print , printer interface DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Property Sheet Pages for Printers





Printer interface DLLs, in conjunction with [CPSUI](common-property-sheet-user-interface.md), are responsible for creating the property sheet pages that users of Windows 2000 and later employ to view and modify configuration parameters associated with printers and print documents. Each printer interface DLL must provide a [**DrvDevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548542) function to create printer-specific pages, and a [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548) function to create document-specific pages.

To understand how these functions should be designed, it is important to read the section describing [CPSUI](common-property-sheet-user-interface.md). Displaying property sheet pages involves interaction between an application, the print spooler, the printer interface DLL, and CPSUI. Execution flow is described in [Using CPSUI with Printer Drivers](using-cpsui-with-printer-drivers.md).

 

 




