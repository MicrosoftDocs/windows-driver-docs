---
title: VPE Callback Functions
description: VPE Callback Functions
ms.assetid: c36e99a5-0657-4945-b5e8-21d875e9d1ec
keywords:
- DirectX VPE support WDK DirectDraw , initialization
- drawing VPEs WDK DirectDraw , initialization
- DirectDraw VPEs WDK Windows 2000 display , initialization
- video port extensions WDK DirectDraw , initialization
- VPEs WDK DirectDraw , initialization
- initializing DirectX VPE functionality
- callback functions WDK video port extensions
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550375" data-raw-source="[&lt;em&gt;DdVideoPortCanCreate&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550375)"><em>DdVideoPortCanCreate</em></a></p></td>
<td align="left"><p>Determines whether the driver can support a DirectDraw VPE object of the specified description.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550383" data-raw-source="[&lt;em&gt;DdVideoPortColorControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550383)"><em>DdVideoPortColorControl</em></a></p></td>
<td align="left"><p>Gets or sets the VPE object color controls.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550391" data-raw-source="[&lt;em&gt;DdVideoPortCreate&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550391)"><em>DdVideoPortCreate</em></a></p></td>
<td align="left"><p>Notifies the driver that DirectDraw created a VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550406" data-raw-source="[&lt;em&gt;DdVideoPortDestroy&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550406)"><em>DdVideoPortDestroy</em></a></p></td>
<td align="left"><p>Notifies the driver that DirectDraw destroyed the specified VPE object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550408" data-raw-source="[&lt;em&gt;DdVideoPortFlip&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550408)"><em>DdVideoPortFlip</em></a></p></td>
<td align="left"><p>Performs a physical flip, causing the VPE object to start writing data to the new surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550413" data-raw-source="[&lt;em&gt;DdVideoPortGetBandwidth&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550413)"><em>DdVideoPortGetBandwidth</em></a></p></td>
<td align="left"><p>Reports the bandwidth limitations of the device&#39;s frame buffer memory based on the specified VPE object output format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550415" data-raw-source="[&lt;em&gt;DdVideoPortGetConnectInfo&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550415)"><em>DdVideoPortGetConnectInfo</em></a></p></td>
<td align="left"><p>Returns the connections supported by the specified VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550420" data-raw-source="[&lt;em&gt;DdVideoPortGetField&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550420)"><em>DdVideoPortGetField</em></a></p></td>
<td align="left"><p>Determines whether the current field of an interlaced signal is even or odd.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550425" data-raw-source="[&lt;em&gt;DdVideoPortGetFlipStatus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550425)"><em>DdVideoPortGetFlipStatus</em></a></p></td>
<td align="left"><p>Determines whether the most recently requested flip on a surface has occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550430" data-raw-source="[&lt;em&gt;DdVideoPortGetInputFormats&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550430)"><em>DdVideoPortGetInputFormats</em></a></p></td>
<td align="left"><p>Determines the input formats that the DirectDraw VPE object can accept.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550435" data-raw-source="[&lt;em&gt;DdVideoPortGetLine&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550435)"><em>DdVideoPortGetLine</em></a></p></td>
<td align="left"><p>Returns the current line number of the hardware video port.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550440" data-raw-source="[&lt;em&gt;DdVideoPortGetOutputFormats&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550440)"><em>DdVideoPortGetOutputFormats</em></a></p></td>
<td align="left"><p>Determines the output formats that the VPE object supports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550441" data-raw-source="[&lt;em&gt;DdVideoPortGetSignalStatus&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550441)"><em>DdVideoPortGetSignalStatus</em></a></p></td>
<td align="left"><p>Retrieves the status of the video signal currently being presented to the hardware video port.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550450" data-raw-source="[&lt;em&gt;DdVideoPortUpdate&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550450)"><em>DdVideoPortUpdate</em></a></p></td>
<td align="left"><p>Starts and stops the VPE object and modifies the VPE object data stream.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550455" data-raw-source="[&lt;em&gt;DdVideoPortWaitForSync&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550455)"><em>DdVideoPortWaitForSync</em></a></p></td>
<td align="left"><p>Waits until the next vertical synch occurs.</p></td>
</tr>
</tbody>
</table>

 

 

 





