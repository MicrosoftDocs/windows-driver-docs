---
title: Tuner Events
author: windows-driver-content
description: Tuner Events
ms.assetid: eb5e0698-2641-4d47-9fa3-d1969a03c795
keywords:
- tuner events WDK video capture
- events WDK video capture
- EVENTSETID_TUNER
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Tuner Events


The [EVENTSETID\_TUNER](https://msdn.microsoft.com/library/windows/hardware/ff559566) event set contains tuner events. The following tables describe the events that are part of the EVENTSETID\_TUNER event set. The second table describes a tuner event that is implemented for an AVStream minidriver that runs on Windows Vista and later.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>EVENTSETID_TUNER KS event</th>
<th>Event description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSEVENT_TUNER_CHANGED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561894)</p></td>
<td><p>Signals to DirectShow that the tuner has changed, for example, because of tuning to a new television channel.</p></td>
</tr>
</tbody>
</table>

 

The following table describes the EVENTSETID\_TUNER event that is new for Windows Vista.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>EVENTSETID_TUNER KS event</th>
<th>Event description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSEVENT_TUNER_INITIATE_SCAN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561898)</p></td>
<td><p>Initiates a signal scan and notifies DirectShow when the scan completes.</p></td>
</tr>
</tbody>
</table>

 

 

 




