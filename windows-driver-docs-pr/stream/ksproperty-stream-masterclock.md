---
title: KSPROPERTY\_STREAM\_MASTERCLOCK
description: The KSPROPERTY\_STREAM\_MASTERCLOCK property is an optional property that should be implemented if the pin uses or produces a master clock that can be used for synchronization.
MS-HAID:
- 'ks-prop\_34bcda1f-32f9-45e9-8176-7c3b02434ba8.xml'
- 'stream.ksproperty\_stream\_masterclock'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b8fb4d7b-e2e3-498c-9f76-4075d3ae0cb2
keywords: ["KSPROPERTY_STREAM_MASTERCLOCK Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_MASTERCLOCK
api_location:
- ks.h
api_type:
- HeaderDef
---

# KSPROPERTY\_STREAM\_MASTERCLOCK


The KSPROPERTY\_STREAM\_MASTERCLOCK property is an optional property that should be implemented if the pin uses or produces a master clock that can be used for synchronization.

## <span id="ddk_ksproperty_stream_masterclock_ks"></span><span id="DDK_KSPROPERTY_STREAM_MASTERCLOCK_KS"></span>


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
<td><p>HANDLE</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The property returns a **NULL** handle when queried. Support is determined by whether the call returns successfully.

You can use KSPROPERTY\_STREAM\_MASTERCLOCK to query whether a master clock is supported by a pin or to set the current master clock for a pin. This is typically done through a graph manager, such as in DirectShow. A master clock handle is retrieved and can be used to set the master clock on another pin, or can be used as the user-mode proxy of a master clock, such as in a DirectShow graph.

When the clock is set on a pin, the pin references the underlying file object and can later perform queries against that file object. The file handle itself must be closed by the client that queried for the handle.

A filter does not need to support the property when it neither produces a master clock nor needs to reference one, such as a converter filter placed in the middle of a graph with no need to synchronize with other streams. The property can also be used as read-only when a filter produces a master clock but does not synchronize to an external master clock.

Also see [KS Clocks](https://msdn.microsoft.com/library/windows/hardware/ff567307) and [AVStream Clocks](https://msdn.microsoft.com/library/windows/hardware/ff554208).

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


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_STREAM_MASTERCLOCK%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





