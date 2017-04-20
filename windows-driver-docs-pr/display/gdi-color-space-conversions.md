---
title: GDI Color Space Conversions
description: GDI Color Space Conversions
ms.assetid: f1840d58-9f93-4aa3-8344-d5e61c176254
keywords:
- surface negotiation WDK GDI , color space conversions
- color channels WDK GDI
- color space conversions WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI Color Space Conversions


## <span id="ddk_gdi_color_space_conversions_gg"></span><span id="DDK_GDI_COLOR_SPACE_CONVERSIONS_GG"></span>


GDI uses three RGB color spaces for its bitmap representations. In each of these color spaces, three bitfields, or *color channels*, are used to specify the number of bits used for red, green, and blue, respectively, in a given color. To be able to match GDI's capabilities with bitmaps, video drivers must be able to convert from one RGB color space to another.

GDI recognizes the following RGB color spaces:

-   5:5:5 RGB: five-bit color channels for red, green, and blue

-   5:6:5 RGB: a five-bit color channel for red, a six-bit color channel for green, and a five-bit color channel for blue

-   8:8:8 RGB: eight-bit color channels for red, green, and blue

In general, when converting from a color channel with more bits to one with fewer bits, GDI discards the lower-order bits. When the conversion goes from a color channel with fewer bits to one with more bits, all of the bits of the smaller channel are copied to the larger channel. To fill out the remaining bits of the larger channel, some of the bits of the smaller channel are copied again to the larger channel. The following table summarizes the rules that GDI uses to convert from one RGB color space to another. In this table, color channels whose values change in the conversion are shown in **bold** font style.

### <span id="GDI_Color_Space_Conversion_Rules"></span><span id="gdi_color_space_conversion_rules"></span><span id="GDI_COLOR_SPACE_CONVERSION_RULES"></span>GDI Color Space Conversion Rules

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">From</th>
<th align="left">To</th>
<th align="left">Rule</th>
<th align="left">Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>5:5:5</p></td>
<td align="left"><p>5:6:5</p></td>
<td align="left"><p>The most-significant bit (MSB) of the source's green channel is appended to the low-order end of the target's green channel.</p></td>
<td align="left"><p>(0x15, <strong>0x19</strong>, 0x1D) becomes</p>
<div>
 
</div>
(0x15, <strong>0x33</strong>, 0x1D)
<div>
 
</div>
Note that only the green channel changes. The 5-bit channel value of the source is 1 1001, in binary, which is converted to a 6-bit value, 11 0011.</td>
</tr>
<tr class="even">
<td align="left"><p>5:5:5</p></td>
<td align="left"><p>8:8:8</p></td>
<td align="left"><p>For each channel, the three MSBs of the source channel are appended to the lower-order end of the target channel.</p></td>
<td align="left"><p>(<strong>0x15</strong>, <strong>0x19</strong>, <strong>0x1D</strong>) becomes</p>
<div>
 
</div>
(<strong>0xAD</strong>, <strong>0xCE</strong>, <strong>0xEF</strong>)
<div>
 
</div>
In the red channel, 1 0101 becomes 1010 1101. Similar changes occur in the green and blue channels.</td>
</tr>
<tr class="odd">
<td align="left"><p>5:6:5</p></td>
<td align="left"><p>5:5:5</p></td>
<td align="left"><p>Discard the least-significant bit (LSB) of the source's green channel.</p></td>
<td align="left"><p>(0x15, <strong>0x33</strong>, 0x1D) becomes</p>
<div>
 
</div>
(0x15, <strong>0x19</strong>, 0x1D)
<div>
 
</div>
Note that only the green channel changes. Discard the lowest bit
<div>
 
</div>
of 11 0011 to get 1 1001.</td>
</tr>
<tr class="even">
<td align="left"><p>5:6:5</p></td>
<td align="left"><p>8:8:8</p></td>
<td align="left"><p>For the 5-bit (red and blue) channels of the source, copy the three MSBs from the source and append them to the lower-order end of the target. For the 6-bit green channel, copy the two MSBs from the source and append them to the lower-order end of the target.</p></td>
<td align="left"><p>(<strong>0x15</strong>, <strong>0x33</strong>, <strong>0x1D</strong>) becomes</p>
<div>
 
</div>
(<strong>0xAD</strong>, <strong>0xCF</strong>, <strong>0xEF</strong>)
<div>
 
</div>
In the red channel, 1 0101 becomes 1010 1101. In the green channel,11 0011 becomes
<div>
 
</div>
1100 1111. The transformation in the blue channel is similar to that of the red channel.</td>
</tr>
<tr class="odd">
<td align="left"><p>8:8:8</p></td>
<td align="left"><p>5:5:5</p></td>
<td align="left"><p>Discard the three LSBs from each channel of the source.</p></td>
<td align="left"><p>(<strong>0xAB</strong>, <strong>0xCD</strong>, <strong>0xEF</strong>) becomes</p>
<div>
 
</div>
(<strong>0x15</strong>, <strong>0x19</strong>, <strong>0x1D</strong>)
<div>
 
</div>
In the red channel, 1010 1011 becomes 1 0101. Similar transformations occur in the other two channels.</td>
</tr>
<tr class="even">
<td align="left"><p>8:8:8</p></td>
<td align="left"><p>5:6:5</p></td>
<td align="left"><p>Discard the three LSBs from the red and blue channels. Discard the two LSBs from the green channel.</p></td>
<td align="left"><p>(<strong>0xAB</strong>, <strong>0xCD</strong>, <strong>0xEF</strong>) becomes</p>
<div>
 
</div>
(<strong>0x15</strong>, <strong>0x33</strong>, <strong>0x1D</strong>)
<div>
 
</div>
In the green channel, 1100 1101 becomes 11 0011. The changes in the red and blue channels are identical to those of the previously-listed transformation.</td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Color%20Space%20Conversions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




