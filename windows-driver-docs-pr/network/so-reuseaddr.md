---
title: SO_REUSEADDR
description: SO_REUSEADDR
ms.assetid: 9436492b-0bfb-4234-bcf3-c44657a846d7
ms.date: 08/08/2017
keywords: 
 -SO_REUSEADDR Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SO\_REUSEADDR


The state of the SO\_REUSEADDR socket option determines whether the local transport address to which a socket will be bound is always shared with other sockets. This socket option applies only to listening sockets, datagram sockets, and connection-oriented sockets.

If a WSK application sets this socket option, it must do so before the socket is bound to a local transport address.

To set the state of this socket option, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p>SO_REUSEADDR</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>SOL_SOCKET</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>sizeof(ULONG)</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a ULONG-typed variable that contains the value for the new state of the socket option:</p>
<ul>
<li><p>0: Disable always sharing the local transport address</p></li>
<li><p>1: Enable always sharing the local transport address</p></li>
</ul></td>
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

To retrieve the state of this socket option, a WSK application calls the **WskControlSocket** function with the following parameters.

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
<td><p><strong>WskGetOption</strong></p></td>
</tr>
<tr class="even">
<td><p><em>ControlCode</em></p></td>
<td><p>SO_REUSEADDR</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>SOL_SOCKET</p></td>
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
<td><p>sizeof(ULONG)</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to a ULONG-typed variable that receives the value of the state of the socket option:</p>
<ul>
<li><p>0: Always sharing the local transport address is disabled</p></li>
<li><p>1: Always sharing the local transport address is enabled</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

A WSK application must specify a pointer to an IRP when calling the **WskControlSocket** function to set or retrieve the state of the SO\_REUSEADDR socket option.

The default state of this socket option is that always sharing the local transport address is disabled.

For more information about using the SO\_REUSEADDR socket option and its impact on the sharing of local transport addresses between sockets, see [Sharing Transport Addresses](https://msdn.microsoft.com/library/windows/hardware/ff570806).

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
<td>Ws2def.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

 

 




