---
title: Creating Property Sheet Pages for Printers
description: Creating Property Sheet Pages for Printers
keywords:
- printer interface DLL WDK , property sheet pages
- property sheet pages WDK print , creating
- property sheet pages WDK print , printer interface DLL
ms.date: 01/27/2023
---

# Creating Property Sheet Pages for Printers

[!include[Print Support Apps](../includes/print-support-apps.md)]

Printer interface DLLs, in conjunction with [CPSUI](common-property-sheet-user-interface.md), are responsible for creating the property sheet pages that users of Windows 2000 and later employ to view and modify configuration parameters associated with printers and print documents. Each printer interface DLL must provide a [**DrvDevicePropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicepropertysheets) function to create printer-specific pages, and a [**DrvDocumentPropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets) function to create document-specific pages.

To understand how these functions should be designed, it is important to read the section describing [CPSUI](common-property-sheet-user-interface.md). Displaying property sheet pages involves interaction between an application, the print spooler, the printer interface DLL, and CPSUI. Execution flow is described in [Using CPSUI with Printer Drivers](using-cpsui-with-printer-drivers.md).
