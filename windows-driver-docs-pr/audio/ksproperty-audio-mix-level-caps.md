---
title: KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS
description: The KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS property specifies the mix-level capabilities of a supermixer node (KSNODETYPE\_SUPERMIX). A single get-property request retrieves information for all combinations of input and output channels.
ms.assetid: ab7a5dfb-8975-41bb-9347-953406701804
keywords: ["KSPROPERTY_AUDIO_MIX_LEVEL_CAPS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_MIX_LEVEL_CAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS


The KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS property specifies the mix-level capabilities of a supermixer node ([**KSNODETYPE\_SUPERMIX**](ksnodetype-supermix.md)). A single *get*-property request retrieves information for all combinations of input and output channels.

## <span id="ddk_ksproperty_audio_mix_level_caps_ks"></span><span id="DDK_KSPROPERTY_AUDIO_MIX_LEVEL_CAPS_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537088" data-raw-source="[&lt;strong&gt;KSAUDIO_MIXCAP_TABLE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537088)"><strong>KSAUDIO_MIXCAP_TABLE</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSAUDIO\_MIXCAP\_TABLE, which specifies the capabilities of all *m*\**n* input-output pathways in a supermixer node with *m* input channels and *n* output channels.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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


[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSAUDIO\_MIXCAP\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff537088)

[**KSNODETYPE\_SUPERMIX**](ksnodetype-supermix.md)

 

 






