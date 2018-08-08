---
title: KSEVENT\_VIDCAP\_AUTO\_UPDATE
description: The KSEVENT\_VIDCAP\_AUTO\_UPDATE event is triggered when a property value changes.
ms.assetid: dd7e665f-104d-4276-94aa-62d64faba69d
keywords: ["KSEVENT_VIDCAP_AUTO_UPDATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VIDCAP_AUTO_UPDATE
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSEVENT\_VIDCAP\_AUTO\_UPDATE


The KSEVENT\_VIDCAP\_AUTO\_UPDATE event is triggered when a property value changes.

## <span id="ddk_ksevent_vidcap_auto_update_ks"></span><span id="DDK_KSEVENT_VIDCAP_AUTO_UPDATE_KS"></span>


### <span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<th>Event descriptor type</th>
<th>Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>[<strong>KSEVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561744)</p></td>
<td><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Clients might register for this event to be notified if a user flips a switch on the device, changing a property value. For this event to be available, the hardware implementation must provide support for this feature.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

 

 





