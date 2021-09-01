---
title: Direction
description: Determines the order in which multiple logical pages are placed on the media.
ms.date: 08/31/2021
ms.localizationpriority: medium
---

# Direction

Schema Path: \\Printer.Layout.NumberUp.Direction

Node Type: Property

Description: The property that determines the order in which multiple logical pages are placed on the media. The child values of this property contain the current direction and a list of the directions supported by the print device.

The Direction property contains two child values: CurrentValue and Supported.

## CurrentValue

Schema Path: \\Printer.Layout.NumberUp.Direction:CurrentValue

Node Type: Value

Data Type: BIDI\_STRING

Description: The current (default) orientation in which to lay out the logical page(s). Each possible value consists of a horizontal direction and a vertical direction.

The following table lists the possible values.

| Value | Definition | Logical Page Order (4Up) |
|--|--|--|
| RightDown | Print logical pages in horizontal rows, with the first row across the top of the sheet, and succeeding rows printed lower on the sheet. Within each row, logical pages are printed from right to left. | 2 1<br>4 3 |
| DownRight | Print logical pages in vertical columns, with the first column closest to the right side of the sheet, and succeeding columns farther left on the sheet. Within each column, logical pages are printed from top to bottom. | 3 1<br>4 2 |
| LeftDown | Print logical pages in horizontal rows, with the first row across the top of the sheet, and succeeding rows printed lower on the sheet. Within each row, logical pages are printed from left to right. | 1 2<br>3 4 |
| DownLeft | Print logical pages in vertical columns, with the first column closest to the left side of the sheet, and succeeding columns farther right on the sheet. Within each column, logical pages are printed from top to bottom. | 1 3<br>2 4 |

## Supported

Schema Path: \\Printer.Layout.NumberUp.Direction:Supported

Node Type: Value

Data Type: BIDI_STRING

Description: A comma-separated list of all values supported for Direction.
