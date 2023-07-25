---
title: PCD source file format
description: PCD source file format
keywords:
- Plotter Driver WDK print , minidrivers
- MSPlot WDK print , minidrivers
- minidrivers WDK MSPlot
- PCD files WDK MSPlot
- .pcd files
- keywords WDK MSPlot
ms.date: 07/19/2023
---

# PCD source file format

[!include[Print Support Apps](../includes/print-support-apps.md)]

All plotter device characteristics are specified using the following format:

*keyword* { *value* }

where *keyword* is one of the PCD source file keywords and *value* is a quoted string or numeric value. For example, the following statement specifies that the plotter supports color:

```cpp
ColorCap {1}
```

Keywords are described in the following table.

| Keyword | Value definition | Default value |
|--|--|--|
| **BezierCap** | 1=Device supports HPGL2 Beziers extension.<br><br>0=No support. | 0 |
| **ColorCap** | 1=Color device<br><br>0=Monochrome device | 0 |
| **COLORINFO** | 30 DWORD-sized values representing the contents of a [**COLORINFO**](/windows/win32/api/winddi/ns-winddi-colorinfo) structure | {<br>{6810,3050,0}, // xr, yr, Yr<br>{2260,6550,0}, // xg, yg, Yg<br>{1810,500,0}, // xb, yb, Yb<br>{2000,2450,0}, // xc, yc, Yc<br>{5210,2100,0}, // xm, ym, Ym<br>{4750,5100,0}, // xy, yy, Yy<br>{3324,3474,10000}, // xw, yw, Yw<br>10000,10000,10000, // RGB gamma<br>1422,952, // M/C, Y/C<br>787,495, // C/M, Y/M<br>324,248 // C/Y, M/Y<br>} |
| **DeviceMargin** | Four DWORD-sized values representing the left, top, right, and bottom paper margins, in 1/1000-mm units. | {5000,<br>5000,<br>5000,<br>36000} |
| **DeviceName** | Quoted string representing a displayable device name (31 characters max.) | "HPGL/2 Plotter" |
| **DevicePelsDPI** | One DWORD-sized value representing the device's effective DPI. For more information, see the **upDevicePelsDPI** member of [**GDIINFO**](/windows/win32/api/winddi/ns-winddi-gdiinfo). | The default is zero, causing GDI to calculate a value. |
| **DeviceSize** | Two DWORD-sized values representing maximum paper size, in *x* and *y* coordinates of 1/1000-mm units.<br><br>A *y* value of 25400 (1 inch) or less indicates the device accepts variable paper lengths. | {215900,<br>279400} |
| **FormInfo** | A form description for each form supported by the plotter. For more information, see the **Form Descriptions** section that follows this table. | None. |
| **HTPatternSize** | One of the HT_PATSIZE_-prefixed constants that identify standard halftoning patterns. | 0xffffffff |
| **InitString** | Quoted C-language string representing commands sent to the printer by the driver's [**DrvStartPage**](/windows/win32/api/winddi/nf-winddi-drvstartpage) function. | NULL string. |
| **MaxCopies** | Maximum number of copies per page that the device can render. | 1 |
| **MaxPens** | Number of pens (32 maximum) | 8 |
| **MaxPolygonPts** | Maximum number of points to define a polygon to be stroked or filled. | 128 |
| **MaxQuality** | Number of quality levels (4 maximum) | 4 |
| **MaxScale** | Maximum scale size. 0-10000 (100 is 100%) | 100 |
| **NoBitmapFont** | 1=Device doesn't support bitmap fonts.<br><br>0=Bitmap fonts are supported. | 0 |
| **PaperTrayCap** |1=Device has paper tray source.<br><br>0=No support.  | 0 |
| **PaperTraySize** | Two DWORD-sized values representing the paper tray width and height, in 1/1000-mm units. | {-1, -1} |
| **PlotDPI** | Two DWORD-sized values representing a pen plotter's *x* and *y* resolution, in dots per inch. | {1016, 1016} |
| **PlotPenData** | A pen description for each pen. For more information, see the **Pen Descriptions** section that follows this table. | None. |
| **PushPopPal** | 1=Driver must push/pop palette when switching between RTL and HPGL2.<br><br>0=Push/pop isn't required. | 0 |
| **RasterByteAlign** | 1=Device must receive all raster data on byte-aligned x coordinates.<br><br>0=Byte alignment isn't required. | 0 |
| **RasterCap** | 1=Raster device<br><br>0=Pen device | 0 |
| **RasterDPI** | Two DWORD-sized values representing *x* and *y* resolution, in dots per inch.<br><br>For raster plotters, this is the raster resolution.<br><br>For pen plotters, this is the ideal resolution the GDI supplies to an application. | {300, 300} |
| **RollFeedCap** | 1=Device has roll paper source.<br><br>0=No support. | 0 |
| **ROPLevel** | ROP_LEVEL_0 = No RasterOp support.<br><br>ROP_LEVEL_1 = Rop1 support.<br><br>ROP_LEVEL_2 = Rop2 support.<br><br>ROP_LEVEL_3 = Rop3 support. | ROP_LEVEL_0 |
| **RTLMonoEncode5** | 1=HP Raster Transfer Language (RTL) Monochrome Compression Mode 5 is supported.<br><br>0=No support. | 0 |
| **RTLMonoFixPal** | RTL Monochrome palette only.<br><br>0=White, 1=Black | 0 |
| **RTLMonoNoCID** | 1=In RTL Mono mode, CID commands aren't required.<br><br>0=In RTL Mono mode, CID commands are required. | 0 |
| **RTLNoDPIxy** |1=RTL DPI X,Y move commands aren't supported.<br><br>0=These commands are supported.  | 0 |
| **TransparentCap** | 1=Device supports transparent mode.<br><br>0=No support. | 0 |
| **WindingFillCap** | 1=Device supports winding fills.<br><br>0=No support. | 0 |

## Pen Descriptions

Each pen description must have the following format:

**PlotPenData {***Pen Number***,** *Color***}**

where *Pen Number* identifies the pen's slot number and *Color* is a PC_IDX_-prefixed color identifier. Following are example pen descriptions:

```PCD
PlotPenData {1, PC_IDX_WHITE}
PlotPenData {2, PC_IDX_BLACK}
PlotPenData {3, PC_IDX_RED}
```

## Form Descriptions

Each form description must have the following format:

**FormInfo {"***Form Description***",** *Width***,** *Length***,** *Left Margin***,** *Top Margin***,** *Right Margin***,** *Bottom Margin***}**

where *Form Description* is a string describing the form, *Width* and *Length* specify the form size in 1/1000-mm units, and the margins are also specified in 1/1000-mm units. Following are three examples:

```PCD
FormInfo {"Roll Paper 24 in",    609600,      0, 0, 0, 0, 0}
FormInfo {"ANSI A 8.5 x 11 in",  215900, 279400, 0, 0, 0, 0}
FormInfo {"ISO A4 210 x 297 mm", 210000, 297000, 0, 0, 0, 0}
```
