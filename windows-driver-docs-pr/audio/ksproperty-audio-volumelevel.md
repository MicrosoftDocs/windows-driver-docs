---
title: KSPROPERTY\_AUDIO\_VOLUMELEVEL
description: The KSPROPERTY\_AUDIO\_VOLUMELEVEL property specifies the volume level of a channel in a volume node (KSNODETYPE\_VOLUME).
ms.assetid: 5b420c71-fc82-413d-a93d-e8f3408cc8d7
keywords: ["KSPROPERTY_AUDIO_VOLUMELEVEL Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_VOLUMELEVEL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_VOLUMELEVEL


The KSPROPERTY\_AUDIO\_VOLUMELEVEL property specifies the volume level of a channel in a volume node ([**KSNODETYPE\_VOLUME**](ksnodetype-volume.md)).

## <span id="ddk_ksproperty_audio_volumelevel_ks"></span><span id="DDK_KSPROPERTY_AUDIO_VOLUMELEVEL_KS"></span>


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
<td align="left"><p>Node via Filter or Pin instance</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537145" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY_AUDIO_CHANNEL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537145)"><strong>KSNODEPROPERTY_AUDIO_CHANNEL</strong></a></p></td>
<td align="left"><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value is of type LONG and specifies the volume level of a channel in a given stream. Volume-level values use the following scale:

-2147483648 is -infinity decibels (attenuation),

-2147483647 is -32767.99998474 decibels (attenuation), and

+2147483647 is +32767.99998474 decibels (gain).

&gt; \[!Note\]
&gt;  The decibel range is represented by integer values from -2147483648 to +2147483647, where this scale has a resolution of 1/65536 decibel.

 

If a value is specified beyond the range of the filter, the request to set this property will still be successful. But the actual value that was applied to the filter can only be determined by a subsequent Get call to this property.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_VOLUMELEVEL property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The property descriptor for this property specifies a channel number. If the stream that passes through the volume node contains *n* channels, the channels are numbered 0 through *n*-1. For more information, see [Exposing Multichannel Nodes](https://msdn.microsoft.com/library/windows/hardware/ff536380).

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


[Customizing Default Audio Volume Settings](https://msdn.microsoft.com/library/windows/hardware/jj870738)

[Default Audio Volume Settings](https://msdn.microsoft.com/library/windows/hardware/ff536251)

[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537145)

[**KSNODETYPE\_VOLUME**](ksnodetype-volume.md)

 

 






