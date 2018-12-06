---
title: Video Control Properties
description: Video Control Properties
ms.assetid: 3b39295f-b4fa-4d6a-bad8-f759bda284b1
keywords:
- video control properties WDK video capture
- control properties WDK video capture
- PROPSETID_VIDCAP_VIDEOCONTROL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Control Properties


The [PROPSETID\_VIDCAP\_VIDEOCONTROL](https://msdn.microsoft.com/library/windows/hardware/ff568120) property set contains properties related to the control and capabilities of video hardware, such as the available frame rates that the hardware can capture at and the orientation of the video image. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_VIDEOCONTROL property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_VIDEOCONTROL KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566035" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566035)"><strong>KSPROPERTY_VIDEOCONTROL_CAPS</strong></a></p></td>
<td><p>Returns information on the capabilities of the video stream, such as image orientation and triggering acquisition of a frame of video from the stream.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566024" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566024)"><strong>KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE</strong></a></p></td>
<td><p>Returns the actual frame rate for which the hardware is streaming video for a specific pin.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566040" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_FRAME_RATES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566040)"><strong>KSPROPERTY_VIDEOCONTROL_FRAME_RATES</strong></a></p></td>
<td><p>Returns the number of available frame rates that the device can stream video at.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566042" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_MODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566042)"><strong>KSPROPERTY_VIDEOCONTROL_MODE</strong></a></p></td>
<td><p>Controls the modes for a video stream, such as image flipping and triggering acquisition of a frame of video from the stream.</p></td>
</tr>
</tbody>
</table>

 

 

 




