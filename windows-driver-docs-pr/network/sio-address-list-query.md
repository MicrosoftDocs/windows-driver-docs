---
title: SIO_ADDRESS_LIST_QUERY
description: SIO_ADDRESS_LIST_QUERY
ms.date: 08/08/2017
ms.topic: reference
keywords: 
 -SIO_ADDRESS_LIST_QUERY Network Drivers Starting with Windows Vista
---

# SIO\_ADDRESS\_LIST\_QUERY


The SIO\_ADDRESS\_LIST\_QUERY socket I/O control operation allows a WSK application to query the current list of local transport addresses for a socket's address family. This socket I/O control operation applies to all socket types.

To query the current list of local transport addresses for a socket's address family, a WSK application calls the [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) function with the following parameters.

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
<td><p>SIO_ADDRESS_LIST_QUERY</p></td>
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
<td><p>The size, in bytes, of the buffer that is pointed to by the <em>OutputBuffer</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to the buffer that receives the current list of local transport addresses. The size of the buffer is specified in the <em>OutputSize</em> parameter.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>A pointer to a ULONG-typed variable that receives the number of bytes of data that is copied into the buffer that is pointed to by the <em>OutputBuffer</em> parameter.</p></td>
</tr>
</tbody>
</table>

 

A WSK application does not specify a pointer to an IRP when calling the **WskControlSocket** function to query the current list of local transport addresses for a socket's address family.

If the call to the **WskControlSocket** function succeeds, the output buffer contains a [**SOCKET\_ADDRESS\_LIST**](/windows/win32/api/ws2def/ns-ws2def-socket_address_list) structure followed by the SOCKADDR structures for each of the local transport addresses for the socket's address family.

If the **WskControlSocket** function returns STATUS\_BUFFER\_OVERFLOW, the variable that is pointed to by the *OutputSizeReturned* parameter contains the output buffer size, in bytes, that is required to contain the complete list of local transport addresses for the socket's address family.

The [**SIO\_ADDRESS\_LIST\_CHANGE**](sio-address-list-change.md) socket I/O control operation allows a WSK application to be notified when there has been a change to the list of local transport addresses for a socket's address family.

## Requirements

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
<td>Ws2def.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

 

