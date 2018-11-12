---
title: KSPROPERTY\_COPY\_MACROVISION
description: The KSPROPERTY\_COPY\_MACROVISION property indicates the Macrovision level of the data stream.
ms.assetid: 6863bcf6-06bc-4bd2-896e-43c083aa07d5
keywords: ["KSPROPERTY_COPY_MACROVISION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_COPY_MACROVISION
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_COPY\_MACROVISION


The KSPROPERTY\_COPY\_MACROVISION property indicates the Macrovision level of the data stream.

## <span id="ddk_ksproperty_copy_macrovision_ks"></span><span id="DDK_KSPROPERTY_COPY_MACROVISION_KS"></span>


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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567316" data-raw-source="[&lt;strong&gt;KS_COPY_MACROVISION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567316)"><strong>KS_COPY_MACROVISION</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KS\_COPY\_MACROVISION structure the specifies the Macrovision level of the data stream.

Remarks
-------

For more information about Macrovision level, see [DVD Copyright Protection](https://msdn.microsoft.com/library/windows/hardware/ff558736).

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
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KS\_COPY\_MACROVISION**](https://msdn.microsoft.com/library/windows/hardware/ff567316)

 

 






