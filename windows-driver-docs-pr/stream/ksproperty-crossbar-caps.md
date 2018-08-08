---
title: KSPROPERTY\_CROSSBAR\_CAPS
description: The KSPROPERTY\_CROSSBAR\_CAPS property retrieves the crossbar capabilities of the device (the number of input and output pins on the crossbar). This property must be implemented.
ms.assetid: f7dd806c-065d-48c7-ab58-3f5ef95451d5
keywords: ["KSPROPERTY_CROSSBAR_CAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CROSSBAR_CAPS
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

# KSPROPERTY\_CROSSBAR\_CAPS


The KSPROPERTY\_CROSSBAR\_CAPS property retrieves the crossbar capabilities of the device (the number of input and output pins on the crossbar). This property must be implemented.

## <span id="ddk_ksproperty_crossbar_caps_ks"></span><span id="DDK_KSPROPERTY_CROSSBAR_CAPS_KS"></span>


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
<td><p>[<strong>KSPROPERTY_CROSSBAR_CAPS_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565120)</p></td>
<td><p>Pair of ULONGs</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a pair of ULONGs that specify the number of audio and video input pins on the crossbar, and the number of audio and video output pins on the crossbar.

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

[**KSPROPERTY\_CROSSBAR\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565120)

 

 






