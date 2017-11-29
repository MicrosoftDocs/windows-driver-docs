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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_STREAM\_RATE


The KSPROPERTY\_STREAM\_RATE property works in conjunction with [**KSPROPERTY\_STREAM\_RATECAPABILITY**](ksproperty-stream-ratecapability.md) and is used to set the rate of a segment after querying the capability of the pin.

## <span id="ddk_ksproperty_stream_rate_ks"></span><span id="DDK_KSPROPERTY_STREAM_RATE_KS"></span>


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
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSRATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566752)</p></td>
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

## <span id="see_also"></span>See also


[**KSPROPERTY\_STREAM\_RATECAPABILITY**](ksproperty-stream-ratecapability.md)

[**KSRATE**](https://msdn.microsoft.com/library/windows/hardware/ff566752)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_STREAM_RATE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





