---
title: Video Capture Events
author: windows-driver-content
description: Video Capture Events
ms.assetid: 9d40b9f7-41c1-4410-afc7-9b4ff1c2fe7e
keywords:
- events WDK video capture
- KSEVENTSETID_VIDCAPNotify
- video capture events WDK AVStream
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Capture Events


The [KSEVENTSETID\_VIDCAPNotify](https://msdn.microsoft.com/library/windows/hardware/ff561773) event set contains events related to tuner events. The following table describes the events that are part of the KSEVENTSETID\_VIDCAPNotify event set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSEVENTSETID_VIDCAPNotify KS events</th>
<th>Event description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSEVENT_VIDCAPTOSTI_EXT_TRIGGER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561912)</p></td>
<td><p>Signals to a registered client when a button on a video capture device is triggered.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSEVENT_VIDCAP_AUTO_UPDATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561916)</p></td>
<td><p>Signals to a registered client when a property value changes.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSEVENT_VIDCAP_SEARCH</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561923)</p></td>
<td><p>Signals to a registered client when a search completes.</p></td>
</tr>
</tbody>
</table>

 

 

 




