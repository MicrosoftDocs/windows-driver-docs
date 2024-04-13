---
title: KSPROPERTY_TUNER_IF_MEDIUM
description: KSPROPERTY\_TUNER\_IF\_MEDIUM describes the medium for the intermediate frequency pin for devices that support digital TV tuning. This property is optional.
keywords: ["KSPROPERTY_TUNER_IF_MEDIUM Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_TUNER_IF_MEDIUM
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_TUNER\_IF\_MEDIUM


KSPROPERTY\_TUNER\_IF\_MEDIUM describes the medium for the intermediate frequency pin for devices that support digital TV tuning. This property is optional.

## <span id="ddk_ksproperty_tuner_if_medium_ks"></span><span id="DDK_KSPROPERTY_TUNER_IF_MEDIUM_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_if_medium_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_IF_MEDIUM_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_if_medium_s)"><strong>KSPROPERTY_TUNER_IF_MEDIUM_S</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/stream/kspin-medium-structure" data-raw-source="[&lt;strong&gt;KSPIN_MEDIUM&lt;/strong&gt;](./kspin-medium-structure.md)"><strong>KSPIN_MEDIUM</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPIN\_MEDIUM structure that specifies the Medium GUID for the pin that is capable of supporting tuning to an intermediate frequency.

## Remarks

The **IFMedium** member of the KSPROPERTY\_TUNER\_IF\_MEDIUM\_S structure specifies the Medium GUID of the intermediate frequency pin.

If the video capture minidriver supports KSPROPERTY\_TUNER\_IF\_MEDIUM, then *kstvtune.ax* creates an additional pin that represents the hardware-based MPEG-2 transport stream originating at the tuner. This pin is used solely to define graph topology. Data samples flowing through the user-mode stream from this pin on *kstvtune.ax* consist of [**KS\_TVTUNER\_CHANGE\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_tvtuner_change_info) structures.

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

[**KSPROPERTY\_TUNER\_IF\_MEDIUM\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_if_medium_s)
