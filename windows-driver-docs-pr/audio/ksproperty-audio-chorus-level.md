---
title: KSPROPERTY\_AUDIO\_CHORUS\_LEVEL
description: The KSPROPERTY\_AUDIO\_CHORUS\_LEVEL property specifies the chorus level. This is a property of a chorus node (KSNODETYPE\_CHORUS).
keywords: ["KSPROPERTY_AUDIO_CHORUS_LEVEL Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_AUDIO_CHORUS_LEVEL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_AUDIO\_CHORUS\_LEVEL


The KSPROPERTY\_AUDIO\_CHORUS\_LEVEL property specifies the chorus level. This is a property of a chorus node ([**KSNODETYPE\_CHORUS**](ksnodetype-chorus.md)).

## <span id="ddk_ksproperty_audio_chorus_level_ks"></span><span id="DDK_KSPROPERTY_AUDIO_CHORUS_LEVEL_KS"></span>


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
<td align="left"><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)"><strong>KSNODEPROPERTY</strong></a></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies the chorus level. Chorus-level values follow a linear range from 0 to 100\*(65536-1/65536) percent:

-   The value 0x00010000 represents 100 percent.

-   The value 0xFFFFFFFF represents 100\*(65536-1/65536) percent.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_CHORUS\_LEVEL property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

This property is used to get and set the volume level of the chorus echo.

Chorus is a voice-doubling effect that is created by echoing the original sound with a slight delay and slightly modulating the delay of the echo. For more information, see the description of the **IDirectSoundFXChorus** interface in the Microsoft Windows SDK documentation.

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


[**KSNODETYPE\_CHORUS**](ksnodetype-chorus.md)

[**KSNODEPROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)

