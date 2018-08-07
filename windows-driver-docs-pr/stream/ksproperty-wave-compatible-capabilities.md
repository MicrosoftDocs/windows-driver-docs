---
title: KSPROPERTY\_WAVE\_COMPATIBLE\_CAPABILITIES
description: The KSPROPERTY\_WAVE\_COMPATIBLE\_CAPABILITIES property determines a device's wave compatible capabilities.
ms.assetid: 59b24d84-8b98-4928-aaae-46cb14c0d140
keywords: ["KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES
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

# KSPROPERTY\_WAVE\_COMPATIBLE\_CAPABILITIES


The KSPROPERTY\_WAVE\_COMPATIBLE\_CAPABILITIES property determines a device's wave compatible capabilities.

## <span id="ddk_ksproperty_wave_compatible_capabilities_ks"></span><span id="DDK_KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES_KS"></span>


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
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSWAVE_COMPATCAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567242)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSWAVE\_COMPATCAPS structure that describes if the wave device accepts input, produces output, or does both.

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

[**KSWAVE\_COMPATCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567242)

 

 






