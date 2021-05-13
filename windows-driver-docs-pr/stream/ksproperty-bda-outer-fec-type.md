---
title: KSPROPERTY\_BDA\_OUTER\_FEC\_TYPE
description: Clients use KSPROPERTY\_BDA\_OUTER\_FEC\_TYPE to control the outer forward error correction (FEC) type of a demodulator node.
keywords: ["KSPROPERTY_BDA_OUTER_FEC_TYPE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_OUTER_FEC_TYPE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_OUTER\_FEC\_TYPE


Clients use KSPROPERTY\_BDA\_OUTER\_FEC\_TYPE to control the outer forward error correction (FEC) type of a demodulator node.

## <span id="ddk_ksproperty_bda_outer_fec_type_ks"></span><span id="DDK_KSPROPERTY_BDA_OUTER_FEC_TYPE_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>FECMethod</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The returned value from the FECMethod enumerated type identifies an FEC type.

The **NodeId** member of KSP\_NODE specifies the identifier of the demodulator node.

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


[**FECMethod**](/previous-versions/windows/desktop/mstv/fecmethod)

[**KSP\_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

 

