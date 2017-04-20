---
title: Video Control Properties
author: windows-driver-content
description: Video Control Properties
ms.assetid: 3b39295f-b4fa-4d6a-bad8-f759bda284b1
keywords:
- video control properties WDK video capture
- control properties WDK video capture
- PROPSETID_VIDCAP_VIDEOCONTROL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>KSPROPERTY_VIDEOCONTROL_CAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566035)</p></td>
<td><p>Returns information on the capabilities of the video stream, such as image orientation and triggering acquisition of a frame of video from the stream.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VIDEOCONTROL_ACTUAL_FRAME_RATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566024)</p></td>
<td><p>Returns the actual frame rate for which the hardware is streaming video for a specific pin.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VIDEOCONTROL_FRAME_RATES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566040)</p></td>
<td><p>Returns the number of available frame rates that the device can stream video at.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VIDEOCONTROL_MODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566042)</p></td>
<td><p>Controls the modes for a video stream, such as image flipping and triggering acquisition of a frame of video from the stream.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Control%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


