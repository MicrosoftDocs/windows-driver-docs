---
title: KSPROPERTY\_STREAM\_RATE
description: The KSPROPERTY\_STREAM\_RATE property works in conjunction with KSPROPERTY\_STREAM\_RATECAPABILITY and is used to set the rate of a segment after querying the capability of the pin.
ms.assetid: 125dcd39-fb67-4d9f-81af-b7f4c0e566cc
keywords: ["KSPROPERTY_STREAM_RATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_RATE
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAM\_RATE


The KSPROPERTY\_STREAM\_RATE property works in conjunction with [**KSPROPERTY\_STREAM\_RATECAPABILITY**](ksproperty-stream-ratecapability.md) and is used to set the rate of a segment after querying the capability of the pin.

## <span id="ddk_ksproperty_stream_rate_ks"></span><span id="DDK_KSPROPERTY_STREAM_RATE_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566752" data-raw-source="[&lt;strong&gt;KSRATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566752)"><strong>KSRATE</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

KSPROPERTY\_STREAM\_RATE should be implemented if a pin allows rate changes, or the interface between topologically-related pins is different and results in a different time stamp format being used.

The property is supported by pins that can modify the rate of data through resampling or time stamp changes so that a requested rate can be closer to the nominal rate of 1.0.

Reading the property returns the current rate and segment. Setting the rate for a new segment replaces any current rate setting. In this manner, stopping a fast-forward request can be done by requesting a rate setting of 1.0, which should always be accepted. If the specified rate is not obtainable, the pin can reject the request instead of attempting a best-fit setting.

The rate setting and query both use the [**KSRATE**](https://msdn.microsoft.com/library/windows/hardware/ff566752) structure that specifies the presentation start, duration, and rate. Rate changes can only be performed in pause or run state and are stopped after changing to any other state. The rate change is specified by the percentage over or under the nominal 1.0 rate that the pin is to adjust for and the current setting is returned in the same format.

This property should also be used to translate the interface and time units specified in the previous property and should be implemented on filters that change interfaces between pins, even if rate changes are not supported. For example, a filter that supports KSINTERFACE\_STANDARD\_POSITION on one pin and translates to KSINTERFACE\_STANDARD\_STREAMING on another pin related by topology may not support rate changes. The filter should be able to take the change request on either pin and either interface and change to its own interface and units, though the rate would be unchanged.

If the pin also produces a clock, a rate change must not change the slope of the physical time, because any client using the clock for rate matching is expecting the slope to be as if the underlying hardware were running at a nominal 1.0 rate. This means that a pin that cannot ensure that the physical clock slope remains consistent without significant drift cannot accept rate adjustment requests.

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


[**KSPROPERTY\_STREAM\_RATECAPABILITY**](ksproperty-stream-ratecapability.md)

[**KSRATE**](https://msdn.microsoft.com/library/windows/hardware/ff566752)

 

 






