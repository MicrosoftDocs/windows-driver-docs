---
title: KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT
description: The KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT property retrieves an array of supported pixel formats.
ms.assetid: 74cc8cbc-cd81-43e1-ba15-3105a4c70808
keywords: ["KSPROPERTY_VPCONFIG_GETVIDEOFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_GETVIDEOFORMAT
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

# KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT


The KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT property retrieves an array of supported pixel formats.

## <span id="ddk_ksproperty_vpconfig_getvideoformat_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_GETVIDEOFORMAT_KS"></span>


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
<td><p>[<strong>DDPIXELFORMAT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550274)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a DDPIXELFORMAT structure that describes the pixel format of the video port.

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

[**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274)

 

 






