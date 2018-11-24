---
title: KSPROPERTY\_AUDIO\_POSITIONEX
description: The KSPROPERTY\_AUDIO\_POSITIONEX property provides the caller with the stream position and the associated timestamp information for a kernel streaming (KS)-based audio driver.
ms.assetid: 660b1ee9-7c52-4d95-8df9-b1c0dce320e3
keywords: ["KSPROPERTY_AUDIO_POSITIONEX Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_POSITIONEX
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_POSITIONEX


The KSPROPERTY\_AUDIO\_POSITIONEX property provides the caller with the stream position and the associated timestamp information for a kernel streaming (KS)-based audio driver.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537092" data-raw-source="[&lt;strong&gt;KSAUDIO_POSITIONEX&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537092)"><strong>KSAUDIO_POSITIONEX</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSAUDIO\_POSITIONEX that receives the position information from the property handler. The position information that is specified by the KSAUDIO\_POSITIONEX structure is the position information for the pin that was selected by the caller.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The KSPROPERTY\_AUDIO\_POSITIONEX property request returns S\_OK if the call was successful. Otherwise, it returns the appropriate HRESULT error code.

Remarks
-------

Typically, audio applications must monitor the current position of an audio stream. This position is specified as a byte offset from the beginning of the stream. There are two possible interpretations of the stream position information:

-   In the case of a rendering stream, the stream position is the byte offset of the audio frame that is currently playing through the digital-to-analog converters (DACs).

-   In the case of a capture stream, the stream position is the byte offset of the audio frame that is currently being recorded through the analog-to-digital converters (ADCs).

A driver that supports the KSPROPERTY\_AUDIO\_POSITIONEX property generates a timestamp window for the stream position value. The timestamp window is the interval between the timestamp that is sampled before stream position is determined and the timestamp that is taken after the stream position is determined. The caller then determines whether it can use the timestamp window.

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
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSAUDIO\_POSITIONEX**](https://msdn.microsoft.com/library/windows/hardware/ff537092)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 






