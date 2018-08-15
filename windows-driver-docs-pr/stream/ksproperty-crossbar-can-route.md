---
title: KSPROPERTY\_CROSSBAR\_CAN\_ROUTE
description: The KSPROPERTY\_CROSSBAR\_CAN\_ROUTE property retrieves whether the device is capable of supporting a specified routing. This property must be implemented.
ms.assetid: bb966d0a-6ecf-4bbb-a881-30d468abe220
keywords: ["KSPROPERTY_CROSSBAR_CAN_ROUTE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CROSSBAR_CAN_ROUTE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_CROSSBAR\_CAN\_ROUTE


The KSPROPERTY\_CROSSBAR\_CAN\_ROUTE property retrieves whether the device is capable of supporting a specified routing. This property must be implemented.

## <span id="ddk_ksproperty_crossbar_can_route_ks"></span><span id="DDK_KSPROPERTY_CROSSBAR_CAN_ROUTE_KS"></span>


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
<td><p>[<strong>KSPROPERTY_CROSSBAR_ROUTE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565128)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies whether the streaming minidriver supports a specified routing between the two pins. A nonzero value indicates that routing is supported. If the minidriver does not support routing between the two pins, this value is zero.

Remarks
-------

The **CanRoute** member of the KSPROPERTY\_CROSSBAR\_ROUTE\_S structure indicates if the device is capable of supporting a specified routing.

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

[**KSPROPERTY\_CROSSBAR\_ROUTE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565128)

 

 






