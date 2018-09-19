---
title: KSPROPERTY\_WAVE\_BUFFER
description: The KSPROPERTY\_WAVE\_BUFFER property describes a wave device's buffer.
ms.assetid: b2ef458a-a701-4403-875b-1b06164c80a1
keywords: ["KSPROPERTY_WAVE_BUFFER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_WAVE_BUFFER
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_WAVE\_BUFFER


The KSPROPERTY\_WAVE\_BUFFER property describes a wave device's buffer.

## <span id="ddk_ksproperty_wave_buffer_ks"></span><span id="DDK_KSPROPERTY_WAVE_BUFFER_KS"></span>


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
<td><p>[<strong>KSPROPERTY</strong>](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)</p></td>
<td><p>[<strong>KSWAVE_BUFFER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567239)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSWAVE\_BUFFER structure that describes the looping attributes of the buffer, buffer size (in bytes), and starting address of the buffer.

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

[**KSWAVE\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff567239)

 

 






