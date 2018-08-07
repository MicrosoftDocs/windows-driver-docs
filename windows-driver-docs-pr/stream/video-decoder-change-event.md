---
title: Video Decoder Change Event
author: windows-driver-content
description: Video Decoder Change Event
ms.assetid: 94269541-49e5-4273-874a-c6c2643ec2ae
keywords:
- video decoder changed event WDK video capture
- decoder changed event WDK video capture
- events WDK video capture
- EVENTSETID_VIDEODECODER
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Video Decoder Change Event


The [EVENTSETID\_VIDEODECODER](https://msdn.microsoft.com/library/windows/hardware/ff559569) event set contains the video decoder changed event. The following table describes the events that are part of the EVENTSETID\_VIDEODECODER event set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>EVENTSETID_VIDEODECODER KS events</th>
<th>Event description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSEVENT_VIDEODECODER_CHANGED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561931)</p></td>
<td><p>Signals to DirectShow that the video decoder has changed, for example, because of the selection of an SVideo input port from a composite input port.</p></td>
</tr>
</tbody>
</table>

 

 

 




