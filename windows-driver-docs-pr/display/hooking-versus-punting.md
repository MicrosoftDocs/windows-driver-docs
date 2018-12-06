---
title: Hooking Versus Punting
description: Hooking Versus Punting
ms.assetid: 52544915-8392-4eb1-8186-6a7fbad8ed4a
keywords:
- surface negotiation WDK GDI , hooking
- surface negotiation WDK GDI , punting
- hooking WDK GDI
- punting WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556180" data-raw-source="[&lt;strong&gt;DrvBitBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556180)"><strong>DrvBitBlt</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564185" data-raw-source="[&lt;strong&gt;EngBitBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564185)"><strong>EngBitBlt</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556258" data-raw-source="[&lt;strong&gt;DrvPlgBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556258)"><strong>DrvPlgBlt</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564982" data-raw-source="[&lt;strong&gt;EngPlgBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564982)"><strong>EngPlgBlt</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556302" data-raw-source="[&lt;strong&gt;DrvStretchBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556302)"><strong>DrvStretchBlt</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565025" data-raw-source="[&lt;strong&gt;EngStretchBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565025)"><strong>EngStretchBlt</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556306" data-raw-source="[&lt;strong&gt;DrvStretchBltROP&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556306)"><strong>DrvStretchBltROP</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565027" data-raw-source="[&lt;strong&gt;EngStretchBltROP&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565027)"><strong>EngStretchBltROP</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557277" data-raw-source="[&lt;strong&gt;DrvTextOut&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557277)"><strong>DrvTextOut</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565034" data-raw-source="[&lt;strong&gt;EngTextOut&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565034)"><strong>EngTextOut</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556316" data-raw-source="[&lt;strong&gt;DrvStrokePath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556316)"><strong>DrvStrokePath</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565033" data-raw-source="[&lt;strong&gt;EngStrokePath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565033)"><strong>EngStrokePath</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556220" data-raw-source="[&lt;strong&gt;DrvFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556220)"><strong>DrvFillPath</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564860" data-raw-source="[&lt;strong&gt;EngFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564860)"><strong>EngFillPath</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556311" data-raw-source="[&lt;strong&gt;DrvStrokeAndFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556311)"><strong>DrvStrokeAndFillPath</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565030" data-raw-source="[&lt;strong&gt;EngStrokeAndFillPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565030)"><strong>EngStrokeAndFillPath</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556245" data-raw-source="[&lt;strong&gt;DrvLineTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556245)"><strong>DrvLineTo</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564962" data-raw-source="[&lt;strong&gt;EngLineTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564962)"><strong>EngLineTo</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556182" data-raw-source="[&lt;strong&gt;DrvCopyBits&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556182)"><strong>DrvCopyBits</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564196" data-raw-source="[&lt;strong&gt;EngCopyBits&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564196)"><strong>EngCopyBits</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556176" data-raw-source="[&lt;strong&gt;DrvAlphaBlend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556176)"><strong>DrvAlphaBlend</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564182" data-raw-source="[&lt;strong&gt;EngAlphaBlend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564182)"><strong>EngAlphaBlend</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556236" data-raw-source="[&lt;strong&gt;DrvGradientFill&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556236)"><strong>DrvGradientFill</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564957" data-raw-source="[&lt;strong&gt;EngGradientFill&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564957)"><strong>EngGradientFill</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557283" data-raw-source="[&lt;strong&gt;DrvTransparentBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557283)"><strong>DrvTransparentBlt</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565037" data-raw-source="[&lt;strong&gt;EngTransparentBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565037)"><strong>EngTransparentBlt</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 





