---
title: Using Events in Display Drivers
description: Using Events in Display Drivers
keywords:
- events WDK Windows 2000 display
- display drivers WDK Windows 2000 , events
ms.date: 04/20/2017
---

# Using Events in Display Drivers


## <span id="ddk_using_events_in_display_drivers_gg"></span><span id="DDK_USING_EVENTS_IN_DISPLAY_DRIVERS_GG"></span>


GDI provides support for events, a type of [kernel dispatcher object](../kernel/introduction-to-kernel-dispatcher-objects.md) that can be used to synchronize two threads running below DISPATCH\_LEVEL. A display driver can use events to synchronize access to the video hardware:

-   By the display driver and the video miniport driver

-   By the display or video miniport driver and another component, such as an OpenGL driver or a program extension (such as the Display program in Control Panel).

The following table lists the GDI event-related functions.

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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engclearevent" data-raw-source="[&lt;strong&gt;EngClearEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engclearevent)"><strong>EngClearEvent</strong></a></p></td>
<td align="left"><p>Sets a given event object to the nonsignaled state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engcreateevent" data-raw-source="[&lt;strong&gt;EngCreateEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engcreateevent)"><strong>EngCreateEvent</strong></a></p></td>
<td align="left"><p>Creates a synchronization event object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engdeleteevent" data-raw-source="[&lt;strong&gt;EngDeleteEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engdeleteevent)"><strong>EngDeleteEvent</strong></a></p></td>
<td align="left"><p>Deletes the specified event object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engmapevent" data-raw-source="[&lt;strong&gt;EngMapEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engmapevent)"><strong>EngMapEvent</strong></a></p></td>
<td align="left"><p>Maps a user-mode event object to kernel mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engreadstateevent" data-raw-source="[&lt;strong&gt;EngReadStateEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engreadstateevent)"><strong>EngReadStateEvent</strong></a></p></td>
<td align="left"><p>Returns the current state of a given event object: signaled or nonsignaled.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsetevent" data-raw-source="[&lt;strong&gt;EngSetEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsetevent)"><strong>EngSetEvent</strong></a></p></td>
<td align="left"><p>Sets an event object to the signaled state if it was not already in that state, and returns the event object's previous state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunmapevent" data-raw-source="[&lt;strong&gt;EngUnmapEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunmapevent)"><strong>EngUnmapEvent</strong></a></p></td>
<td align="left"><p>Cleans up the kernel-mode resources allocated for a mapped user-mode event.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engwaitforsingleobject" data-raw-source="[&lt;strong&gt;EngWaitForSingleObject&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engwaitforsingleobject)"><strong>EngWaitForSingleObject</strong></a></p></td>
<td align="left"><p>Puts the current thread into a wait state until the given dispatch object is set to the signaled state, or (optionally) until the wait times out.</p></td>
</tr>
</tbody>
</table>

 

The video port driver also provides support for events to video miniport drivers. See [Events in Video Miniport Drivers (Windows 2000 Model)](events-in-video-miniport-drivers--windows-2000-model-.md) for more information.

For a broader perspective on events, see [Event Objects](../kernel/event-objects.md).

