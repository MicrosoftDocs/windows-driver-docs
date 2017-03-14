---
title: GDI Services for Paths
description: GDI Services for Paths
ms.assetid: 8fc51b7e-d787-48ed-a865-528547abefc5
keywords: ["GDI WDK Windows 2000 display , paths", "graphics drivers WDK Windows 2000 display , paths", "drawing WDK GDI , paths", "paths WDK GDI", "filling paths WDK GDI"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Services%20for%20Paths%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




