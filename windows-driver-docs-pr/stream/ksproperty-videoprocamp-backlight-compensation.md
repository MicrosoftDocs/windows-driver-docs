---
title: KSPROPERTY\_VIDEOPROCAMP\_BACKLIGHT\_COMPENSATION
description: The KSPROPERTY\_VIDEOPROCAMP\_BACKLIGHT\_COMPENSATION property controls the back-light compensation setting on the camera. This property is optional.
ms.assetid: d893fc01-048a-4f2e-8587-d71be0796dcc
keywords: ["KSPROPERTY_VIDEOPROCAMP_BACKLIGHT_COMPENSATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOPROCAMP_BACKLIGHT_COMPENSATION
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

# KSPROPERTY\_VIDEOPROCAMP\_BACKLIGHT\_COMPENSATION


The KSPROPERTY\_VIDEOPROCAMP\_BACKLIGHT\_COMPENSATION property controls the back-light compensation setting on the camera. This property is optional.

## <span id="ddk_ksproperty_videoprocamp_backlight_compensation_ks"></span><span id="DDK_KSPROPERTY_VIDEOPROCAMP_BACKLIGHT_COMPENSATION_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_VIDEOPROCAMP_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566089) or [<strong>KSPROPERTY_VIDEOPROCAMP_NODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566080)</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's back-light compensation setting. This value may be either 0 or 1. The default value for this property is 1. A value of 0 indicates that the back-light compensation is disabled. The default value of 1 indicates that the back-light compensation is enabled.

Remarks
-------

The **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_S structure specifies whether the backlight compensation is enabled or disabled.

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

[**KSPROPERTY\_VIDEOPROCAMP\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566089)

 

 






