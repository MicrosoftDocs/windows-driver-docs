---
title: Video Decoder Properties
author: windows-driver-content
description: Video Decoder Properties
ms.assetid: 671a310b-52a6-49f0-8848-e586a37c25ff
keywords:
- video decoder properties WDK video capture
- decoder properties WDK video capture
- PROPSETID_VIDCAP_VIDEODECODER
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Decoder Properties


The [PROPSETID\_VIDCAP\_VIDEODECODER](https://msdn.microsoft.com/library/windows/hardware/ff568121) property set contains properties related to the operation of analog video decoder devices, such as the transmission standard and timing signals. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_VIDEODECODER property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_VIDEODECODER KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VIDEODECODER_CAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566046)</p></td>
<td><p>Returns information on the capabilities of the video decoder device, such as signal standard (NTSC, PAL, SECAM) and settling time.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VIDEODECODER_STANDARD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566058)</p></td>
<td><p>Controls the current analog video standard.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VIDEODECODER_STATUS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566060)</p></td>
<td><p>Returns the status of the video decoding device, such as number of lines in the video signal and whether the signal is locked.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566051)</p></td>
<td><p>Controls three-state output of the video decoder.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_VIDEODECODER_VCR_TIMING</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566062)</p></td>
<td><p>Controls whether the video decoder uses VCR timing or broadcast timing.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Decoder%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


