---
title: KSPROPERTY\_AUDIO\_DYNAMIC\_RANGE
description: The KSPROPERTY\_AUDIO\_DYNAMIC\_RANGE property specifies the dynamic range of the audio stream that is output from a loudness node (KSNODETYPE\_LOUDNESS).
ms.assetid: bab1cc2c-0751-4425-8546-9587baece585
keywords: ["KSPROPERTY_AUDIO_DYNAMIC_RANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_DYNAMIC_RANGE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_DYNAMIC\_RANGE


The KSPROPERTY\_AUDIO\_DYNAMIC\_RANGE property specifies the dynamic range of the audio stream that is output from a loudness node ([**KSNODETYPE\_LOUDNESS**](ksnodetype-loudness.md)).

## <span id="ddk_ksproperty_audio_dynamic_range_ks"></span><span id="DDK_KSPROPERTY_AUDIO_DYNAMIC_RANGE_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537085" data-raw-source="[&lt;strong&gt;KSAUDIO_DYNAMIC_RANGE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537085)"><strong>KSAUDIO_DYNAMIC_RANGE</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSAUDIO\_DYNAMIC\_RANGE, which specifies the dynamic range for the loudness node's output stream.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_DYNAMIC\_RANGE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

By default, the values for the **QuietCompression** and **LoudCompression** members of the KSAUDIO\_DYNAMIC\_RANGE structure are set to zero percent. This produces the full dynamic range of the audio stream. The miniport driver sets the property to its default value when it instantiates the pin whose data path contains the node.

Some devices might not support changes to **QuietCompression** and **LoudCompression**. If the client attempts to change a value that the device does not support, the miniport driver should return an error.

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

[**KSNODETYPE\_LOUDNESS**](ksnodetype-loudness.md)

[**KSAUDIO\_DYNAMIC\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff537085)

 

 






