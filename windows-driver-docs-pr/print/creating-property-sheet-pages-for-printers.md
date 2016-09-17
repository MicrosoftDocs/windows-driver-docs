---
title: Creating Property Sheet Pages for Printers
author: windows-driver-content
description: Creating Property Sheet Pages for Printers
MS-HAID:
- 'drvarch\_be5800a3-1080-42dd-b7d3-aa8ae59ec9d9.xml'
- 'print.creating\_property\_sheet\_pages\_for\_printers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b9b7aa52-39b7-4809-acdf-e72293da37e1
keywords: ["printer interface DLL WDK , property sheet pages", "property sheet pages WDK print , creating", "property sheet pages WDK print , printer interface DLL"]
---

# Creating Property Sheet Pages for Printers


## <a href="" id="ddk-creating-property-sheet-pages-for-printers-gg"></a>


Printer interface DLLs, in conjunction with [CPSUI](common-property-sheet-user-interface.md), are responsible for creating the property sheet pages that users of Windows 2000 and later employ to view and modify configuration parameters associated with printers and print documents. Each printer interface DLL must provide a [**DrvDevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548542) function to create printer-specific pages, and a [**DrvDocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff548548) function to create document-specific pages.

To understand how these functions should be designed, it is important to read the section describing [CPSUI](common-property-sheet-user-interface.md). Displaying property sheet pages involves interaction between an application, the print spooler, the printer interface DLL, and CPSUI. Execution flow is described in [Using CPSUI with Printer Drivers](using-cpsui-with-printer-drivers.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Creating%20Property%20Sheet%20Pages%20for%20Printers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


