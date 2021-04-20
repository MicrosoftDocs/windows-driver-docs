---
title: GDI Event Services
description: GDI Event Services
keywords:
- GDI WDK Windows 2000 display , events
- graphics drivers WDK Windows 2000 display , events
- drawing WDK GDI , events
- events WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Event Services


## <span id="ddk_gdi_event_services_gg"></span><span id="DDK_GDI_EVENT_SERVICES_GG"></span>


GDI provides several services related to events. Drivers using these services can create and delete events, map and unmap events, and read, set and clear events.

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
<td align="left"><p>Sets a specified event object to the nonsignaled state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engcreateevent" data-raw-source="[&lt;strong&gt;EngCreateEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engcreateevent)"><strong>EngCreateEvent</strong></a></p></td>
<td align="left"><p>Creates a synchronization event object that can be used to synchronize hardware access between a display driver and the video miniport driver.</p></td>
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
<td align="left"><p>Returns the current state of the specified event object: signaled or nonsignaled.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsetevent" data-raw-source="[&lt;strong&gt;EngSetEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsetevent)"><strong>EngSetEvent</strong></a></p></td>
<td align="left"><p>Sets the specified event object to the signaled state, and returns the event object's previous state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engunmapevent" data-raw-source="[&lt;strong&gt;EngUnmapEvent&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engunmapevent)"><strong>EngUnmapEvent</strong></a></p></td>
<td align="left"><p>Cleans up the kernel-mode resources allocated for a mapped user-mode event.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engwaitforsingleobject" data-raw-source="[&lt;strong&gt;EngWaitForSingleObject&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engwaitforsingleobject)"><strong>EngWaitForSingleObject</strong></a></p></td>
<td align="left"><p>Puts the current thread of the display driver into a wait state until the specified event object is set to the signaled state, or until the wait times out.</p></td>
</tr>
</tbody>
</table>

 

