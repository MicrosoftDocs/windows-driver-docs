---
title: KSPROPERTY\_TUNER\_MODE\_CAPS
description: The KSPROPERTY\_TUNER\_MODE\_CAPS property describes the capabilities of a tuning mode for a tuner that supports analog TV or radio tuning. This property must be implemented.
ms.assetid: 521468df-40f5-4e52-9206-127e42ad5780
keywords: ["KSPROPERTY_TUNER_MODE_CAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_MODE_CAPS
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TUNER\_MODE\_CAPS


The KSPROPERTY\_TUNER\_MODE\_CAPS property describes the capabilities of a tuning mode for a tuner that supports analog TV or radio tuning. This property must be implemented.

## <span id="ddk_ksproperty_tuner_mode_caps_ks"></span><span id="DDK_KSPROPERTY_TUNER_MODE_CAPS_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565872" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_MODE_CAPS_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565872)"><strong>KSPROPERTY_TUNER_MODE_CAPS_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies a tuner's tuning capabilities.

Remarks
-------

The **StandardsSupported** member of the KSPROPERTY\_TUNER\_MODE\_CAPS\_S structure specifies the current analog video standard.

For each separate mode (analog TV, digital TV, FM, AM, or DSS), the minidriver reports capabilities such as minimum and maximum frequency, tuning granularity, settling time, and number of inputs.

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

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872)

 

 






