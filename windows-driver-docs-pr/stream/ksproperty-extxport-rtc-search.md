---
title: KSPROPERTY\_EXTXPORT\_RTC\_SEARCH
description: The KSPROPERTY\_EXTXPORT\_RTC\_SEARCH property searches to a relative time counter (RTC) on a tape.
keywords: ["KSPROPERTY_EXTXPORT_RTC_SEARCH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_RTC_SEARCH
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_EXTXPORT\_RTC\_SEARCH


The KSPROPERTY\_EXTXPORT\_RTC\_SEARCH property searches to a relative time counter (RTC) on a tape.

## <span id="ddk_ksproperty_extxport_rtc_search_ks"></span><span id="DDK_KSPROPERTY_EXTXPORT_RTC_SEARCH_KS"></span>


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
<td><p>Device</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)"><strong>KSPROPERTY_EXTXPORT_S</strong></a></p></td>
<td><p>DWORD</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a DWORD that specifies the timecode, in hour:minute:second:frame, to search to on a tape.

## Remarks

The **dwTimecode** member of the KSPROPERTY\_EXTXPORT\_S structure specifies the relative time counter setting to search to.

This method is defined, but not supported.

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

[**KSPROPERTY\_EXTXPORT\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)

