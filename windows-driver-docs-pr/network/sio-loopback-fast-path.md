---
title: SIO\_LOOPBACK\_FAST\_PATH control code
author: windows-driver-content
description: The SIO\_LOOPBACK\_FAST\_PATH socket I/O control code allows a WSK application to configure a TCP socket for faster operations on the loopback interface.
ms.assetid: 5A5AD945-9EFD-4157-AFA4-F9C3995B7C43
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -SIO_LOOPBACK_FAST_PATH control code Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20SIO_LOOPBACK_FAST_PATH%20control%20code%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


