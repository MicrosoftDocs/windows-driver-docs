---
title: Kernel-Mode Video Transport Callback Functions
description: Kernel-Mode Video Transport Callback Functions
ms.assetid: 1edd5b68-91da-4846-87bd-6fcabb9e5abf
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557409" data-raw-source="[&lt;em&gt;DxBobNextField&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557409)"><em>DxBobNextField</em></a></p></td>
<td align="left"><p>Bobs the next field of interleaved data.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557413" data-raw-source="[&lt;em&gt;DxEnableIRQ&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557413)"><em>DxEnableIRQ</em></a></p></td>
<td align="left"><p>Indicates to the miniport driver which IRQs should be enabled or disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557417" data-raw-source="[&lt;em&gt;DxFlipOverlay&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557417)"><em>DxFlipOverlay</em></a></p></td>
<td align="left"><p>Flips the overlay.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557420" data-raw-source="[&lt;em&gt;DxFlipVideoPort&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557420)"><em>DxFlipVideoPort</em></a></p></td>
<td align="left"><p>Flips the video port extensions (VPE) object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557427" data-raw-source="[&lt;em&gt;DxGetCurrentAutoflip&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557427)"><em>DxGetCurrentAutoflip</em></a></p></td>
<td align="left"><p>Determines which surface is receiving the current field of video data for capture purposes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557428" data-raw-source="[&lt;em&gt;DxGetIRQInfo&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557428)"><em>DxGetIRQInfo</em></a></p></td>
<td align="left"><p>Indicates that the driver manages the interrupt request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557431" data-raw-source="[&lt;em&gt;DxGetPolarity&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557431)"><em>DxGetPolarity</em></a></p></td>
<td align="left"><p>Returns the polarity (even or odd) of the current field being written by the VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557437" data-raw-source="[&lt;em&gt;DxGetPreviousAutoflip&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557437)"><em>DxGetPreviousAutoflip</em></a></p></td>
<td align="left"><p>Determines which surface received the previous field of video data for capture purposes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557438" data-raw-source="[&lt;em&gt;DxGetTransferStatus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557438)"><em>DxGetTransferStatus</em></a></p></td>
<td align="left"><p>Determines which hardware bus master completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562880" data-raw-source="[&lt;em&gt;DxLock&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562880)"><em>DxLock</em></a></p></td>
<td align="left"><p>Locks the frame buffer so that it can be accessed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562882" data-raw-source="[&lt;em&gt;DxSetState&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562882)"><em>DxSetState</em></a></p></td>
<td align="left"><p>Switches from bob mode to weave mode, and vice versa.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562885" data-raw-source="[&lt;em&gt;DxSkipNextField&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562885)"><em>DxSkipNextField</em></a></p></td>
<td align="left"><p>Skips or reenables the next field.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562887" data-raw-source="[&lt;em&gt;DxTransfer&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562887)"><em>DxTransfer</em></a></p></td>
<td align="left"><p>Bus masters data from a surface to the buffer specified in the memory descriptor list (MDL).</p></td>
</tr>
</tbody>
</table>

 

 

 





