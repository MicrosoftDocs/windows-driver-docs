---
title: SIO_WSK_SET_TCP_SILENT_MODE control code
description: The SIO_WSK_SET_TCP_SILENT_MODE socket I/O control operation allows a WSK client to enable silent mode on the TCP connection.
ms.date: 07/18/2017
ms.topic: reference
keywords:
 - SIO_WSK_SET_TCP_SILENT_MODE control code Network Drivers Starting with Windows Vista
---

# SIO\_WSK\_SET\_TCP\_SILENT\_MODE control code


The **SIO\_WSK\_SET\_TCP\_SILENT\_MODE** socket I/O control operation allows a WSK client to enable silent mode on the TCP connection.

A TCP connection in silent mode will not send any data or control packets on the wire. This socket I/O control operation applies only to connected TCP sockets. It is not supported on loopback.

To perform this operation, call the [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) function with the following parameters.

## Parameters

*RequestType* \[in\]  
Use **WskIoctl** for this operation.

*ControlCode* \[in\]  
The control code for the operation. Use **SIO\_WSK\_SET\_TCP\_SILENT\_MODE** for this operation.

*Level*   
Use zero for this operation.

*InputSize* \[in\]  
Use zero for this operation.

*InputBuffer* \[in\]  
Use **NULL** for this operation.

*OutputSize* \[out\]  
Use zero for this operation.

*OutputBuffer* \[in\]  
Use **NULL** for this operation.

*OutputSizeReturned* \[out\]  
Use **NULL** for this operation.

## Remarks

A WSK application must specify a pointer to an IRP when calling the [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) function to enable silent mode.

The WSK application before calling [**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) to enable silent mode must ensure that there are no pending send or disconnect requests.

[**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket) will return **STATUS\_SUCCESS** when silent mode is enabled. Once silent mode is enabled, send and disconnect requests will be failed with **STATUS\_INVALID\_DEVICE\_STATE** and all received control or data packets will be discarded silently.

The only valid operation on this socket is [**WskCloseSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_close_socket).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 8, Windows Server 2012, and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wsk.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

## See also


[**WskCloseSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_close_socket)

[**WskControlSocket**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_socket)

 

