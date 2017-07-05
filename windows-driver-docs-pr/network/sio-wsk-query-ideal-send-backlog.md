---
title: SIO\_WSK\_QUERY\_IDEAL\_SEND\_BACKLOG
description: SIO\_WSK\_QUERY\_IDEAL\_SEND\_BACKLOG
MS-HAID:
- 'wskref\_da6de22e-a65d-460f-942d-bad9118df669.xml'
- 'netvista.sio\_wsk\_query\_ideal\_send\_backlog'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8d05b1dc-9dbf-4726-9eaf-721d1fb8282e
keywords: ["SIO_WSK_QUERY_IDEAL_SEND_BACKLOG Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- SIO_WSK_QUERY_IDEAL_SEND_BACKLOG
api_location:
- Wsk.h
api_type:
- HeaderDef
---

# SIO\_WSK\_QUERY\_IDEAL\_SEND\_BACKLOG


The SIO\_WSK\_QUERY\_IDEAL\_SEND\_BACKLOG socket I/O control operation allows a WSK application to query the ideal send backlog size for a connection-oriented socket. This socket I/O control operation applies only to connection-oriented sockets.

The ideal send backlog size for a connection-oriented socket is the optimal amount of send data that needs to be kept outstanding (that is, passed to the WSK subsystem but not yet completed) to keep the socket's data stream full at all times. A WSK application can use this size to incrementally probe and lock the buffers of data to be sent based on the underlying connection's flow control state.

If a WSK application uses this socket I/O control operation to query the ideal send backlog size, it must do so after the connection-oriented socket has been connected to a remote transport address.

To query the ideal send backlog size for a connection-oriented socket, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p>SIO_WSK_QUERY_IDEAL_SEND_BACKLOG</p></td>
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
<td><p>A pointer to a SIZE_T-typed variable that receives the current ideal send backlog size</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

 

```

```

A WSK application must specify a pointer to an IRP when calling the **WskControlSocket** function to query the ideal send backlog size for a connection-oriented socket.

A connection-oriented socket can be notified of changes to the ideal send backlog size by enabling its [*WskSendBacklogEvent*](https://msdn.microsoft.com/library/windows/hardware/ff571147) event callback function.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20SIO_WSK_QUERY_IDEAL_SEND_BACKLOG%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




