---
title: SIO\_WSK\_QUERY\_INSPECT\_ID
author: windows-driver-content
description: SIO\_WSK\_QUERY\_INSPECT\_ID
ms.assetid: 6fc3e5ea-61df-47fc-8f79-f9ae272b3544
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - SIO_WSK_QUERY_INSPECT_ID Network Drivers Starting with Windows Vista
---

# SIO\_WSK\_QUERY\_INSPECT\_ID


The SIO\_WSK\_QUERY\_INSPECT\_ID socket I/O control operation allows a WSK application to query the inspection identification data for a connection-oriented socket that has been successfully accepted on a listening socket that has conditional accept mode enabled. This socket I/O control operation applies only to connection-oriented sockets that have been accepted on a listening socket that has conditional accept mode enabled.

To query the inspection identification data for a connection-oriented socket, a WSK application calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p>SIO_WSK_QUERY_INSPECT_ID</p></td>
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
<td><p>sizeof(WSK_INSPECT_ID)</p></td>
</tr>
<tr class="odd">
<td><p><em>OutputBuffer</em></p></td>
<td><p>A pointer to a WSK_INSPECT_ID structure that receives the inspection identification data</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>A pointer to a ULONG-typed variable that receives the number of bytes of data that is copied into the buffer that is pointed to by the <em>OutputBuffer</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><em>Irp</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

 

```

```

If a WSK application calls the **WskControlSocket** function to query the inspection identification data for any socket other than a connection-oriented socket that was accepted on a listening socket that has conditional accept mode enabled, the **WskControlSocket** function returns STATUS\_INVALID\_DEVICE\_REQUEST.

For more information about conditionally accepting connections, see [Listening for and Accepting Incoming Connections](https://msdn.microsoft.com/library/windows/hardware/ff557059).

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20SIO_WSK_QUERY_INSPECT_ID%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


