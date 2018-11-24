---
title: KSPROPERTY\_BDA\_PIN\_TYPE
description: Clients use KSPROPERTY\_BDA\_PIN\_TYPE to retrieve the value that specifies the type of a pin.
ms.assetid: 3d2a976b-67ff-4469-aa96-7aa8bd5f229e
keywords: ["KSPROPERTY_BDA_PIN_TYPE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIN_TYPE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_PIN\_TYPE


Clients use KSPROPERTY\_BDA\_PIN\_TYPE to retrieve the value that specifies the type of a pin.

## <span id="ddk_ksproperty_bda_pin_type_ks"></span><span id="DDK_KSPROPERTY_BDA_PIN_TYPE_KS"></span>


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
<td><p>Pin</p></td>
<td><p>KSPROPERTY</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The returned value specifies the pin type.

When the network provider creates a pin for a filter using KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY, it specifies a pin type from the list of pin types included in the filter's BDA template topology. KSPROPERTY\_BDA\_PIN\_TYPE returns this pin type. In the filter's BDA template topology each pin type can only occur once, but it can occur multiple times in an actual topology. The value for the pin type corresponds to the index of the element in the zero-based array of pin types. This array of pin types is an array of KSPIN\_DESCRIPTOR\_EX structures.

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


[**KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY**](ksmethod-bda-create-pin-factory.md)

[**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534)

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

 

 






