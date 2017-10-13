---
title: SIO_WSK_SET_TCP_SILENT_MODE control code
author: windows-driver-content
description: The SIO_WSK_SET_TCP_SILENT_MODE socket I/O control operation allows a WSK client to enable silent mode on the TCP connection.
ms.assetid: 8ADC7FF4-86AC-4424-B763-8B62BF440D9F
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - SIO_WSK_SET_TCP_SILENT_MODE control code Network Drivers Starting with Windows Vista
---

# SIO\_WSK\_SET\_TCP\_SILENT\_MODE control code


The **SIO\_WSK\_SET\_TCP\_SILENT\_MODE** socket I/O control operation allows a WSK client to enable silent mode on the TCP connection.

A TCP connection in silent mode will not send any data or control packets on the wire. This socket I/O control operation applies only to connected TCP sockets. It is not supported on loopback.

To perform this operation, call the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function with the following parameters.

Parameters
----------

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

Remarks
-------

A WSK application must specify a pointer to an IRP when calling the [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) function to enable silent mode.

The WSK application before calling [**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) to enable silent mode must ensure that there are no pending send or disconnect requests.

[**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127) will return **STATUS\_SUCCESS** when silent mode is enabled. Once silent mode is enabled, send and disconnect requests will be failed with **STATUS\_INVALID\_DEVICE\_STATE** and all received control or data packets will be discarded silently.

The only valid operation on this socket is [**WskCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571124).

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
<td><p>Available in Windows 8, Windows Server 2012, and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wsk.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

## See also


[**WskCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571124)

[**WskControlSocket**](https://msdn.microsoft.com/library/windows/hardware/ff571127)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20SIO_WSK_SET_TCP_SILENT_MODE%20control%20code%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


