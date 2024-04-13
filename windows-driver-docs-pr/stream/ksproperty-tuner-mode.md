---
title: KSPROPERTY_TUNER_MODE
description: User-mode clients use the KSPROPERTY\_TUNER\_MODE property to get or set the tuning mode of a device, such as analog TV, digital TV, FM, AM, or DSS. This property must be implemented.
keywords: ["KSPROPERTY_TUNER_MODE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_TUNER_MODE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_TUNER\_MODE


User-mode clients use the KSPROPERTY\_TUNER\_MODE property to get or set the tuning mode of a device, such as analog TV, digital TV, FM, AM, or DSS. This property must be implemented.

## <span id="ddk_ksproperty_tuner_mode_ks"></span><span id="DDK_KSPROPERTY_TUNER_MODE_KS"></span>


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
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_mode_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_MODE_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_mode_s)"><strong>KSPROPERTY_TUNER_MODE_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies a tuner's current tuning mode.

## Remarks

The **Mode** member of the KSPROPERTY\_TUNER\_MODE\_S structure specifies the current tuner mode.

## Requirements

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


[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY\_TUNER\_MODE\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_mode_s)

