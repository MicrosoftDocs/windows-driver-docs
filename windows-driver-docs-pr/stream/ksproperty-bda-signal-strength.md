---
title: KSPROPERTY\_BDA\_SIGNAL\_STRENGTH
description: Clients use KSPROPERTY\_BDA\_SIGNAL\_STRENGTH to determine the carrier strength of the signal in mDb (1/1000 of a decibel (DB)).
ms.assetid: b8b71135-cc0b-4a59-940a-dd766cab3305
keywords: ["KSPROPERTY_BDA_SIGNAL_STRENGTH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SIGNAL_STRENGTH
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_SIGNAL\_STRENGTH


Clients use KSPROPERTY\_BDA\_SIGNAL\_STRENGTH to determine the carrier strength of the signal in mDb (1/1000 of a decibel (DB)).

## <span id="ddk_ksproperty_bda_signal_strength_ks"></span><span id="DDK_KSPROPERTY_BDA_SIGNAL_STRENGTH_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Pin or Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value specifies the carrier strength of the signal in mDb.

A strength of 0 is nominal strength as expected for the given type of broadcast network. Subnominal strengths are reported as positive mDb. Super-nominal strengths are reported as negative mDb.

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


[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






