---
title: PagesPerSheet
description: PagesPerSheet
ms.assetid: 019c9344-7661-4c39-a441-469d340e61cb
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PagesPerSheet


Schema Path:\\Printer.Layout.NumberUp.PagesPerSheet

Node Type:Property

Description:Defines the number of logical pages that can be printed on a single side of the selected media. The value entries that are children of this property specify the current number of logical pages per media sheet, and a list of numbers, each specifying a different number of pages per sheet.

The PagesPerSheet property contains two child values: **CurrentValue** and **Supported**.

### <span id="currentvalue"></span><span id="CURRENTVALUE"></span>CurrentValue

Schema Path:\\Printer.Layout.NumberUp.PagesPerSheet:CurrentValue

Node Type:Value

Data Type:BIDI\_INT

Description:The current (default) number of logical pages that should be placed on a single side of the selected media.

### <span id="supported"></span><span id="SUPPORTED"></span>Supported

Schema Path:\\Printer.Layout.NumberUp.PagesPerSheet:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all the values supported for PagesPerSheet.

 

 




