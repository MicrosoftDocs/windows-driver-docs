---
title: Methods for Specifying Pages
author: windows-driver-content
description: Methods for Specifying Pages
ms.assetid: 76006a2b-37b9-4490-913e-dcfc01812d43
keywords: ["Common Property Sheet User Interface WDK print , specifying pages", "CPSUI WDK print , specifying pages", "property sheet pages WDK print , specifying", "COMPROPSHEETUI", "PROPSHEETPAGE"]
---

# Methods for Specifying Pages


## <a href="" id="ddk-methods-for-specifying-pages-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Methods%20for%20Specifying%20Pages%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


