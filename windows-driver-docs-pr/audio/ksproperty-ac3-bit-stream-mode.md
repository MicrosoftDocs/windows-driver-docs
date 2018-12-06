---
title: KSPROPERTY\_AC3\_BIT\_STREAM\_MODE
description: The KSPROPERTY\_AC3\_BIT\_STREAM\_MODE property specifies the bit-stream mode, which is the type of audio service that is encoded into an AC-3 stream.
ms.assetid: ee3705f5-f16d-4f5e-a551-bea8986d88b6
keywords: ["KSPROPERTY_AC3_BIT_STREAM_MODE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AC3_BIT_STREAM_MODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AC3\_BIT\_STREAM\_MODE


The KSPROPERTY\_AC3\_BIT\_STREAM\_MODE property specifies the bit-stream mode, which is the type of audio service that is encoded into an AC-3 stream.

## <span id="ddk_ksproperty_ac3_bit_stream_mode_ks"></span><span id="DDK_KSPROPERTY_AC3_BIT_STREAM_MODE_KS"></span>


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
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537077" data-raw-source="[&lt;strong&gt;KSAC3_BIT_STREAM_MODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537077)"><strong>KSAC3_BIT_STREAM_MODE</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSAC3\_BIT\_STREAM\_MODE structure that specifies the bit-stream mode.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AC3\_BIT\_STREAM\_MODE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSAC3\_BIT\_STREAM\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff537077)

 

 






