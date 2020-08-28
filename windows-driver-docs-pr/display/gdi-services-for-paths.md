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


To assist vector devices in filling complex areas, their drivers can call the engine functions, listed in the following table, that create, modify, and enumerate a path. The driver has access to paths through the [**PATHOBJ**](/windows/desktop/api/winddi/ns-winddi-_pathobj) structure.

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
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-engcreatepath" data-raw-source="[&lt;strong&gt;EngCreatePath&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-engcreatepath)"><strong>EngCreatePath</strong></a></p></td>
<td align="left"><p>Allocates a path for the driver's temporary use. The driver should delete this path before returning to GDI from its current drawing call.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-engdeletepath" data-raw-source="[&lt;strong&gt;EngDeletePath&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-engdeletepath)"><strong>EngDeletePath</strong></a></p></td>
<td align="left"><p>Deletes a path allocated by the <strong>EngCreatePath</strong> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_bclosefigure" data-raw-source="[&lt;strong&gt;PATHOBJ_bCloseFigure&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_bclosefigure)"><strong>PATHOBJ_bCloseFigure</strong></a></p></td>
<td align="left"><p>Closes a path (for filling) by drawing a line back to the starting point.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_benum" data-raw-source="[&lt;strong&gt;PATHOBJ_bEnum&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_benum)"><strong>PATHOBJ_bEnum</strong></a></p></td>
<td align="left"><p>Retrieves the next <a href="https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-_pathdata" data-raw-source="[&lt;strong&gt;PATHDATA&lt;/strong&gt;](/windows/desktop/api/winddi/ns-winddi-_pathdata)"><strong>PATHDATA</strong></a> record from a path. Each record describes all or part of a subpath.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_benumcliplines" data-raw-source="[&lt;strong&gt;PATHOBJ_bEnumClipLines&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_benumcliplines)"><strong>PATHOBJ_bEnumClipLines</strong></a></p></td>
<td align="left"><p>Enumerates clipped line segments from a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_bmoveto" data-raw-source="[&lt;strong&gt;PATHOBJ_bMoveTo&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_bmoveto)"><strong>PATHOBJ_bMoveTo</strong></a></p></td>
<td align="left"><p>Changes the current position in a <a href="https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-_pathobj" data-raw-source="[&lt;strong&gt;PATHOBJ&lt;/strong&gt;](/windows/desktop/api/winddi/ns-winddi-_pathobj)"><strong>PATHOBJ</strong></a>-defined path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_bpolybezierto" data-raw-source="[&lt;strong&gt;PATHOBJ_bPolyBezierTo&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_bpolybezierto)"><strong>PATHOBJ_bPolyBezierTo</strong></a></p></td>
<td align="left"><p>Draws Bezier curves (cubic splines) in a PATHOBJ-defined path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_bpolylineto" data-raw-source="[&lt;strong&gt;PATHOBJ_bPolyLineTo&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_bpolylineto)"><strong>PATHOBJ_bPolyLineTo</strong></a></p></td>
<td align="left"><p>Draws lines in a PATHOBJ-defined path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_venumstart" data-raw-source="[&lt;strong&gt;PATHOBJ_vEnumStart&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_venumstart)"><strong>PATHOBJ_vEnumStart</strong></a></p></td>
<td align="left"><p>Notifies a <a href="https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-_pathobj" data-raw-source="[&lt;strong&gt;PATHOBJ&lt;/strong&gt;](/windows/desktop/api/winddi/ns-winddi-_pathobj)"><strong>PATHOBJ</strong></a> that the driver will begin calling <strong>PATHOBJ_bEnum</strong> to enumerate the curves in the specified path. This function must be called in case of an enumeration restart.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_venumstartcliplines" data-raw-source="[&lt;strong&gt;PATHOBJ_vEnumStartClipLines&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_venumstartcliplines)"><strong>PATHOBJ_vEnumStartClipLines</strong></a></p></td>
<td align="left"><p>Allows the driver to ask for lines to be clipped against a <a href="https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-_clipobj" data-raw-source="&lt;strong&gt;CLIPOBJ&lt;/strong&gt;"><em>clip region</em></a> is more complex than a single rectangle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-pathobj_vgetbounds" data-raw-source="[&lt;strong&gt;PATHOBJ_vGetBounds&lt;/strong&gt;](/windows/desktop/api/winddi/nf-winddi-pathobj_vgetbounds)"><strong>PATHOBJ_vGetBounds</strong></a></p></td>
<td align="left"><p>Returns a bounding rectangle for the path.</p></td>
</tr>
</tbody>
</table>

 

 

