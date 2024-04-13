---
title: KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS
description: The KSPROPERTY\_VIDEOPROCAMP\_BRIGHTNESS property controls the brightness setting. This property is optional.
keywords: ["KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_VIDEOPROCAMP\_BRIGHTNESS


The KSPROPERTY\_VIDEOPROCAMP\_BRIGHTNESS property controls the brightness setting. This property is optional.

## <span id="ddk_ksproperty_videoprocamp_brightness_ks"></span><span id="DDK_KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS_KS"></span>


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
<td><p>Filter or node</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videoprocamp_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videoprocamp_s)"><strong>KSPROPERTY_VIDEOPROCAMP_S</strong></a> or <a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videoprocamp_node_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_NODE_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videoprocamp_node_s)"><strong>KSPROPERTY_VIDEOPROCAMP_NODE_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's brightness setting. This value is expressed in IRE units multiplied by 100 for NTSC sources. For non-NTSC sources, the units are arbitrary, with 0 representing blanking and 10000 representing pure white.

## Remarks

The **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_S structure specifies the brightness.

Brightness is also known as the black level. Modifying the brightness setting shifts the entire video signal equally for all luminance values.

Every video capture minidriver must define a range and default value for this property. The required range must be -10000 through +10000. The default value must be 750 (7.5 IRE).

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

[**KSPROPERTY\_VIDEOPROCAMP\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videoprocamp_s)

