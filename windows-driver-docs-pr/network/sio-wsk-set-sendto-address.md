---
title: SIO\_WSK\_SET\_SENDTO\_ADDRESS
description: SIO\_WSK\_SET\_SENDTO\_ADDRESS
MS-HAID:
- 'wskref\_a94e0bb6-6292-4248-9dd1-ea486fae1b8a.xml'
- 'netvista.sio\_wsk\_set\_sendto\_address'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2dd149d2-adc6-4e03-92de-ed76aa048886
keywords: ["SIO_WSK_SET_SENDTO_ADDRESS Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- SIO_WSK_SET_SENDTO_ADDRESS
api_location:
- Wsk.h
api_type:
- HeaderDef
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

 

```

```

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

 

```

```

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20SIO_WSK_SET_SENDTO_ADDRESS%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




