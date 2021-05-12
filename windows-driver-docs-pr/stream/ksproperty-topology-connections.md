---
title: KSPROPERTY\_TOPOLOGY\_CONNECTIONS
description: The KSPROPERTY\_TOPOLOGY\_CONNECTIONS property queries all connections between nodes of a KS filter.
keywords: ["KSPROPERTY_TOPOLOGY_CONNECTIONS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TOPOLOGY_CONNECTIONS
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TOPOLOGY\_CONNECTIONS


The KSPROPERTY\_TOPOLOGY\_CONNECTIONS property queries all connections between nodes of a KS filter.

## <span id="ddk_ksproperty_topology_connections_ks"></span><span id="DDK_KSPROPERTY_TOPOLOGY_CONNECTIONS_KS"></span>


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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p>A <a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)"><strong>KSMULTIPLE_ITEM</strong></a> structure, followed by a sequence of <a href="/windows-hardware/drivers/ddi/ks/ns-ks-kstopology_connection" data-raw-source="[&lt;strong&gt;KSTOPOLOGY_CONNECTION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kstopology_connection)"><strong>KSTOPOLOGY_CONNECTION</strong></a> structures.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The KSMULTIPLE\_ITEM header is followed by a KSTOPOLOGY\_CONNECTION structure, which describes a single data-path connection in a KS filter.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSMULTIPLE\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KSTOPOLOGY\_CONNECTION**](/windows-hardware/drivers/ddi/ks/ns-ks-kstopology_connection)

