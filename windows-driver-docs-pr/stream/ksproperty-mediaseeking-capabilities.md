---
title: KSPROPERTY\_MEDIASEEKING\_CAPABILITIES
description: The KSPROPERTY\_MEDIASEEKING\_CAPABILITIES property retrieves the media-seeking capabilities of a filter.
ms.assetid: f0ee8fed-cdb5-44f9-96c3-d6edf235ea35
keywords: ["KSPROPERTY_MEDIASEEKING_CAPABILITIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_CAPABILITIES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_MEDIASEEKING\_CAPABILITIES


The KSPROPERTY\_MEDIASEEKING\_CAPABILITIES property retrieves the media-seeking capabilities of a filter.

## <span id="ddk_ksproperty_mediaseeking_capabilities_ks"></span><span id="DDK_KSPROPERTY_MEDIASEEKING_CAPABILITIES_KS"></span>


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
<td><p>Filter</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p>KS_SEEKING_CAPABILITIES</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The capabilities of a filter that this property retrieves include the ability to seek to an absolute position, to seek forwards or backwards in the media, to get the current position while in play or stop mode, to get the duration, or to play backwards. Note that these are capabilities of the filter as a whole; this property is designed to map to DirectShow seeking capabilities where such capabilities are queried only on a filter, not a pin, basis.

If this property is not supported, it is assumed that the filter does not require positional information and that the filter can be treated as a pass through.

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


[KSPROPSETID\_MediaSeeking](kspropsetid-mediaseeking.md)

 

 






