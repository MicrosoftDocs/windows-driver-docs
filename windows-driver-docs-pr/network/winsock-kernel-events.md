---
title: Winsock Kernel Events
description: Winsock Kernel Events
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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_accept_event" data-raw-source="[&lt;em&gt;WskAcceptEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_accept_event)"><em>WskAcceptEvent</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>An incoming connection request has arrived.<em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_inspect_event" data-raw-source="[&lt;em&gt;WskInspectEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_inspect_event)"><em>WskInspectEvent</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>An incoming connection request has been dropped.</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_abort_event" data-raw-source="[&lt;em&gt;WskAbortEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_abort_event)"><em>WskAbortEvent</em></a></p></td>
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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_from_event" data-raw-source="[&lt;em&gt;WskReceiveFromEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_from_event)"><em>WskReceiveFromEvent</em></a></p></td>
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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_event" data-raw-source="[&lt;em&gt;WskReceiveEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_receive_event)"><em>WskReceiveEvent</em></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>The socket has been disconnected.</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_disconnect_event" data-raw-source="[&lt;em&gt;WskDisconnectEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_disconnect_event)"><em>WskDisconnectEvent</em></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>The ideal send backlog size has changed.</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_send_backlog_event" data-raw-source="[&lt;em&gt;WskSendBacklogEvent&lt;/em&gt;](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_send_backlog_event)"><em>WskSendBacklogEvent</em></a></p></td>
</tr>
</tbody>
</table>

 

When a WSK application creates a socket, the socket's event callback functions are disabled by default. A WSK application must enable a socket's event callback functions in order for the WSK subsystem to call the socket's event callback functions when socket events occur. For more information about enabling and disabling a socket's event callback functions, see [Enabling and Disabling Event Callback Functions](enabling-and-disabling-event-callback-functions.md).

If a WSK application registers an [extension interface](winsock-kernel-extension-interfaces.md) for a socket, the extension interface might support additional events. For more information about registering an extension interface for a socket, see [Registering an Extension Interface](registering-an-extension-interface.md).

The WSK subsystem can also notify a WSK application of events that are not specific to a particular socket. In order for a WSK application to be notified of these events, the WSK application must implement a [*WskClientEvent*](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_client_event) event callback function. There are currently no events defined that are not specific to a particular socket. A WSK application's *WskClientEvent* event callback function is always enabled and cannot be disabled.

A WSK application's event callback functions must not wait for completion of other WSK requests in the context of WSK completion or event callback functions. The callback may initiate other WSK requests assuming that it doesn't spend too much time at DISPATCH\_LEVEL or exhaust the kernel stack, but it must not wait for their completion even when the callback is called at IRQL = PASSIVE\_LEVEL.

