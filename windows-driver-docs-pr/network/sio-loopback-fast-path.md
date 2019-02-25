---
title: SIO_LOOPBACK_FAST_PATH control code
description: The SIO_LOOPBACK_FAST_PATH socket I/O control code allows a WSK application to configure a TCP socket for faster operations on the loopback interface.
ms.assetid: 5A5AD945-9EFD-4157-AFA4-F9C3995B7C43
ms.date: 08/08/2017
keywords: 
 -SIO_LOOPBACK_FAST_PATH control code Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SIO\_LOOPBACK\_FAST\_PATH control code


**Important**  The **SIO\_LOOPBACK\_FAST\_PATH** is deprecated and is not recommended to be used in your code.

 

The **SIO\_LOOPBACK\_FAST\_PATH** socket I/O control code allows a WSK application to configure a TCP socket for faster operations on the loopback interface.

To use this IOCTL, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p><strong>SIO_LOOPBACK_FAST_PATH</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>The size, in bytes, of the input buffer.</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to the input buffer. This parameter contains a pointer to a <strong>Boolean</strong> value that indicates if the socket should be configured for fast loopback operations.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSize</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
<tr class="odd">
<td><p>Irp</p></td>
<td><p>A pointer to an IRP.</p></td>
</tr>
</tbody>
</table>

 

An application can use the **SIO\_LOOPBACK\_FAST\_PATH** IOCTL to improve the performance of loopback operations on a TCP socket. This IOCTL requests that the TCP/IP stack use a special fast path for loopback operations on this socket. The **SIO\_LOOPBACK\_FAST\_PATH** IOCTL can be used only with TCP sockets. This IOCTL must be used on both sides of the loopback session. The TCP loopback fast path is supported using either the IPv4 or IPv6 loopback interface.

The socket that plans to initiate the connection request must apply this IOCTL before making the connection request. The socket that is listening for the connection request must apply this IOCTL before accepting the connection.

Once an application establishes the connection on a loopback interface using the fast path, all packets for the lifetime of the connection must use the fast path.

Applying **SIO\_LOOPBACK\_FAST\_PATH** to a socket which will be connected to a non-loopback path will have no effect.

This TCP loopback optimization results in packets that flow through Transport Layer (TL) instead of the traditional loopback through Network Layer. This optimization improves the latency for loopback packets. Once an applications opts in for a connection level setting to use the loopback fast path, all packets will follow the loopback path. For loopback communications, congestion and packet drop are not expected. The notion of congestion control and reliable delivery in TCP will be unnecessary. This, however, is not true for flow control. Without flow control, the sender can overwhelm the receive buffer, leading to erroneous TCP loopback behavior. The flow control in the TCP optimized loopback path is maintained by placing send requests in a queue. When the receive buffer is full, the TCP/IP stack guarantees that the sends won't complete until the queue is serviced, maintaining flow control.

TCP fast path loopback connections in the presence of a Windows Filtering Platform (WFP) callout for connection data must take the unoptimized slow path for loopback. So WFP filters will prevent this new loopback fast path from being used. When a WFP filter is enabled, the system will use the slow path even if the **SIO\_LOOPBACK\_FAST\_PATH** IOCTL was set. This ensues that user-mode applications have the full WFP security capability.

By default, **SIO\_LOOPBACK\_FAST\_PATH** is disabled.

Only a subset of the TCP/IP socket options are supported when the **SIO\_LOOPBACK\_FAST\_PATH** IOCTL is used to enable the loopback fast path on a socket. The list of supported options includes the following:

-   IP\_TTL
-   IP\_UNICAST\_IF
-   IPV6\_UNICAST\_HOPS
-   IPV6\_UNICAST\_IF
-   IPV6\_V6ONLY
-   [**SO\_CONDITIONAL\_ACCEPT**](https://msdn.microsoft.com/library/windows/desktop/dd264794)
-   [SO\_EXCLUSIVEADDRUSE](https://msdn.microsoft.com/library/windows/desktop/cc150667)
-   [**SO\_PORT\_SCALABILITY**](https://msdn.microsoft.com/library/windows/desktop/cc150670)
-   SO\_RCVBUF
-   SO\_REUSEADDR
-   TCP\_BSDURGENT

A WSK application must specify a pointer to an IRP and a completion routine when calling the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function for this type of request. The application must not release the buffer till the WSK subsystem has completed the IRP. When it completes the IRP, the subsystem invokes the completion routine. In the completion routine, the application must check the IRP status and release all resources that it had previously allocated for the request.

For more information about WSK IRP handling, see [Using IRPs with Winsock Kernel Functions](https://msdn.microsoft.com/library/windows/hardware/ff571006).

When completing the IRP, the subsystem will set *Irp-&gt;IoStatus.Status* to **STATUS\_SUCCESS** if the request is successful. Otherwise, *Irp-&gt;IoStatus.Status* will be set to **STATUS\_INVALID\_BUFFER\_SIZE** or **STATUS\_NOT\_SUPPORTED** if the call is not successful.

## Return value


Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 8</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Mstcpip.h</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**SIO\_LOOPBACK\_FAST\_PATH (SDK)**](https://msdn.microsoft.com/library/windows/desktop/jj841212)

[Using IRPs with Winsock Kernel Functions](https://msdn.microsoft.com/library/windows/hardware/ff571006)

 

 




