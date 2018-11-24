---
title: KSPROPERTY\_WAVE\_PAN
description: The KSPROPERTY\_WAVE\_PAN property specifies a wave device's pan setting.
ms.assetid: 5ec4dc6d-44cb-4716-9f5b-dd044cd38239
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
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567249" data-raw-source="[&lt;strong&gt;KSWAVE_PAN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567249)"><strong>KSWAVE_PAN</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSWAVE\_PAN structure the describes the left and right pan level.

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

[**KSWAVE\_PAN**](https://msdn.microsoft.com/library/windows/hardware/ff567249)

 

 






