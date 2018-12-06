---
title: KSPROPERTY\_GENERAL\_COMPONENTID
description: The KSPROPERTY\_GENERAL\_COMPONENTID property is an optional property that allows a client to access general component information stored in the KSCOMPONENTID structure.
ms.assetid: fbbdf3f6-c71a-4a6d-ba15-ec7b7bdc1e0e
keywords: ["KSPROPERTY_GENERAL_COMPONENTID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_GENERAL_COMPONENTID
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_GENERAL\_COMPONENTID


The KSPROPERTY\_GENERAL\_COMPONENTID property is an optional property that allows a client to access general component information stored in the [**KSCOMPONENTID**](https://msdn.microsoft.com/library/windows/hardware/ff561027) structure.

## <span id="ddk_ksproperty_general_componentid_ks"></span><span id="DDK_KSPROPERTY_GENERAL_COMPONENTID_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561027" data-raw-source="[&lt;strong&gt;KSCOMPONENTID&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561027)"><strong>KSCOMPONENTID</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The [**KSCOMPONENTID**](https://msdn.microsoft.com/library/windows/hardware/ff561027) structure contains GUID values for **Manufacturer**, **Product**, **Component**, and **Name**. It contains ULONG values for **Version** and **Revision**.

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


[**KSCOMPONENTID**](https://msdn.microsoft.com/library/windows/hardware/ff561027)

 

 






