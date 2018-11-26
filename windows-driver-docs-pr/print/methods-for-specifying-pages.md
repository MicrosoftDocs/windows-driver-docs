---
title: Methods for Specifying Pages
description: Methods for Specifying Pages
ms.assetid: 76006a2b-37b9-4490-913e-dcfc01812d43
keywords:
- Common Property Sheet User Interface WDK print , specifying pages
- CPSUI WDK print , specifying pages
- property sheet pages WDK print , specifying
- COMPROPSHEETUI
- PROPSHEETPAGE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Methods for Specifying Pages





An application can use any of three methods to specify property sheet pages to CPSUI. Each of the following methods involves calling CPSUI's [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) function, specifying one of the [ComPropSheet function codes](https://msdn.microsoft.com/library/windows/hardware/ff546214).

-   Supplying a [**COMPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff546211) structure

    If an application describes a property sheet page by passing a COMPROPSHEETUI structure to **ComPropSheet**, it can:

    -   Use one of the [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md) to specify a predefined, standard page type that printer interface DLLs can use for printer property sheets.
    -   Specify a set of user-modifiable [property sheet options](property-sheet-options.md) that will appear on the page.
    -   Specify a [page event callback](page-event-callbacks.md) function that CPSUI will call when a user views or modifies the page's options.
-   Supplying a PROPSHEETPAGE structure

    A PROPSHEETPAGE structure (described in the Microsoft Windows SDK documentation) can be used to describe a property sheet page, if the page cannot be constructed using the common (standard) dialogs available when using a COMPROPSHEETUI structure. Printer interface DLLs typically should not need to use this method.

-   Supplying a callback function

    An application can pass [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) the address of a [**PFNPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff559812)-typed callback function, which CPSUI immediately calls. The callback function is responsible for calling **ComPropSheet** itself to create property sheet pages.

    The print spooler uses this method to inform CPSUI of the existence a printer interface DLL's [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548) and [**DrvDevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548542) functions. Likewise, the [*Unidrv*](https://msdn.microsoft.com/library/windows/hardware/ff556343#wdkgloss-unidrv) and [*Pscript*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pscript) drivers use the technique to inform CPSUI of the existence of [**IPrintOemUI::DocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554173) and [**IPrintOemUI::DevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554165) COM methods in [user interface plug-ins](user-interface-plug-ins.md).

Whichever method is used for specifying new pages, the pages must be assigned to a [group parent](group-parent.md) by passing a group parent handle to the **ComPropSheet** function.

 

 




