---
title: KSPROPERTY\_VIDEOCOMPRESSION\_QUALITY
description: The KSPROPERTY\_VIDECOMPRESSION\_QUALITY property controls the video compression quality setting. This property must be implemented.
ms.assetid: 7566f60e-fe49-4009-bd61-b29d2adb4e8c
keywords: ["KSPROPERTY_VIDEOCOMPRESSION_QUALITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOCOMPRESSION_QUALITY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VIDEOCOMPRESSION\_QUALITY


The KSPROPERTY\_VIDECOMPRESSION\_QUALITY property controls the video compression quality setting. This property must be implemented.

## <span id="ddk_ksproperty_videocompression_quality_ks"></span><span id="DDK_KSPROPERTY_VIDEOCOMPRESSION_QUALITY_KS"></span>


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
<td><p>Filter</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566018" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCOMPRESSION_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566018)"><strong>KSPROPERTY_VIDEOCOMPRESSION_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a video compression quality value.

Remarks
-------

The **Value** member of the KSPROPERTY\_VIDEOCOMPRESSION\_S structure specifies the quality metric.

Values for this property range from 0 to 10000. Zero indicates the lowest quality, 10000 the highest. The minidriver determines its own default value.

Minidrivers that support this property should set the **KS\_CompressionCaps\_CanQuality** flag in the **Capabilities** member of the [**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565979) structure that retrieves the minidriver's video compression capabilities. If a minidriver sets the KS\_CompressionCaps\_CanQuality, it should support both get and set requests for the property.

Values for this property range from 0 to 10000. Zero indicates the lowest quality, 10000 the highest. The minidriver determines its own default value.

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

[**KSPROPERTY\_VIDEOCOMPRESSION\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566018)

[**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565979)

 

 






