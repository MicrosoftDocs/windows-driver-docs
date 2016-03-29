---
title: Returning Printer-Specific Information
description: Returning Printer-Specific Information
ms.assetid: 7a47b395-4b01-437f-bed7-967b31b5841e
keywords: ["printer graphics DLL WDK , return printer-specific information", "graphics DLL WDK printer , return printer-specific information", "returning printer-specific information WDK printer graphics"]
---

# Returning Printer-Specific Information


## <a href="" id="ddk-returning-printer-specific-information-gg"></a>


GDI sometimes requests a printer graphics DLL to return printer-specific information in between print jobs, by calling such **DrvQuery**-prefixed graphics DDI functions as [**DrvQueryAdvanceWidths**](https://msdn.microsoft.com/library/windows/hardware/ff556259) (if defined by the graphics DLL).

An example of when this might occur is the case of a word processing application that is maintaining a WYSIWYG screen display of a printable page. To correctly display the line breaks in text, the word processor must base line-fitting calculations on character widths and other font metrics from the selected printer's implementation of a font.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Returning%20Printer-Specific%20Information%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




