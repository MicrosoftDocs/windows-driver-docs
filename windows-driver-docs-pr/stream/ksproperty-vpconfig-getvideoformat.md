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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT


The KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT property retrieves an array of supported pixel formats.

## <span id="ddk_ksproperty_vpconfig_getvideoformat_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_GETVIDEOFORMAT_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550274" data-raw-source="[&lt;strong&gt;DDPIXELFORMAT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550274)"><strong>DDPIXELFORMAT</strong></a></p></td>
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

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274)

 

 






