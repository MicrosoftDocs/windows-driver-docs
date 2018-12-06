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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_EXTXPORT\_STATE


The KSPROPERTY\_EXTXPORT\_STATE property sets or gets an external device's transport mode and state.

## <span id="ddk_ksproperty_extxport_state_ks"></span><span id="DDK_KSPROPERTY_EXTXPORT_STATE_KS"></span>


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
<td><p>Device</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565167" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565167)"><strong>KSPROPERTY_EXTXPORT_S</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568546" data-raw-source="[&lt;strong&gt;TRANSPORT_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568546)"><strong>TRANSPORT_STATE</strong></a></p></td>
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

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSPROPERTY\_EXTXPORT\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565167)

[**TRANSPORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff568546)

 

 






