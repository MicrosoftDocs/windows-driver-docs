---
title: SIO_WSK_QUERY_RECEIVE_BACKLOG
description: SIO_WSK_QUERY_RECEIVE_BACKLOG
ms.assetid: 5924c6ae-fa9d-4a8c-acbe-65ca0664ad74
ms.date: 07/18/2017
keywords:
 - SIO_WSK_QUERY_RECEIVE_BACKLOG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SIO\_WSK\_QUERY\_RECEIVE\_BACKLOG


The SIO\_WSK\_QUERY\_RECEIVE\_BACKLOG socket I/O control operation allows a WSK application to query the current backlog of received data for a connection-oriented socket. This socket I/O control operation applies only to connection-oriented sockets.

If a WSK application uses this socket I/O control operation to query the receive backlog, it must do so after the connection-oriented socket has been connected to a remote transport address.

To query the current backlog of received data for a connection-oriented socket, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p>SIO_WSK_QUERY_RECEIVE_BACKLOG</p></td>
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
<td><p>sizeof(SIZE_T)</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to a SIZE_T-typed variable that receives the current backlog of received data</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

A WSK application must specify a pointer to an IRP when calling the **WskControlSocket** function to query the current backlog of received data for a connection-oriented socket.

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

 

 




