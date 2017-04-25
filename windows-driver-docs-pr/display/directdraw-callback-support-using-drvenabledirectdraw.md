---
title: DirectDraw Callback Support Using DrvEnableDirectDraw
description: DirectDraw Callback Support Using DrvEnableDirectDraw
ms.assetid: 74caab2b-6976-411a-97af-7c94b0c12fa0
keywords:
- DirectDraw driver initialization WDK Windows 2000 display , Windows 2000
- callback functions WDK DirectDraw
- DrvEnableDirectDraw
- DirectDraw driver initialization WDK Windows 2000 display , callback functions
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectDraw Callback Support Using DrvEnableDirectDraw


## <span id="ddk_directdraw_callback_support_using_drvenabledirectdraw_gg"></span><span id="DDK_DIRECTDRAW_CALLBACK_SUPPORT_USING_DRVENABLEDIRECTDRAW_GG"></span>


The display driver can implement the [**DrvEnableDirectDraw**](https://msdn.microsoft.com/library/windows/hardware/ff556208) function to indicate various DirectDraw callback support. To indicate support, the driver returns pointers to the [**DD\_CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff550485), [**DD\_SURFACECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551721), and [**DD\_PALETTECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551681) structures in the *pCallBacks*, *pSurfaceCallBacks*, and *pPaletteCallBacks* parameters.

The driver populates members of the [**DD\_CALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff550485) structure to indicate that it supports the following callback functions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Callback Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<em>DdCanCreateSurface</em>](https://msdn.microsoft.com/library/windows/hardware/ff549213)</p></td>
<td align="left"><p>Returns a value that indicates whether the driver can create a surface of the specified surface description.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdCreatePalette</em>](https://msdn.microsoft.com/library/windows/hardware/ff549254)</p></td>
<td align="left"><p>Creates a DirectDrawPalette object for the specified DirectDraw object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdCreateSurface</em>](https://msdn.microsoft.com/library/windows/hardware/ff549263)</p></td>
<td align="left"><p>Creates a DirectDraw surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdGetScanLine</em>](https://msdn.microsoft.com/library/windows/hardware/ff549497)</p></td>
<td align="left"><p>Returns the number of the current physical scan line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdMapMemory</em>](https://msdn.microsoft.com/library/windows/hardware/ff549641)</p></td>
<td align="left"><p>Maps application-modifiable portions of the frame buffer into the user-mode address space of the specified process, or it unmaps memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdWaitForVerticalBlank</em>](https://msdn.microsoft.com/library/windows/hardware/ff550457)</p></td>
<td align="left"><p>Returns the vertical blank status of the device.</p></td>
</tr>
</tbody>
</table>

 

The driver populates members of the [**DD\_SURFACECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551721) structure to indicate that it supports the following callback functions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Callback Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<em>DdAddAttachedSurface</em>](https://msdn.microsoft.com/library/windows/hardware/ff549194)</p></td>
<td align="left"><p>Attaches a surface to another surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdBlt</em>](https://msdn.microsoft.com/library/windows/hardware/ff549205)</p></td>
<td align="left"><p>Performs a bit-block transfer (blt) of display data from a source surface to a destination surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdDestroySurface</em>](https://msdn.microsoft.com/library/windows/hardware/ff549281)</p></td>
<td align="left"><p>Destroys a DirectDraw surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdFlip</em>](https://msdn.microsoft.com/library/windows/hardware/ff549306)</p></td>
<td align="left"><p>Causes the surface memory associated with the target surface to become the primary surface, and the current surface to become the nonprimary surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdGetBltStatus</em>](https://msdn.microsoft.com/library/windows/hardware/ff549385)</p></td>
<td align="left"><p>Queries the blt status of the specified surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdGetFlipStatus</em>](https://msdn.microsoft.com/library/windows/hardware/ff549429)</p></td>
<td align="left"><p>Determines whether the most recently requested flip on a surface has occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdLock</em>](https://msdn.microsoft.com/library/windows/hardware/ff549599)</p></td>
<td align="left"><p>Locks a specified area of surface memory and provides a valid pointer to a block of memory associated with a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdSetColorKey</em>](https://msdn.microsoft.com/library/windows/hardware/ff550301)</p></td>
<td align="left"><p>Sets the color key value for the specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdSetOverlayPosition</em>](https://msdn.microsoft.com/library/windows/hardware/ff550311)</p></td>
<td align="left"><p>Sets the position for an overlay.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdSetPalette</em>](https://msdn.microsoft.com/library/windows/hardware/ff550312)</p></td>
<td align="left"><p>Attaches a palette to the specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdUnlock</em>](https://msdn.microsoft.com/library/windows/hardware/ff550365)</p></td>
<td align="left"><p>Releases the lock held on the specified surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdUpdateOverlay</em>](https://msdn.microsoft.com/library/windows/hardware/ff550369)</p></td>
<td align="left"><p>Repositions or modifies the visual attributes of an overlay surface.</p></td>
</tr>
</tbody>
</table>

 

The driver populates members of the [**DD\_PALETTECALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551681) structure to indicate that it supports the following callback functions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Callback Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<em>DdDestroyPalette</em>](https://msdn.microsoft.com/library/windows/hardware/ff549276)</p></td>
<td align="left"><p>Destroys the specified palette.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdSetEntries</em>](https://msdn.microsoft.com/library/windows/hardware/ff550302)</p></td>
<td align="left"><p>Updates the palette entries in the specified palette.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectDraw%20Callback%20Support%20Using%20DrvEnableDirectDraw%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




