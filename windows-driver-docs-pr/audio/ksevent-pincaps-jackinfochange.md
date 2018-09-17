---
title: KSEVENT\_PINCAPS\_JACKINFOCHANGE
description: The KSEVENT\_PINCAPS\_JACKINFOCHANGE event indicates to the audio stack that the jack information for the audio device has changed.
ms.assetid: 46514043-5044-4373-94ca-b00898aeefba
keywords: ["KSEVENT_PINCAPS_JACKINFOCHANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_PINCAPS_JACKINFOCHANGE
api_location:
- Ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSEVENT\_PINCAPS\_JACKINFOCHANGE


The `KSEVENT_PINCAPS_JACKINFOCHANGE` event indicates to the audio stack that the jack information for the audio device has changed.

### <span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Target</th>
<th align="left">Event descriptor type</th>
<th align="left">Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Pin</p></td>
<td align="left"><p>[<strong>KSEVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561744)</p></td>
<td align="left"><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a **KSEVENTDATA** structure that specifies the notification method to use for this event.

Remarks
-------

For information about how to implement support for the `KSEVENT_PINCAPS_JACKINFOCHANGE` event, see the Remarks section of the [**KSEVENT\_PINCAPS\_FORMATCHANGE**](ksevent-pincaps-formatchange.md) topic.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744)

[**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750)

[**KSEVENT\_PINCAPS\_FORMATCHANGE**](ksevent-pincaps-formatchange.md)

 

 






