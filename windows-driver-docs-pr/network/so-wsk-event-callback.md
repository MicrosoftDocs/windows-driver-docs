---
title: SO\_WSK\_EVENT\_CALLBACK
author: windows-driver-content
description: SO\_WSK\_EVENT\_CALLBACK
ms.assetid: cb697103-20ef-4667-8823-060a68d904c8
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - SO_WSK_EVENT_CALLBACK Network Drivers Starting with Windows Vista
---

# SO\_WSK\_EVENT\_CALLBACK


The SO\_WSK\_EVENT\_CALLBACK socket option allows a WSK application to enable and disable a socket's event callback functions. This socket option applies only to listening sockets, datagram sockets, connection-oriented sockets, and basic sockets that have registered an extension interface for which at least one event callback function is defined.

If a WSK application uses this socket option to enable or disable event callback functions on either a listening socket or a datagram socket, it must do so after the socket has been bound to a local transport address.

If a WSK application uses this socket option to enable or disable event callback functions on a connection-oriented socket, it must do so after the socket has been connected to a remote transport address.

To enable or disable event callback functions on a socket, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>RequestType</em></p></td>
<td><p><strong>WskSetOption</strong></p></td>
</tr>
<tr class="even">
<td><p><em>ControlCode</em></p></td>
<td><p>SO_WSK_EVENT_CALLBACK</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>SOL_SOCKET</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>sizeof(WSK_EVENT_CALLBACK_CONTROL)</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a [<strong>WSK_EVENT_CALLBACK_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff571166) structure</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSize</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

 

```

```

A WSK application does not specify a pointer to an IRP when calling the **WskControlSocket** function to enable event callback functions on a socket.

A WSK application can optionally specify a pointer to an IRP when calling the **WskControlSocket** function to disable an event callback function on a socket.

When a WSK application calls **WskControlSocket** to disable an event callback function, the WSK subsystem behaves as follows:

-   If there are no in-progress calls to the event callback function that is being disabled when the WSK application calls the **WskControlSocket** function, the event callback function is disabled and the **WskControlSocket** function returns STATUS\_SUCCESS. If the WSK application specifies an IRP, the IRP is completed with success status.

-   If there are in-progress calls to the event callback function that is being disabled when the WSK application calls the **WskControlSocket** function and the WSK application specified an IRP, the **WskControlSocket** function returns STATUS\_PENDING. The WSK subsystem disables the event callback function and completes the IRP after all in-progress calls to the event callback function have returned.

-   If there are in-progress calls to the event callback function that is being disabled when the WSK application calls the **WskControlSocket** function and the WSK application did not specify an IRP, the **WskControlSocket** function returns STATUS\_EVENT\_PENDING. The WSK subsystem disables the event callback function after all in-progress calls to the event callback function have returned.

When enabling or disabling any of the standard WSK event callback functions, a WSK application sets the **NpiId** member of the [**WSK\_EVENT\_CALLBACK\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff571166) structure to a pointer to the WSK [Network Programming Interface (NPI)](https://msdn.microsoft.com/library/windows/hardware/ff568373) identifier, NPI\_WSK\_INTERFACE\_ID.

When enabling or disabling any callback functions for an extension interface, a WSK application sets the **NpiId** member of the WSK\_EVENT\_CALLBACK\_CONTROL structure to a pointer to the NPI identifier for that extension interface.

When enabling event callback functions, a WSK application can simultaneously enable any combination of the event callback functions that are valid for a particular [category](https://msdn.microsoft.com/library/windows/hardware/ff571093) of WSK socket. The WSK application simultaneously enables these combinations by setting the **EventMask** member of the WSK\_EVENT\_CALLBACK\_CONTROL structure to a bitwise OR of the event flags for all of the event callback functions that are being enabled.

When disabling event callback functions, a WSK application must disable each event callback function independently. A WSK application independently disables an event callback function by setting the **EventMask** member of the WSK\_EVENT\_CALLBACK\_CONTROL structure to a bitwise OR of the event flag for the event callback function that is being disabled and the WSK\_EVENT\_DISABLE flag.

The following table shows the valid event flags for a listening socket.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event flag</th>
<th>Event callback function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WSK_EVENT_ACCEPT</p></td>
<td><p>[<em>WskAcceptEvent</em>](https://msdn.microsoft.com/library/windows/hardware/ff571120)</p></td>
</tr>
</tbody>
</table>

 

```

```

The following table shows the valid event flags for a datagram socket.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event flag</th>
<th>Event callback function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WSK_EVENT_RECEIVE_FROM</p></td>
<td><p>[<em>WskReceiveFromEvent</em>](https://msdn.microsoft.com/library/windows/hardware/ff571142)</p></td>
</tr>
</tbody>
</table>

 

```

```

The following table shows the valid event flags for a connection-oriented socket.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event flag</th>
<th>Event callback function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WSK_EVENT_DISCONNECT</p></td>
<td><p>[<em>WskDisconnectEvent</em>](https://msdn.microsoft.com/library/windows/hardware/ff571130)</p></td>
</tr>
<tr class="even">
<td><p>WSK_EVENT_RECEIVE</p></td>
<td><p>[<em>WskReceiveEvent</em>](https://msdn.microsoft.com/library/windows/hardware/ff571140)</p></td>
</tr>
<tr class="odd">
<td><p>WSK_EVENT_SEND_BACKLOG</p></td>
<td><p>[<em>WskSendBacklogEvent</em>](https://msdn.microsoft.com/library/windows/hardware/ff571147)</p></td>
</tr>
</tbody>
</table>

 

```

```

A listening socket can automatically enable event callback functions on connection-oriented sockets that are accepted by the listening socket. A WSK application automatically enables these callback functions by enabling the connection-oriented socket event callback functions on the listening socket. The event callback functions are automatically enabled on an accepted connection-oriented socket only if the socket is accepted by the listening socket's [*WskAcceptEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571120) event callback function. If the connection-oriented socket is accepted by the listening socket's [**WskAccept**](https://msdn.microsoft.com/library/windows/hardware/ff571109) function, the accepted socket's event callback functions are not automatically enabled.

After any connection-oriented event callback functions are enabled on a listening socket, they cannot be disabled on the listening socket. If the *WskAcceptEvent* event callback function is disabled and then re-enabled on a listening socket, any connection-oriented event callback functions that were originally enabled on that listening socket will continue to be applied to all connection-oriented sockets that are accepted by the *WskAcceptEvent* event callback function.

For more information about enabling and disabling a socket's event callback functions, see [Enabling and Disabling Event Callback Functions](https://msdn.microsoft.com/library/windows/hardware/ff548851).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wsk.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20SO_WSK_EVENT_CALLBACK%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


