---
title: XR Layout
description: XR Layout
ms.assetid: a5c5d627-8d1a-4091-a7b2-893165e7fe45
keywords:
- Direct3D version 10.1 WDK Windows 7 display , XR layout
- extended format WDK Windows 7 display , XR layout
- XR layout WDK Windows 7 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XR Layout


This section applies only to Windows 7 and later operating systems.

XR is a fixed-point 1.9 format. The value is biased by -0.5, which results in a dynamic range of approximately \[-0.5,1.5\]. The fixed point representation implies a scale of 2x to shift the decimal point one place to the right.

Each XR element occupies one 32-bit DWORD, which is laid out as shown in the following table regardless of host CPU endianness.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bits 31:30</th>
<th align="left">Bits 29:20</th>
<th align="left">Bits 19:10</th>
<th align="left">Bits 9:0</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Alpha channel</p></td>
<td align="left"><p>Blue channel</p></td>
<td align="left"><p>Green channel</p></td>
<td align="left"><p>Red channel</p></td>
</tr>
</tbody>
</table>

 

Each of the red, green and blue channels is laid out as shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit 9</th>
<th align="left">Bits 8:0</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1-bit integer part</p></td>
<td align="left"><p>9-bit fractional part</p></td>
</tr>
</tbody>
</table>

 

 

 





