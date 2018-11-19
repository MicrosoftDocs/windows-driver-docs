---
title: TV Audio Properties
description: TV Audio Properties
ms.assetid: 0eed4007-9fd9-4927-8ac7-2e23fd082dec
keywords:
- TV audio properties WDK video capture
- audio properties WDK video capture
- PROPSETID_VIDCAP_TVAUDIO
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565933" data-raw-source="[&lt;strong&gt;KSPROPERTY_TVAUDIO_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565933)"><strong>KSPROPERTY_TVAUDIO_CAPS</strong></a></p></td>
<td><p>Returns information about the capabilities of the TV audio device, such as whether the hardware supports mono or stereo audio and SAP.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565942" data-raw-source="[&lt;strong&gt;KSPROPERTY_TVAUDIO_CURRENTLY_AVAILABLE_MODES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565942)"><strong>KSPROPERTY_TVAUDIO_CURRENTLY_AVAILABLE_MODES</strong></a></p></td>
<td><p>Returns the currently available TV audio modes, at the time the property was queried.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565944" data-raw-source="[&lt;strong&gt;KSPROPERTY_TVAUDIO_MODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565944)"><strong>KSPROPERTY_TVAUDIO_MODE</strong></a></p></td>
<td><p>Controls the current audio mode for the TV audio device.</p></td>
</tr>
</tbody>
</table>

 

 

 




