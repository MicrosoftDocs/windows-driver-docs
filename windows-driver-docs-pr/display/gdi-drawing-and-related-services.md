---
title: GDI Drawing and Related Services
description: GDI Drawing and Related Services
keywords:
- GDI WDK Windows 2000 display , drawing services
- graphics drivers WDK Windows 2000 display , drawing services
- drawing WDK GDI , drawing services supported
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Drawing and Related Services


## <span id="ddk_gdi_drawing_and_related_services_gg"></span><span id="DDK_GDI_DRAWING_AND_RELATED_SERVICES_GG"></span>


To support the [**CLIPOBJ**](/windows/win32/api/winddi/ns-winddi-clipobj), [**BRUSHOBJ**](/windows/win32/api/winddi/ns-winddi-brushobj), and [**XFORMOBJ**](/previous-versions/windows/hardware/drivers/ff570618(v=vs.85)) structures, GDI offers several drawing services, listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">GDI Drawing Service Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-brushobj_hgetcolortransform" data-raw-source="[&lt;strong&gt;BRUSHOBJ_hGetColorTransform&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-brushobj_hgetcolortransform)"><strong>BRUSHOBJ_hGetColorTransform</strong></a></p></td>
<td align="left"><p>Retrieves the color transform for the specified brush.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-brushobj_pvallocrbrush" data-raw-source="[&lt;strong&gt;BRUSHOBJ_pvAllocRbrush&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-brushobj_pvallocrbrush)"><strong>BRUSHOBJ_pvAllocRbrush</strong></a></p></td>
<td align="left"><p>Allocates memory for the driver's realization of a brush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-brushobj_pvgetrbrush" data-raw-source="[&lt;strong&gt;BRUSHOBJ_pvGetRbrush&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-brushobj_pvgetrbrush)"><strong>BRUSHOBJ_pvGetRbrush</strong></a></p></td>
<td align="left"><p>Returns a pointer to the driver's realization of the brush. Realizes the brush if it has not yet been realized.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-brushobj_ulgetbrushcolor" data-raw-source="[&lt;strong&gt;BRUSHOBJ_ulGetBrushColor&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-brushobj_ulgetbrushcolor)"><strong>BRUSHOBJ_ulGetBrushColor</strong></a></p></td>
<td align="left"><p>Returns the RGB color of the specified solid brush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-clipobj_benum" data-raw-source="[&lt;strong&gt;CLIPOBJ_bEnum&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-clipobj_benum)"><strong>CLIPOBJ_bEnum</strong></a></p></td>
<td align="left"><p>Retrieves a batch of rectangles from the clip region.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-clipobj_cenumstart" data-raw-source="[&lt;strong&gt;CLIPOBJ_cEnumStart&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-clipobj_cenumstart)"><strong>CLIPOBJ_cEnumStart</strong></a></p></td>
<td align="left"><p>Sets parameters for enumeration of the rectangles in all or part of the clipped region. (The region can be enumerated once without calling this function, but subsequent enumerations require this function's use).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-clipobj_ppogetpath" data-raw-source="[&lt;strong&gt;CLIPOBJ_ppoGetPath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-clipobj_ppogetpath)"><strong>CLIPOBJ_ppoGetPath</strong></a></p></td>
<td align="left"><p>Is used to retrieve complicated regions as a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engalphablend" data-raw-source="[&lt;strong&gt;EngAlphaBlend&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engalphablend)"><strong>EngAlphaBlend</strong></a></p></td>
<td align="left"><p>Provides bit-block transfer capabilities with <a href="/windows-hardware/drivers/#wdkgloss-alpha-blending" data-raw-source="&lt;em&gt;alpha blending&lt;/em&gt;"><em>alpha blending</em></a>. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvalphablend" data-raw-source="[&lt;strong&gt;DrvAlphaBlend&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvalphablend)"><strong>DrvAlphaBlend</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engbitblt" data-raw-source="[&lt;strong&gt;EngBitBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engbitblt)"><strong>EngBitBlt</strong></a></p></td>
<td align="left"><p>Provides general bit-block transfer capabilities either between <a href="/windows-hardware/drivers/#wdkgloss-device-managed-surface" data-raw-source="&lt;em&gt;device-managed surfaces&lt;/em&gt;"><em>device-managed surfaces</em></a>, or between a device-managed surface and a GDI-managed standard format bitmap. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvbitblt" data-raw-source="[&lt;strong&gt;DrvBitBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvbitblt)"><strong>DrvBitBlt</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engcontrolsprites" data-raw-source="[&lt;strong&gt;EngControlSprites&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engcontrolsprites)"><strong>EngControlSprites</strong></a></p></td>
<td align="left"><p>Tears down or redraws sprites on the specified WNDOBJ area.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engcopybits" data-raw-source="[&lt;strong&gt;EngCopyBits&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engcopybits)"><strong>EngCopyBits</strong></a></p></td>
<td align="left"><p>Translates between device-managed raster surfaces and GDI standard-format bitmaps. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvcopybits" data-raw-source="[&lt;strong&gt;DrvCopyBits&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvcopybits)"><strong>DrvCopyBits</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engcreateclip" data-raw-source="[&lt;strong&gt;EngCreateClip&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engcreateclip)"><strong>EngCreateClip</strong></a></p></td>
<td align="left"><p>Allocates a <a href="/windows/win32/api/winddi/ns-winddi-clipobj" data-raw-source="[&lt;strong&gt;CLIPOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_clipobj)"><strong>CLIPOBJ</strong></a> for the driver's temporary use. The driver should call the <a href="/windows/win32/api/winddi/nf-winddi-engdeleteclip" data-raw-source="[&lt;strong&gt;EngDeleteClip&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdeleteclip)"><strong>EngDeleteClip</strong></a> function to delete it when it is no longer needed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdeleteclip" data-raw-source="[&lt;strong&gt;EngDeleteClip&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdeleteclip)"><strong>EngDeleteClip</strong></a></p></td>
<td align="left"><p>Deletes a CLIPOBJ allocated with the <a href="/windows/win32/api/winddi/nf-winddi-engcreateclip" data-raw-source="[&lt;strong&gt;EngCreateClip&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engcreateclip)"><strong>EngCreateClip</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdeviceiocontrol" data-raw-source="[&lt;strong&gt;EngDeviceIoControl&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdeviceiocontrol)"><strong>EngDeviceIoControl</strong></a></p></td>
<td align="left"><p>Sends a control code to the specified video miniport driver, causing the device to perform the specified operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engfillpath" data-raw-source="[&lt;strong&gt;EngFillPath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engfillpath)"><strong>EngFillPath</strong></a></p></td>
<td align="left"><p>Fills (paints) a specified path. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvfillpath" data-raw-source="[&lt;strong&gt;DrvFillPath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvfillpath)"><strong>DrvFillPath</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-enggradientfill" data-raw-source="[&lt;strong&gt;EngGradientFill&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-enggradientfill)"><strong>EngGradientFill</strong></a></p></td>
<td align="left"><p>Shades the specified graphics primitives. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvgradientfill" data-raw-source="[&lt;strong&gt;DrvGradientFill&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvgradientfill)"><strong>DrvGradientFill</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-englineto" data-raw-source="[&lt;strong&gt;EngLineTo&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-englineto)"><strong>EngLineTo</strong></a></p></td>
<td align="left"><p>Draws a single, solid, integer-only cosmetic line. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvlineto" data-raw-source="[&lt;strong&gt;DrvLineTo&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvlineto)"><strong>DrvLineTo</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmovepointer" data-raw-source="[&lt;strong&gt;EngMovePointer&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmovepointer)"><strong>EngMovePointer</strong></a></p></td>
<td align="left"><p>Moves the engine-managed pointer on the device. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvmovepointer" data-raw-source="[&lt;strong&gt;DrvMovePointer&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvmovepointer)"><strong>DrvMovePointer</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engpaint" data-raw-source="[&lt;strong&gt;EngPaint&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engpaint)"><strong>EngPaint</strong></a></p></td>
<td align="left"><p>Paints a specified region. This is the GDI simulation for the obsolete <a href="/windows/win32/api/winddi/nf-winddi-drvpaint" data-raw-source="[&lt;strong&gt;DrvPaint&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvpaint)"><strong>DrvPaint</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engplgblt" data-raw-source="[&lt;strong&gt;EngPlgBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engplgblt)"><strong>EngPlgBlt</strong></a></p></td>
<td align="left"><p>Performs a rotate bit-block transfer. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvplgblt" data-raw-source="[&lt;strong&gt;DrvPlgBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvplgblt)"><strong>DrvPlgBlt</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsetpointershape" data-raw-source="[&lt;strong&gt;EngSetPointerShape&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsetpointershape)"><strong>EngSetPointerShape</strong></a></p></td>
<td align="left"><p>Sets the shape of the pointer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsetpointertag" data-raw-source="[&lt;strong&gt;EngSetPointerTag&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsetpointertag)"><strong>EngSetPointerTag</strong></a></p></td>
<td align="left"><p>Creates a shape that is ORed with the application's pointer shape on <a href="/windows/win32/api/winddi/nf-winddi-drvsetpointershape" data-raw-source="[&lt;strong&gt;DrvSetPointerShape&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvsetpointershape)"><strong>DrvSetPointerShape</strong></a> calls to other associated drivers in a mirrored system.</p>
<div>
 
</div>
This function is obsolete for Windows 2000 and later.</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engstretchblt" data-raw-source="[&lt;strong&gt;EngStretchBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engstretchblt)"><strong>EngStretchBlt</strong></a></p></td>
<td align="left"><p>Performs a stretching bit-block transfer. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvstretchblt" data-raw-source="[&lt;strong&gt;DrvStretchBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstretchblt)"><strong>DrvStretchBlt</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engstretchbltrop" data-raw-source="[&lt;strong&gt;EngStretchBltROP&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engstretchbltrop)"><strong>EngStretchBltROP</strong></a></p></td>
<td align="left"><p>Performs a stretching bit-block transfer using a <a href="/windows-hardware/drivers/#wdkgloss-raster-operation--rop-" data-raw-source="&lt;em&gt;ROP&lt;/em&gt;"><em>ROP</em></a>. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvstretchbltrop" data-raw-source="[&lt;strong&gt;DrvStretchBltROP&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstretchbltrop)"><strong>DrvStretchBltROP</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engstrokeandfillpath" data-raw-source="[&lt;strong&gt;EngStrokeAndFillPath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engstrokeandfillpath)"><strong>EngStrokeAndFillPath</strong></a></p></td>
<td align="left"><p>Strokes (draws) a path and fills it at the same time. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvstrokeandfillpath" data-raw-source="[&lt;strong&gt;DrvStrokeAndFillPath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstrokeandfillpath)"><strong>DrvStrokeAndFillPath</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engstrokepath" data-raw-source="[&lt;strong&gt;EngStrokePath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engstrokepath)"><strong>EngStrokePath</strong></a></p></td>
<td align="left"><p>Strokes (draws) a path. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvstrokepath" data-raw-source="[&lt;strong&gt;DrvStrokePath&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvstrokepath)"><strong>DrvStrokePath</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engtransparentblt" data-raw-source="[&lt;strong&gt;EngTransparentBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engtransparentblt)"><strong>EngTransparentBlt</strong></a></p></td>
<td align="left"><p>Performs a transparent blt. This is the GDI simulation for the <a href="/windows/win32/api/winddi/nf-winddi-drvtransparentblt" data-raw-source="[&lt;strong&gt;DrvTransparentBlt&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-drvtransparentblt)"><strong>DrvTransparentBlt</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-xformobj_bapplyxform" data-raw-source="[&lt;strong&gt;XFORMOBJ_bApplyXform&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-xformobj_bapplyxform)"><strong>XFORMOBJ_bApplyXform</strong></a></p></td>
<td align="left"><p>Applies the given transform or its inverse to the given array of points.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-xformobj_igetfloatobjxform" data-raw-source="[&lt;strong&gt;XFORMOBJ_iGetFloatObjXform&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-xformobj_igetfloatobjxform)"><strong>XFORMOBJ_iGetFloatObjXform</strong></a></p></td>
<td align="left"><p>Downloads a FLOATOBJ transform to the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-xformobj_igetxform" data-raw-source="[&lt;strong&gt;XFORMOBJ_iGetXform&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-xformobj_igetxform)"><strong>XFORMOBJ_iGetXform</strong></a></p></td>
<td align="left"><p>Downloads a transform to the driver.</p></td>
</tr>
</tbody>
</table>

 

