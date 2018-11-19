---
title: SIO_WSK_SET_SENDTO_ADDRESS
description: SIO_WSK_SET_SENDTO_ADDRESS
ms.assetid: 2dd149d2-adc6-4e03-92de-ed76aa048886
ms.date: 07/18/2017
keywords:
 - SIO_WSK_SET_SENDTO_ADDRESS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SIO\_WSK\_SET\_SENDTO\_ADDRESS


The SIO\_WSK\_SET\_SENDTO\_ADDRESS socket I/O control operation allows a WSK application to specify a fixed destination transport address for a datagram socket. This socket I/O control operation applies only to datagram sockets.

If a WSK application sets a fixed destination transport address for a datagram socket, all datagrams that are sent over the socket are sent to the fixed destination transport address. However, datagrams that are received on the socket will be accepted from any transport address.

A WSK application can override a fixed destination transport address when it sends a datagram over the socket by specifying an alternative remote transport address in the *RemoteAddress* parameter when calling the [**WskSendTo**](https://msdn.microsoft.com/library/windows/hardware/ff571148) function. In this situation, the datagram is sent to the alternative remote transport address instead of the fixed destination transport address.

If a WSK application uses this socket I/O control operation to specify a fixed destination transport address, it must do so after the datagram socket has been bound to a local transport address.

To set a fixed destination transport address for a datagram socket, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p>SIO_WSK_SET_SENDTO_ADDRESS</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>The size of the SOCKADDR structure that is pointed to by the <em>InputBuffer</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a structure that specifies a fixed destination transport address for the datagram socket. The pointer must be a pointer to the specific SOCKADDR structure type that corresponds to the address family that the WSK application specified when it created the datagram socket.</p></td>
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


To clear a fixed destination transport address for a datagram socket, a WSK application calls the **WskControlSocket** function with the following parameters.

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
<td><p>SIO_WSK_SET_SENDTO_ADDRESS</p></td>
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



A WSK application must specify a pointer to an IRP when calling the **WskControlSocket** function to set or clear a fixed destination transport address for a datagram socket.

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

 

 




