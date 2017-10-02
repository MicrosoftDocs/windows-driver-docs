---
title: SIO_ADDRESS_LIST_QUERY
author: windows-driver-content
description: SIO\_ADDRESS\_LIST\_QUERY
ms.assetid: c50520a3-6ba3-448e-bbb4-bf3425dcbc41
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -SIO_ADDRESS_LIST_QUERY Network Drivers Starting with Windows Vista
---

# SIO\_ADDRESS\_LIST\_QUERY


The SIO\_ADDRESS\_LIST\_QUERY socket I/O control operation allows a WSK application to query the current list of local transport addresses for a socket's address family. This socket I/O control operation applies to all socket types.

To query the current list of local transport addresses for a socket's address family, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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

If the call to the **WskControlSocket** function succeeds, the output buffer contains a [**SOCKET\_ADDRESS\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff570826) structure followed by the SOCKADDR structures for each of the local transport addresses for the socket's address family.

If the **WskControlSocket** function returns STATUS\_BUFFER\_OVERFLOW, the variable that is pointed to by the *OutputSizeReturned* parameter contains the output buffer size, in bytes, that is required to contain the complete list of local transport addresses for the socket's address family.

The [**SIO\_ADDRESS\_LIST\_CHANGE**](sio-address-list-change.md) socket I/O control operation allows a WSK application to be notified when there has been a change to the list of local transport addresses for a socket's address family.

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20SIO_ADDRESS_LIST_QUERY%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


