---
title: DVD Decoder Related KS Events
description: DVD Decoder Related KS Events
ms.assetid: 19fd2c88-72f4-4742-8c96-74be250dd59d
keywords:
- DVD decoder minidrivers WDK , KS events
- decoder minidrivers WDK DVD , KS events
- KS events WDK DVD decoder
- events WDK DVD decoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DVD Decoder Related KS Events





The following tables describe the kernel streaming event set and its respective event that is related to DVD decoder hardware:

The [KSEVENTSETID\_VPNotify](https://msdn.microsoft.com/library/windows/hardware/ff561780) event set groups all kernel streaming events that are related to tuner events.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSEVENTSETID_VPNotify KS Events</th>
<th>Event Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561933" data-raw-source="[&lt;strong&gt;KSEVENT_VPNOTIFY_FORMATCHANGE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561933)"><strong>KSEVENT_VPNOTIFY_FORMATCHANGE</strong></a></p></td>
<td><p>Notifies DirectShow of a change in the video port configuration, such as a change in resolution from 640x480 to 720x480.</p></td>
</tr>
</tbody>
</table>

 

 

 




