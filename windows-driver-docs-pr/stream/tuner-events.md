---
title: Tuner Events
description: Tuner Events
keywords:
- tuner events WDK video capture
- events WDK video capture
- EVENTSETID_TUNER
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tuner Events


The [EVENTSETID\_TUNER](./eventsetid-tuner.md) event set contains tuner events. The following tables describe the events that are part of the EVENTSETID\_TUNER event set. The second table describes a tuner event that is implemented for an AVStream minidriver that runs on Windows Vista and later.

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
<td><p><a href="/windows-hardware/drivers/stream/ksevent-tuner-changed" data-raw-source="[&lt;strong&gt;KSEVENT_TUNER_CHANGED&lt;/strong&gt;](./ksevent-tuner-changed.md)"><strong>KSEVENT_TUNER_CHANGED</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/stream/ksevent-tuner-initiate-scan" data-raw-source="[&lt;strong&gt;KSEVENT_TUNER_INITIATE_SCAN&lt;/strong&gt;](./ksevent-tuner-initiate-scan.md)"><strong>KSEVENT_TUNER_INITIATE_SCAN</strong></a></p></td>
<td><p>Initiates a signal scan and notifies DirectShow when the scan completes.</p></td>
</tr>
</tbody>
</table>

 

