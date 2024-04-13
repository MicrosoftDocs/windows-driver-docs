---
title: SO_WSK_SECURITY
description: SO_WSK_SECURITY
ms.date: 07/18/2017
ms.topic: reference
keywords:
 - SO_WSK_SECURITY Network Drivers Starting with Windows Vista
---

# SO\_WSK\_SECURITY


The SO\_WSK\_SECURITY socket option allows a WSK application to either apply a security descriptor to a socket or retrieve a cached copy of a socket's security descriptor from a socket. The security descriptor controls the sharing of the local transport address to which the socket is bound.

This socket option applies only to listening sockets, datagram sockets, and connection-oriented sockets.

If a WSK application uses this socket option to apply a security descriptor to a socket, it must do so before the socket is bound to a local transport address.

To apply a security descriptor to a socket, a WSK application calls the [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) function with the following parameters.

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
<td><p>SO_WSK_SECURITY</p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>SOL_SOCKET</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>sizeof(PSECURITY_DESCRIPTOR)</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a PSECURITY_DESCRIPTOR-typed variable. This variable must contain a pointer to a cached copy of a security descriptor that was obtained by calling the <a href="/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client" data-raw-source="[&lt;strong&gt;WskControlClient&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client)"><strong>WskControlClient</strong></a> function with the <a href="wsk-cache-sd.md" data-raw-source="[&lt;strong&gt;WSK_CACHE_SD&lt;/strong&gt;](wsk-cache-sd.md)"><strong>WSK_CACHE_SD</strong></a> control code.</p></td>
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

A WSK application must specify a pointer to an IRP when calling the **WskControlSocket** function to apply a security descriptor to a socket.

If a WSK application uses this socket option to apply a security descriptor to a socket, the new security descriptor replaces any security descriptor that was previously applied to the socket.

A WSK application must not release the cached copy of the security descriptor until after the IRP is completed.

A WSK application can also apply a security descriptor to a socket when the socket is initially created by specifying a pointer to a cached copy of a security descriptor in the *SecurityDescriptor* parameter when it calls the [**WskSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket) or [**WskSocketConnect**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_socket_connect) function.

If a WSK application does not apply a security descriptor to a socket, the WSK subsystem uses a default security descriptor that does not allow sharing of the local transport address.

To retrieve a cached copy of a socket's security descriptor from a socket, a WSK application calls the [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) function with the following parameters.

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
<td><p>SO_WSK_SECURITY</p></td>
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
<td><p>sizeof(PSECURITY_DESCRIPTOR)</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to a PSECURITY_DESCRIPTOR-typed variable. This variable receives a pointer to a cached copy of the socket's security descriptor.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

A WSK application must specify a pointer to an IRP when calling the **WskControlSocket** function to retrieve a cached copy of a socket's security descriptor from a socket.

A WSK application must call the [**WskControlClient**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client) function with the [**WSK\_RELEASE\_SD**](wsk-release-sd.md) control code to release the cached copy of the security descriptor when it is no longer needed.

See the reference page for the [SECURITY_DESCRIPTOR](/windows/win32/api/winnt/ns-winnt-security_descriptor) structure for more information.

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
<td>Wsk.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

