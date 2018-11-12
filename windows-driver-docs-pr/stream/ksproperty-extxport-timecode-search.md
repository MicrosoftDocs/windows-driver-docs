---
title: KSPROPERTY\_EXTXPORT\_TIMECODE\_SEARCH
description: The KSPROPERTY\_EXTXPORT\_TIMECODE\_SEARCH property searches to a specific timecode.
ms.assetid: 34252fce-426b-4f75-b57f-fa86654ffc5f
keywords: ["KSPROPERTY_EXTXPORT_TIMECODE_SEARCH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_TIMECODE_SEARCH
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_EXTXPORT\_TIMECODE\_SEARCH


The KSPROPERTY\_EXTXPORT\_TIMECODE\_SEARCH property searches to a specific timecode.

## <span id="ddk_ksproperty_extxport_timecode_search_ks"></span><span id="DDK_KSPROPERTY_EXTXPORT_TIMECODE_SEARCH_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565167" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTXPORT_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565167)"><strong>KSPROPERTY_EXTXPORT_S</strong></a></p></td>
<td><p>Embedded <strong>TIMECODE</strong> structure</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is an embedded **TIMECODE** structure member of the KSPROPERTY\_EXTXPORT\_S structure that describes the specific timecode to search to, including frame, second, minute and hour.

Remarks
-------

This method is defined, but not supported.

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

[**KSPROPERTY\_EXTXPORT\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565167)

 

 






