---
title: KSPROPERTY\_CLOCK\_TIME
description: Clients use the KSPROPERTY\_CLOCK\_TIME property to determine the current presentation time on a clock.
ms.assetid: 42bae8fa-bff0-4411-bf32-5aa4da3e4f02
keywords: ["KSPROPERTY_CLOCK_TIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_TIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CLOCK\_TIME


Clients use the KSPROPERTY\_CLOCK\_TIME property to determine the current presentation time on a clock.

## <span id="ddk_ksproperty_clock_time_ks"></span><span id="DDK_KSPROPERTY_CLOCK_TIME_KS"></span>


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
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p>LONGLONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns a value of type LONGLONG, specifying the current presentation time in 100-nanosecond units.

The presentation time of a clock can be reversed, unlike the physical time. The presentation time of a clock typically represents a timestamp on an underlying data stream. For example, a clock for a DVD player can report the timestamp of the current position in the DVD as its presentation time.

Clocks are not required to support a 100-nanosecond resolution. To determine the clock resolution, clients can use the [**KSPROPERTY\_CLOCK\_RESOLUTION**](ksproperty-clock-resolution.md) request.

Requirements
------------

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


[KSPROPSETID\_Clock](kspropsetid-clock.md)

 

 






