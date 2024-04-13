---
title: KSPROPERTY_TUNER_CAPS
description: The KSPROPERTY\_TUNER\_CAPS property describes the basic capabilities of a tuner. This property must be implemented.
keywords: ["KSPROPERTY_TUNER_CAPS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_TUNER_CAPS
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_TUNER\_CAPS


The KSPROPERTY\_TUNER\_CAPS property describes the basic capabilities of a tuner. This property must be implemented.

## <span id="ddk_ksproperty_tuner_caps_ks"></span><span id="DDK_KSPROPERTY_TUNER_CAPS_KS"></span>


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
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_caps_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_CAPS_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_caps_s)"><strong>KSPROPERTY_TUNER_CAPS_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies the tuning modes supported by the streaming minidriver.

## Remarks

The **ModesSupported** member of the KSPROPERTY\_TUNER\_CAPS\_S structure indicates the tuning modes supported by the video capture minidriver.

A single tuning device may support tuning digital TV, analog TV, AM/FM radio, as well as digital satellite systems (DSS).

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

[**KSPROPERTY\_TUNER\_CAPS\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_caps_s)

[**KSPROPERTY\_TUNER\_MODE\_CAPS**](ksproperty-tuner-mode-caps.md)

