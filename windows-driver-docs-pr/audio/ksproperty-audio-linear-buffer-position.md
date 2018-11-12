---
title: KSPROPERTY\_AUDIO\_LINEAR\_BUFFER\_POSITION
description: The KSPROPERTY\_AUDIO\_LINEAR\_BUFFER\_POSITION property request retrieves a number that represents the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream.
ms.assetid: 08CC3164-2B8F-4368-8A34-6F8954992D3A
keywords: ["KSPROPERTY_AUDIO_LINEAR_BUFFER_POSITION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_LINEAR_BUFFER_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_LINEAR\_BUFFER\_POSITION


The KSPROPERTY\_AUDIO\_LINEAR\_BUFFER\_POSITION property request retrieves a number that represents the number of bytes that the DMA has fetched from the audio buffer since the beginning of the stream.

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
<td align="left"><p>ULONGULONG</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The KSPROPERTY\_AUDIO\_LINEAR\_BUFFER\_POSITION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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

 

 





