---
title: TV Audio Properties
author: windows-driver-content
description: TV Audio Properties
ms.assetid: 0eed4007-9fd9-4927-8ac7-2e23fd082dec
keywords:
- TV audio properties WDK video capture
- audio properties WDK video capture
- PROPSETID_VIDCAP_TVAUDIO
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 




