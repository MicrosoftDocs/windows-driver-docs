---
title: Methods for specifying pages
description: Provides information about methods for specifying pages.
keywords:
- Common Property Sheet User Interface WDK print, specifying pages
- CPSUI WDK print, specifying pages
- property sheet pages WDK print, specifying
- COMPROPSHEETUI
- PROPSHEETPAGE
ms.date: 09/14/2022
---

# Methods for specifying pages

An application can use any of three methods to specify property sheet pages to CPSUI. Each of the following methods involves calling CPSUI's [**ComPropSheet**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfncompropsheet) function, specifying one of the [ComPropSheet function codes](/windows-hardware/drivers/ddi/_print/index).

- Supplying a [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) structure

    If an application describes a property sheet page by passing a COMPROPSHEETUI structure to **ComPropSheet**, it can:

  - Use one of the [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md) to specify a predefined, standard page type that printer interface DLLs can use for printer property sheets.

  - Specify a set of user-modifiable [property sheet options](property-sheet-options.md) that will appear on the page.

  - Specify a [page event callback](page-event-callbacks.md) function that CPSUI will call when a user views or modifies the page's options.

- Supplying a [**PROPSHEETPAGE**](/windows/win32/controls/pss-propsheetpage) structure

    A **PROPSHEETPAGE** structure can be used to describe a property sheet page, if the page cannot be constructed using the common (standard) dialogs available when using a **COMPROPSHEETUI** structure. Printer interface DLLs typically should not need to use this method.

- Supplying a callback function

    An application can pass [**ComPropSheet**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfncompropsheet) the address of a [**PFNPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfnpropsheetui)-typed callback function, which CPSUI immediately calls. The callback function is responsible for calling **ComPropSheet** itself to create property sheet pages.

    The print spooler uses this method to inform CPSUI of the existence a printer interface DLL's [**DrvDocumentPropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdocumentpropertysheets) and [**DrvDevicePropertySheets**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicepropertysheets) functions. Likewise, the *Unidrv* and *Pscript* drivers use the technique to inform CPSUI of the existence of [**IPrintOemUI::DocumentPropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-documentpropertysheets) and [**IPrintOemUI::DevicePropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devicepropertysheets) COM methods in [user interface plug-ins](user-interface-plug-ins.md).

Whichever method is used for specifying new pages, the pages must be assigned to a [group parent](group-parent.md) by passing a group parent handle to the **ComPropSheet** function.
