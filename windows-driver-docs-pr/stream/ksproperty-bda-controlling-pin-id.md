---
title: KSPROPERTY\_BDA\_CONTROLLING\_PIN\_ID
description: Clients use KSPROPERTY\_BDA\_CONTROLLING\_PIN\_ID to retrieve the controlling pin for a node in the BDA template connection list.
keywords: ["KSPROPERTY_BDA_CONTROLLING_PIN_ID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_CONTROLLING_PIN_ID
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_CONTROLLING\_PIN\_ID


Clients use KSPROPERTY\_BDA\_CONTROLLING\_PIN\_ID to retrieve the controlling pin for a node in the BDA template connection list.

## <span id="ddk_ksproperty_bda_controlling_pin_id_ks"></span><span id="DDK_KSPROPERTY_BDA_CONTROLLING_PIN_ID_KS"></span>


### Usage Summary Table

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
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p>KSP_BDA_NODE_PIN</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The returned value specifies the controlling pin ID.

Nodes are associated with one pin in the filter, either an input pin or an output pin. Nodes can only be accessed through the controlling pin because nodes do not have their own file handle. The network provider can use this property and the KSP\_BDA\_NODE\_PIN structure to query for the controlling pin for each node in the BDA template connection list (KSTOPOLOGY\_CONNECTION or BDA\_TEMPLATE\_CONNECTION array).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**BdaPropertyGetControllingPinId**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertygetcontrollingpinid)

[**BDA\_TEMPLATE\_CONNECTION**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_template_connection)

[**KSP\_BDA\_NODE\_PIN**](/windows-hardware/drivers/ddi/bdamedia/ns-bdamedia-_ksp_bda_node_pin)

[**KSTOPOLOGY\_CONNECTION**](/windows-hardware/drivers/ddi/ks/ns-ks-kstopology_connection)

 

