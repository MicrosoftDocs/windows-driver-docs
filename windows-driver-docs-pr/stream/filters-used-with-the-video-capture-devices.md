---
title: Filters Used with the Video Capture Devices
description: Filters Used with the Video Capture Devices
ms.assetid: 797f855d-5c6f-45bc-8b4a-f03543fa196d
keywords:
- filter graph configurations WDK video capture , DirectShow
- DirectShow WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




