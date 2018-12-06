---
title: KSPROPERTY\_PIN\_NAME
description: The client uses KSPROPERTY\_PIN\_NAME to retrieve the Registry name of a pin factory. This is a localized Unicode string.
ms.assetid: 763c3116-95f5-4d32-8c46-d8d91f537bd4
keywords: ["KSPROPERTY_PIN_NAME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_NAME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_NAME


The client uses KSPROPERTY\_PIN\_NAME to retrieve the Registry name of a pin factory. This is a localized Unicode string.

## <span id="ddk_ksproperty_pin_name_ks"></span><span id="DDK_KSPROPERTY_PIN_NAME_KS"></span>


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
<td><p>Pin</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566722)"><strong>KSP_PIN</strong></a></p></td>
<td><p>A buffer containing the localized Unicode string.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Specify this property using KSP\_PIN, where the member specifies the pin factory for which to return the registry name.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

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


[**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722)

 

 






