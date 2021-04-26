---
title: Crossbar Properties
description: Crossbar Properties
keywords:
- crossbar properties WDK video capture
- PROPSETID_VIDCAP_CROSSBAR
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Crossbar Properties


The [PROPSETID\_VIDCAP\_CROSSBAR](./propsetid-vidcap-crossbar.md) property set contains properties related to the routing of data from video input pins (with corresponding audio, if present) to output pins. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_CROSSBAR property set.

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
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-crossbar-can-route" data-raw-source="[&lt;strong&gt;KSPROPERTY_CROSSBAR_CAN_ROUTE&lt;/strong&gt;](./ksproperty-crossbar-can-route.md)"><strong>KSPROPERTY_CROSSBAR_CAN_ROUTE</strong></a></p></td>
<td><p>Returns information on whether a specific routing is possible.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-crossbar-caps" data-raw-source="[&lt;strong&gt;KSPROPERTY_CROSSBAR_CAPS&lt;/strong&gt;](./ksproperty-crossbar-caps.md)"><strong>KSPROPERTY_CROSSBAR_CAPS</strong></a></p></td>
<td><p>Returns the capabilities of the crossbar, including the number of input pins and the number of output pins.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-crossbar-pininfo" data-raw-source="[&lt;strong&gt;KSPROPERTY_CROSSBAR_PININFO&lt;/strong&gt;](./ksproperty-crossbar-pininfo.md)"><strong>KSPROPERTY_CROSSBAR_PININFO</strong></a></p></td>
<td><p>Returns the pin information, such as the direction of dataflow, pin medium GUIDs, and pin type.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-crossbar-route" data-raw-source="[&lt;strong&gt;KSPROPERTY_CROSSBAR_ROUTE&lt;/strong&gt;](./ksproperty-crossbar-route.md)"><strong>KSPROPERTY_CROSSBAR_ROUTE</strong></a></p></td>
<td><p>Controls a specific routing, including which input pin to route to which output pin.</p></td>
</tr>
</tbody>
</table>

 

