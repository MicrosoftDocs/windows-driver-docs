---
title: KSPROPERTY\_CLOCK\_PHYSICALTIME
description: Clients use the KSPROPERTY\_CLOCK\_PHYSICAL\_TIME property to determine the current physical time of a clock.
ms.assetid: cc747fd4-1df0-4d44-b43e-b43532c1228b
keywords: ["KSPROPERTY_CLOCK_PHYSICALTIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_PHYSICALTIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_CLOCK\_PHYSICALTIME


Clients use the KSPROPERTY\_CLOCK\_PHYSICAL\_TIME property to determine the current physical time of a clock.

## <span id="ddk_ksproperty_clock_physicaltime_ks"></span><span id="DDK_KSPROPERTY_CLOCK_PHYSICALTIME_KS"></span>


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
<td><p>[<strong>KSPROPERTY</strong>](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)</p></td>
<td><p>LONGLONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns a value of type LONGLONG, representing the current physical time in 100-nanosecond units.

The physical time of a clock is an ever-progressing counter. Unlike the presentation time, it cannot reverse.

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


[**KSPROPERTY\_CLOCK\_CORRELATEDPHYSICALTIME**](ksproperty-clock-correlatedphysicaltime.md)

[**KSPROPERTY\_CLOCK\_CORRELATEDTIME**](ksproperty-clock-correlatedtime.md)

 

 






