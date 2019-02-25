---
title: Direction
description: Direction
ms.assetid: 19aa1c88-968d-4789-89cc-00b76b1a30d9
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Direction


Schema Path:\\Printer.Layout.NumberUp.Direction

Node Type:Property

Description:The property that determines the order in which multiple logical pages are placed on the media. The child values of this property contain the current direction and a list of the directions supported by the print device.

The Direction property contains two child values: CurrentValue and Supported.

### <span id="currentvalue"></span><span id="CURRENTVALUE"></span> CurrentValue

Schema Path:\\Printer.Layout.NumberUp.Direction:CurrentValue

Node Type:Value

Data Type:BIDI\_STRING

Description:The current (default) orientation in which to lay out the logical page(s). Each possible value consists of a horizontal direction and a vertical direction.

The following table lists the possible values.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
<th>Logical Page Order (4Up)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>RightDown</p></td>
<td><p>Print logical pages in horizontal rows, with the first row across the top of the sheet, and succeeding rows printed lower on the sheet. Within each row, logical pages are printed from right to left.</p></td>
<td><p>2 1</p>
<p>4 3</p></td>
</tr>
<tr class="even">
<td><p>DownRight</p></td>
<td><p>Print logical pages in vertical columns, with the first column closest to the right side of the sheet, and succeeding columns farther left on the sheet. Within each column, logical pages are printed from top to bottom.</p></td>
<td><p>3 1</p>
<p>4 2</p></td>
</tr>
<tr class="odd">
<td><p>LeftDown</p></td>
<td><p>Print logical pages in horizontal rows, with the first row across the top of the sheet, and succeeding rows printed lower on the sheet. Within each row, logical pages are printed from left to right.</p></td>
<td><p>1 2</p>
<p>3 4</p></td>
</tr>
<tr class="even">
<td><p>DownLeft</p></td>
<td><p>Print logical pages in vertical columns, with the first column closest to the left side of the sheet, and succeeding columns farther right on the sheet. Within each column, logical pages are printed from top to bottom.</p></td>
<td><p>1 3</p>
<p>2 4</p></td>
</tr>
</tbody>
</table>

 

### <span id="supported"></span><span id="SUPPORTED"></span> Supported

Schema Path:\\Printer.Layout.NumberUp.Direction:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all values supported for Direction.

 

 




