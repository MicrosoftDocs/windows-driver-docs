---
title: KSPROPERTY\_STREAM\_RATECAPABILITY
description: The KSPROPERTY\_STREAM\_RATECAPABILITY property allows a graph manager to query all connection points involved in the flow of a particular stream (obtained through KSPROPERTY\_PIN\_DATAROUTING) for their capability in adjusting a requested rate to the nominal rate.
MS-HAID:
- 'ks-prop\_4aa69be9-445c-437e-9965-767e34ef8a44.xml'
- 'stream.ksproperty\_stream\_ratecapability'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 73e3bf4e-2815-4890-ba12-77fbe7a7c589
keywords: ["KSPROPERTY_STREAM_RATECAPABILITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_RATECAPABILITY
api_location:
- ks.h
api_type:
- HeaderDef
---

# KSPROPERTY\_STREAM\_RATECAPABILITY


The KSPROPERTY\_STREAM\_RATECAPABILITY property allows a graph manager to query all connection points involved in the flow of a particular stream (obtained through KSPROPERTY\_PIN\_DATAROUTING) for their capability in adjusting a requested rate to the nominal rate.

## <span id="ddk_ksproperty_stream_ratecapability_ks"></span><span id="DDK_KSPROPERTY_STREAM_RATECAPABILITY_KS"></span>


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
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSRATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566752)</p></td>
<td><p>[<strong>KSRATE_CAPABILITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566754)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

KSPROPERTY\_STREAM\_RATECAPABILITY should be implemented if a pin allows rate changes, or the interface between topologically-related pins is different and results in the use of a different time stamp format. The property can also be used to translate time stamp formats in general, such as skip degradation requests.

The property is supported by pins that modify the rate of data through resampling or time stamp changes. All rate changes involve requesting a rate and determining how much a specific pin can correct that rate to obtain the nominal 1.0 rate. For example, a pin requesting a video playback rate of 2.0 would imply a request to render at twice the nominal rate of the video clip; a rate request of 0.5 would imply a half-speed rendering.

The rate request contains both the presentation start time and the duration for that rate request. This allows for constraints that might apply to specific portions of a data stream to be taken into account. The presentation time, numerator/denominator pair, and duration units are expressed in terms of the Interface specified in the structure. If a standard interface is not used, the initial rate change queries cannot be sent to a pin.

A pin must be able to accept interface identifiers used by any pin with similar topology. It must also translate the interface identifier and time units to its own corresponding values. In this manner, a client can traverse a graph from one known interface point and have units translated by connection points at each step of the way.

It is important to support this property if Interface changes are made even if rate changes cannot be made, so the Interface and time units can be adjusted when queries are made. The result would not change the rate returned but would change the Interface, PresentationStart, and Duration.

Rate capability requests can only be performed in Pause or Run state and become invalid after changing to any other state. Queries where the rate is initially 1.0 should always succeed as they typically are just requests to translate time stamp formats.

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


[**KSRATE**](https://msdn.microsoft.com/library/windows/hardware/ff566752)

[**KSRATE\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/ff566754)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_STREAM_RATECAPABILITY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





