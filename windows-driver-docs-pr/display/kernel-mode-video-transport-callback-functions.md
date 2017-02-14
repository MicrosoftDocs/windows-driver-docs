---
title: Kernel-Mode Video Transport Callback Functions
description: Kernel-Mode Video Transport Callback Functions
ms.assetid: 1edd5b68-91da-4846-87bd-6fcabb9e5abf
keywords: ["DxApi miniport drivers WDK DirectDraw , kernel-mode video transport callback functions", "kernel-mode video transport WDK DirectDraw , callback functions", "callback functions WDK kernel-mode video transport"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Kernel-Mode%20Video%20Transport%20Callback%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




