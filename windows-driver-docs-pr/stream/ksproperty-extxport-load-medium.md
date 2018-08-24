---
title: KSPROPERTY\_EXTXPORT\_LOAD\_MEDIUM
description: The KSPROPERTY\_EXTXPORT\_LOAD\_MEDIUM property sets or gets an external device's load medium. For example eject, open tray, close tray, etc.
ms.assetid: 13ec61ae-4be7-4af6-875f-a6ca178cf6bc
keywords: ["KSPROPERTY_EXTXPORT_LOAD_MEDIUM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_LOAD_MEDIUM
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

# KSPROPERTY\_EXTXPORT\_LOAD\_MEDIUM


The KSPROPERTY\_EXTXPORT\_LOAD\_MEDIUM property sets or gets an external device's load medium. For example eject, open tray, close tray, etc.

## <span id="ddk_ksproperty_extxport_load_medium_ks"></span><span id="DDK_KSPROPERTY_EXTXPORT_LOAD_MEDIUM_KS"></span>


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
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the current load medium. For example eject, open tray or closed tray.

Remarks
-------

The **LoadMedium** member of the KSPROPERTY\_EXTXPORT\_S structure specifies the load medium.

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

 

 






