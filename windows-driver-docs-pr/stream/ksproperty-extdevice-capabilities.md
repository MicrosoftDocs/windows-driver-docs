---
title: KSPROPERTY\_EXTDEVICE\_CAPABILITIES
description: The KSPROPERTY\_EXTDEVICE\_CAPABILITIES property retrieves the capabilities of an external device.
ms.assetid: c408b4cf-2fd9-41b2-b182-47baa551fd93
keywords: ["KSPROPERTY_EXTDEVICE_CAPABILITIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTDEVICE_CAPABILITIES
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

# KSPROPERTY\_EXTDEVICE\_CAPABILITIES


The KSPROPERTY\_EXTDEVICE\_CAPABILITIES property retrieves the capabilities of an external device.

## <span id="ddk_ksproperty_extdevice_capabilities_ks"></span><span id="DDK_KSPROPERTY_EXTDEVICE_CAPABILITIES_KS"></span>


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
<td><p>Device</p></td>
<td><p>[<strong>KSPROPERTY_EXTDEVICE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565156)</p></td>
<td><p>[<strong>DEVCAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558699)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a DEVCAPS structure that describes the capabilities of the external device.

Remarks
-------

The **Capabilities** member of the KSPROPERTY\_EXTDEVICE\_S structure specifies the external device's capabilities.

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

[**DEVCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff558699)

 

 






