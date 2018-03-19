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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>EngCreatePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564755)</p></td>
<td align="left"><p>Allocates a path for the driver's temporary use. The driver should delete this path before returning to GDI from its current drawing call.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngDeletePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564811)</p></td>
<td align="left"><p>Deletes a path allocated by the <strong>EngCreatePath</strong> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PATHOBJ_bCloseFigure</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568850)</p></td>
<td align="left"><p>Closes a path (for filling) by drawing a line back to the starting point.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PATHOBJ_bEnum</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568851)</p></td>
<td align="left"><p>Retrieves the next [<strong>PATHDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568848) record from a path. Each record describes all or part of a subpath.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PATHOBJ_bEnumClipLines</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568852)</p></td>
<td align="left"><p>Enumerates clipped line segments from a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PATHOBJ_bMoveTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568853)</p></td>
<td align="left"><p>Changes the current position in a [<strong>PATHOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568849)-defined path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PATHOBJ_bPolyBezierTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568854)</p></td>
<td align="left"><p>Draws Bezier curves (cubic splines) in a PATHOBJ-defined path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PATHOBJ_bPolyLineTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568855)</p></td>
<td align="left"><p>Draws lines in a PATHOBJ-defined path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PATHOBJ_vEnumStart</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568856)</p></td>
<td align="left"><p>Notifies a [<strong>PATHOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568849) that the driver will begin calling <strong>PATHOBJ_bEnum</strong> to enumerate the curves in the specified path. This function must be called in case of an enumeration restart.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PATHOBJ_vEnumStartClipLines</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568857)</p></td>
<td align="left"><p>Allows the driver to ask for lines to be clipped against a [<strong>CLIPOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff539417). This is useful when the [<em>clip region</em>](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-clip-region) is more complex than a single rectangle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PATHOBJ_vGetBounds</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568858)</p></td>
<td align="left"><p>Returns a bounding rectangle for the path.</p></td>
</tr>
</tbody>
</table>

 

 

 





