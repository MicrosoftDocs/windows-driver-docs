---
title: Kernel-Mode Video Transport Callback Functions
description: Kernel-Mode Video Transport Callback Functions
keywords:
- DxApi miniport drivers WDK DirectDraw , kernel-mode video transport callback functions
- kernel-mode video transport WDK DirectDraw , callback functions
- callback functions WDK kernel-mode video transport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel-Mode Video Transport Callback Functions


## <span id="ddk_kernel_mode_video_transport_callback_functions_gg"></span><span id="DDK_KERNEL_MODE_VIDEO_TRANSPORT_CALLBACK_FUNCTIONS_GG"></span>


The following table lists the kernel-mode video transport callback functions that are implemented in a video miniport driver.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DxApi Callback Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_bobnextfield" data-raw-source="[&lt;em&gt;DxBobNextField&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_bobnextfield)"><em>DxBobNextField</em></a></p></td>
<td align="left"><p>Bobs the next field of interleaved data.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_enableirq" data-raw-source="[&lt;em&gt;DxEnableIRQ&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_enableirq)"><em>DxEnableIRQ</em></a></p></td>
<td align="left"><p>Indicates to the miniport driver which IRQs should be enabled or disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_flipoverlay" data-raw-source="[&lt;em&gt;DxFlipOverlay&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_flipoverlay)"><em>DxFlipOverlay</em></a></p></td>
<td align="left"><p>Flips the overlay.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_flipvideoport" data-raw-source="[&lt;em&gt;DxFlipVideoPort&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_flipvideoport)"><em>DxFlipVideoPort</em></a></p></td>
<td align="left"><p>Flips the video port extensions (VPE) object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_getcurrentautoflip" data-raw-source="[&lt;em&gt;DxGetCurrentAutoflip&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_getcurrentautoflip)"><em>DxGetCurrentAutoflip</em></a></p></td>
<td align="left"><p>Determines which surface is receiving the current field of video data for capture purposes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_getirqinfo" data-raw-source="[&lt;em&gt;DxGetIRQInfo&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_getirqinfo)"><em>DxGetIRQInfo</em></a></p></td>
<td align="left"><p>Indicates that the driver manages the interrupt request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_getpolarity" data-raw-source="[&lt;em&gt;DxGetPolarity&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_getpolarity)"><em>DxGetPolarity</em></a></p></td>
<td align="left"><p>Returns the polarity (even or odd) of the current field being written by the VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_getpreviousautoflip" data-raw-source="[&lt;em&gt;DxGetPreviousAutoflip&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_getpreviousautoflip)"><em>DxGetPreviousAutoflip</em></a></p></td>
<td align="left"><p>Determines which surface received the previous field of video data for capture purposes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_gettransferstatus" data-raw-source="[&lt;em&gt;DxGetTransferStatus&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_gettransferstatus)"><em>DxGetTransferStatus</em></a></p></td>
<td align="left"><p>Determines which hardware bus master completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_lock" data-raw-source="[&lt;em&gt;DxLock&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_lock)"><em>DxLock</em></a></p></td>
<td align="left"><p>Locks the frame buffer so that it can be accessed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_setstate" data-raw-source="[&lt;em&gt;DxSetState&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_setstate)"><em>DxSetState</em></a></p></td>
<td align="left"><p>Switches from bob mode to weave mode, and vice versa.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_skipnextfield" data-raw-source="[&lt;em&gt;DxSkipNextField&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_skipnextfield)"><em>DxSkipNextField</em></a></p></td>
<td align="left"><p>Skips or reenables the next field.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/dxmini/nc-dxmini-pdx_transfer" data-raw-source="[&lt;em&gt;DxTransfer&lt;/em&gt;](/windows/win32/api/dxmini/nc-dxmini-pdx_transfer)"><em>DxTransfer</em></a></p></td>
<td align="left"><p>Bus masters data from a surface to the buffer specified in the memory descriptor list (MDL).</p></td>
</tr>
</tbody>
</table>

 

