---
title: KSPROPERTY_STREAM_TIMEFORMAT
description: The KSPROPERTY\_STREAM\_TIMEFORMAT property is used to retrieve the time format used on a particular pin connection.
keywords: ["KSPROPERTY_STREAM_TIMEFORMAT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_STREAM_TIMEFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_STREAM\_TIMEFORMAT


The KSPROPERTY\_STREAM\_TIMEFORMAT property is used to retrieve the time format used on a particular pin connection.

## <span id="ddk_ksproperty_stream_timeformat_ks"></span><span id="DDK_KSPROPERTY_STREAM_TIMEFORMAT_KS"></span>


### Usage Summary Table

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
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](./ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td><p>GUID</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The property returns a GUID specifying the time format used in the connection and indicating the format of the presentation time and extent. The defined time formats correspond to those defined by DirectShow.

KSPROPERTY\_STREAM\_TIMEFORMAT is an optional property that should be implemented if the pin supports the rate, presentation time/extent, or skip degradation properties (For more information about these properties, see [Quality Management](./quality-management.md)). This allows a client to determine the time format used for connection and the format of the time stamp information used in rate, presentation time/extent, and skip degradation operations.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY**](ksproperty-structure.md)
