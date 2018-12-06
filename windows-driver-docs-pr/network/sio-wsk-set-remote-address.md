---
title: SIO_WSK_SET_REMOTE_ADDRESS
description: SIO_WSK_SET_REMOTE_ADDRESS
ms.assetid: 1db11c7a-c9ce-428e-b4da-4a49904a9e4c
ms.date: 07/18/2017
keywords:
 - SIO_WSK_SET_REMOTE_ADDRESS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SIO\_WSK\_SET\_REMOTE\_ADDRESS


The SIO\_WSK\_SET\_REMOTE\_ADDRESS socket I/O control operation allows a WSK application to specify a fixed remote transport address for a datagram socket. This socket I/O control operation applies only to datagram sockets.

If a WSK application sets a fixed remote transport address for a datagram socket, all datagrams that are sent over the socket are sent to the fixed remote transport address, and only datagrams that are received from the fixed remote transport address are accepted.

A WSK application can override a fixed remote transport address when it sends a datagram over the socket by specifying an alternative remote transport address in the *RemoteAddress* parameter when calling the [**WskSendTo**](https://msdn.microsoft.com/library/windows/hardware/ff571148) function. In this situation, the datagram is sent to the alternative remote transport address instead of the fixed remote transport address. However, any responses that are sent back from an alternative remote transport address will not be accepted.

If a WSK application uses this socket I/O control operation to specify a fixed remote transport address, it must do so after the datagram socket has been bound to a local transport address.

To set a fixed remote transport address for a datagram socket, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p><strong>WskIoctl</strong></p></td>
</tr>
<tr class="even">
<td><p><em>ControlCode</em></p></td>
<td><p>SIO_WSK_SET_REMOTE_ADDRESS</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>The size of the SOCKADDR structure pointed to by the <em>InputBuffer</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a structure that specifies a fixed remote transport address for the datagram socket. The pointer must be a pointer to the specific SOCKADDR structure type that corresponds to the address family that the WSK application specified when it created the datagram socket.</p></td>
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


To clear a fixed remote transport address for a datagram socket, a WSK application calls the **WskControlSocket** function with the following parameters.

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
<td><p><strong>WskIoctl</strong></p></td>
</tr>
<tr class="even">
<td><p><em>ControlCode</em></p></td>
<td><p>SIO_WSK_SET_REMOTE_ADDRESS</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>NULL</p></td>
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


A WSK application must specify a pointer to an IRP when calling the **WskControlSocket** function to set or clear a fixed remote transport address for a datagram socket.

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
