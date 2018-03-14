---
title: KSPROPERTY\_CROSSBAR\_PININFO
description: The KSPROPERTY\_CROSSBAR\_PININFO property retrieves the type of physical connection represented by the pin including settings such as data flow direction, medium GUID(s) and pin-type.
ms.assetid: d025b401-bc75-40d6-a367-1b98e065a48d
keywords: ["KSPROPERTY_CROSSBAR_PININFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CROSSBAR_PININFO
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_CROSSBAR\_PININFO


The KSPROPERTY\_CROSSBAR\_PININFO property retrieves the type of physical connection represented by the pin including settings such as data flow direction, medium GUID(s) and pin-type. For video pins this property also indicates if there is an audio pin associated with a particular video pin. This property must be implemented.

## <span id="ddk_ksproperty_crossbar_pininfo_ks"></span><span id="DDK_KSPROPERTY_CROSSBAR_PININFO_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<td><p>[<strong>KSPROPERTY_CROSSBAR_PININFO_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565123)</p></td>
<td><p>[<strong>KSPROPERTY_CROSSBAR_PININFO_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565123)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_CROSSBAR\_PININFO\_S structure.

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

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPROPERTY\_CROSSBAR\_PININFO\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565123)

 

 






