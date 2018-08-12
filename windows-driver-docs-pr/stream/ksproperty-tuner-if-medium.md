---
title: KSPROPERTY\_TUNER\_IF\_MEDIUM
description: KSPROPERTY\_TUNER\_IF\_MEDIUM describes the medium for the intermediate frequency pin for devices that support digital TV tuning. This property is optional.
ms.assetid: 1144777c-e81c-4b8f-a634-411591c71356
keywords: ["KSPROPERTY_TUNER_IF_MEDIUM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_IF_MEDIUM
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

# KSPROPERTY\_TUNER\_IF\_MEDIUM


KSPROPERTY\_TUNER\_IF\_MEDIUM describes the medium for the intermediate frequency pin for devices that support digital TV tuning. This property is optional.

## <span id="ddk_ksproperty_tuner_if_medium_ks"></span><span id="DDK_KSPROPERTY_TUNER_IF_MEDIUM_KS"></span>


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
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY_TUNER_IF_MEDIUM_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565848)</p></td>
<td><p>[<strong>KSPIN_MEDIUM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563538)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPIN\_MEDIUM structure that specifies the Medium GUID for the pin that is capable of supporting tuning to an intermediate frequency.

Remarks
-------

The **IFMedium** member of the KSPROPERTY\_TUNER\_IF\_MEDIUM\_S structure specifies the Medium GUID of the intermediate frequency pin.

If the video capture minidriver supports KSPROPERTY\_TUNER\_IF\_MEDIUM, then *kstvtune.ax* creates an additional pin that represents the hardware-based MPEG-2 transport stream originating at the tuner. This pin is used solely to define graph topology. Data samples flowing through the user-mode stream from this pin on *kstvtune.ax* consist of [**KS\_TVTUNER\_CHANGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567691) structures.

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

[**KSPROPERTY\_TUNER\_IF\_MEDIUM\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565848)

 

 






