---
title: Direction
description: Direction
ms.assetid: 19aa1c88-968d-4789-89cc-00b76b1a30d9
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Direction%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




