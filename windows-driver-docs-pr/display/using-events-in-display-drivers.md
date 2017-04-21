---
title: Using Events in Display Drivers
description: Using Events in Display Drivers
ms.assetid: 0c02d64f-0aad-43b4-b105-09ab8901e0de
keywords:
- events WDK Windows 2000 display
- display drivers WDK Windows 2000 , events
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>EngClearEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564190)</p></td>
<td align="left"><p>Sets a given event object to the nonsignaled state.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngCreateEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564211)</p></td>
<td align="left"><p>Creates a synchronization event object.</p></td>
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
<td align="left"><p>Returns the current state of a given event object: signaled or nonsignaled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565013)</p></td>
<td align="left"><p>Sets an event object to the signaled state if it was not already in that state, and returns the event object's previous state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngUnmapEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565434)</p></td>
<td align="left"><p>Cleans up the kernel-mode resources allocated for a mapped user-mode event.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngWaitForSingleObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565461)</p></td>
<td align="left"><p>Puts the current thread into a wait state until the given dispatch object is set to the signaled state, or (optionally) until the wait times out.</p></td>
</tr>
</tbody>
</table>

 

The video port driver also provides support for events to video miniport drivers. See [Events in Video Miniport Drivers (Windows 2000 Model)](events-in-video-miniport-drivers--windows-2000-model-.md) for more information.

For a broader perspective on events, see [Event Objects](https://msdn.microsoft.com/library/windows/hardware/ff544323).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20Events%20in%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




