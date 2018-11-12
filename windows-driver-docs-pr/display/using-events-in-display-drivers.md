---
title: Using Events in Display Drivers
description: Using Events in Display Drivers
ms.assetid: 0c02d64f-0aad-43b4-b105-09ab8901e0de
keywords:
- events WDK Windows 2000 display
- display drivers WDK Windows 2000 , events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Events in Display Drivers


## <span id="ddk_using_events_in_display_drivers_gg"></span><span id="DDK_USING_EVENTS_IN_DISPLAY_DRIVERS_GG"></span>


GDI provides support for events, a type of [kernel dispatcher object](https://msdn.microsoft.com/library/windows/hardware/ff553202) that can be used to synchronize two threads running below DISPATCH\_LEVEL. A display driver can use events to synchronize access to the video hardware:

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564190" data-raw-source="[&lt;strong&gt;EngClearEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564190)"><strong>EngClearEvent</strong></a></p></td>
<td align="left"><p>Sets a given event object to the nonsignaled state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564211" data-raw-source="[&lt;strong&gt;EngCreateEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564211)"><strong>EngCreateEvent</strong></a></p></td>
<td align="left"><p>Creates a synchronization event object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564801" data-raw-source="[&lt;strong&gt;EngDeleteEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564801)"><strong>EngDeleteEvent</strong></a></p></td>
<td align="left"><p>Deletes the specified event object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564970" data-raw-source="[&lt;strong&gt;EngMapEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564970)"><strong>EngMapEvent</strong></a></p></td>
<td align="left"><p>Maps a user-mode event object to kernel mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565001" data-raw-source="[&lt;strong&gt;EngReadStateEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565001)"><strong>EngReadStateEvent</strong></a></p></td>
<td align="left"><p>Returns the current state of a given event object: signaled or nonsignaled.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565013" data-raw-source="[&lt;strong&gt;EngSetEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565013)"><strong>EngSetEvent</strong></a></p></td>
<td align="left"><p>Sets an event object to the signaled state if it was not already in that state, and returns the event object&#39;s previous state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565434" data-raw-source="[&lt;strong&gt;EngUnmapEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565434)"><strong>EngUnmapEvent</strong></a></p></td>
<td align="left"><p>Cleans up the kernel-mode resources allocated for a mapped user-mode event.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565461" data-raw-source="[&lt;strong&gt;EngWaitForSingleObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565461)"><strong>EngWaitForSingleObject</strong></a></p></td>
<td align="left"><p>Puts the current thread into a wait state until the given dispatch object is set to the signaled state, or (optionally) until the wait times out.</p></td>
</tr>
</tbody>
</table>

 

The video port driver also provides support for events to video miniport drivers. See [Events in Video Miniport Drivers (Windows 2000 Model)](events-in-video-miniport-drivers--windows-2000-model-.md) for more information.

For a broader perspective on events, see [Event Objects](https://msdn.microsoft.com/library/windows/hardware/ff544323).

 

 





