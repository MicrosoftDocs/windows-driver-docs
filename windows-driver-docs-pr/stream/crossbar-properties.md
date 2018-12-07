---
title: Crossbar Properties
description: Crossbar Properties
ms.assetid: 41e46d45-90f8-4b0c-ab27-1fec4202b711
keywords:
- crossbar properties WDK video capture
- PROPSETID_VIDCAP_CROSSBAR
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Crossbar Properties


The [PROPSETID\_VIDCAP\_CROSSBAR](https://msdn.microsoft.com/library/windows/hardware/ff567804) property set contains properties related to the routing of data from video input pins (with corresponding audio, if present) to output pins. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_CROSSBAR property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_CROSSBAR KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565117" data-raw-source="[&lt;strong&gt;KSPROPERTY_CROSSBAR_CAN_ROUTE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565117)"><strong>KSPROPERTY_CROSSBAR_CAN_ROUTE</strong></a></p></td>
<td><p>Returns information on whether a specific routing is possible.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565118" data-raw-source="[&lt;strong&gt;KSPROPERTY_CROSSBAR_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565118)"><strong>KSPROPERTY_CROSSBAR_CAPS</strong></a></p></td>
<td><p>Returns the capabilities of the crossbar, including the number of input pins and the number of output pins.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565121" data-raw-source="[&lt;strong&gt;KSPROPERTY_CROSSBAR_PININFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565121)"><strong>KSPROPERTY_CROSSBAR_PININFO</strong></a></p></td>
<td><p>Returns the pin information, such as the direction of dataflow, pin medium GUIDs, and pin type.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565126" data-raw-source="[&lt;strong&gt;KSPROPERTY_CROSSBAR_ROUTE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565126)"><strong>KSPROPERTY_CROSSBAR_ROUTE</strong></a></p></td>
<td><p>Controls a specific routing, including which input pin to route to which output pin.</p></td>
</tr>
</tbody>
</table>

 

 

 




