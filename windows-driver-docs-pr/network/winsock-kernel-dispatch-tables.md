---
title: Winsock Kernel Dispatch Tables
description: Winsock Kernel Dispatch Tables
keywords:
- Winsock Kernel WDK networking , dispatch tables
- WSK WDK networking , dispatch tables
- dispatch tables WDK Winsock Kernel
- functions WDK Winsock Kernel
- basic sockets WDK Winsock Kernel
- listening sockets WDK Winsock Kernel
- datagram sockets WDK Winsock Kernel
- connection-oriented sockets WDK Winsock Kernel
- event callback functions WDK Winsock Kernel
ms.date: 04/20/2017
---

# Winsock Kernel Dispatch Tables


The [socket object](winsock-kernel-objects.md) for a Winsock Kernel (WSK) socket contains a pointer to a provider dispatch table structure that contains function pointers to the socket functions supported by the socket. A WSK application calls the functions in the provider dispatch table structure to perform network I/O operations on the socket. Because each WSK [socket category](winsock-kernel-socket-categories.md) supports a different set of socket functions, the WSK [Network Programming Interface (NPI)](network-programming-interface.md) defines a different provider dispatch table structure for each category of WSK socket.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Socket category</th>
<th align="left">Dispatch table structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Basic socket</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_basic_dispatch" data-raw-source="[&lt;strong&gt;WSK_PROVIDER_BASIC_DISPATCH&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_basic_dispatch)"><strong>WSK_PROVIDER_BASIC_DISPATCH</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Listening socket</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_listen_dispatch" data-raw-source="[&lt;strong&gt;WSK_PROVIDER_LISTEN_DISPATCH&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_listen_dispatch)"><strong>WSK_PROVIDER_LISTEN_DISPATCH</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Datagram socket</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_datagram_dispatch" data-raw-source="[&lt;strong&gt;WSK_PROVIDER_DATAGRAM_DISPATCH&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_datagram_dispatch)"><strong>WSK_PROVIDER_DATAGRAM_DISPATCH</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Connection-oriented socket</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_connection_dispatch" data-raw-source="[&lt;strong&gt;WSK_PROVIDER_CONNECTION_DISPATCH&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_provider_connection_dispatch)"><strong>WSK_PROVIDER_CONNECTION_DISPATCH</strong></a></p></td>
</tr>
</tbody>
</table>

 

If a WSK application uses event callback functions for the sockets that it creates, it must provide a client dispatch table structure that contains function pointers to the socket's event callback functions whenever it creates a new socket. Because each WSK socket category supports a different set of event callback functions, the WSK NPI defines a different client dispatch table structure for each category of WSK socket.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Socket category</th>
<th align="left">Dispatch table structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Listening socket</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_client_listen_dispatch" data-raw-source="[&lt;strong&gt;WSK_CLIENT_LISTEN_DISPATCH&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_client_listen_dispatch)"><strong>WSK_CLIENT_LISTEN_DISPATCH</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Datagram socket</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_client_datagram_dispatch" data-raw-source="[&lt;strong&gt;WSK_CLIENT_DATAGRAM_DISPATCH&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_client_datagram_dispatch)"><strong>WSK_CLIENT_DATAGRAM_DISPATCH</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Connection-oriented socket</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_client_connection_dispatch" data-raw-source="[&lt;strong&gt;WSK_CLIENT_CONNECTION_DISPATCH&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_client_connection_dispatch)"><strong>WSK_CLIENT_CONNECTION_DISPATCH</strong></a></p></td>
</tr>
</tbody>
</table>

 

**Note**  Basic sockets do not support any event callback functions. Therefore, no client dispatch table structure is defined for basic sockets.

 

