---
title: KSPROPERTY\_VIDEODECODER\_STATUS
description: The KSPROPERTY\_VIDEDECODER\_STATUS property retrieves status information from the video decoder. This property must be implemented.
ms.assetid: 1d8cb537-1d85-4536-bd75-33beea0f586d
keywords: ["KSPROPERTY_VIDEODECODER_STATUS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEODECODER_STATUS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_VIDEODECODER\_STATUS


The KSPROPERTY\_VIDEDECODER\_STATUS property retrieves status information from the video decoder. This property must be implemented.

## <span id="ddk_ksproperty_videodecoder_status_ks"></span><span id="DDK_KSPROPERTY_VIDEODECODER_STATUS_KS"></span>


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
<td><p>[<strong>KSPROPERTY_VIDEODECODER_STATUS_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566061)</p></td>
<td><p>[<strong>KSPROPERTY_VIDEODECODER_STATUS_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566061)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_VIDEODECODER\_STATUS\_S structure that specifies the present status of a video decoding device, such as number of lines in the incoming analog signal and whether the signal is locked in.

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

[**KSPROPERTY\_VIDEODECODER\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566061)

 

 






