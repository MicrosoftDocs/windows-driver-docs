---
title: KS\_AM\_RATE\_SimpleRateChange
description: The KS\_AM\_RATE\_SimpleDataRate property sets the time stamp rate on a filter.
ms.assetid: 07399986-de5a-42fc-975e-05ea57570f58
keywords: ["KS_AM_RATE_SimpleRateChange Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KS_AM_RATE_SimpleRateChange
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KS\_AM\_RATE\_SimpleRateChange


The KS\_AM\_RATE\_SimpleDataRate property sets the time stamp rate on a filter.

## <span id="ddk_ks_am_rate_simpleratechange_ks"></span><span id="DDK_KS_AM_RATE_SIMPLERATECHANGE_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567291" data-raw-source="[&lt;strong&gt;KS_AM_SimpleRateChange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567291)"><strong>KS_AM_SimpleRateChange</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KS\_AM\_SimpleRateChange structure that describes a simple rate change for an MPEG-2 stream, such as fast-forward or rewind.

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


[**KS\_AM\_SimpleRateChange**](https://msdn.microsoft.com/library/windows/hardware/ff567291)

 

 






