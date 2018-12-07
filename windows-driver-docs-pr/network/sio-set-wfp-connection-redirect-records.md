---
title: SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS control code
description: The SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS socket I/O control operation allows a Winsock client to specify the redirect record to the new TCP socket used for connecting to the final destination.
ms.assetid: 51FC55BB-FD7A-4FDE-B1FC-02745AC03E33
ms.date: 08/08/2017
keywords: 
 -SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS control code Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS control code


The **SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS** socket I/O control operation allows a Winsock client to specify the redirect record to the new TCP socket used for connecting to the final destination.

A WFP redirect record is a buffer of opaque data that WFP must set on an outbound proxy connection so that the redirected connection and the original connection are logically related.

For more information about redirection, see [Using Bind or Connect Redirection](https://msdn.microsoft.com/library/windows/hardware/ff571005).

To set the redirect record to the new TCP socket used for connecting to the final destination, a Winsock client calls the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

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
<td><p><strong>SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS</strong></p></td>
</tr>
<tr class="odd">
<td><p><em>Level</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>The size of the redirect record pointed to by the InputBuffer parameter.</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to the redirect record associated with the socket.</p></td>
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
<tr class="odd">
<td><p>Irp</p></td>
<td><p>A pointer to an IRP.</p></td>
</tr>
</tbody>
</table>

 

The Winsock client must allocate a buffer and specify a pointer to the buffer and its size in *InputBuffer* and *InputSize.*

A Winsock client must specify a pointer to an IRP and a completion routine when calling the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function for this type of request. The client must not release the buffer till the WSK subsystem has completed the IRP. When it completes the IRP, the subsystem invokes the completion routine. In the completion routine, the client must check the IRP status and release all resources that it had previously allocated for the request.

**Note**  It is also possible to perform this query in a user-mode application by using [**SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS (SDK)**](https://msdn.microsoft.com/library/windows/desktop/hh859714).

 

For more information about WSK IRP handling, see [Using IRPs with Winsock Kernel Functions](https://msdn.microsoft.com/library/windows/hardware/ff571006).

The client can get the status of the IRP by checking *Irp-&gt;IoStatus.Status*. *Irp-&gt;IoStatus.Status* will be set to **STATUS\_SUCCESS** if the request is successful. Otherwise, it will contain **STATUS\_INTEGER\_OVERFLOW**, or **STATUS\_ACCESS\_DENIED** if the call is not successful.

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


[Using Bind or Connect Redirection](https://msdn.microsoft.com/library/windows/hardware/ff571005)

[Using IRPs with Winsock Kernel Functions](https://msdn.microsoft.com/library/windows/hardware/ff571006)

[**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](sio-query-wfp-connection-redirect-records.md)

[**SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS (SDK)**](https://msdn.microsoft.com/library/windows/desktop/hh859714)

 

 




