---
title: KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT
description: The KSPROPERTY\_VIDEOPROCAMP\_DIGITAL\_MULTIPLIER\_LIMIT property specifies the upper limit for the amount of digital zoom that can be applied to the image.
keywords: ["KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_VIDEOPROCAMP\_DIGITAL\_MULTIPLIER\_LIMIT


The KSPROPERTY\_VIDEOPROCAMP\_DIGITAL\_MULTIPLIER\_LIMIT property specifies the upper limit for the amount of digital zoom that can be applied to the image.

## <span id="ddk_ksproperty_videoprocamp_digital_multiplier_limit_ks"></span><span id="DDK_KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT_KS"></span>


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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
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

 

The property value (operation data) is a LONG that specifies a camera's upper digital multiplier limit. The value specifies the maximum value of the digital multiplier that the device can apply to the optical image.

## Remarks

When making a set request, the client should supply a digital multiplier value in the **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_NODE\_S structure.

A client might use a set request to establish a user-defined upper limit for digital zoom.

When making a get request, the client receives one of the preceding values in the **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_NODE\_S structure.

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

