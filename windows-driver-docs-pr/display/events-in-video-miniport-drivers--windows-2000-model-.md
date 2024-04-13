---
title: Events in Video Miniport Drivers (Windows 2000 Model)
description: Events in Video Miniport Drivers (Windows 2000 Model)
keywords:
- video miniport drivers WDK Windows 2000 , events
- events WDK video miniport
ms.date: 04/20/2017
---

# Events in Video Miniport Drivers (Windows 2000 Model)


## <span id="ddk_events_in_video_miniport_drivers_windows_2000_model__gg"></span><span id="DDK_EVENTS_IN_VIDEO_MINIPORT_DRIVERS_WINDOWS_2000_MODEL__GG"></span>


The video port driver provides support for events, a type of [kernel dispatcher object](../kernel/introduction-to-kernel-dispatcher-objects.md) that can be used to synchronize two threads running below DISPATCH\_LEVEL. A video miniport driver can use events to synchronize access to the video hardware:

-   By the video miniport driver and the display driver

-   By the display or video miniport driver and another component, such as an OpenGL driver or a program extension (such as the Display program in Control Panel).

The following table lists the event-related functions that the video port driver supplies.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/video/nf-video-videoportclearevent" data-raw-source="[&lt;strong&gt;VideoPortClearEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/nf-video-videoportclearevent)"><strong>VideoPortClearEvent</strong></a></p></td>
<td align="left"><p>Sets a given event object to the nonsignaled state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/video/nf-video-videoportcreateevent" data-raw-source="[&lt;strong&gt;VideoPortCreateEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/nf-video-videoportcreateevent)"><strong>VideoPortCreateEvent</strong></a></p></td>
<td align="left"><p>Creates an event object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/video/nf-video-videoportdeleteevent" data-raw-source="[&lt;strong&gt;VideoPortDeleteEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/nf-video-videoportdeleteevent)"><strong>VideoPortDeleteEvent</strong></a></p></td>
<td align="left"><p>Deletes the specified event object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/video/nf-video-videoportreadstateevent" data-raw-source="[&lt;strong&gt;VideoPortReadStateEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/nf-video-videoportreadstateevent)"><strong>VideoPortReadStateEvent</strong></a></p></td>
<td align="left"><p>Returns the current state of a given event object: signaled or nonsignaled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/video/nf-video-videoportsetevent" data-raw-source="[&lt;strong&gt;VideoPortSetEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/nf-video-videoportsetevent)"><strong>VideoPortSetEvent</strong></a></p></td>
<td align="left"><p>Sets an event object to the signaled state if it was not already in that state, and returns the event object's previous state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/video/nf-video-videoportwaitforsingleobject" data-raw-source="[&lt;strong&gt;VideoPortWaitForSingleObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/video/nf-video-videoportwaitforsingleobject)"><strong>VideoPortWaitForSingleObject</strong></a></p></td>
<td align="left"><p>Puts the current thread into a wait state until the given dispatch object is set to the signaled state, or (optionally) until the wait times out.</p></td>
</tr>
</tbody>
</table>

 

GDI also provides support for events to display drivers. See [Using Events in Display Drivers](using-events-in-display-drivers.md) for more information.

For a broader perspective on events, see [Event Objects](../kernel/event-objects.md) in the *Kernel-Mode Drivers Design Guide*.

