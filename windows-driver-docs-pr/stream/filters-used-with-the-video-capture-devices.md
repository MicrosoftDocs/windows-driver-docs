---
title: Filters Used with the Video Capture Devices
author: windows-driver-content
description: Filters Used with the Video Capture Devices
ms.assetid: 797f855d-5c6f-45bc-8b4a-f03543fa196d
keywords:
- filter graph configurations WDK video capture , DirectShow
- DirectShow WDK video capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Filters Used with the Video Capture Devices


Microsoft DirectShow is the common client for video capture minidrivers. User-mode DirectShow filters expose the capabilities contained in the video capture minidriver to user-mode applications.

Microsoft provides four DirectShow filters that work with Stream class minidrivers to expose the underlying video capture minidriver functionality:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Filter functionality</th>
<th>Property sets supported by kernel streaming</th>
<th>Purpose</th>
<th>DLL</th>
<th>DirectShow interfaces exposed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Video capture</p></td>
<td><p>PROPSETID_VIDCAP_DROPPEDFRAMES</p>
<p>PROPSETID_VIDCAP_VIDEOCOMPRESSION</p>
<p>PROPSETID_VIDCAP_VIDEOCONTROL</p>
<p>PROPSETID_VIDCAP_VIDEODECODER</p>
<p>PROPSETID_VIDCAP_CAMERAMCONTROL</p>
<p>PROPSETID_VIDCAP_VIDEOPROCAMP</p></td>
<td><p>Provides output streams of digital video data and ancillary data streams.</p></td>
<td><p><em>KsProxy.ax</em></p></td>
<td><p><strong>IAMAnalogVideoDecoder</strong></p>
<p><strong>IAMCameraControl</strong></p>
<p><strong>IAMVideoProcAmp</strong></p>
<p><strong>IAMDroppedFrames</strong></p>
<p><strong>IAMStreamConfig</strong></p>
<p><strong>IAMVideoControl</strong></p>
<p><strong>IAMVideoCompression</strong></p>
<p><strong>IAMBufferNegotiation</strong></p></td>
</tr>
<tr class="even">
<td><p>TV tuning</p></td>
<td><p>PROPSETID_TUNER</p></td>
<td><p>Provides tuning control of analog TV, digital TV, FM and AM tuners.</p></td>
<td><p><em>KsTvTune.ax</em></p></td>
<td><p><strong>IAMTVTuner</strong></p></td>
</tr>
<tr class="odd">
<td><p>TV audio</p></td>
<td><p>PROPSETID_VIDCAP_TVAUDIO</p></td>
<td><p>Provides control of TV audio such as SAP selection.</p></td>
<td><p><em>KsXBar.ax</em></p></td>
<td><p><strong>IAMTVAudio</strong></p></td>
</tr>
<tr class="even">
<td><p>Crossbar</p></td>
<td><p>PROPSETID_VIDCAP_CROSSBAR</p></td>
<td><p>Provides routing of video and audio streams.</p></td>
<td><p><em>KsXBar.ax</em></p></td>
<td><p><strong>IAMCrossbar</strong></p></td>
</tr>
</tbody>
</table>

 

Each of these filters, and the functionality they expose (video capture, TV/radio tuning, TV audio and crossbar) appears in a filter graph as a separate filter exposing unique interfaces.

For more information about the DirectShow interfaces listed in the table above, see the DirectShow Software Development Kit (SDK). The DirectShow SDK documentation also includes a sample application (AMCAP) that demonstrates how to construct the full range of both WDM and VfW capture graphs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Filters%20Used%20with%20the%20Video%20Capture%20Devices%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


