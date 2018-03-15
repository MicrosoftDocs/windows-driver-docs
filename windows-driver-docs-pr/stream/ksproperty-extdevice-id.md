---
title: KSPROPERTY\_EXTDEVICE\_ID
description: The KSPROPERTY\_EXTDEVICE\_ID property retrieves an external device's generalized system-wide Id.
ms.assetid: ff0f37f8-55a8-45b9-8cf1-81e2cc5ac3aa
keywords: ["KSPROPERTY_EXTDEVICE_ID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTDEVICE_ID
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

# KSPROPERTY\_EXTDEVICE\_ID


The KSPROPERTY\_EXTDEVICE\_ID property retrieves an external device's generalized system-wide Id.

## <span id="ddk_ksproperty_extdevice_id_ks"></span><span id="DDK_KSPROPERTY_EXTDEVICE_ID_KS"></span>


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
<td><p>DWORD array</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a DWORD array that specifies the external device's unique node Id

Remarks
-------

The **NodeUniqueID** member of the KSPROPERTY\_EXTDEVICE\_S structure specifies the external device's unique node Id.

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

 

 






