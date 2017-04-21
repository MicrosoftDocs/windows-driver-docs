---
title: Video Compression Properties
author: windows-driver-content
description: Video Compression Properties
ms.assetid: 2fd69425-7c36-4766-88e6-7f02d5fa6659
keywords:
- video compression properties WDK video capture
- compression properties WDK video capture
- PROPSETID_VIDCAP_VIDEOCOMPRESSION
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Compression Properties


The [PROPSETID\_VIDCAP\_VIDEOCOMPRESSION](https://msdn.microsoft.com/library/windows/hardware/ff567813) property set contains properties related to the video compression. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_VIDEOCOMPRESSION property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_VIDEOCOMPRESSION KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VIDEOCOMPRESSION_GETINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565975)</p></td>
<td><p>Returns information about the video compression capabilities of the device.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VIDEOCOMPRESSION_KEYFRAME_RATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565986)</p></td>
<td><p>Controls the keyframe rate of the video compression.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_FRAME_SIZE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565991)</p></td>
<td><p>Specifies a temporary new frame size to override the current size.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_KEYFRAME</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566004)</p></td>
<td><p>Specifies a temporary new keyframe rate to override the current rate.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VIDEOCOMPRESSION_PFRAMES_PER_KEYFRAME</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566009)</p></td>
<td><p>Controls the predicted frame interval.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VIDEOCOMPRESSION_QUALITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566015)</p></td>
<td><p>Controls the video compression quality setting.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VIDEOCOMPRESSION_WINDOWSIZE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566019)</p></td>
<td><p>Controls the data rate of the average video frame.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Compression%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


