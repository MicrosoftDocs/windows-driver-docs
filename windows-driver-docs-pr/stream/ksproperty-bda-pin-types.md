---
title: KSPROPERTY\_BDA\_PIN\_TYPES
description: Clients use KSPROPERTY\_BDA\_PIN\_TYPES to retrieve a list of pin types.
ms.assetid: de11ab3c-a787-4831-aad4-e97f46432032
keywords: ["KSPROPERTY_BDA_PIN_TYPES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIN_TYPES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_PIN\_TYPES


Clients use KSPROPERTY\_BDA\_PIN\_TYPES to retrieve a list of pin types.

## <span id="ddk_ksproperty_bda_pin_types_ks"></span><span id="DDK_KSPROPERTY_BDA_PIN_TYPES_KS"></span>


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
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p>KSPROPERTY</p></td>
<td><p>List of KSPIN_DESCRIPTOR_EXs</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

In a template topology each pin type can only occur once, but it can occur multiple times in an actual topology. This list of pin types is an array of KSPIN\_DESCRIPTOR\_EX structures.

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
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**BdaPropertyPinTypes**](https://msdn.microsoft.com/library/windows/hardware/ff556499)

[**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534)

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

 

 






