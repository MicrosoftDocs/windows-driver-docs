---
title: Styled Cosmetic Lines
description: Styled Cosmetic Lines
keywords:
- lines WDK GDI , styled cosmetic
- GDI WDK Windows 2000 display , lines, styled cosmetic
- graphics drivers WDK Windows 2000 display , lines, styled cosmetic
- drawing WDK GDI , lines, styled cosmetic
- styled cosmetic lines WDK GDI
- cosmetic lines WDK GDI , styled
ms.date: 04/20/2017
---

# Styled Cosmetic Lines

The [**DrvStrokePath**](/windows/win32/api/winddi/nf-winddi-drvstrokepath) function must support the drawing of cosmetic lines with arbitrary clipping using a solid-color brush. The driver can make a call to the GDI service [**PATHOBJ_vEnumStartClipLines**](/windows/win32/api/winddi/nf-winddi-pathobj_venumstartcliplines) to precompute the clipping.

Styling of a cosmetic line is similar to that of a geometric wide line because it is specified by a repeating array. For a styled cosmetic line, the array entries are LONG values that contain the lengths in style steps. The relation between style steps and pixels is defined by the **xStyleStep**, **yStyleStep**, and **denStyleStep** fields in the [**GDIINFO**](/windows/win32/api/winddi/ns-winddi-gdiinfo) structure returned by the [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function.

When the driver calls [**PATHOBJ_bEnumClipLines**](/windows/win32/api/winddi/nf-winddi-pathobj_benumcliplines), to handle styled cosmetic lines through complex clipping, GDI modifies the value of the [**CLIPLINE**](/windows/win32/api/winddi/ns-winddi-clipline) structure's **iStyleState** member to represent the style state. The style state is the offset back to the first pixel of the line segment; that is, the first pixel that would be rendered if the line were not clipped. The style state consists of two 16-bit values packed into a ULONG value. If HIGH and LOW are the high-order and the low-order 16 bits of the style state, a fractional version of the style state, referred to as style position, can be computed as:

```style position = HIGH + LOW/denStyleStep```

For example, if the values in **iStyleState** are 1 and 2, and **denStyleStep** is 3, then style position is 5/3. To determine exactly where the drawing of the style begins in the style array, take the product:

```style position * denStyleStep```

In this example, with a **denStyleStep** value of 3, the drawing position is calculated to exclude the first five (5/3 \* 3) pixels of the style array. That is, drawing begins at the sixth pixel in the style array of this clipped line.

There are y-styled cosmetic lines and x-styled cosmetic lines. If a line extends dx device units in the x direction and dy units in the y direction, the line is y-styled when the following is true:

```(dy * yStyleStep)  >=  (dx * xStyleStep)```

In this case, the style position is advanced by **yStyleStep**/**denStyleStep** for each pixel advanced in the y direction.

Conversely, a line is x-styled and the style position is advanced by **xStyleStep**/**denStyleStep** for each pixel advanced in the x direction when the following is true:

```(dx * xStyleStep)  >  (dy * yStyleStep)```

When the style position advances to a new integer, the style step advances one unit in the style array.

The following figure shows several cosmetic styled lines having different slopes.

:::image type="content" source="images/102-02.png" alt-text="Diagram showing various styled cosmetic lines with different slopes on a non-square pixel grid.":::

In this illustration, the pixel grid shown is not square, but is shown as it would be for an EGA display in which four pixels in the x direction represent the same distance as three pixels in the y direction. The style steps in the [**GDIINFO**](/windows/win32/api/winddi/ns-winddi-gdiinfo) structure ensure that styled lines appear the same at any slope on displays whose pixels are not square. In this illustration, the styling array (defined by the **pstyle** member of the [**LINEATTRS**](/windows/win32/api/winddi/ns-winddi-lineattrs) structure) is {1,1}, which is a broken line having equal-sized dots and gaps. The driver's value of **xStyleStep** is 3, **yStyleStep** is 4, and **denStyleStep** is 12.

To illustrate further, suppose a dot matrix printer has a 144-dpi horizontal resolution and a 72-dpi vertical resolution. In addition, suppose the dot length of the minimum dot is 1/24-inch. To support this printer, select the smallest numbers for **xStyleStep** and **yStyleStep** that can compensate for the printer's aspect ratio, such as 1 for **xStyleStep** and 2 (144/72) for **yStyleStep**, and 6 (144/24) for **denStyleStep**.

If the LA_ALTERNATE bit is set in the flag in the [**LINEATTRS**](/windows/win32/api/winddi/ns-winddi-lineattrs) structure, a special style is used for a cosmetic line. In this case, every other pixel is on, regardless of direction or aspect ratio. Style state is returned as if the style array is {1,1} and **xStyleStep**, **yStyleStep**, and **denStyleStep** are all one. In other words, if **lStyleState** is zero, the first pixel is on; if **lStyleState** is one, the first pixel is off.

If the LA_STARTGAP bit is set in the LINEATTRS flag, the sense of the elements in the style array is inverted. The first array entry specifies the length of the first gap, the second entry specifies the length of the first dash, and so forth.
