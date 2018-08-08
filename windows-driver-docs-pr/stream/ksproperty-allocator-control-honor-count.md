---
title: KSPROPERTY\_ALLOCATOR\_CONTROL\_HONOR\_COUNT
description: The KSPROPERTY\_ALLOCATOR\_CONTROL\_HONOR\_COUNT property informs the Overlay Mixer how to determine the number of DirectDraw surfaces to allocate. This property is optional.
ms.assetid: 3a867554-a6ef-49bd-89e7-e5d09a21609e
keywords: ["KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_ALLOCATOR\_CONTROL\_HONOR\_COUNT


The KSPROPERTY\_ALLOCATOR\_CONTROL\_HONOR\_COUNT property informs the Overlay Mixer how to determine the number of DirectDraw surfaces to allocate. This property is optional.

## <span id="ddk_ksproperty_allocator_control_honor_count_ks"></span><span id="DDK_KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT_KS"></span>


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
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>DWORD</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a DWORD that specifies how the Overlay Mixer is to calculate the number of and use of overlay surfaces.

Remarks
-------

KSPROPERTY\_ALLOCATOR\_CONTROL\_HONOR\_COUNT property requests must return 1 to force the Overlay Mixer to use the number of surfaces specified in the [**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING**](ksproperty-connection-allocatorframing.md) property. A return value of zero causes the Overlay Mixer to calculate how many surfaces to allocate.

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

[**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING**](ksproperty-connection-allocatorframing.md)

 

 






