---
title: KSPROPERTY\_RTC\_READER
description: The KSPROPERTY\_RTC\_READER property retrieves the relative time counter (RTC) for the current tape position.
ms.assetid: 728a4504-de60-47c7-a381-3513f2d4745b
keywords: ["KSPROPERTY_RTC_READER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTC_READER
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_RTC\_READER


The KSPROPERTY\_RTC\_READER property retrieves the relative time counter (RTC) for the current tape position.

## <span id="ddk_ksproperty_rtc_reader_ks"></span><span id="DDK_KSPROPERTY_RTC_READER_KS"></span>


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
<td><p>Device</p></td>
<td><p>[<strong>KSPROPERTY_TIMECODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565781)</p></td>
<td><p>[<strong>TIMECODE_SAMPLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568528)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a TIMECODE\_SAMPLE structure that specifies the relative time counter of the current tape position.

Remarks
-------

The **TimecodeSamp** member of the KSPROPERTY\_TIMECODE\_S structure describes the relative time counter for the current tape position.

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

[**KSPROPERTY\_TIMECODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565781)

[**TIMECODE\_SAMPLE**](https://msdn.microsoft.com/library/windows/hardware/ff568528)

 

 






