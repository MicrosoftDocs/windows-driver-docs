---
title: KSPROPERTY\_STREAM\_MASTERCLOCK
description: The KSPROPERTY\_STREAM\_MASTERCLOCK property is an optional property that should be implemented if the pin uses or produces a master clock that can be used for synchronization.
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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAM\_MASTERCLOCK


The KSPROPERTY\_STREAM\_MASTERCLOCK property is an optional property that should be implemented if the pin uses or produces a master clock that can be used for synchronization.

## <span id="ddk_ksproperty_stream_masterclock_ks"></span><span id="DDK_KSPROPERTY_STREAM_MASTERCLOCK_KS"></span>


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

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

 

 






