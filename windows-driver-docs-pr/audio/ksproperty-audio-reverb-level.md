---
title: KSPROPERTY\_AUDIO\_REVERB\_LEVEL
description: The KSPROPERTY\_AUDIO\_REVERB\_LEVEL property specifies the current reverberation level. This is a property of a reverb node (KSNODETYPE\_REVERB).
ms.assetid: f38396a2-5528-4085-a051-fcfb73e9c1d1
keywords: ["KSPROPERTY_AUDIO_REVERB_LEVEL Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_REVERB_LEVEL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_REVERB\_LEVEL


The KSPROPERTY\_AUDIO\_REVERB\_LEVEL property specifies the current reverberation level. This is a property of a reverb node ([**KSNODETYPE\_REVERB**](ksnodetype-reverb.md)).

## <span id="ddk_ksproperty_audio_reverb_level_ks"></span><span id="DDK_KSPROPERTY_AUDIO_REVERB_LEVEL_KS"></span>


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
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies the reverberation level. Reverb values follow a linear range from 0 to 100\*(65536-1/65536) percent:

-   The value 0x00010000 represents 100 percent.

-   The value 0xFFFFFFFF represents 100\*(65536-1/65536) percent.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_REVERB\_LEVEL property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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


[**KSNODETYPE\_REVERB**](ksnodetype-reverb.md)

[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

 

 






