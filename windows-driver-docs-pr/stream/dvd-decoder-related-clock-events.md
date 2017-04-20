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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DVD Decoder Related Clock Events


## <a href="" id="ddk-dvd-related-clock-events-ksg"></a>


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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20DVD%20Decoder%20Related%20Clock%20Events%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


