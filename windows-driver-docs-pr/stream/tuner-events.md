---
title: Tuner Events
author: windows-driver-content
description: Tuner Events
ms.assetid: eb5e0698-2641-4d47-9fa3-d1969a03c795
keywords: ["tuner events WDK video capture", "events WDK video capture", "EVENTSETID_TUNER"]
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Tuner%20Events%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


