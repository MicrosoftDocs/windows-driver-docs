---
title: KSPROPERTY\_VPCONFIG\_MAXPIXELRATE
description: The KSPROPERTY\_VPCONFIG\_MAXPIXELRATE property specifies the maximum pixel rate based on pixel format and specifies the dimension (width by height) of the connection.
keywords: ["KSPROPERTY_VPCONFIG_MAXPIXELRATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_MAXPIXELRATE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VPCONFIG\_MAXPIXELRATE


The KSPROPERTY\_VPCONFIG\_MAXPIXELRATE property specifies the maximum pixel rate based on pixel format and specifies the dimension (width by height) of the connection.

## <span id="ddk_ksproperty_vpconfig_maxpixelrate_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_MAXPIXELRATE_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksvpmaxpixelrate" data-raw-source="[&lt;strong&gt;KSVPMAXPIXELRATE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksvpmaxpixelrate)"><strong>KSVPMAXPIXELRATE</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSVPMAXPIXELRATE structure that describes the width, height, and maximum number of pixels per second that the video port supports.

## Requirements

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


[**KSPROPERTY**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSVPMAXPIXELRATE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksvpmaxpixelrate)

