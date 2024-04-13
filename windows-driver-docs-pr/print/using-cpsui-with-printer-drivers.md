---
title: Use CPSUI with Printer Drivers
description: Provides information about how to use Using CPSUI with printer drivers.
keywords:
- Common Property Sheet User Interface WDK print, displaying property sheet pages
- CPSUI WDK print, displaying property sheet pages
- property sheet pages WDK print, displaying
- displaying property sheet pages
- Common Property Sheet User Interface WDK print, about CPSUI
- CPSUI WDK print , about CPSUI
- property sheet pages WDK print, about CPSUI with printer drivers
ms.date: 01/31/2023
---

# Use CPSUI with printer drivers

[!include[Print Support Apps](../includes/print-support-apps.md)]

The print spooler, in conjunction with [printer interface DLLs](printer-interface-dll.md), uses CPSUI to create property sheet pages for print documents and printer devices. The following steps are involved when an application (such as Microsoft Word) displays a property sheet for a print document:

1. The application calls the print spooler's [**DocumentProperties**](/windows/win32/printdocs/documentproperties) function, specifying the printer on which the document is to be printed.

1. The print spooler calls CPSUI's entry point function, [**CommonPropertySheetUI**](/windows-hardware/drivers/ddi/compstui/nf-compstui-commonpropertysheetuia), specifying an internal [**PFNPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfnpropsheetui)-typed callback function.

1. CPSUI calls the spooler's PFNPROPSHEETUI-typed callback function.

1. The spooler's PFNPROPSHEETUI-typed callback function calls CPSUI's [**ComPropSheet**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfncompropsheet) function (with a [**CPSFUNC_ADD_PFNPROPSHEETUI**](/previous-versions/ff546391(v=vs.85)) function code) to notify CPSUI of the address of the appropriate printer interface DLL's [**DrvDocumentPropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets) function.

1. CPSUI calls the printer interface DLL's **DrvDocumentPropertySheets** function.

1. The printer interface DLL's **DrvDocumentPropertySheets** function calls CPSUI's **ComPropSheet** function (typically with a [**CPSFUNC_ADD_PCOMPROPSHEETUI**](/previous-versions/ff546388(v=vs.85)) function code) to provide CPSUI with property sheet page descriptions and [page event callbacks](page-event-callbacks.md).

1. CPSUI's **ComPropSheet** function calls **CreatePropertySheetPage** (described in the Windows SDK documentation) to create the property sheet pages specified by the printer interface DLL. CPSUI then calls [**PropertySheet**](/windows/win32/api/prsht/nf-prsht-propertysheeta) to display the property sheet pages.

The following diagram illustrates these steps.

![diagram illustrating the modules involved in displaying a property sheet.](images/usecpsui.png)

As the application user traverses the property sheet pages and modifies option values, the operating system notifies CPSUI of page events and CPSUI, in turn, calls the page event callback supplied by the printer interface DLL. The page event callback handles page events and stores newly selected option values internally, as necessary.

When the user dismisses the property sheet by clicking on the **Ok** or **Cancel** button, CPSUI destroys the pages and causes the **CommonPropertySheetUI** function to return to the print spooler, which then returns control to the application.

When an application displays a property sheet for a printer device instead of a print document, the same steps are followed, except that the application calls the spooler's **PrinterProperties** function and the spooler passes the address of the printer interface DLL's [**DrvDevicePropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicepropertysheets) function to CPSUI.
