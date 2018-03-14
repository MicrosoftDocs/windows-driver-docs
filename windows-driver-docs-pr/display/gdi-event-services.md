---
title: GDI Event Services
description: GDI Event Services
ms.assetid: 966fa3ce-c72c-4b91-9cf7-b789d39e69b5
keywords:
- GDI WDK Windows 2000 display , events
- graphics drivers WDK Windows 2000 display , events
- drawing WDK GDI , events
- events WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>EngClearEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564190)</p></td>
<td align="left"><p>Sets a specified event object to the nonsignaled state.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngCreateEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564211)</p></td>
<td align="left"><p>Creates a synchronization event object that can be used to synchronize hardware access between a display driver and the video miniport driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngDeleteEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564801)</p></td>
<td align="left"><p>Deletes the specified event object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngMapEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564970)</p></td>
<td align="left"><p>Maps a user-mode event object to kernel mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngReadStateEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565001)</p></td>
<td align="left"><p>Returns the current state of the specified event object: signaled or nonsignaled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565013)</p></td>
<td align="left"><p>Sets the specified event object to the signaled state, and returns the event object's previous state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngUnmapEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565434)</p></td>
<td align="left"><p>Cleans up the kernel-mode resources allocated for a mapped user-mode event.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngWaitForSingleObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565461)</p></td>
<td align="left"><p>Puts the current thread of the display driver into a wait state until the specified event object is set to the signaled state, or until the wait times out.</p></td>
</tr>
</tbody>
</table>

 

 

 





