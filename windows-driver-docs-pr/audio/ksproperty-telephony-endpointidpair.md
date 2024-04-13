---
title: KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR
description: The KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR property contains the render and capture endpoints for cellular audio routing.
keywords: ["KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR


The **KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR** property contains the render and capture endpoints for cellular audio routing.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](../stream/ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointidpair" data-raw-source="[&lt;strong&gt;KSTOPOLOGY_ENDPOINTIDPAIR&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointidpair)"><strong>KSTOPOLOGY_ENDPOINTIDPAIR</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value is of type [**KSTOPOLOGY\_ENDPOINTIDPAIR**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointidpair), which specifies the render and capture endpoints.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR** property request returns the render and capture endpoints for cellular audio routing.

## Remarks

Cellular routing is controlled by **KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR** property on the topology filter. This property takes a pair of [**KSTOPOLOGY\_ENDPOINTID**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointid) structures for the requested endpoint combination. **KSTOPOLOGY\_ENDPOINTID** contains a reference string for the topology filter of an endpoint and a topology filter pin ID to which the endpoint is connected. The driver provides basic support for this property and returns all of the valid pairs of render and capture endpoints that can be used for cellular audio routing. It is the driver’s responsibility to handle moving both render and capture cellular audio to this new endpoint combination, meeting whatever constraints are necessary for the hardware. This property must be settable even when there is no active phone call in the system.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>None supported</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Client</p></td>
<td align="left"><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>
