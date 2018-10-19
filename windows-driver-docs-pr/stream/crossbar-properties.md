---
title: Crossbar Properties
author: windows-driver-content
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
<td><p>[<strong>KSPROPERTY_CROSSBAR_CAN_ROUTE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565117)</p></td>
<td><p>Returns information on whether a specific routing is possible.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CROSSBAR_CAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565118)</p></td>
<td><p>Returns the capabilities of the crossbar, including the number of input pins and the number of output pins.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_CROSSBAR_PININFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565121)</p></td>
<td><p>Returns the pin information, such as the direction of dataflow, pin medium GUIDs, and pin type.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_CROSSBAR_ROUTE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565126)</p></td>
<td><p>Controls a specific routing, including which input pin to route to which output pin.</p></td>
</tr>
</tbody>
</table>

 

 

 




