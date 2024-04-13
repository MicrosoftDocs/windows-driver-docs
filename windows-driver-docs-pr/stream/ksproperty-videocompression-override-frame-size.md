---
title: KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_FRAME_SIZE
description: The KSPROPERTY\_VIDEOCOMPRESSION\_OVERRIDE\_FRAME\_SIZE property temporarily overrides the frame size (byte count). This property is optional.
keywords: ["KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_FRAME_SIZE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_FRAME_SIZE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_VIDEOCOMPRESSION\_OVERRIDE\_FRAME\_SIZE


The KSPROPERTY\_VIDEOCOMPRESSION\_OVERRIDE\_FRAME\_SIZE property temporarily overrides the frame size (byte count). This property is optional.

## <span id="ddk_ksproperty_videocompression_override_frame_size_ks"></span><span id="DDK_KSPROPERTY_VIDEOCOMPRESSION_OVERRIDE_FRAME_SIZE_KS"></span>


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
<td><p>Filter</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocompression_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOCOMPRESSION_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocompression_s)"><strong>KSPROPERTY_VIDEOCOMPRESSION_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a temporary frame size override value.

## Remarks

The **Value** member of the KSPROPERTY\_VIDEOCOMPRESSION\_S structure specifies the overriding data rate for the frame.

Minidrivers that support this property should set the **KS\_CompressionCaps\_CanCrunch** flag in the **Capabilities** member of the [**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocompression_getinfo_s) structure that retrieves the device's video compression capabilities.

This property is not supported by video capture minidrivers.

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


[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY\_VIDEOCOMPRESSION\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocompression_s)

[**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videocompression_getinfo_s)

