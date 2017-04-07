---
title: Hooking Versus Punting
description: Hooking Versus Punting
ms.assetid: 52544915-8392-4eb1-8186-6a7fbad8ed4a
keywords: ["surface negotiation WDK GDI , hooking", "surface negotiation WDK GDI , punting", "hooking WDK GDI", "punting WDK GDI"]
---

# Hooking Versus Punting


## <span id="ddk_hooking_versus_punting_gg"></span><span id="DDK_HOOKING_VERSUS_PUNTING_GG"></span>


The terms *hooking* and *punting* refer to driver decisions on whether it provides standard bitmap drawing operations, or relies on GDI to provide them. If the driver implements engine-managed surfaces, GDI can handle all drawing operations. A driver can, however, provide one or more of the [drawing functions](optional-display-driver-functions.md) if its hardware can accelerate those operations. It does this by implementing, or hooking, a *DrvXxx* function.

A driver writer may wish to implement only a subset of the drawing operations a particular graphics DDI entry point implements. For any operations the driver does not support, it can call the appropriate GDI functions to carry them out. This is referred to as punting to GDI. There are some situations in which the operation must be implemented in the driver. For example, if the driver implements a device-managed surface, certain drawing functions must be implemented in the display driver.

### <span id="Hooking"></span><span id="hooking"></span><span id="HOOKING"></span>Hooking

By default, when a drawing surface is an engine-managed surface, GDI handles the drawing (rendering) operation. For a driver to take advantage of hardware that offers acceleration for some or all of these drawing functions for a given surface, or to make use of special block transfer hardware, it can hook these functions. To hook calls, the driver specifies the hooks as flags of the *flHook* parameter of the [**EngAssociateSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564183) and [**EngModifySurface**](https://msdn.microsoft.com/library/windows/hardware/ff564976) functions.

If the driver specifies the hook flag of a function, it must provide that function in its list of supported graphics DDI entry points. The driver can optimize the operation where there is hardware support. Such a driver might handle only certain cases on a hooked call. For example, if complicated graphics are requested on a call that is hooked, it may still be more efficient to punt the callback to GDI, allowing GDI to handle the operation.

Here is another example of a driver that chooses whether to handle a hooked call. Consider a driver that supports hardware capable of handling bit-block-transfer calls with certain [*ROPs*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raster-operation--rop-). Even though this driver can carry out many operations on its own, it is otherwise just a frame buffer. Such a driver will return a handle to the bitmap surface for the frame buffer as the surface for its [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev), but it will hook the [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180) call for itself. When GDI calls *DrvBitBlt*, the driver can check the ROP to see if it is one of those supported by the hardware. If not, the driver can pass the operation back to GDI with a call to the [**EngBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff564185) function.

Drivers that support device-managed surfaces must hook out some of the drawing functions; namely [**DrvCopyBits**](https://msdn.microsoft.com/library/windows/hardware/ff556182), [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277), and [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316). Although GDI simulations can handle other drawing functions, it is recommended for performance reasons that drivers of this type hook out other functions, such as the [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180) and [**DrvRealizeBrush**](https://msdn.microsoft.com/library/windows/hardware/ff556273) functions, because simulation requires drawing from and to the surface.

### <span id="Punting"></span><span id="punting"></span><span id="PUNTING"></span>Punting

*Punting* the callback to GDI means to put in a call to the corresponding GDI simulation. In general, for every *DrvXxx* graphics call, there is a corresponding GDI **Eng***Xxx* simulation call that takes the same arguments. As long as the driver has made the bitmap nonopaque, all parameters can be passed without change to a GDI simulation. For each call the driver punts back to GDI, the size of the driver is reduced (since the code for that functionality can be omitted). However, because the engine owns the call, the driver does not have control over the execution speed. For some complicated cases, there may be no real advantage to providing support in the driver.

### <span id="Hookable_GDI_Graphics_Output_Functions"></span><span id="hookable_gdi_graphics_output_functions"></span><span id="HOOKABLE_GDI_GRAPHICS_OUTPUT_FUNCTIONS"></span>Hookable GDI Graphics Output Functions

The graphics output functions that the driver can hook and the corresponding GDI simulations are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver Graphics Output Function</th>
<th align="left">Corresponding GDI Simulation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DrvBitBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556180)</p></td>
<td align="left"><p>[<strong>EngBitBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564185)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvPlgBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556258)</p></td>
<td align="left"><p>[<strong>EngPlgBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564982)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvStretchBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556302)</p></td>
<td align="left"><p>[<strong>EngStretchBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565025)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvStretchBltROP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556306)</p></td>
<td align="left"><p>[<strong>EngStretchBltROP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565027)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557277)</p></td>
<td align="left"><p>[<strong>EngTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565034)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvStrokePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556316)</p></td>
<td align="left"><p>[<strong>EngStrokePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565033)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556220)</p></td>
<td align="left"><p>[<strong>EngFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564860)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvStrokeAndFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556311)</p></td>
<td align="left"><p>[<strong>EngStrokeAndFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565030)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvLineTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556245)</p></td>
<td align="left"><p>[<strong>EngLineTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564962)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvCopyBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556182)</p></td>
<td align="left"><p>[<strong>EngCopyBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564196)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvAlphaBlend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556176)</p></td>
<td align="left"><p>[<strong>EngAlphaBlend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564182)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvGradientFill</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556236)</p></td>
<td align="left"><p>[<strong>EngGradientFill</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564957)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvTransparentBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557283)</p></td>
<td align="left"><p>[<strong>EngTransparentBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565037)</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Hooking%20Versus%20Punting%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




