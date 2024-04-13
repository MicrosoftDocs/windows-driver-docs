---
title: VPE Callback Functions
description: VPE Callback Functions
keywords:
- DirectX VPE support WDK DirectDraw , initialization
- drawing VPEs WDK DirectDraw , initialization
- DirectDraw VPEs WDK Windows 2000 display , initialization
- video port extensions WDK DirectDraw , initialization
- VPEs WDK DirectDraw , initialization
- initializing DirectX VPE functionality
- callback functions WDK video port extensions
ms.date: 04/20/2017
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
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_cancreatevideoport" data-raw-source="[&lt;em&gt;DdVideoPortCanCreate&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_cancreatevideoport)"><em>DdVideoPortCanCreate</em></a></p></td>
<td align="left"><p>Determines whether the driver can support a DirectDraw VPE object of the specified description.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_colorcontrol" data-raw-source="[&lt;em&gt;DdVideoPortColorControl&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_colorcontrol)"><em>DdVideoPortColorControl</em></a></p></td>
<td align="left"><p>Gets or sets the VPE object color controls.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_createvideoport" data-raw-source="[&lt;em&gt;DdVideoPortCreate&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_createvideoport)"><em>DdVideoPortCreate</em></a></p></td>
<td align="left"><p>Notifies the driver that DirectDraw created a VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_destroyvport" data-raw-source="[&lt;em&gt;DdVideoPortDestroy&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_destroyvport)"><em>DdVideoPortDestroy</em></a></p></td>
<td align="left"><p>Notifies the driver that DirectDraw destroyed the specified VPE object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_flip" data-raw-source="[&lt;em&gt;DdVideoPortFlip&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_flip)"><em>DdVideoPortFlip</em></a></p></td>
<td align="left"><p>Performs a physical flip, causing the VPE object to start writing data to the new surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getbandwidth" data-raw-source="[&lt;em&gt;DdVideoPortGetBandwidth&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getbandwidth)"><em>DdVideoPortGetBandwidth</em></a></p></td>
<td align="left"><p>Reports the bandwidth limitations of the device's frame buffer memory based on the specified VPE object output format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getvportconnect" data-raw-source="[&lt;em&gt;DdVideoPortGetConnectInfo&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getvportconnect)"><em>DdVideoPortGetConnectInfo</em></a></p></td>
<td align="left"><p>Returns the connections supported by the specified VPE object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getfield" data-raw-source="[&lt;em&gt;DdVideoPortGetField&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getfield)"><em>DdVideoPortGetField</em></a></p></td>
<td align="left"><p>Determines whether the current field of an interlaced signal is even or odd.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getflipstatus" data-raw-source="[&lt;em&gt;DdVideoPortGetFlipStatus&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getflipstatus)"><em>DdVideoPortGetFlipStatus</em></a></p></td>
<td align="left"><p>Determines whether the most recently requested flip on a surface has occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getinputformats" data-raw-source="[&lt;em&gt;DdVideoPortGetInputFormats&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getinputformats)"><em>DdVideoPortGetInputFormats</em></a></p></td>
<td align="left"><p>Determines the input formats that the DirectDraw VPE object can accept.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getline" data-raw-source="[&lt;em&gt;DdVideoPortGetLine&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getline)"><em>DdVideoPortGetLine</em></a></p></td>
<td align="left"><p>Returns the current line number of the hardware video port.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getoutputformats" data-raw-source="[&lt;em&gt;DdVideoPortGetOutputFormats&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getoutputformats)"><em>DdVideoPortGetOutputFormats</em></a></p></td>
<td align="left"><p>Determines the output formats that the VPE object supports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getsignalstatus" data-raw-source="[&lt;em&gt;DdVideoPortGetSignalStatus&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_getsignalstatus)"><em>DdVideoPortGetSignalStatus</em></a></p></td>
<td align="left"><p>Retrieves the status of the video signal currently being presented to the hardware video port.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_update" data-raw-source="[&lt;em&gt;DdVideoPortUpdate&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_update)"><em>DdVideoPortUpdate</em></a></p></td>
<td align="left"><p>Starts and stops the VPE object and modifies the VPE object data stream.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_waitforsync" data-raw-source="[&lt;em&gt;DdVideoPortWaitForSync&lt;/em&gt;](/windows/win32/api/ddrawint/nc-ddrawint-pdd_vportcb_waitforsync)"><em>DdVideoPortWaitForSync</em></a></p></td>
<td align="left"><p>Waits until the next vertical synch occurs.</p></td>
</tr>
</tbody>
</table>

 

