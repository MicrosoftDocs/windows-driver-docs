---
title: KSPROPERTY\_AC3\_ROOM\_TYPE
description: The KSPROPERTY\_AC3\_ROOM\_TYPE property specifies the type and calibration of the mixing room in which the final audio session was produced.
keywords: ["KSPROPERTY_AC3_ROOM_TYPE Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_AC3_ROOM_TYPE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_AC3\_ROOM\_TYPE


The KSPROPERTY\_AC3\_ROOM\_TYPE property specifies the type and calibration of the mixing room in which the final audio session was produced.

## <span id="ddk_ksproperty_ac3_room_type_ks"></span><span id="DDK_KSPROPERTY_AC3_ROOM_TYPE_KS"></span>


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
<td align="left"><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](../stream/ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_room_type" data-raw-source="[&lt;strong&gt;KSAC3_ROOM_TYPE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_room_type)"><strong>KSAC3_ROOM_TYPE</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSAC3\_ROOM\_TYPE structure that specifies the type of mixing room in which the AC-3-encoded stream was produced.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AC3\_ROOM\_TYPE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

This property provides information about the production environment of the AC-3-encoded stream. The property value is not typically used by the AC-3 decoder, but might be used by other audio components.

If the encoded stream does not specify a room type, the property request returns an error code.

## Requirements

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


[**KSPROPERTY**](../stream/ksproperty-structure.md)

[**KSAC3\_ROOM\_TYPE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksac3_room_type)
