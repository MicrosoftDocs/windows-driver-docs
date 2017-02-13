---
title: VPE Callback Functions
description: VPE Callback Functions
ms.assetid: c36e99a5-0657-4945-b5e8-21d875e9d1ec
keywords: ["DirectX VPE support WDK DirectDraw , initialization", "drawing VPEs WDK DirectDraw , initialization", "DirectDraw VPEs WDK Windows 2000 display , initialization", "video port extensions WDK DirectDraw , initialization", "VPEs WDK DirectDraw , initialization", "initializing DirectX VPE functionality", "callback functions WDK video port extensions"]
---

# VPE Callback Functions


## <span id="ddk_vpe_callback_functions_gg"></span><span id="DDK_VPE_CALLBACK_FUNCTIONS_GG"></span>


The following table lists the video port extensions (VPE) callback functions that are implemented in a display driver. A display driver that supports VPE must implement some VPE callback functions; some are optional depending on the hardware capabilities.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">VPE Callback Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<em>DdVideoPortCanCreate</em>](https://msdn.microsoft.com/library/windows/hardware/ff550375)</p></td>
<td align="left"><p>Determines whether the driver can support a DirectDraw VPE object of the specified description.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdVideoPortColorControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff550383)</p></td>
<td align="left"><p>Gets or sets the VPE object color controls.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdVideoPortCreate</em>](https://msdn.microsoft.com/library/windows/hardware/ff550391)</p></td>
<td align="left"><p>Notifies the driver that DirectDraw created a VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdVideoPortDestroy</em>](https://msdn.microsoft.com/library/windows/hardware/ff550406)</p></td>
<td align="left"><p>Notifies the driver that DirectDraw destroyed the specified VPE object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdVideoPortFlip</em>](https://msdn.microsoft.com/library/windows/hardware/ff550408)</p></td>
<td align="left"><p>Performs a physical flip, causing the VPE object to start writing data to the new surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdVideoPortGetBandwidth</em>](https://msdn.microsoft.com/library/windows/hardware/ff550413)</p></td>
<td align="left"><p>Reports the bandwidth limitations of the device's frame buffer memory based on the specified VPE object output format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdVideoPortGetConnectInfo</em>](https://msdn.microsoft.com/library/windows/hardware/ff550415)</p></td>
<td align="left"><p>Returns the connections supported by the specified VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdVideoPortGetField</em>](https://msdn.microsoft.com/library/windows/hardware/ff550420)</p></td>
<td align="left"><p>Determines whether the current field of an interlaced signal is even or odd.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdVideoPortGetFlipStatus</em>](https://msdn.microsoft.com/library/windows/hardware/ff550425)</p></td>
<td align="left"><p>Determines whether the most recently requested flip on a surface has occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdVideoPortGetInputFormats</em>](https://msdn.microsoft.com/library/windows/hardware/ff550430)</p></td>
<td align="left"><p>Determines the input formats that the DirectDraw VPE object can accept.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdVideoPortGetLine</em>](https://msdn.microsoft.com/library/windows/hardware/ff550435)</p></td>
<td align="left"><p>Returns the current line number of the hardware video port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdVideoPortGetOutputFormats</em>](https://msdn.microsoft.com/library/windows/hardware/ff550440)</p></td>
<td align="left"><p>Determines the output formats that the VPE object supports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdVideoPortGetSignalStatus</em>](https://msdn.microsoft.com/library/windows/hardware/ff550441)</p></td>
<td align="left"><p>Retrieves the status of the video signal currently being presented to the hardware video port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>DdVideoPortUpdate</em>](https://msdn.microsoft.com/library/windows/hardware/ff550450)</p></td>
<td align="left"><p>Starts and stops the VPE object and modifies the VPE object data stream.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>DdVideoPortWaitForSync</em>](https://msdn.microsoft.com/library/windows/hardware/ff550455)</p></td>
<td align="left"><p>Waits until the next vertical synch occurs.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20VPE%20Callback%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




