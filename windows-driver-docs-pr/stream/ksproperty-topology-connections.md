---
title: KSPROPERTY\_TOPOLOGY\_CONNECTIONS
description: The KSPROPERTY\_TOPOLOGY\_CONNECTIONS property queries all connections between nodes of a KS filter.
ms.assetid: 8ea77244-14c1-4e27-9b96-e0f5a6c491e9
keywords: ["KSPROPERTY_TOPOLOGY_CONNECTIONS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TOPOLOGY_CONNECTIONS
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>KSPROPERTY</strong>](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)</p></td>
<td><p>A [<strong>KSMULTIPLE_ITEM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563441) structure, followed by a sequence of [<strong>KSTOPOLOGY_CONNECTION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567148) structures.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The KSMULTIPLE\_ITEM header is followed by a KSTOPOLOGY\_CONNECTION structure, which describes a single data-path connection in a KS filter.

Requirements
------------

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


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

[**KSTOPOLOGY\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/ff567148)

 

 






