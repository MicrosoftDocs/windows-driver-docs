---
title: KSPROPERTY\_VIDEODECODER\_STANDARD
description: The KSPROPERTY\_VIDEODECODER\_STANDARD property controls the current analog video standard. This property must be implemented.
ms.assetid: 955c267a-703e-4d18-a4e9-710f316cfb48
keywords: ["KSPROPERTY_VIDEODECODER_STANDARD Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEODECODER_STANDARD
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

# KSPROPERTY\_VIDEODECODER\_STANDARD


The KSPROPERTY\_VIDEODECODER\_STANDARD property controls the current analog video standard. This property must be implemented.

## <span id="ddk_ksproperty_videodecoder_standard_ks"></span><span id="DDK_KSPROPERTY_VIDEODECODER_STANDARD_KS"></span>


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
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY_VIDEODECODER_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566052)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the current analog video standard.

Remarks
-------

The **Value** member of the KSPROPERTY\_VIDEODECODER\_S structure specifies the current analog video standard.

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

[**KSPROPERTY\_VIDEODECODER\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566052)

 

 






