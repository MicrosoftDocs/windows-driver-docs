---
title: TV Audio Properties
author: windows-driver-content
description: TV Audio Properties
ms.assetid: 0eed4007-9fd9-4927-8ac7-2e23fd082dec
keywords: ["TV audio properties WDK video capture", "audio properties WDK video capture", "PROPSETID_VIDCAP_TVAUDIO"]
---

# TV Audio Properties


The [PROPSETID\_VIDCAP\_TVAUDIO](https://msdn.microsoft.com/library/windows/hardware/ff567811) property set contains properties related to TV audio. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_TVAUDIO property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_TVAUDIO KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_TVAUDIO_CAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565933)</p></td>
<td><p>Returns information about the capabilities of the TV audio device, such as whether the hardware supports mono or stereo audio and SAP.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_TVAUDIO_CURRENTLY_AVAILABLE_MODES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565942)</p></td>
<td><p>Returns the currently available TV audio modes, at the time the property was queried.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_TVAUDIO_MODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565944)</p></td>
<td><p>Controls the current audio mode for the TV audio device.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20TV%20Audio%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


