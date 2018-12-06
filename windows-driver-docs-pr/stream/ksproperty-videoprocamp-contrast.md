---
title: KSPROPERTY\_VIDEOPROCAMP\_CONTRAST
description: The KSPROPERTY\_VIDEOPROCAMP\_CONTRAST property controls a camera's contrast (luma gain) setting. This property is optional.
ms.assetid: 0e94aec4-b258-44be-aa6e-f0a40b803564
keywords: ["KSPROPERTY_VIDEOPROCAMP_CONTRAST Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOPROCAMP_CONTRAST
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VIDEOPROCAMP\_CONTRAST


The KSPROPERTY\_VIDEOPROCAMP\_CONTRAST property controls a camera's contrast (luma gain) setting. This property is optional.

## <span id="ddk_ksproperty_videoprocamp_contrast_ks"></span><span id="DDK_KSPROPERTY_VIDEOPROCAMP_CONTRAST_KS"></span>


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
<td><p>Filter or node</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566089" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566089)"><strong>KSPROPERTY_VIDEOPROCAMP_S</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff566080" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_NODE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566080)"><strong>KSPROPERTY_VIDEOPROCAMP_NODE_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's contrast setting. The contrast value is expressed as a gain factor multiplied by 100.

Remarks
-------

The **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_S structure specifies the contrast value.

Every video capture minidriver must define a range and default value for the **Value** member of this property. The required range must be 0 to 10000. The default value must be 100 (1x).

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

[**KSPROPERTY\_VIDEOPROCAMP\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566089)

 

 






