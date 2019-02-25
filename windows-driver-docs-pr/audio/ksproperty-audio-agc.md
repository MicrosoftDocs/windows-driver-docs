---
title: KSPROPERTY\_AUDIO\_AGC
description: The KSPROPERTY\_AUDIO\_AGC property specifies the state of the AGC (automatic gain control) for a channel in an AGC node (KSNODETYPE\_AGC).
ms.assetid: 72630e9b-a1e7-4319-831a-94f8b856cf93
keywords: ["KSPROPERTY_AUDIO_AGC Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_AGC
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_AGC


The KSPROPERTY\_AUDIO\_AGC property specifies the state of the AGC (automatic gain control) for a channel in an AGC node ([**KSNODETYPE\_AGC**](ksnodetype-agc.md)).

## <span id="ddk_ksproperty_audio_agc_ks"></span><span id="DDK_KSPROPERTY_AUDIO_AGC_KS"></span>


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
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff537145" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY_AUDIO_CHANNEL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537145)"><strong>KSNODEPROPERTY_AUDIO_CHANNEL</strong></a></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type BOOL and indicates whether AGC is turned on or off. A value of **TRUE** indicates that the AGC is on. **FALSE** indicates that it is off.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_AGC property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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


[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537145)

[**KSNODETYPE\_AGC**](ksnodetype-agc.md)

 

 






