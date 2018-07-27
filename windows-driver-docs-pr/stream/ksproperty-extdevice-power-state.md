---
title: KSPROPERTY\_EXTDEVICE\_POWER\_STATE
description: The KSPROPERTY\_EXTDEVICE\_POWER\_STATE property sets or gets the power state of an external device.
ms.assetid: bfca1f3d-b563-4ddd-b823-85487b4a4093
keywords: ["KSPROPERTY_EXTDEVICE_POWER_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTDEVICE_POWER_STATE
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

# KSPROPERTY\_EXTDEVICE\_POWER\_STATE


The KSPROPERTY\_EXTDEVICE\_POWER\_STATE property sets or gets the power state of an external device.

## <span id="ddk_ksproperty_extdevice_power_state_ks"></span><span id="DDK_KSPROPERTY_EXTDEVICE_POWER_STATE_KS"></span>


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
<td><p>[<strong>KSPROPERTY_EXTDEVICE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565156)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the external device's power state.

Remarks
-------

The **PowerState** member of the KSPROPERTY\_EXTDEVICE\_S structure specifies the external device's power setting. The **PowerState** member may be set to equal on or standby. For example, a battery-powered external device, such as a DV camcorder may be powered off. An AC-powered DVHS device may be placed in standby. If a device is in standby, it may be powered-on later.

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

[**KSPROPERTY\_EXTDEVICE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565156)

 

 






