---
title: KSPROPERTY\_BDA\_SYMBOL\_RATE
description: Clients use KSPROPERTY\_BDA\_SYMBOL\_RATE to control the symbol rate of a demodulator node.
ms.assetid: 11e2e020-3037-4a68-a8d6-c68efd86a518
keywords: ["KSPROPERTY_BDA_SYMBOL_RATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SYMBOL_RATE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_SYMBOL\_RATE


Clients use KSPROPERTY\_BDA\_SYMBOL\_RATE to control the symbol rate of a demodulator node.

## <span id="ddk_ksproperty_bda_symbol_rate_ks"></span><span id="DDK_KSPROPERTY_BDA_SYMBOL_RATE_KS"></span>


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
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The returned value specifies the symbol rate.

The **NodeId** member of KSP\_NODE specifies the identifier of the demodulator node.

## See also


[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






