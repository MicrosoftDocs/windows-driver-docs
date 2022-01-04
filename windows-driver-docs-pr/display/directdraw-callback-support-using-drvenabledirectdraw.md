---
title: DirectDraw Callback Support Using DrvEnableDirectDraw
description: DirectDraw Callback Support Using DrvEnableDirectDraw
keywords:
- DirectDraw driver initialization WDK Windows 2000 display , Windows 2000
- callback functions WDK DirectDraw
- DrvEnableDirectDraw
- DirectDraw driver initialization WDK Windows 2000 display , callback functions
ms.date: 04/20/2017
---

# DirectDraw Callback Support Using DrvEnableDirectDraw


## <span id="ddk_directdraw_callback_support_using_drvenabledirectdraw_gg"></span><span id="DDK_DIRECTDRAW_CALLBACK_SUPPORT_USING_DRVENABLEDIRECTDRAW_GG"></span>


The display driver can implement the [**DrvEnableDirectDraw**](/windows/win32/api/winddi/nf-winddi-drvenabledirectdraw) function to indicate various DirectDraw callback support. To indicate support, the driver returns pointers to the [**DD\_CALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_callbacks), [**DD\_SURFACECALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surfacecallbacks), and [**DD\_PALETTECALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_palettecallbacks) structures in the *pCallBacks*, *pSurfaceCallBacks*, and *pPaletteCallBacks* parameters.

The driver populates members of the [**DD\_CALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_callbacks) structure to indicate that it supports the following callback functions.

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
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff549213(v=vs.85)" data-raw-source="[&lt;em&gt;DdCanCreateSurface&lt;/em&gt;](/previous-versions/windows/hardware/drivers/ff549213(v=vs.85))"><em>DdCanCreateSurface</em></a></p></td>
<td align="left"><p>Returns a value that indicates whether the driver can create a surface of the specified surface description.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_createpalette" data-raw-source="[&lt;em&gt;DdCreatePalette&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createpalette)"><em>DdCreatePalette</em></a></p></td>
<td align="left"><p>Creates a DirectDrawPalette object for the specified DirectDraw object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff549263(v=vs.85)" data-raw-source="[&lt;em&gt;DdCreateSurface&lt;/em&gt;](/previous-versions/windows/hardware/drivers/ff549263(v=vs.85))"><em>DdCreateSurface</em></a></p></td>
<td align="left"><p>Creates a DirectDraw surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_getscanline" data-raw-source="[&lt;em&gt;DdGetScanLine&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getscanline)"><em>DdGetScanLine</em></a></p></td>
<td align="left"><p>Returns the number of the current physical scan line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_mapmemory" data-raw-source="[&lt;em&gt;DdMapMemory&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mapmemory)"><em>DdMapMemory</em></a></p></td>
<td align="left"><p>Maps application-modifiable portions of the frame buffer into the user-mode address space of the specified process, or it unmaps memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_waitforverticalblank" data-raw-source="[&lt;em&gt;DdWaitForVerticalBlank&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_waitforverticalblank)"><em>DdWaitForVerticalBlank</em></a></p></td>
<td align="left"><p>Returns the vertical blank status of the device.</p></td>
</tr>
</tbody>
</table>

 

The driver populates members of the [**DD\_SURFACECALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surfacecallbacks) structure to indicate that it supports the following callback functions.

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
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_addattachedsurface" data-raw-source="[&lt;em&gt;DdAddAttachedSurface&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_addattachedsurface)"><em>DdAddAttachedSurface</em></a></p></td>
<td align="left"><p>Attaches a surface to another surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_blt" data-raw-source="[&lt;em&gt;DdBlt&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_blt)"><em>DdBlt</em></a></p></td>
<td align="left"><p>Performs a bit-block transfer (blt) of display data from a source surface to a destination surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_destroysurface" data-raw-source="[&lt;em&gt;DdDestroySurface&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_destroysurface)"><em>DdDestroySurface</em></a></p></td>
<td align="left"><p>Destroys a DirectDraw surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_flip" data-raw-source="[&lt;em&gt;DdFlip&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_flip)"><em>DdFlip</em></a></p></td>
<td align="left"><p>Causes the surface memory associated with the target surface to become the primary surface, and the current surface to become the nonprimary surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_getbltstatus" data-raw-source="[&lt;em&gt;DdGetBltStatus&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_getbltstatus)"><em>DdGetBltStatus</em></a></p></td>
<td align="left"><p>Queries the blt status of the specified surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_getflipstatus" data-raw-source="[&lt;em&gt;DdGetFlipStatus&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_getflipstatus)"><em>DdGetFlipStatus</em></a></p></td>
<td align="left"><p>Determines whether the most recently requested flip on a surface has occurred.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_lock" data-raw-source="[&lt;em&gt;DdLock&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_lock)"><em>DdLock</em></a></p></td>
<td align="left"><p>Locks a specified area of surface memory and provides a valid pointer to a block of memory associated with a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_setcolorkey" data-raw-source="[&lt;em&gt;DdSetColorKey&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_setcolorkey)"><em>DdSetColorKey</em></a></p></td>
<td align="left"><p>Sets the color key value for the specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_setoverlayposition" data-raw-source="[&lt;em&gt;DdSetOverlayPosition&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_setoverlayposition)"><em>DdSetOverlayPosition</em></a></p></td>
<td align="left"><p>Sets the position for an overlay.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_setpalette" data-raw-source="[&lt;em&gt;DdSetPalette&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_setpalette)"><em>DdSetPalette</em></a></p></td>
<td align="left"><p>Attaches a palette to the specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_unlock" data-raw-source="[&lt;em&gt;DdUnlock&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_unlock)"><em>DdUnlock</em></a></p></td>
<td align="left"><p>Releases the lock held on the specified surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_updateoverlay" data-raw-source="[&lt;em&gt;DdUpdateOverlay&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_updateoverlay)"><em>DdUpdateOverlay</em></a></p></td>
<td align="left"><p>Repositions or modifies the visual attributes of an overlay surface.</p></td>
</tr>
</tbody>
</table>

 

The driver populates members of the [**DD\_PALETTECALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_palettecallbacks) structure to indicate that it supports the following callback functions.

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
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_palcb_destroypalette" data-raw-source="[&lt;em&gt;DdDestroyPalette&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_palcb_destroypalette)"><em>DdDestroyPalette</em></a></p></td>
<td align="left"><p>Destroys the specified palette.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_palcb_setentries" data-raw-source="[&lt;em&gt;DdSetEntries&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_palcb_setentries)"><em>DdSetEntries</em></a></p></td>
<td align="left"><p>Updates the palette entries in the specified palette.</p></td>
</tr>
</tbody>
</table>

 

