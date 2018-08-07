---
title: KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES
description: The KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES property enumerates the available frame rates. This property is optional.
ms.assetid: f2b6fabc-c03b-4fa5-9e5b-43d7a1c26578
keywords: ["KSPROPERTY_VIDEOCONTROL_FRAME_RATES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOCONTROL_FRAME_RATES
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

# KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES


The KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES property enumerates the available frame rates. This property is optional.

## <span id="ddk_ksproperty_videocontrol_frame_rates_ks"></span><span id="DDK_KSPROPERTY_VIDEOCONTROL_FRAME_RATES_KS"></span>


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
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY_VIDEOCONTROL_FRAME_RATES_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566041)</p></td>
<td><p>[<strong>KSMULTIPLE_ITEM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563441) array</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSMULTIPLE\_ITEM array that describes available frame rates in 100-nanosecond units.

Remarks
-------

The available frame rates are returned in a KSMULTIPLE\_ITEM array. The application sends the minidriver a KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES request specifying the stream index and image dimensions in a KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES\_S structure. The minidriver returns frame rates information in the caller's KSMULTIPLE\_ITEM array buffer. This buffer has a fixed header (KSMULTIPLE\_ITEM), and a variable length amount of data following it (based on the values in the KSMULTIPLE\_ITEM structure).

Individual values are in 100-nansecond increments.

If the size of the buffer passed to the minidriver is zero, the minidriver should set the **NumberOfBytesToTransfer** member of the HW\_STREAM\_REQUEST\_BLOCK structure passed to the minidriver to the size of the buffer required and return STATUS\_BUFFER\_OVERFLOW.

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

[**KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566041)

 

 






