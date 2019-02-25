---
title: KSPROPERTY\_STREAM\_PRESENTATIONTIME
description: The KSPROPERTY\_STREAM\_PRESENTATIONTIME property is used to retrieve and set the current presentation time of a filter pin.
ms.assetid: fb7bcd04-e600-4bab-b7e7-2b99e2bc0a6c
keywords: ["KSPROPERTY_STREAM_PRESENTATIONTIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_PRESENTATIONTIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAM\_PRESENTATIONTIME


The KSPROPERTY\_STREAM\_PRESENTATIONTIME property is used to retrieve and set the current presentation time of a filter pin.

## <span id="ddk_ksproperty_stream_presentationtime_ks"></span><span id="DDK_KSPROPERTY_STREAM_PRESENTATIONTIME_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567145" data-raw-source="[&lt;strong&gt;KSTIME&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567145)"><strong>KSTIME</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

KSPROPERTY\_STREAM\_PRESENTATIONTIME is an optional property that should be implemented if a pin retains positional information or uses different interfaces with different time stamp formats on topologically related pins. Therefore, it would need to have the time stamps translated as a seek presentation time occurs.

The presentation time of the filter pin is specified as a [**KSTIME**](https://msdn.microsoft.com/library/windows/hardware/ff567145) structure whose interpretation depends on the interface used. For the standard streaming interface, time is specified in 100-nanosecond increments (unless the numerator and denominator specify otherwise) representing the presentation position of the stream the filter is currently processing or is seeking to process. If this is a rendering filter, this position represents the data that is currently being rendered. This positioning information is synchronized with the master clock's presentation time. Presentation time typically begins at zero and may represent a time offset into file data. The numerator and denominator can be used to specify block alignment that the interface enforces.

This property is also used when translating positional values during propagation of a seek request. The seek positional value on one pin is translated within the filter to presentation time on topologically related pins. A client sets this property with a new stream position in order to seek. This typically is called by the proxy when a seek is required after canceling outstanding I/O and resetting device state. If a reset has not been performed, the filter may have to automatically cancel and reset appropriately. The property is passed a KSTIME containing the new stream position in units consistent with the interface used on the connection.

After a client (for example, a DirectShow proxy) writes a seek request to one connection, it then queries the other topologically related connections for a presentation time. Any other connections that conduct a successful read request make the proxy pass the result position to the other end of that connection. In this manner, seek positions are propagated (for example, throughout the DirectShow graph) without having to know the unit format other than the initial unit format passed by a client. Translations occurs within the filter as the positional information propagates through the topology within a filter. This roundabout method is used because communication methods may be limited between various filters in a graph depending on the interfaces they use. When setting a new seek position, the numerator/denominator pair must be acceptable to the pin.

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


[**KSTIME**](https://msdn.microsoft.com/library/windows/hardware/ff567145)

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

 

 






