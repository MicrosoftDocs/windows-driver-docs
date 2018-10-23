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
<td align="left"><p>[<em>DxBobNextField</em>](https://msdn.microsoft.com/library/windows/hardware/ff557409)</p></td>
<td align="left"><p>Bobs the next field of interleaved data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DxEnableIRQ</em>](https://msdn.microsoft.com/library/windows/hardware/ff557413)</p></td>
<td align="left"><p>Indicates to the miniport driver which IRQs should be enabled or disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DxFlipOverlay</em>](https://msdn.microsoft.com/library/windows/hardware/ff557417)</p></td>
<td align="left"><p>Flips the overlay.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DxFlipVideoPort</em>](https://msdn.microsoft.com/library/windows/hardware/ff557420)</p></td>
<td align="left"><p>Flips the video port extensions (VPE) object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DxGetCurrentAutoflip</em>](https://msdn.microsoft.com/library/windows/hardware/ff557427)</p></td>
<td align="left"><p>Determines which surface is receiving the current field of video data for capture purposes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DxGetIRQInfo</em>](https://msdn.microsoft.com/library/windows/hardware/ff557428)</p></td>
<td align="left"><p>Indicates that the driver manages the interrupt request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DxGetPolarity</em>](https://msdn.microsoft.com/library/windows/hardware/ff557431)</p></td>
<td align="left"><p>Returns the polarity (even or odd) of the current field being written by the VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DxGetPreviousAutoflip</em>](https://msdn.microsoft.com/library/windows/hardware/ff557437)</p></td>
<td align="left"><p>Determines which surface received the previous field of video data for capture purposes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DxGetTransferStatus</em>](https://msdn.microsoft.com/library/windows/hardware/ff557438)</p></td>
<td align="left"><p>Determines which hardware bus master completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DxLock</em>](https://msdn.microsoft.com/library/windows/hardware/ff562880)</p></td>
<td align="left"><p>Locks the frame buffer so that it can be accessed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DxSetState</em>](https://msdn.microsoft.com/library/windows/hardware/ff562882)</p></td>
<td align="left"><p>Switches from bob mode to weave mode, and vice versa.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DxSkipNextField</em>](https://msdn.microsoft.com/library/windows/hardware/ff562885)</p></td>
<td align="left"><p>Skips or reenables the next field.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DxTransfer</em>](https://msdn.microsoft.com/library/windows/hardware/ff562887)</p></td>
<td align="left"><p>Bus masters data from a surface to the buffer specified in the memory descriptor list (MDL).</p></td>
</tr>
</tbody>
</table>

 

 

 





