---
title: PCD Source File Format
description: PCD Source File Format
ms.assetid: 8651d6ca-7cd7-4c07-aa66-2766dd2222e0
keywords:
- Plotter Driver WDK print , minidrivers
- MSPlot WDK print , minidrivers
- minidrivers WDK MSPlot
- PCD files WDK MSPlot
- .pcd files
- keywords WDK MSPlot
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PCD Source File Format





All plotter device characteristics are specified using the following format:

*keyword* { *value* }

where *keyword* is one of the PCD source file keywords and *value* is a quoted string or numeric value. For example, the following statement specifies that the plotter supports color:

```cpp
ColorCap {1}
```

Keywords are described in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyword</th>
<th>Value Definition</th>
<th>Default Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>BezierCap</strong></p></td>
<td><p>1=Device supports HPGL2 Beziers extension.</p>
<p>0=No support.</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><strong>ColorCap</strong></p></td>
<td><p>1=Color device</p>
<p>0=Monochrome device</p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><strong>COLORINFO</strong></p></td>
<td><p>Thirty DWORD-sized values representing the contents of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539441" data-raw-source="[&lt;strong&gt;COLORINFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff539441)"><strong>COLORINFO</strong></a> structure.</p></td>
<td><p></p>
{
{6810,3050,0}, // xr, yr, Yr
{2260,6550,0}, // xg, yg, Yg
{1810,500,0}, // xb, yb, Yb
{2000,2450,0}, // xc, yc, Yc
{5210,2100,0}, // xm, ym, Ym
{4750,5100,0}, // xy, yy, Yy
{3324,3474,10000}, // xw, yw, Yw
10000,10000,10000, // RGB gamma
1422,952, // M/C, Y/C
787,495, // C/M, Y/M
324,248 // C/Y, M/Y
}</td>
</tr>
<tr class="even">
<td><p><strong>DeviceMargin</strong></p></td>
<td><p>Four DWORD-sized values representing the left, top, right, and bottom paper margins, in 1/1000 mm units.</p></td>
<td><p></p>
{5000,
5000,
5000,
36000}</td>
</tr>
<tr class="odd">
<td><p><strong>DeviceName</strong></p></td>
<td><p>Quoted string representing a displayable device name (31 characters max.)</p></td>
<td><p>&quot;HPGL/2 Plotter&quot;</p></td>
</tr>
<tr class="even">
<td><p><strong>DevicePelsDPI</strong></p></td>
<td><p>One DWORD-sized value representing the device&#39;s effective DPI. For more information see the <strong>upDevicePelsDPI</strong> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff566484" data-raw-source="[&lt;strong&gt;GDIINFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566484)"><strong>GDIINFO</strong></a>.</p></td>
<td><p>The default is zero, causing GDI to calculate a value.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceSize</strong></p></td>
<td><p>Two DWORD-sized values representing maximum paper size, in <em>x</em> and <em>y</em> coordinates of 1/1000 mm units.</p>
<p>A <em>y</em> value of 25400 (1 inch) or less indicates the device accepts variable paper lengths.</p></td>
<td><p></p>
{215900,
279400}</td>
</tr>
<tr class="even">
<td><p><strong>FormInfo</strong></p></td>
<td><p>A form description for each form supported by the plotter. For more information, see the <strong>Form Descriptions</strong> section that follows this Table.</p></td>
<td><p>None.</p></td>
</tr>
<tr class="odd">
<td><p><strong>HTPatternSize</strong></p></td>
<td><p>One of the HT_PATSIZE_-prefixed constants that identify standard halftoning patterns.</p></td>
<td><p>0xffffffff</p></td>
</tr>
<tr class="even">
<td><p><strong>InitString</strong></p></td>
<td><p>Quoted C-language string representing commands sent to the printer by the driver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff556298" data-raw-source="[&lt;strong&gt;DrvStartPage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556298)"><strong>DrvStartPage</strong></a> function.</p></td>
<td><p>NULL string.</p></td>
</tr>
<tr class="odd">
<td><p><strong>MaxCopies</strong></p></td>
<td><p>Maximum number of copies per page that the device can render.</p></td>
<td><p>1</p></td>
</tr>
<tr class="even">
<td><p><strong>MaxPens</strong></p></td>
<td><p>Number of pens (32 max.)</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p><strong>MaxPolygonPts</strong></p></td>
<td><p>Maximum number of points to define a polygon to be stroked or filled.</p></td>
<td><p>128</p></td>
</tr>
<tr class="even">
<td><p><strong>MaxQuality</strong></p></td>
<td><p>Number of quality levels (4 max.)</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p><strong>MaxScale</strong></p></td>
<td><p>Maximum scale size. 0-10000 (100 is 100%)</p></td>
<td><p>100</p></td>
</tr>
<tr class="even">
<td><p><strong>NoBitmapFont</strong></p></td>
<td><p>1=Device does not support bitmap fonts.</p>
<p>0=Bitmap fonts are supported.</p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><strong>PaperTrayCap</strong></p></td>
<td><p>1=Device has paper tray source.</p>
<p>0=No support.</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><strong>PaperTraySize</strong></p></td>
<td><p>Two DWORD-sized values representing the paper tray width and height, in 1/1000 mm units.</p></td>
<td><p></p>
{-1,
-1}</td>
</tr>
<tr class="odd">
<td><p><strong>PlotDPI</strong></p></td>
<td><p>Two DWORD-sized values representing a pen plotter&#39;s <em>x</em> and <em>y</em> resolution, in dots per inch.</p></td>
<td><p></p>
{1016,
1016}</td>
</tr>
<tr class="even">
<td><p><strong>PlotPenData</strong></p></td>
<td><p>A pen description for each pen. For more information, see the <strong>Pen Descriptions</strong> section that follows this Table.</p></td>
<td><p>None.</p></td>
</tr>
<tr class="odd">
<td><p><strong>PushPopPal</strong></p></td>
<td><p>1=Driver must push/pop palette when switching between RTL and HPGL2.</p>
<p>0=Push/pop is not required.</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><strong>RasterByteAlign</strong></p></td>
<td><p>1=Device must receive all raster data on byte-aligned x coordinates.</p>
<p>0=Byte alignment is not required.</p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><strong>RasterCap</strong></p></td>
<td><p>1=Raster device</p>
<p>0=Pen device</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><strong>RasterDPI</strong></p></td>
<td><p>Two DWORD-sized values representing <em>x</em> and <em>y</em> resolution, in dots per inch.</p>
<p>For raster plotters, this is the raster resolution.</p>
<p>For pen plotters, this is the ideal resolution the GDI supplies to an application.</p></td>
<td><p></p>
{300,
300}</td>
</tr>
<tr class="odd">
<td><p><strong>RollFeedCap</strong></p></td>
<td><p>1=Device has roll paper source.</p>
<p>0=No support.</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><strong>ROPLevel</strong></p></td>
<td><p>ROP_LEVEL_0 = No RasterOp support.</p>
<p>ROP_LEVEL_1 = Rop1 support.</p>
<p>ROP_LEVEL_2 = Rop2 support.</p>
<p>ROP_LEVEL_3 = Rop3 support.</p></td>
<td><p>ROP_LEVEL_0</p></td>
</tr>
<tr class="odd">
<td><p><strong>RTLMonoEncode5</strong></p></td>
<td><p>1=HP Raster Transfer Language (RTL) Monochrome Compression Mode 5 is supported.</p>
<p>0=No support.</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><strong>RTLMonoFixPal</strong></p></td>
<td><p>RTL Monochrome palette only.</p>
<p>0=White, 1=Black</p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><strong>RTLMonoNoCID</strong></p></td>
<td><p>1=In RTL Mono mode, CID commands are not required.</p>
<p>0=In RTL Mono mode, CID commands are required.</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><strong>RTLNoDPIxy</strong></p></td>
<td><p>1=RTL DPI X,Y move commands are not supported.</p>
<p>0=These commands are supported.</p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><strong>TransparentCap</strong></p></td>
<td><p>1=Device supports transparent mode.</p>
<p>0=No support.</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><strong>WindingFillCap</strong></p></td>
<td><p>1=Device supports winding fills.</p>
<p>0=No support.</p></td>
<td><p>0</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-pen-descriptions-gg"></a>Pen Descriptions

