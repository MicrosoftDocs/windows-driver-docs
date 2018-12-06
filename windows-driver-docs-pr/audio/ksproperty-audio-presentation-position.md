---
title: KSPROPERTY\_AUDIO\_PRESENTATION\_POSITION
description: The KSPROPERTY\_AUDIO\_PRESENTATION\_POSITION property request retrieves a structure that specifies the current position within the audio data being rendered to the endpoint.
ms.assetid: 21067580-12FF-4327-B9AA-D16E2635FA12
keywords: ["KSPROPERTY_AUDIO_PRESENTATION_POSITION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_PRESENTATION_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_PRESENTATION\_POSITION


The KSPROPERTY\_AUDIO\_PRESENTATION\_POSITION property request retrieves a structure that specifies the current position within the audio data being rendered to the endpoint.

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
<td align="left"><p>Node via Pin instance</p></td>
<td align="left"><p>KSP_NODE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh450865" data-raw-source="[&lt;strong&gt;KSAUDIO_PRESENTATION_POSITION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh450865)"><strong>KSAUDIO_PRESENTATION_POSITION</strong></a></p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The KSPROPERTY\_AUDIO\_PRESENTATION\_POSITION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

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
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSAUDIO\_PRESENTATION\_POSITION**](https://msdn.microsoft.com/library/windows/hardware/hh450865)

 

 






