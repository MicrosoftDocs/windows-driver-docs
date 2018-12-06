---
title: KSPROPERTY\_STREAM\_QUALITY
description: The KSPROPERTY\_STREAM\_QUALITY property is an optional property that should be implemented if the pin generates Quality Management complaints.
ms.assetid: ed4d9baa-967a-41b3-b8b9-910b86230254
keywords: ["KSPROPERTY_STREAM_QUALITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_QUALITY
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAM\_QUALITY


The KSPROPERTY\_STREAM\_QUALITY property is an optional property that should be implemented if the pin generates Quality Management complaints.

## <span id="ddk_ksproperty_stream_quality_ks"></span><span id="DDK_KSPROPERTY_STREAM_QUALITY_KS"></span>


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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566730" data-raw-source="[&lt;strong&gt;KSQUALITY_MANAGER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566730)"><strong>KSQUALITY_MANAGER</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When this request is made, the pin connection in turn notifies the quality manager by providing [**KSQUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff566728) structures with the given context parameter.

If a pin does not report quality problems, it does not need to support KSPROPERTY\_STREAM\_QUALITY.

Also see [Quality Management](https://msdn.microsoft.com/library/windows/hardware/ff568124).

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

[**KSQUALITY\_MANAGER**](https://msdn.microsoft.com/library/windows/hardware/ff566730)

[**KSQUALITY**](https://msdn.microsoft.com/library/windows/hardware/ff566728)

 

 






