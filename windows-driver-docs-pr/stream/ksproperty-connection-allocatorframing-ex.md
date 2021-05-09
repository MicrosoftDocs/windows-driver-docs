---
title: KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX
description: AVStream clients use the KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX property to determine framing requirements for a pin.
keywords: ["KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX


AVStream clients use the KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX property to determine framing requirements for a pin.

## <span id="ddk_ksproperty_connection_allocatorframing_ex_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX_KS"></span>


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
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing_ex" data-raw-source="[&lt;strong&gt;KSALLOCATOR_FRAMING_EX&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing_ex)"><strong>KSALLOCATOR_FRAMING_EX</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

This property returns a [**KSALLOCATOR\_FRAMING\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing_ex), which describes the framing requirements for an AVStream pin.

Minidrivers running under stream class should use [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING**](ksproperty-connection-allocatorframing.md).

See [KS Allocators](./ks-allocators.md). and [AVStream Allocators](./avstream-allocators.md).

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


[**KSALLOCATOR\_FRAMING\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing_ex)

