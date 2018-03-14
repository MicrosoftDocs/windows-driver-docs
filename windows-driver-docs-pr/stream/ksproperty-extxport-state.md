---
title: KSPROPERTY\_EXTXPORT\_STATE
description: The KSPROPERTY\_EXTXPORT\_STATE property sets or gets an external device's transport mode and state.
ms.assetid: c508b6ce-2a37-4fca-9edf-66700d9cbd15
keywords: ["KSPROPERTY_EXTXPORT_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_STATE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_EXTXPORT\_STATE


The KSPROPERTY\_EXTXPORT\_STATE property sets or gets an external device's transport mode and state.

## <span id="ddk_ksproperty_extxport_state_ks"></span><span id="DDK_KSPROPERTY_EXTXPORT_STATE_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Device</p></td>
<td><p>[<strong>KSPROPERTY_EXTXPORT_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565167)</p></td>
<td><p>[<strong>TRANSPORT_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568546)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a TRANSPORT\_STATE structure that describes the current mode and state of the external transport. For example when the mode is set to play, the state might be set to freeze (paused).

Remarks
-------

The **XPrtState** member of the KSPROPERTY\_EXTXPORT\_S structure specifies the mode and state.

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

[**KSPROPERTY\_EXTXPORT\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565167)

[**TRANSPORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff568546)

 

 






