---
title: Using CPSUI with Printer Drivers
author: windows-driver-content
description: Using CPSUI with Printer Drivers
ms.assetid: 898a855d-6a9a-4f98-9ee4-bad439427326
keywords: ["Common Property Sheet User Interface WDK print , displaying property sheet pages", "CPSUI WDK print , displaying property sheet pages", "property sheet pages WDK print , displaying", "displaying property sheet pages", "Common Property Sheet User Interface WDK print , about CPSUI", "CPSUI WDK print , about CPSUI", "property sheet pages WDK print , about CPSUI with printer drivers"]
---

# Using CPSUI with Printer Drivers


## <a href="" id="ddk-using-cpsui-with-printer-drivers-gg"></a>


The print spooler, in conjunction with [printer interface DLLs](printer-interface-dll.md), uses CPSUI to create property sheet pages for print documents and printer devices. The following steps are involved when an application (such as Microsoft Word) displays a property sheet for a print document:

1.  The application calls the print spooler's **DocumentProperties** function (described in the Microsoft Windows SDK documentation), specifying the printer on which the document is to be printed.

2.  The print spooler calls CPSUI's entry point function, [**CommonPropertySheetUI**](https://msdn.microsoft.com/library/windows/hardware/ff546148), specifying an internal [**PFNPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff559812)-typed callback function.

3.  CPSUI calls the spooler's PFNPROPSHEETUI-typed callback function.

4.  The spooler's PFNPROPSHEETUI-typed callback function calls CPSUI's [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) function (with a [**CPSFUNC\_ADD\_PFNPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff546391) function code) to notify CPSUI of the address of the appropriate printer interface DLL's [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548) function.

5.  CPSUI calls the printer interface DLL's **DrvDocumentPropertySheets** function.

6.  The printer interface DLL's **DrvDocumentPropertySheets** function calls CPSUI's **ComPropSheet** function (typically with a [**CPSFUNC\_ADD\_PCOMPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff546388) function code) to provide CPSUI with property sheet page descriptions and [page event callbacks](page-event-callbacks.md).

7.  CPSUI's **ComPropSheet** function calls **CreatePropertySheetPage** (described in the Windows SDK documentation) to create the property sheet pages specified by the printer interface DLL. CPSUI then calls **PropertySheet** (described in the Windows SDK documentation) to display the property sheet pages.

The following diagram illustrates these steps.

![diagram illustrating the modules involved in displaying a property sheet](images/usecpsui.png)

As the application user traverses the property sheet pages and modifies option values, the operating system notifies CPSUI of page events and CPSUI, in turn, calls the page event callback supplied by the printer interface DLL. The page event callback handles page events and stores newly selected option values internally, as necessary.

When the user dismisses the property sheet by clicking on the **Ok** or **Cancel** button, CPSUI destroys the pages and causes the **CommonPropertySheetUI** function to return to the print spooler, which then returns control to the application.

When an application displays a property sheet for a printer device instead of a print document, the same steps are followed, except that the application calls the spooler's **PrinterProperties** function and the spooler passes the address of the printer interface DLL's [**DrvDevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548542) function to CPSUI.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20CPSUI%20with%20Printer%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


