---
title: KSPROPERTY\_AUDIO\_BUFFER\_DURATION
description: The KSPROPERTY\_AUDIO\_BUFFER\_DURATION property allows the size of the client application buffer to be reported as time duration.
ms.assetid: 9749464f-d351-468b-b785-fa84705ef2c0
keywords: ["KSPROPERTY_AUDIO_BUFFER_DURATION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_BUFFER_DURATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_BUFFER\_DURATION


The KSPROPERTY\_AUDIO\_BUFFER\_DURATION property allows the size of the client application buffer to be reported as time duration.

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
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p>KSPROPERTY</p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value is of type ULONG and represents the client buffer duration that is measured in milliseconds.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_BUFFER\_DURATION property request returns STATUS\_SUCCESS to indicate that the property request has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

You can adjust the duration of the request for isochronous audio data capture to help improve the performance of your USB audio device. A shorter duration reduces latency but it also means that the USB audio stack must make more frequent deferred procedure calls (DPC), which may cause degraded performance.

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
<td align="left"><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 





