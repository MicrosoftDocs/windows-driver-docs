---
title: PagesPerSheet
description: Defines the number of logical pages that can be printed on a single side of the selected media.
ms.date: 09/02/2021
---

# PagesPerSheet

Schema Path: \\Printer.Layout.NumberUp.PagesPerSheet

Node Type: Property

Description:Defines the number of logical pages that can be printed on a single side of the selected media. The value entries that are children of this property specify the current number of logical pages per media sheet, and a list of numbers, each specifying a different number of pages per sheet.

The PagesPerSheet property contains two child values: **CurrentValue** and **Supported**.

## CurrentValue

Schema Path: \\Printer.Layout.NumberUp.PagesPerSheet:CurrentValue

Node Type: Value

Data Type: BIDI_INT

Description: The current (default) number of logical pages that should be placed on a single side of the selected media.

## Supported

Schema Path: \\Printer.Layout.NumberUp.PagesPerSheet:Supported

Node Type: Value

Data Type: BIDI_STRING

Description: A comma-separated list of all the values supported for PagesPerSheet.
