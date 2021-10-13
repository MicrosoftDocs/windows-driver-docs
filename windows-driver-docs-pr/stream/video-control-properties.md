---
title: Video Control Properties
description: Video Control Properties
keywords:
- video control properties WDK video capture
- control properties WDK video capture
- PROPSETID_VIDCAP_VIDEOCONTROL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Control Properties


The [PROPSETID\_VIDCAP\_VIDEOCONTROL](./propsetid-vidcap-videocontrol.md) property set contains properties related to the control and capabilities of video hardware, such as the available frame rates that the hardware can capture at and the orientation of the video image. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_VIDEOCONTROL property set.

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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-videocontrol-caps" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_CAPS&lt;/strong&gt;](./ksproperty-videocontrol-caps.md)"><strong>KSPROPERTY_VIDEOCONTROL_CAPS</strong></a></p></td>
<td><p>Returns information on the capabilities of the video stream, such as image orientation and triggering acquisition of a frame of video from the stream.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-videocontrol-actual-frame-rate" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE&lt;/strong&gt;](./ksproperty-videocontrol-actual-frame-rate.md)"><strong>KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE</strong></a></p></td>
<td><p>Returns the actual frame rate for which the hardware is streaming video for a specific pin.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-videocontrol-frame-rates" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_FRAME_RATES&lt;/strong&gt;](./ksproperty-videocontrol-frame-rates.md)"><strong>KSPROPERTY_VIDEOCONTROL_FRAME_RATES</strong></a></p></td>
<td><p>Returns the number of available frame rates that the device can stream video at.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-videocontrol-mode" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCONTROL_MODE&lt;/strong&gt;](./ksproperty-videocontrol-mode.md)"><strong>KSPROPERTY_VIDEOCONTROL_MODE</strong></a></p></td>
<td><p>Controls the modes for a video stream, such as image flipping and triggering acquisition of a frame of video from the stream.</p></td>
</tr>
</tbody>
</table>

 

