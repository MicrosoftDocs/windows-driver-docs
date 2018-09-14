---
title: KSPROPERTY\_PIN\_NECESSARYINSTANCES
description: This property returns the minimum number of pins that the pin factory must instantiate before the filter can perform I/O operations.
ms.assetid: d30d7546-3d16-42df-b640-a8ec37bca35c
keywords: ["KSPROPERTY_PIN_NECESSARYINSTANCES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_NECESSARYINSTANCES
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_NECESSARYINSTANCES


This property returns the minimum number of pins that the pin factory must instantiate before the filter can perform I/O operations.

## <span id="ddk_ksproperty_pin_necessaryinstances_ks"></span><span id="DDK_KSPROPERTY_PIN_NECESSARYINSTANCES_KS"></span>


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
<td><p>[<strong>KSP_PIN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566722)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Specify this property using KSP\_PIN, where the member specifies the relevant pin factory.

KSPROPERTY\_PIN\_NECESSARYINSTANCES returns a value of type ULONG, specifying the minimum number of pins that the pin factory must instantiate.

The class driver does not handle this property; the stream minidriver must provide handling on its own.

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

 

 






