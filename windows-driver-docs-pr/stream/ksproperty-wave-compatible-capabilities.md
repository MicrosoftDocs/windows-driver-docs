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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_WAVE\_COMPATIBLE\_CAPABILITIES


The KSPROPERTY\_WAVE\_COMPATIBLE\_CAPABILITIES property determines a device's wave compatible capabilities.

## <span id="ddk_ksproperty_wave_compatible_capabilities_ks"></span><span id="DDK_KSPROPERTY_WAVE_COMPATIBLE_CAPABILITIES_KS"></span>


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
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567242" data-raw-source="[&lt;strong&gt;KSWAVE_COMPATCAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567242)"><strong>KSWAVE_COMPATCAPS</strong></a></p></td>
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

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSWAVE\_COMPATCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567242)

 

 






