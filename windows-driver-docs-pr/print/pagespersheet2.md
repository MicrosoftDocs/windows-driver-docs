---
title: PagesPerSheet
description: PagesPerSheet
ms.assetid: 019c9344-7661-4c39-a441-469d340e61cb
---

# PagesPerSheet


Schema Path:\\Printer.Layout.NumberUp.PagesPerSheet

Node Type:Property

Description:Defines the number of logical pages that can be printed on a single side of the selected media. The value entries that are children of this property specify the current number of logical pages per media sheet, and a list of numbers, each specifying a different number of pages per sheet.

The PagesPerSheet property contains two child values: **CurrentValue** and **Supported**.

### CurrentValue

Schema Path:\\Printer.Layout.NumberUp.PagesPerSheet:CurrentValue

Node Type:Value

Data Type:BIDI\_INT

Description:The current (default) number of logical pages that should be placed on a single side of the selected media.

### Supported

Schema Path:\\Printer.Layout.NumberUp.PagesPerSheet:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all the values supported for PagesPerSheet.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PagesPerSheet%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




