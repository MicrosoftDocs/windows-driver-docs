---
title: KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH
description: The KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH property specifies the chorus modulation depth. This is a property of a chorus node (KSNODETYPE\_CHORUS).
ms.assetid: A14DA707-7ED6-4E86-87C7-9A4E40062FE8
keywords: ["KSPROPERTY_AUDIO_CHORUS_MODULATION_DEPTH Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_CHORUS_MODULATION_DEPTH
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH


The KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH property specifies the chorus modulation depth. This is a property of a chorus node ([**KSNODETYPE\_CHORUS**](ksnodetype-chorus.md)).

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
<td align="left"><p>KSNODEPROPERTY</p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value is of type ULONG and it specifies the chorus modulation depth. It is expressed in milliseconds and sets the speed (frequency) of the modulator. The value can range from 0 to 255.9961 in 1/256th increments. To accommodate this, the property value should be expressed as a fixed point 16.16 value, where the following is true:

-   The value 0x00010000 represents 1 ms
-   The value 0xFFFFFFFF represents (65536-1/65536) ms

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Windows Vista</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSNODETYPE\_CHORUS**](ksnodetype-chorus.md)

 

 






