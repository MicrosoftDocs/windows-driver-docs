---
title: GDI Services for Paths
description: GDI Services for Paths
ms.assetid: 8fc51b7e-d787-48ed-a865-528547abefc5
keywords:
- GDI WDK Windows 2000 display , paths
- graphics drivers WDK Windows 2000 display , paths
- drawing WDK GDI , paths
- paths WDK GDI
- filling paths WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Services for Paths


## <span id="ddk_gdi_services_for_paths_gg"></span><span id="DDK_GDI_SERVICES_FOR_PATHS_GG"></span>


To assist vector devices in filling complex areas, their drivers can call the engine functions, listed in the following table, that create, modify, and enumerate a path. The driver has access to paths through the [**PATHOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff568849) structure.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">GDI Path Service Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564755" data-raw-source="[&lt;strong&gt;EngCreatePath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564755)"><strong>EngCreatePath</strong></a></p></td>
<td align="left"><p>Allocates a path for the driver&#39;s temporary use. The driver should delete this path before returning to GDI from its current drawing call.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564811" data-raw-source="[&lt;strong&gt;EngDeletePath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564811)"><strong>EngDeletePath</strong></a></p></td>
<td align="left"><p>Deletes a path allocated by the <strong>EngCreatePath</strong> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568850" data-raw-source="[&lt;strong&gt;PATHOBJ_bCloseFigure&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568850)"><strong>PATHOBJ_bCloseFigure</strong></a></p></td>
<td align="left"><p>Closes a path (for filling) by drawing a line back to the starting point.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568851" data-raw-source="[&lt;strong&gt;PATHOBJ_bEnum&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568851)"><strong>PATHOBJ_bEnum</strong></a></p></td>
<td align="left"><p>Retrieves the next <a href="https://msdn.microsoft.com/library/windows/hardware/ff568848" data-raw-source="[&lt;strong&gt;PATHDATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568848)"><strong>PATHDATA</strong></a> record from a path. Each record describes all or part of a subpath.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568852" data-raw-source="[&lt;strong&gt;PATHOBJ_bEnumClipLines&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568852)"><strong>PATHOBJ_bEnumClipLines</strong></a></p></td>
<td align="left"><p>Enumerates clipped line segments from a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568853" data-raw-source="[&lt;strong&gt;PATHOBJ_bMoveTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568853)"><strong>PATHOBJ_bMoveTo</strong></a></p></td>
<td align="left"><p>Changes the current position in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568849" data-raw-source="[&lt;strong&gt;PATHOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568849)"><strong>PATHOBJ</strong></a>-defined path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568854" data-raw-source="[&lt;strong&gt;PATHOBJ_bPolyBezierTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568854)"><strong>PATHOBJ_bPolyBezierTo</strong></a></p></td>
<td align="left"><p>Draws Bezier curves (cubic splines) in a PATHOBJ-defined path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568855" data-raw-source="[&lt;strong&gt;PATHOBJ_bPolyLineTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568855)"><strong>PATHOBJ_bPolyLineTo</strong></a></p></td>
<td align="left"><p>Draws lines in a PATHOBJ-defined path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568856" data-raw-source="[&lt;strong&gt;PATHOBJ_vEnumStart&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568856)"><strong>PATHOBJ_vEnumStart</strong></a></p></td>
<td align="left"><p>Notifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568849" data-raw-source="[&lt;strong&gt;PATHOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568849)"><strong>PATHOBJ</strong></a> that the driver will begin calling <strong>PATHOBJ_bEnum</strong> to enumerate the curves in the specified path. This function must be called in case of an enumeration restart.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568857" data-raw-source="[&lt;strong&gt;PATHOBJ_vEnumStartClipLines&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568857)"><strong>PATHOBJ_vEnumStartClipLines</strong></a></p></td>
<td align="left"><p>Allows the driver to ask for lines to be clipped against a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539417" data-raw-source="[&lt;strong&gt;CLIPOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff539417)"><strong>CLIPOBJ</strong></a>. This is useful when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-clip-region" data-raw-source="[&lt;em&gt;clip region&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-clip-region)"><em>clip region</em></a> is more complex than a single rectangle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568858" data-raw-source="[&lt;strong&gt;PATHOBJ_vGetBounds&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568858)"><strong>PATHOBJ_vGetBounds</strong></a></p></td>
<td align="left"><p>Returns a bounding rectangle for the path.</p></td>
</tr>
</tbody>
</table>

 

 

 





