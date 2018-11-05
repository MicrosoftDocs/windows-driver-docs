---
title: Using GDI 8-Bit-Per-Pixel CMY Mask Modes
description: Using GDI 8-Bit-Per-Pixel CMY Mask Modes
ms.assetid: 0631f292-c1f1-4627-b116-0b54a34ea295
keywords:
- GDI WDK Windows 2000 display , halftoning
- graphics drivers WDK Windows 2000 display , halftoning
- drawing WDK GDI , halftoning
- halftoning WDK GDI
- 8-bit-per-pixel CMY mask modes WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using GDI 8-Bit-Per-Pixel CMY Mask Modes


## <span id="ddk_using_gdi_8_bit_per_pixel_cmy_mask_modes_gg"></span><span id="DDK_USING_GDI_8_BIT_PER_PIXEL_CMY_MASK_MODES_GG"></span>


In Microsoft Windows 2000, the [**HT\_Get8BPPMaskPalette**](https://msdn.microsoft.com/library/windows/hardware/ff567320) function returned 8-bit-per-pixel monochrome or CMY palettes. In Windows XP and later, this function has been modified so that it also returns inverted-index CMY palettes when the *Use8BPPMaskPal* parameter is set to **TRUE**. The type of palette returned depends on the value stored in *pPaletteEntry*\[0\] when **HT\_Get8BPPMaskPalette** is called. If *pPaletteEntry*\[0\] is set to 'RGB0', an inverted-index palette is returned. If *pPaletteEntry*\[0\] is set to 0, a normal CMY palette is returned.

The reason for this change in behavior of **HT\_Get8BPPMaskPalette** is that when Windows GDI uses ROPs, which are based on the indexes in a palette and not on the palette colors, it assumes that index 0 of the palette is always black and that the last index is always white. GDI does not check the palette entries. This change in **HT\_Get8BPPMaskPalette** ensures correct ROP output, instead of a result that is inverted.

To correct the GDI ROP behavior, GDI in Windows XP and later supports a special CMY palette composition format in which the CMY mask palette entries start at index 255 (white) and work down to index 0 (black), instead of starting at index 0 (white) and working up to index 255 (black). The CMY inverted modes also move all CMY mask color entries to the middle of a full 256-entry palette, with the beginning and end of the palette padded with equal numbers of black and white entries.

**Note**   In the discussion that follows, the term *CMY mode* refers to a mode supported in the previous implementation of [**HT\_Get8BPPMaskPalette**](https://msdn.microsoft.com/library/windows/hardware/ff567320). The term *CMY\_INVERTED mode* refers to modes supported only on Windows XP and later GDI, in which this function inverts bitmask indexes when *pPaletteEntry*\[0\] is set to 'RGB0'.

 

The following steps are required for all Windows XP and later drivers that use Windows GDI halftone 8-bit-per-pixel CMY mask modes. If you are developing a driver for Windows 2000, you should limit the driver's use to 8-bit-per-pixel monochrome palettes.

1.  Set the **flHTFlags** member of the [**GDIINFO**](https://msdn.microsoft.com/library/windows/hardware/ff566484) structure to HT\_FLAG\_INVERT\_8BPP\_BITMASK\_IDX so that GDI will render images in one of the CMY\_INVERTED modes.

2.  Set *pPaletteEntry*\[0\] as follows prior to a call to **HT\_Get8BPPMaskPalette**:

    ```cpp
    pPaletteEntry[0].peRed   = &#39;R&#39;;
    pPaletteEntry[0].peGreen = &#39;G&#39;;
    pPaletteEntry[0].peBlue  = &#39;B&#39;;
    pPaletteEntry[0].peFlags = &#39;0&#39;;
    ```

    To do this, a caller should use the **HT\_SET\_BITMASKPAL2RGB** macro (defined in *winddi.h*). Here is an example showing the use of this macro:

    ```cpp
    HT_SET_BITMASKPAL2RGB(pPaletteEntry)
    ```

    Here *pPaletteEntry* is the pointer to the PALETTEENTRY that was passed in the call to the **HT\_Get8BPPMaskPalette** function. When this macro completes execution, *pPaletteEntry*\[0\] will contain the string 'RGB0'.

3.  Check the *pPaletteEntry* parameter returned from the call to [**HT\_Get8BPPMaskPalette**](https://msdn.microsoft.com/library/windows/hardware/ff567320) using the **HT\_IS\_BITMASKPALRGB** macro, which is defined in *winddi.h*. Here is an example showing the use of this macro.

    ```cpp
    InvCMYSupported = HT_IS_BITMASKPALRGB(pPaletteEntry)
    ```

    In this expression, *pPaletteEntry* is the pointer to the PALETTEENTRY that was passed to the **HT\_Get8BPPMaskPalette** function. If this macro returns **TRUE**, then GDI *does* support the inverted CMY 8-bit-per-pixel bitmask modes. The caller must use a translation table to convert the palette indexes to ink levels. See [Translating 8-Bit-Per-Pixel Halftone Indexes to Ink Levels](translating-8-bit-per-pixel-halftone-indexes-to-ink-levels.md) for an example of a function that generates this translation table.

    If this macro returns **FALSE**, then the current version of GDI *does not* support the inverted CMY 8-bit-per-pixel bitmask modes. In that case, GDI supports only the older CMY noninverted modes.

For GDI versions that support the 8-bit-per-pixel CMY\_INVERTED modes, the meaning of the *CMYMask* parameter value passed to the [**HT\_Get8BPPMaskPalette**](https://msdn.microsoft.com/library/windows/hardware/ff567320) function has been changed. The following table summarizes the changes:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">CMYMask
<div>
 
</div>
Value</th>
<th align="left">CMY Mode Indexes
<div>
 
</div>
(pPaletteEntry[0] != &#39;RGB0&#39;)</th>
<th align="left">CMY_INVERTED Mode Indexes
<div>
 
</div>
(pPaletteEntry[0] == &#39;RGB0&#39;)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>0: White</p>
<div>
 
</div>
1 to 254: Light Gray --&gt; Dark Gray
<div>
 
</div>
255: Black</td>
<td align="left"><p>0 - Black</p>
<div>
 
</div>
1 to 254: Dark Gray --&gt; Light Gray
<div>
 
</div>
255: White</td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>0: White</p>
<div>
 
</div>
1 to 123: 123 5x5x5 colors
<div>
 
</div>
124 to 255: Black</td>
<td align="left"><p>0 to 65: Black</p>
<div>
 
</div>
66 to 189: 123 5x5x5 colors plus one duplicate. The entry at index 127 is copied to index 128.
<div>
 
</div>
190 to 255: White
<div>
 
</div>
<div>
 
</div>
The values at indexes 127 and 128 are duplicated to ensure that the XOR ROP works correctly.</td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>0: White</p>
<div>
 
</div>
1 to 214: 214 6x6x6 colors
<div>
 
</div>
215 to 255: Black</td>
<td align="left"><p>0 to 20: Black</p>
<div>
 
</div>
21 to 234: 214 6x6x6 colors
<div>
 
</div>
235 to 255: White</td>
</tr>
<tr class="even">
<td align="left"><p>3 to 255</p></td>
<td align="left"><p>0: White</p>
<div>
 
</div>
1 to 254: CxMxY color bitmask
<div>
 
</div>
255: Black
<div>
 
</div>
<div>
 
</div>
In the product above, C, M, and Y represent the number of levels of cyan, magenta, and yellow, respectively.
<div>
 
</div>
<div>
 
</div>
<strong>Note</strong>: For these modes, a valid combination must not have any of the cyan, magenta, or yellow ink levels equal to zero. For such a combination, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567320" data-raw-source="[&lt;strong&gt;HT_Get8BPPMaskPalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567320)"><strong>HT_Get8BPPMaskPalette</strong></a> indicates an error condition by returning a zero-count palette in its <em>pPaletteEntry</em> parameter.</td>
<td align="left"><p>0: Black</p>
<div>
 
</div>
1 to 254: Centered CxMxY colors padded with black at the beginning and white at the end
<div>
 
</div>
If CxMxY is an odd number, then the entry at index 128 is a duplicate of the one at index 127.
<div>
 
</div>
255: White
<div>
 
</div>
<div>
 
</div>
In the product above, C, M, and Y represent the number of levels of cyan, magenta, and yellow, respectively.
<div>
 
</div>
<div>
 
</div>
<strong>Note:</strong> The (C x M x Y) indexes are centered in the 256-entry palette. That is, there are equal numbers of black entries padding the low end of the palette and white entries padding the high end.
<div>
 
</div>
<div>
 
</div>
<strong>Note</strong>: For these modes, a valid combination must not have any of the cyan, magenta, or yellow ink levels equal to zero. For such a combination, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567320" data-raw-source="[&lt;strong&gt;HT_Get8BPPMaskPalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567320)"><strong>HT_Get8BPPMaskPalette</strong></a> indicates an error condition by returning a zero-count palette in its <em>pPaletteEntry</em> parameter.</td>
</tr>
</tbody>
</table>

 

-   For a value of *CMYMask* of 0 (Gray scale), the caller can process either the CMY mode or the CMY\_INVERTED mode. Note, however, that GDI ROPs are correctly processed only in the CMY\_INVERTED mode.

    CMY Mode: Indexes 0 to 255 represent a gray scale from white to black.

    CMY\_INVERTED Mode: Indexes 0 to 255 represent a gray scale ranging from black to white.

-   For any valid value of *CMYMask* from 1 to 255, the caller should use the example function shown in [Translating 8-Bit-Per-Pixel Halftone Indexes to Ink Levels](translating-8-bit-per-pixel-halftone-indexes-to-ink-levels.md) to translate indexes to ink levels.

-   For any valid value of *CMYMask* from 1 to 255, the CMY\_INVERTED modes pad the palettes with black entries at the beginning of the array, and an equal number of white entries at the end of the array. The middle of the array is filled with the other colors. This ensures that all 256 of the color palette entries are symmetrically distributed so that GDI ROPs, which are index-based, not color-based, work correctly. The colors are symmetrically distributed when the color at index *N* is the inverse of the color at index (256 - *N*). When a color and its inverse are printed together, the result is black. In other words, for a given color and its inverse, the two cyan ink levels add to the maximum cyan ink level, as do the two magenta ink levels, and the two yellow ink levels. The resulting ink levels correspond to black.

    For example; a CMY palette with three levels each of cyan, magenta, and yellow has a total of 27 (3 x 3 x 3) indexes for colors, including black and white. Because 27 is an odd number, and because GDI requires that a CMY\_INVERTED mode palette be padded with equal numbers of black and white entries, GDI duplicates the entry at the middle index (index 13 of the 27 colors). With the entries at indexes 13 and 14 now the same, palette will now have 28 colors. To fill the palette, GDI places 114 black entries at the beginning of the palette (indexes 0 to 113), places the 28 colors at indexes 114 (black) through 141 (white), and fills the remaining 114 entries with white (indexes 142 through 255). This makes a total of 256 entries (114 + 28 + 114 = 256 entries). This layout of the indexes ensures that all ROPs will be correctly rendered. The example function in [Translating 8-Bit-Per-Pixel Halftone Indexes to Ink Levels](translating-8-bit-per-pixel-halftone-indexes-to-ink-levels.md) shows how to generate the ink levels as well as a Windows 2000 CMY332 index translation table.

    The following table lists the cyan, magenta, and yellow levels for the 3 x 3 x 3 palette discussed in the previous paragraph. The 28 colors (27 original palette colors plus one duplicate) are embedded in the middle of the 256-color palette, with equal amounts of black padding at the beginning and white padding at the end. The palette is symmetric, meaning that if the ink levels at index *N* are added to those at index (256 - *N*), the result will be black (cyan, magenta, and yellow levels = 2).

    <table>
    <colgroup>
    <col width="25%" />
    <col width="25%" />
    <col width="25%" />
    <col width="25%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Palette Index(3x3x3 Index)</th>
    <th align="left">Cyan Level0 to 2</th>
    <th align="left">Magenta Level0 to 2</th>
    <th align="left">Yellow Level0 to 2</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>0 to 113</p>
    <div>
     
    </div>
    Black</td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>114 (0)</p>
    <p>Black</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>115 (1)</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>116 (2)</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>117 (3)</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>118 (4)</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>119 (5)</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>120 (6)</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>121 (7)</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>122 (8)</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>123 (9)</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>124 (10)</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>125 (11)</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>126 (12)</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>127 (13)</p>
    <p>Copied to index 128</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>128 (14)</p>
    <p>Duplicate of entry at index 127</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>129 (15)</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>130 (16)</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>131 (17)</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>132 (18)</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>133 (19)</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>134 (20)</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>135 (21)</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>2</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>136 (22)</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>137 (23)</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>138 (24)</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>1</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>139 (25)</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>2</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>140 (26)</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>1</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>141 (27)</p>
    <p>White</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>142 to 255</p>
    <p>White</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>0</p></td>
    <td align="left"><p>0</p></td>
    </tr>
    </tbody>
    </table>

     

<!-- -->

-   If the requested palette is a CMY mode palette (not a CMY\_INVERTED mode palette), then for values of *CMYMask* from 3 to 255, the rendered 8-bit-per-pixel byte index bits have the following meaning. In this case, the bit patterns represent ink levels that can be used directly without translation. This also applies when a CMY\_INVERTED mode byte index is mapped to CMY mode using a translation table's **CMY332Idx** member. See [Translating 8-Bit-Per-Pixel Halftone Indexes to Ink Levels](translating-8-bit-per-pixel-halftone-indexes-to-ink-levels.md) for more information.

```cpp
  Bit     7 6 5 4 3 2 1 0
          |   | |   | | |
          +---+ +---+ +-+
            |     |    |
            |     |    +-- Yellow 0-3 (Max. 4 levels)
            |     |
            |     +-- Magenta 0-7 (Max. 8 levels)
            |
            +-- Cyan 0-7 (Max. 8 levels)
```

 

 





