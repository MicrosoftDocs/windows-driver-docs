---
title: DirectDraw Callback Support Using DrvEnableDirectDraw
description: DirectDraw Callback Support Using DrvEnableDirectDraw
ms.assetid: 74caab2b-6976-411a-97af-7c94b0c12fa0
keywords:
- DirectDraw driver initialization WDK Windows 2000 display , Windows 2000
- callback functions WDK DirectDraw
- DrvEnableDirectDraw
- DirectDraw driver initialization WDK Windows 2000 display , callback functions
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549213" data-raw-source="[&lt;em&gt;DdCanCreateSurface&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549213)"><em>DdCanCreateSurface</em></a></p></td>
<td align="left"><p>Returns a value that indicates whether the driver can create a surface of the specified surface description.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549254" data-raw-source="[&lt;em&gt;DdCreatePalette&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549254)"><em>DdCreatePalette</em></a></p></td>
<td align="left"><p>Creates a DirectDrawPalette object for the specified DirectDraw object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549263" data-raw-source="[&lt;em&gt;DdCreateSurface&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549263)"><em>DdCreateSurface</em></a></p></td>
<td align="left"><p>Creates a DirectDraw surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549497" data-raw-source="[&lt;em&gt;DdGetScanLine&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549497)"><em>DdGetScanLine</em></a></p></td>
<td align="left"><p>Returns the number of the current physical scan line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549641" data-raw-source="[&lt;em&gt;DdMapMemory&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549641)"><em>DdMapMemory</em></a></p></td>
<td align="left"><p>Maps application-modifiable portions of the frame buffer into the user-mode address space of the specified process, or it unmaps memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550457" data-raw-source="[&lt;em&gt;DdWaitForVerticalBlank&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550457)"><em>DdWaitForVerticalBlank</em></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549194" data-raw-source="[&lt;em&gt;DdAddAttachedSurface&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549194)"><em>DdAddAttachedSurface</em></a></p></td>
<td align="left"><p>Attaches a surface to another surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549205" data-raw-source="[&lt;em&gt;DdBlt&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549205)"><em>DdBlt</em></a></p></td>
<td align="left"><p>Performs a bit-block transfer (blt) of display data from a source surface to a destination surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549281" data-raw-source="[&lt;em&gt;DdDestroySurface&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549281)"><em>DdDestroySurface</em></a></p></td>
<td align="left"><p>Destroys a DirectDraw surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549306" data-raw-source="[&lt;em&gt;DdFlip&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549306)"><em>DdFlip</em></a></p></td>
<td align="left"><p>Causes the surface memory associated with the target surface to become the primary surface, and the current surface to become the nonprimary surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549385" data-raw-source="[&lt;em&gt;DdGetBltStatus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549385)"><em>DdGetBltStatus</em></a></p></td>
<td align="left"><p>Queries the blt status of the specified surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549429" data-raw-source="[&lt;em&gt;DdGetFlipStatus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549429)"><em>DdGetFlipStatus</em></a></p></td>
<td align="left"><p>Determines whether the most recently requested flip on a surface has occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549599" data-raw-source="[&lt;em&gt;DdLock&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549599)"><em>DdLock</em></a></p></td>
<td align="left"><p>Locks a specified area of surface memory and provides a valid pointer to a block of memory associated with a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550301" data-raw-source="[&lt;em&gt;DdSetColorKey&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550301)"><em>DdSetColorKey</em></a></p></td>
<td align="left"><p>Sets the color key value for the specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550311" data-raw-source="[&lt;em&gt;DdSetOverlayPosition&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550311)"><em>DdSetOverlayPosition</em></a></p></td>
<td align="left"><p>Sets the position for an overlay.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550312" data-raw-source="[&lt;em&gt;DdSetPalette&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550312)"><em>DdSetPalette</em></a></p></td>
<td align="left"><p>Attaches a palette to the specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550365" data-raw-source="[&lt;em&gt;DdUnlock&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550365)"><em>DdUnlock</em></a></p></td>
<td align="left"><p>Releases the lock held on the specified surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550369" data-raw-source="[&lt;em&gt;DdUpdateOverlay&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550369)"><em>DdUpdateOverlay</em></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff549276" data-raw-source="[&lt;em&gt;DdDestroyPalette&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549276)"><em>DdDestroyPalette</em></a></p></td>
<td align="left"><p>Destroys the specified palette.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550302" data-raw-source="[&lt;em&gt;DdSetEntries&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550302)"><em>DdSetEntries</em></a></p></td>
<td align="left"><p>Updates the palette entries in the specified palette.</p></td>
</tr>
</tbody>
</table>

 

 

 





