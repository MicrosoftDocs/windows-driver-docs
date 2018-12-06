---
title: KSPROPERTY\_BDA\_PIN\_ID
description: Clients use KSPROPERTY\_BDA\_PIN\_ID to retrieve the BDA identifier (ID) for a pin.
ms.assetid: 6f7a4454-1294-4646-8e21-bfec9a14b612
keywords: ["KSPROPERTY_BDA_PIN_ID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIN_ID
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_PIN\_ID


Clients use KSPROPERTY\_BDA\_PIN\_ID to retrieve the BDA identifier (ID) for a pin.

## <span id="ddk_ksproperty_bda_pin_id_ks"></span><span id="DDK_KSPROPERTY_BDA_PIN_ID_KS"></span>


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

The returned value specifies the pin ID.

When the network provider creates a pin for a filter using KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY, the BDA minidriver for the filter gives that pin an ID. KSPROPERTY\_BDA\_PIN\_ID returns this ID.

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

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

 

 






