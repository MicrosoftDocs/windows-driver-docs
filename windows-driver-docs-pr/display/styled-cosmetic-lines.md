---
title: Styled Cosmetic Lines
description: Styled Cosmetic Lines
ms.assetid: 07e72190-7c8e-471e-9851-ccc037312c5c
keywords:
- lines WDK GDI , styled cosmetic
- GDI WDK Windows 2000 display , lines, styled cosmetic
- graphics drivers WDK Windows 2000 display , lines, styled cosmetic
- drawing WDK GDI , lines, styled cosmetic
- styled cosmetic lines WDK GDI
- cosmetic lines WDK GDI , styled
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Styled Cosmetic Lines


## <span id="ddk_styled_cosmetic_lines_gg"></span><span id="DDK_STYLED_COSMETIC_LINES_GG"></span>


The [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316) function must support the drawing of cosmetic lines with arbitrary clipping using a solid-color brush. The driver can make a call to the GDI service [**PATHOBJ\_vEnumStartClipLines**](https://msdn.microsoft.com/library/windows/hardware/ff568857) to precompute the clipping.

Styling of a cosmetic line is similar to that of a geometric wide line because it is specified by a repeating array. For a styled cosmetic line, the array entries are LONG values that contain the lengths in style steps. The relation between style steps and pixels is defined by the **xStyleStep**, **yStyleStep**, and **denStyleStep** fields in the [**GDIINFO**](https://msdn.microsoft.com/library/windows/hardware/ff566484) structure returned by the [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) function.

When the driver calls [**PATHOBJ\_bEnumClipLines**](https://msdn.microsoft.com/library/windows/hardware/ff568852), to handle styled cosmetic lines through complex clipping, GDI modifies the value of the [**CLIPLINE**](https://msdn.microsoft.com/library/windows/hardware/ff539416) structure's **iStyleState** member to represent the style state. The style state is the offset back to the first pixel of the line segment; that is, the first pixel that would be rendered if the line were not clipped. The style state consists of two 16-bit values packed into a ULONG value. If HIGH and LOW are the high-order and the low-order 16 bits of the style state, a fractional version of the style state, referred to as style position, can be computed as:

`
    style position = HIGH + LOW/denStyleStep
`

For example, if the values in **iStyleState** are 1 and 2, and **denStyleStep** is 3, then style position is 5/3. To determine exactly where the drawing of the style begins in the style array, take the product:

`
    style position * denStyleStep
`

In this example, with a **denStyleStep** value of 3, the drawing position is calculated to exclude the first five (5/3 \* 3) pixels of the style array. That is, drawing begins at the sixth pixel in the style array of this clipped line.

There are y-styled cosmetic lines and x-styled cosmetic lines. If a line extends dx device units in the x direction and dy units in the y direction, the line is y-styled when the following is true:

`
    (dy * yStyleStep)  >=  (dx * xStyleStep)
`

In this case, the style position is advanced by **yStyleStep**/**denStyleStep** for each pixel advanced in the y direction.

Conversely, a line is x-styled and the style position is advanced by **xStyleStep**/**denStyleStep** for each pixel advanced in the x direction when the following is true:

`
    (dx * xStyleStep)  >  (dy * yStyleStep)
`

When the style position advances to a new integer, the style step advances one unit in the style array.

The following figure shows several cosmetic styled lines having different slopes.

![diagram illustrating styled cosmetic lines](images/102-02.png)

In this illustration, the pixel grid shown is not square, but is shown as it would be for an EGA display in which four pixels in the x direction represent the same distance as three pixels in the y direction. The style steps in the [**GDIINFO**](https://msdn.microsoft.com/library/windows/hardware/ff566484) structure ensure that styled lines appear the same at any slope on displays whose pixels are not square. In this illustration, the styling array (defined by the **pstyle** member of the [**LINEATTRS**](https://msdn.microsoft.com/library/windows/hardware/ff568195) structure) is {1,1}, which is a broken line having equal-sized dots and gaps. The driver's value of **xStyleStep** is 3, **yStyleStep** is 4, and **denStyleStep** is 12.

To illustrate further, suppose a dot matrix printer has a 144-dpi horizontal resolution and a 72-dpi vertical resolution. In addition, suppose the dot length of the minimum dot is 1/24-inch. To support this printer, select the smallest numbers for **xStyleStep** and **yStyleStep** that can compensate for the printer's aspect ratio, such as 1 for **xStyleStep** and 2 (144/72) for **yStyleStep**, and 6 (144/24) for **denStyleStep**.

If the LA\_ALTERNATE bit is set in the flag in the [**LINEATTRS**](https://msdn.microsoft.com/library/windows/hardware/ff568195) structure, a special style is used for a cosmetic line. In this case, every other pixel is on, regardless of direction or aspect ratio. Style state is returned as if the style array is {1,1} and **xStyleStep**, **yStyleStep**, and **denStyleStep** are all one. In other words, if **lStyleState** is zero, the first pixel is on; if **lStyleState** is one, the first pixel is off.

If the LA\_STARTGAP bit is set in the LINEATTRS flag, the sense of the elements in the style array is inverted. The first array entry specifies the length of the first gap, the second entry specifies the length of the first dash, and so forth.

 

 





