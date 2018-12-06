---
title: GDI Drawing and Related Services
description: GDI Drawing and Related Services
ms.assetid: b5df84ae-05cf-49dc-aa49-79f912ecd029
keywords:
- GDI WDK Windows 2000 display , drawing services
- graphics drivers WDK Windows 2000 display , drawing services
- drawing WDK GDI , drawing services supported
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Drawing and Related Services


## <span id="ddk_gdi_drawing_and_related_services_gg"></span><span id="DDK_GDI_DRAWING_AND_RELATED_SERVICES_GG"></span>


To support the [**CLIPOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff539417), [**BRUSHOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff538261), and [**XFORMOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570618) structures, GDI offers several drawing services, listed in the following table.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538262" data-raw-source="[&lt;strong&gt;BRUSHOBJ_hGetColorTransform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538262)"><strong>BRUSHOBJ_hGetColorTransform</strong></a></p></td>
<td align="left"><p>Retrieves the color transform for the specified brush.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538263" data-raw-source="[&lt;strong&gt;BRUSHOBJ_pvAllocRbrush&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538263)"><strong>BRUSHOBJ_pvAllocRbrush</strong></a></p></td>
<td align="left"><p>Allocates memory for the driver&#39;s realization of a brush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538264" data-raw-source="[&lt;strong&gt;BRUSHOBJ_pvGetRbrush&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538264)"><strong>BRUSHOBJ_pvGetRbrush</strong></a></p></td>
<td align="left"><p>Returns a pointer to the driver&#39;s realization of the brush. Realizes the brush if it has not yet been realized.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538265" data-raw-source="[&lt;strong&gt;BRUSHOBJ_ulGetBrushColor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538265)"><strong>BRUSHOBJ_ulGetBrushColor</strong></a></p></td>
<td align="left"><p>Returns the RGB color of the specified solid brush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff539420" data-raw-source="[&lt;strong&gt;CLIPOBJ_bEnum&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff539420)"><strong>CLIPOBJ_bEnum</strong></a></p></td>
<td align="left"><p>Retrieves a batch of rectangles from the clip region.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff539421" data-raw-source="[&lt;strong&gt;CLIPOBJ_cEnumStart&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff539421)"><strong>CLIPOBJ_cEnumStart</strong></a></p></td>
<td align="left"><p>Sets parameters for enumeration of the rectangles in all or part of the clipped region. (The region can be enumerated once without calling this function, but subsequent enumerations require this function&#39;s use).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff539423" data-raw-source="[&lt;strong&gt;CLIPOBJ_ppoGetPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff539423)"><strong>CLIPOBJ_ppoGetPath</strong></a></p></td>
<td align="left"><p>Is used to retrieve complicated regions as a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564182" data-raw-source="[&lt;strong&gt;EngAlphaBlend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564182)"><strong>EngAlphaBlend</strong></a></p></td>
<td align="left"><p>Provides bit-block transfer capabilities with <a href="https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending" data-raw-source="[&lt;em&gt;alpha blending&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending)"><em>alpha blending</em></a>. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556176" data-raw-source="[&lt;strong&gt;DrvAlphaBlend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556176)"><strong>DrvAlphaBlend</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564185" data-raw-source="[&lt;strong&gt;EngBitBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564185)"><strong>EngBitBlt</strong></a></p></td>
<td align="left"><p>Provides general bit-block transfer capabilities either between <a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface" data-raw-source="[&lt;em&gt;device-managed surfaces&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface)"><em>device-managed surfaces</em></a>, or between a device-managed surface and a GDI-managed standard format bitmap. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556180" data-raw-source="[&lt;strong&gt;DrvBitBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556180)"><strong>DrvBitBlt</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564193" data-raw-source="[&lt;strong&gt;EngControlSprites&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564193)"><strong>EngControlSprites</strong></a></p></td>
<td align="left"><p>Tears down or redraws sprites on the specified WNDOBJ area.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564196" data-raw-source="[&lt;strong&gt;EngCopyBits&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564196)"><strong>EngCopyBits</strong></a></p></td>
<td align="left"><p>Translates between device-managed raster surfaces and GDI standard-format bitmaps. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556182" data-raw-source="[&lt;strong&gt;DrvCopyBits&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556182)"><strong>DrvCopyBits</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564202" data-raw-source="[&lt;strong&gt;EngCreateClip&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564202)"><strong>EngCreateClip</strong></a></p></td>
<td align="left"><p>Allocates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539417" data-raw-source="[&lt;strong&gt;CLIPOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff539417)"><strong>CLIPOBJ</strong></a> for the driver&#39;s temporary use. The driver should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564786" data-raw-source="[&lt;strong&gt;EngDeleteClip&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564786)"><strong>EngDeleteClip</strong></a> function to delete it when it is no longer needed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564786" data-raw-source="[&lt;strong&gt;EngDeleteClip&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564786)"><strong>EngDeleteClip</strong></a></p></td>
<td align="left"><p>Deletes a CLIPOBJ allocated with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564202" data-raw-source="[&lt;strong&gt;EngCreateClip&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564202)"><strong>EngCreateClip</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564838" data-raw-source="[&lt;strong&gt;EngDeviceIoControl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564838)"><strong>EngDeviceIoControl</strong></a></p></td>
<td align="left"><p>Sends a control code to the specified video miniport driver, causing the device to perform the specified operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564860" data-raw-source="[&lt;strong&gt;EngFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564860)"><strong>EngFillPath</strong></a></p></td>
<td align="left"><p>Fills (paints) a specified path. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556220" data-raw-source="[&lt;strong&gt;DrvFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556220)"><strong>DrvFillPath</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564957" data-raw-source="[&lt;strong&gt;EngGradientFill&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564957)"><strong>EngGradientFill</strong></a></p></td>
<td align="left"><p>Shades the specified graphics primitives. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556236" data-raw-source="[&lt;strong&gt;DrvGradientFill&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556236)"><strong>DrvGradientFill</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564962" data-raw-source="[&lt;strong&gt;EngLineTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564962)"><strong>EngLineTo</strong></a></p></td>
<td align="left"><p>Draws a single, solid, integer-only cosmetic line. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556245" data-raw-source="[&lt;strong&gt;DrvLineTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556245)"><strong>DrvLineTo</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564977" data-raw-source="[&lt;strong&gt;EngMovePointer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564977)"><strong>EngMovePointer</strong></a></p></td>
<td align="left"><p>Moves the engine-managed pointer on the device. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556248" data-raw-source="[&lt;strong&gt;DrvMovePointer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556248)"><strong>DrvMovePointer</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564981" data-raw-source="[&lt;strong&gt;EngPaint&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564981)"><strong>EngPaint</strong></a></p></td>
<td align="left"><p>Paints a specified region. This is the GDI simulation for the obsolete <a href="https://msdn.microsoft.com/library/windows/hardware/ff556256" data-raw-source="[&lt;strong&gt;DrvPaint&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556256)"><strong>DrvPaint</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564982" data-raw-source="[&lt;strong&gt;EngPlgBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564982)"><strong>EngPlgBlt</strong></a></p></td>
<td align="left"><p>Performs a rotate bit-block transfer. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556258" data-raw-source="[&lt;strong&gt;DrvPlgBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556258)"><strong>DrvPlgBlt</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565017" data-raw-source="[&lt;strong&gt;EngSetPointerShape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565017)"><strong>EngSetPointerShape</strong></a></p></td>
<td align="left"><p>Sets the shape of the pointer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565018" data-raw-source="[&lt;strong&gt;EngSetPointerTag&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565018)"><strong>EngSetPointerTag</strong></a></p></td>
<td align="left"><p>Creates a shape that is ORed with the application&#39;s pointer shape on <a href="https://msdn.microsoft.com/library/windows/hardware/ff556289" data-raw-source="[&lt;strong&gt;DrvSetPointerShape&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556289)"><strong>DrvSetPointerShape</strong></a> calls to other associated drivers in a mirrored system.</p>
<div>
 
</div>
This function is obsolete for Windows 2000 and later.</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565025" data-raw-source="[&lt;strong&gt;EngStretchBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565025)"><strong>EngStretchBlt</strong></a></p></td>
<td align="left"><p>Performs a stretching bit-block transfer. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556302" data-raw-source="[&lt;strong&gt;DrvStretchBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556302)"><strong>DrvStretchBlt</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565027" data-raw-source="[&lt;strong&gt;EngStretchBltROP&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565027)"><strong>EngStretchBltROP</strong></a></p></td>
<td align="left"><p>Performs a stretching bit-block transfer using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-" data-raw-source="[&lt;em&gt;ROP&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-)"><em>ROP</em></a>. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556306" data-raw-source="[&lt;strong&gt;DrvStretchBltROP&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556306)"><strong>DrvStretchBltROP</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565030" data-raw-source="[&lt;strong&gt;EngStrokeAndFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565030)"><strong>EngStrokeAndFillPath</strong></a></p></td>
<td align="left"><p>Strokes (draws) a path and fills it at the same time. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556311" data-raw-source="[&lt;strong&gt;DrvStrokeAndFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556311)"><strong>DrvStrokeAndFillPath</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565033" data-raw-source="[&lt;strong&gt;EngStrokePath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565033)"><strong>EngStrokePath</strong></a></p></td>
<td align="left"><p>Strokes (draws) a path. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556316" data-raw-source="[&lt;strong&gt;DrvStrokePath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556316)"><strong>DrvStrokePath</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565037" data-raw-source="[&lt;strong&gt;EngTransparentBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565037)"><strong>EngTransparentBlt</strong></a></p></td>
<td align="left"><p>Performs a transparent blt. This is the GDI simulation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557283" data-raw-source="[&lt;strong&gt;DrvTransparentBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557283)"><strong>DrvTransparentBlt</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570623" data-raw-source="[&lt;strong&gt;XFORMOBJ_bApplyXform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570623)"><strong>XFORMOBJ_bApplyXform</strong></a></p></td>
<td align="left"><p>Applies the given transform or its inverse to the given array of points.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570627" data-raw-source="[&lt;strong&gt;XFORMOBJ_iGetFloatObjXform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570627)"><strong>XFORMOBJ_iGetFloatObjXform</strong></a></p></td>
<td align="left"><p>Downloads a FLOATOBJ transform to the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570630" data-raw-source="[&lt;strong&gt;XFORMOBJ_iGetXform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570630)"><strong>XFORMOBJ_iGetXform</strong></a></p></td>
<td align="left"><p>Downloads a transform to the driver.</p></td>
</tr>
</tbody>
</table>

 

 

 





