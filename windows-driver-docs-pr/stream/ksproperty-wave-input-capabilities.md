---
title: KSPROPERTY\_WAVE\_INPUT\_CAPABILITIES
description: The KSPROPERTY\_WAVE\_INPUT\_CAPABILITIES property returns a wave device's input capabilities.
ms.assetid: 84ed0f41-52b6-40e0-b334-c336e158cbfc
keywords: ["KSPROPERTY_WAVE_INPUT_CAPABILITIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_WAVE_INPUT_CAPABILITIES
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_WAVE\_INPUT\_CAPABILITIES


The KSPROPERTY\_WAVE\_INPUT\_CAPABILITIES property returns a wave device's input capabilities.

## <span id="ddk_ksproperty_wave_input_capabilities_ks"></span><span id="DDK_KSPROPERTY_WAVE_INPUT_CAPABILITIES_KS"></span>


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
<td><p>[<strong>KSPROPERTY</strong>](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)</p></td>
<td><p>[<strong>KSWAVE_INPUT_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567245)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSWAVE\_INPUT\_CAPABILITIES structure that describes the input capabilities of a wave device, including the maximum number of audio channels, the range of bits per sample, the range of sampling frequency, and the total and active number of connections.

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

[**KSWAVE\_INPUT\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567245)

 

 






