---
title: DVD Decoder Related Clock Events
author: windows-driver-content
description: DVD Decoder Related Clock Events
ms.assetid: c3ed0ee4-95a3-4596-9f29-86397b0d8753
keywords:
- DVD decoder minidrivers WDK , master clock
- decoder minidrivers WDK DVD , master clock
- master clocks WDK DVD decoder
- clocks WDK DVD decoder
- events WDK DVD decoder
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DVD Decoder Related Clock Events





Any DVD decoder minidriver stream that supports a master clock for DVD playback must also support the following two clock events: [**KSEVENT\_CLOCK\_POSITION\_MARK**](https://msdn.microsoft.com/library/windows/hardware/ff561811) and [**KSEVENT\_CLOCK\_INTERVAL\_MARK**](https://msdn.microsoft.com/library/windows/hardware/ff561805). These events provide reference information to any component in the system when they need to synchronize any time during DVD playback. The GUID for the event set is [**KSEVENTSETID\_Clock**](https://msdn.microsoft.com/library/windows/hardware/ff561764).

The DVD decoder minidriver should check for outstanding clock events. Typical implementations might examine all clock events on interrupts generated for each video start code, or on interrupts generated for VSYNC. The following events are provided.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KSEVENT_CLOCK_POSITION_MARK</p></td>
<td><p>This event provides notification that a specified stream time has been exceeded. This event is signaled using the <em>SignalStreamEvent</em> parameter to the [<strong>StreamClassStreamNotification</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568266) function. After this call has been made, the <strong>KSEVENT_ENTRY</strong> structure may not be used for any further function calls, including calls to the [<strong>StreamClassGetNextEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568244) function.</p></td>
</tr>
<tr class="even">
<td><p>KSEVENT_CLOCK_INTERVAL_MARK</p></td>
<td><p>This event provides periodic notification at a specified interval after a specified start time has been reached.</p></td>
</tr>
</tbody>
</table>

 

 

 




