---
title: KSPROPERTY\_BDA\_GUARD\_INTERVAL
description: Clients use KSPROPERTY\_BDA\_GUARD\_INTERVAL to control the setting for guard interval of a demodulator node.
ms.assetid: 7c0c6c5e-94fd-4013-9778-d41568ae9f0b
keywords: ["KSPROPERTY_BDA_GUARD_INTERVAL Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_GUARD_INTERVAL
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_GUARD\_INTERVAL


Clients use KSPROPERTY\_BDA\_GUARD\_INTERVAL to control the setting for guard interval of a demodulator node.

## <span id="ddk_ksproperty_bda_guard_interval_ks"></span><span id="DDK_KSPROPERTY_BDA_GUARD_INTERVAL_KS"></span>


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
<td><p>Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>GuardInterval</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The returned value from the GuardInterval enumerated type identifies a setting for guard interval.

The **NodeId** member of KSP\_NODE specifies the identifier of the demodulator node.

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


[**GuardInterval**](https://msdn.microsoft.com/library/windows/hardware/ff559626)

[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






