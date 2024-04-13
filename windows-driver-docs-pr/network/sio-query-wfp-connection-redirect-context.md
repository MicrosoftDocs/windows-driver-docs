---
title: SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT control code
description: The SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT socket I/O control operation allows a Winsock client to retrieve the redirect context for a redirect record for a redirected connection.
ms.date: 08/08/2017
ms.topic: reference
keywords: 
 -SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT control code Network Drivers Starting with Windows Vista
---

# SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT control code


The **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** socket I/O control operation allows a Winsock client to retrieve the redirect context for a redirect record for a redirected connection.

A WFP redirect record is a buffer of opaque data that WFP must set on an outbound proxy connection so that the redirected connection and the original connection are logically related.

**Note**  The [**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](sio-query-wfp-connection-redirect-records.md) query can only be used if the connection was redirected at the **FWPS\_LAYER\_ALE\_CONNECT\_REDIRECT\_V4** or **FWPS\_LAYER\_ALE\_CONNECT\_REDIRECT\_V6** layer by a WFP client.

 

For more information about redirection, see [Using Bind or Connect Redirection](./using-bind-or-connect-redirection.md).

To query the redirect context for a redirect record, a Winsock client calls the [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) function with the following parameters.

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
<td><p><strong>SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT</strong></p></td>
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
<td><p>A pointer to the buffer that receives the redirect context for the redirect record for the accepted TCP connection. The size of the buffer is specified in the <em>OutputSize</em> parameter.</p></td>
</tr>
<tr class="even">
<td><p><em>OutputSizeReturned</em></p></td>
<td><p>A pointer to a <strong>ULONG</strong>-typed variable that receives the number of bytes of data that is copied into the buffer that is pointed to by the <em>OutputBuffer</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p>Irp</p></td>
<td><p>A pointer to an IRP.</p></td>
</tr>
</tbody>
</table>

 

The caller can perform this query in either of the following ways:

-   It can set the *OutputBuffer* to a large buffer approximately 1 KB in size. If the output buffer size is not large enough, [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) will return **STATUS\_BUFFER\_TOO\_SMALL** and *OutputSizeReturned* will contain the required size of the buffer. A larger buffer can then be allocated and **WskControlSocket** called again with the **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** request and *OutputBuffer* set to the larger buffer.
-   Or it can set the *OutputSize* parameter to 0 and the *OutputBuffer* to NULL and then call [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket). Upon completion, the **WskControlSocket** function retrieves the output buffer size, in bytes, in the *OutputSizeReturned* parameter. An appropriately sized buffer can then be allocated and **WskControlSocket** called again with the **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** request and *OutputBuffer* set to the buffer.

**Note**  It is also possible to perform this query in a user-mode application by using [**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT (SDK)**](/windows/win32/winsock/sio-query-wfp-connection-redirect-context).

 

For this type of request, the Winsock client must specify a pointer to an IRP and a pointer to its completion routine. The IRP can be passed to the client by a higher driver or the client can choose to allocate the IRP. To specify the completion routine, the client must call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine). For more details, see [Using IRPs with Winsock Kernel Functions](./using-irps-with-winsock-kernel-functions.md).

The Winsock client must not free the allocated buffer till the IRP is completed by WSK subsystem. When the WSK subsystem completes the IRP, it notifies the client by invoking the completion routine. A reference to that buffer is passed to the client by the WSK subsystem in the *Context* parameter of the completion routine. The size of the buffer is stored in *Irp-&gt;IoStatus.Information*.

The client can get the status of the IRP by checking *Irp-&gt;IoStatus.Status*. *Irp-&gt;IoStatus.Status* will be set to **STATUS\_SUCCESS** if the request is successful. Otherwise, it will contain **STATUS\_INTEGER\_OVERFLOW**, **STATUS\_NOT\_FOUND**, **STATUS\_BUFFER\_TOO\_SMALL**, or **STATUS\_ACCESS\_DENIED** if the call is not successful.

## Requirements

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


[Using Bind or Connect Redirection](./using-bind-or-connect-redirection.md)

[Using IRPs with Winsock Kernel Functions](./using-irps-with-winsock-kernel-functions.md)

[**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](sio-query-wfp-connection-redirect-records.md)

[**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT (SDK)**](/windows/win32/winsock/sio-query-wfp-connection-redirect-context)

 

