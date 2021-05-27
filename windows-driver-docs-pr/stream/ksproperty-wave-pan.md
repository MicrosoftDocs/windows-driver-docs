---
title: KSPROPERTY\_WAVE\_PAN
description: The KSPROPERTY\_WAVE\_PAN property specifies a wave device's pan setting.
keywords: ["KSPROPERTY_WAVE_PAN Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_WAVE_PAN
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_WAVE\_PAN


The KSPROPERTY\_WAVE\_PAN property specifies a wave device's pan setting.

## <span id="ddk_ksproperty_wave_pan_ks"></span><span id="DDK_KSPROPERTY_WAVE_PAN_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/previous-versions/ff567249(v=vs.85)" data-raw-source="[&lt;strong&gt;KSWAVE_PAN&lt;/strong&gt;](/previous-versions/ff567249(v=vs.85))"><strong>KSWAVE_PAN</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSWAVE\_PAN structure the describes the left and right pan level.

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


[**KSPROPERTY**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSWAVE\_PAN**](/previous-versions/ff567249(v=vs.85))

