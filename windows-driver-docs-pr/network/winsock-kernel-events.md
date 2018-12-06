---
title: Winsock Kernel Events
description: Winsock Kernel Events
ms.assetid: 84f7b547-cfbf-468b-b80e-1441c8aa3cf3
keywords:
- Winsock Kernel WDK networking , events
- WSK WDK networking , events
- events WDK Winsock Kernel
- basic sockets WDK Winsock Kernel
- listening sockets WDK Winsock Kernel
- datagram sockets WDK Winsock Kernel
- connection-oriented sockets WDK Winsock Kernel
- event notifications WDK Winsock Kernel
- notifications WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Winsock Kernel Events


The Winsock Kernel (WSK) subsystem can asynchronously notify a WSK application when certain socket events occur, such as when new data has been received on a socket or when a socket has been disconnected. In order for a WSK application to be asynchronously notified of socket events, the WSK application must implement the appropriate event callback functions and enable those event callback functions on the sockets that it creates.

**Note**  A WSK application is not required to implement or use event callback functions. A WSK application can perform most WSK socket operations by calling the appropriate WSK socket functions. The only WSK feature that requires using event callback functions is conditional-accept mode on listening sockets. For more information about the advantages and disadvantages between using WSK functions versus using event callback functions, see [Using Winsock Kernel Functions vs. Event Callback Functions](using-winsock-kernel-functions-vs--event-callback-functions.md).

 

Each WSK [socket category](winsock-kernel-socket-categories.md) supports a different set of socket events.

**Basic sockets**

Basic sockets do not support any socket events.

**Listening sockets**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event</th>
<th align="left">Event callback function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>An incoming connection has been accepted.</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571120" data-raw-source="[&lt;em&gt;WskAcceptEvent&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571120)"><em>WskAcceptEvent</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>An incoming connection request has arrived.<em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571137" data-raw-source="[&lt;em&gt;WskInspectEvent&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571137)"><em>WskInspectEvent</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>An incoming connection request has been dropped.</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571108" data-raw-source="[&lt;em&gt;WskAbortEvent&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571108)"><em>WskAbortEvent</em></a></p></td>
</tr>
</tbody>
</table>

 

\* Applies only to listening sockets that have conditional-accept mode enabled. For more information about using conditional accept mode with listening sockets, see [Listening for and Accepting Incoming Connections](listening-for-and-accepting-incoming-connections.md).

**Datagram sockets**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event</th>
<th align="left">Event callback function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>One or more new datagrams have been received.</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571142" data-raw-source="[&lt;em&gt;WskReceiveFromEvent&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571142)"><em>WskReceiveFromEvent</em></a></p></td>
</tr>
</tbody>
</table>

 

**Connection-oriented sockets**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event</th>
<th align="left">Event callback function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>New data has been received.</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571140" data-raw-source="[&lt;em&gt;WskReceiveEvent&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571140)"><em>WskReceiveEvent</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>The socket has been disconnected.</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571130" data-raw-source="[&lt;em&gt;WskDisconnectEvent&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571130)"><em>WskDisconnectEvent</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>The ideal send backlog size has changed.</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff571147" data-raw-source="[&lt;em&gt;WskSendBacklogEvent&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571147)"><em>WskSendBacklogEvent</em></a></p></td>
</tr>
</tbody>
</table>

 

When a WSK application creates a socket, the socket's event callback functions are disabled by default. A WSK application must enable a socket's event callback functions in order for the WSK subsystem to call the socket's event callback functions when socket events occur. For more information about enabling and disabling a socket's event callback functions, see [Enabling and Disabling Event Callback Functions](enabling-and-disabling-event-callback-functions.md).

If a WSK application registers an [extension interface](winsock-kernel-extension-interfaces.md) for a socket, the extension interface might support additional events. For more information about registering an extension interface for a socket, see [Registering an Extension Interface](registering-an-extension-interface.md).

The WSK subsystem can also notify a WSK application of events that are not specific to a particular socket. In order for a WSK application to be notified of these events, the WSK application must implement a [*WskClientEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571123) event callback function. There are currently no events defined that are not specific to a particular socket. A WSK application's *WskClientEvent* event callback function is always enabled and cannot be disabled.

A WSK application's event callback functions must not wait for completion of other WSK requests in the context of WSK completion or event callback functions. The callback can initiate other WSK requests (assuming that it doesn't spend too much time at DISPATCH\_LEVEL), but it must not wait for their completion even when the callback is called at IRQL = PASSIVE\_LEVEL.

 

 





