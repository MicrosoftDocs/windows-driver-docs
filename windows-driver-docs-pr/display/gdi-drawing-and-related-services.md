---
title: GDI Drawing and Related Services
description: GDI Drawing and Related Services
ms.assetid: b5df84ae-05cf-49dc-aa49-79f912ecd029
keywords: ["GDI WDK Windows 2000 display , drawing services", "graphics drivers WDK Windows 2000 display , drawing services", "drawing WDK GDI , drawing services supported"]
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
<td align="left"><p>[<strong>BRUSHOBJ_hGetColorTransform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff538262)</p></td>
<td align="left"><p>Retrieves the color transform for the specified brush.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BRUSHOBJ_pvAllocRbrush</strong>](https://msdn.microsoft.com/library/windows/hardware/ff538263)</p></td>
<td align="left"><p>Allocates memory for the driver's realization of a brush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>BRUSHOBJ_pvGetRbrush</strong>](https://msdn.microsoft.com/library/windows/hardware/ff538264)</p></td>
<td align="left"><p>Returns a pointer to the driver's realization of the brush. Realizes the brush if it has not yet been realized.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>BRUSHOBJ_ulGetBrushColor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff538265)</p></td>
<td align="left"><p>Returns the RGB color of the specified solid brush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>CLIPOBJ_bEnum</strong>](https://msdn.microsoft.com/library/windows/hardware/ff539420)</p></td>
<td align="left"><p>Retrieves a batch of rectangles from the clip region.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>CLIPOBJ_cEnumStart</strong>](https://msdn.microsoft.com/library/windows/hardware/ff539421)</p></td>
<td align="left"><p>Sets parameters for enumeration of the rectangles in all or part of the clipped region. (The region can be enumerated once without calling this function, but subsequent enumerations require this function's use).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>CLIPOBJ_ppoGetPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff539423)</p></td>
<td align="left"><p>Is used to retrieve complicated regions as a path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngAlphaBlend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564182)</p></td>
<td align="left"><p>Provides bit-block transfer capabilities with [<em>alpha blending</em>](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-alpha-blending). This is the GDI simulation for the [<strong>DrvAlphaBlend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556176) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngBitBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564185)</p></td>
<td align="left"><p>Provides general bit-block transfer capabilities either between [<em>device-managed surfaces</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface), or between a device-managed surface and a GDI-managed standard format bitmap. This is the GDI simulation for the [<strong>DrvBitBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556180) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngControlSprites</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564193)</p></td>
<td align="left"><p>Tears down or redraws sprites on the specified WNDOBJ area.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngCopyBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564196)</p></td>
<td align="left"><p>Translates between device-managed raster surfaces and GDI standard-format bitmaps. This is the GDI simulation for the [<strong>DrvCopyBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556182) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngCreateClip</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564202)</p></td>
<td align="left"><p>Allocates a [<strong>CLIPOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff539417) for the driver's temporary use. The driver should call the [<strong>EngDeleteClip</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564786) function to delete it when it is no longer needed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngDeleteClip</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564786)</p></td>
<td align="left"><p>Deletes a CLIPOBJ allocated with the [<strong>EngCreateClip</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564202) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngDeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564838)</p></td>
<td align="left"><p>Sends a control code to the specified video miniport driver, causing the device to perform the specified operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564860)</p></td>
<td align="left"><p>Fills (paints) a specified path. This is the GDI simulation for the [<strong>DrvFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556220) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngGradientFill</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564957)</p></td>
<td align="left"><p>Shades the specified graphics primitives. This is the GDI simulation for the [<strong>DrvGradientFill</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556236) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngLineTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564962)</p></td>
<td align="left"><p>Draws a single, solid, integer-only cosmetic line. This is the GDI simulation for the [<strong>DrvLineTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556245) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngMovePointer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564977)</p></td>
<td align="left"><p>Moves the engine-managed pointer on the device. This is the GDI simulation for the [<strong>DrvMovePointer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556248) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngPaint</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564981)</p></td>
<td align="left"><p>Paints a specified region. This is the GDI simulation for the obsolete [<strong>DrvPaint</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556256) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngPlgBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564982)</p></td>
<td align="left"><p>Performs a rotate bit-block transfer. This is the GDI simulation for the [<strong>DrvPlgBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556258) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngSetPointerShape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565017)</p></td>
<td align="left"><p>Sets the shape of the pointer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngSetPointerTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565018)</p></td>
<td align="left"><p>Creates a shape that is ORed with the application's pointer shape on [<strong>DrvSetPointerShape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556289) calls to other associated drivers in a mirrored system.</p>
<div>
 
</div>
This function is obsolete for Windows 2000 and later.</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngStretchBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565025)</p></td>
<td align="left"><p>Performs a stretching bit-block transfer. This is the GDI simulation for the [<strong>DrvStretchBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556302) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngStretchBltROP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565027)</p></td>
<td align="left"><p>Performs a stretching bit-block transfer using a [<em>ROP</em>](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-). This is the GDI simulation for the [<strong>DrvStretchBltROP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556306) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngStrokeAndFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565030)</p></td>
<td align="left"><p>Strokes (draws) a path and fills it at the same time. This is the GDI simulation for the [<strong>DrvStrokeAndFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556311) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngStrokePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565033)</p></td>
<td align="left"><p>Strokes (draws) a path. This is the GDI simulation for the [<strong>DrvStrokePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556316) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngTransparentBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565037)</p></td>
<td align="left"><p>Performs a transparent blt. This is the GDI simulation for the [<strong>DrvTransparentBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557283) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>XFORMOBJ_bApplyXform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570623)</p></td>
<td align="left"><p>Applies the given transform or its inverse to the given array of points.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>XFORMOBJ_iGetFloatObjXform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570627)</p></td>
<td align="left"><p>Downloads a FLOATOBJ transform to the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>XFORMOBJ_iGetXform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570630)</p></td>
<td align="left"><p>Downloads a transform to the driver.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Drawing%20and%20Related%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




