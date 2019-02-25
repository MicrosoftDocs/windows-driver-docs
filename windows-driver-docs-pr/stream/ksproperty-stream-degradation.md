---
title: KSPROPERTY\_STREAM\_DEGRADATION
description: The KSPROPERTY\_STREAM\_DEGRADATION property is an optional property that should be implemented if the pin allows degradation strategies.
ms.assetid: b8f9db81-a9ed-4a13-8d64-14854193c91b
keywords: ["KSPROPERTY_STREAM_DEGRADATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_DEGRADATION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAM\_DEGRADATION


The KSPROPERTY\_STREAM\_DEGRADATION property is an optional property that should be implemented if the pin allows degradation strategies.

## <span id="ddk_ksproperty_stream_degradation_ks"></span><span id="DDK_KSPROPERTY_STREAM_DEGRADATION_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563441" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563441)"><strong>KSMULTIPLE_ITEM</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff561671" data-raw-source="[&lt;strong&gt;KSDEGRADE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561671)"><strong>KSDEGRADE</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When queried, the property returns the size and count of the structures to be returned in [**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441) format, followed by [**KSDEGRADE**](https://msdn.microsoft.com/library/windows/hardware/ff561671) structures.

On a query, this property returns the size and count of the structures to be returned in KSMULTIPLE\_ITEM format, followed by KSDEGRADE structures. The multiple item format must be used on both querying and setting degradation strategies.

A client can query this property to retrieve the current degradation settings or it can set this property to change the current degradation settings. The degradation settings are used to modify the usage of resources by a filter pin in response to a quality management (QM) complaint, or to adjust quality back to some higher level. This is typically used by a quality manager to adjust degradation settings, and query the type of setting that can be adjusted and their current values. It may pass multiple KSDEGRADE structures when setting values. For more information about quality managers, see [Quality Management](https://msdn.microsoft.com/library/windows/hardware/ff568124).

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

[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

[**KSDEGRADE**](https://msdn.microsoft.com/library/windows/hardware/ff561671)

 

 






