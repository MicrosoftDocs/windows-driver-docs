---
title: KSPROPERTY\_AUDIO\_REVERB\_TIME
description: The KSPROPERTY\_AUDIO\_REVERB\_TIME property specifies the reverberation time. This is a property of a reverb node (KSNODETYPE\_REVERB).
ms.assetid: ADB53E00-4E0F-4E13-92C7-5ACB1A0B546E
keywords: ["KSPROPERTY_AUDIO_REVERB_TIME Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_REVERB_TIME
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_REVERB\_TIME


The KSPROPERTY\_AUDIO\_REVERB\_TIME property specifies the reverberation time. This is a property of a reverb node ([**KSNODETYPE\_REVERB**](ksnodetype-reverb.md)).

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

 

The property value is of type ULONG, and it specifies the number of seconds for which the reverberation will continue. It is expressed in seconds and the value can range from 0 through 255.9961 in 1/256th increments. To accommodate this, the property value should be expressed as a fixed point 16.16 value, where the following is true:

-   The value 0x00010000 represents 1 second
-   The value 0xFFFFFFFF represents (65536-1/65536) seconds

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_REVERB\_TIME property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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


[**KSNODETYPE\_REVERB**](ksnodetype-reverb.md)

 

 