Each pen description must have the following format:

**PlotPenData {**<em>Pen Number</em>**,** <em>Color</em>**}**

where *Pen Number* identifies the pen's slot number and *Color* is a PC\_IDX\_-prefixed color identifier. Following are example pen descriptions:

```cpp
PlotPenData {1, PC_IDX_WHITE}
PlotPenData {2, PC_IDX_BLACK}
PlotPenData {3, PC_IDX_RED}
```

### <a href="" id="ddk-form-descriptions-gg"></a>Form Descriptions

Each form description must have the following format:

**FormInfo {"**<em>Form Description</em>**",** <em>Width</em>**,** <em>Length</em>**,** <em>Left Margin</em>**,** <em>Top Margin</em>**,** <em>Right Margin</em>**,** <em>Bottom Margin</em>**}**

where *Form Description* is a string describing the form, *Width* and *Length* specify the form size in 1/1000 mm units, and the margins are also specified in 1/1000 mm units. Following are three examples:

```cpp
FormInfo {"Roll Paper 24 in",    609600,      0, 0, 0, 0, 0}
FormInfo {"ANSI A 8.5 x 11 in",  215900, 279400, 0, 0, 0, 0}
FormInfo {"ISO A4 210 x 297 mm", 210000, 297000, 0, 0, 0, 0}
```

 

 




