---
title: KSPROPERTY\_VPCONFIG\_SETVIDEOFORMAT
description: The KSPROPERTY\_VPCONFIG\_SETVIDEOFORMAT property sets the video format. The format must match one that an earlier KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT Get request returned.
ms.assetid: f701ad32-ba85-4766-ac6b-11744af8fc0d
keywords: ["KSPROPERTY_VPCONFIG_SETVIDEOFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_SETVIDEOFORMAT
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VPCONFIG\_SETVIDEOFORMAT


The KSPROPERTY\_VPCONFIG\_SETVIDEOFORMAT property sets the video format. The format must match one that an earlier KSPROPERTY\_VPCONFIG\_GETVIDEOFORMAT **Get** request returned.

## <span id="ddk_ksproperty_vpconfig_setvideoformat_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_SETVIDEOFORMAT_KS"></span>


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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550274" data-raw-source="[&lt;strong&gt;DDPIXELFORMAT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550274)"><strong>DDPIXELFORMAT</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a DDPIXELFORMAT structure that specifies the video format to use.

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

 

 






