---
title: WSK_TDI_BEHAVIOR
description: WSK_TDI_BEHAVIOR
ms.assetid: 84e4c8c3-2c31-4db5-bb25-309c6bb176ff
ms.date: 07/18/2017
keywords:
 - WSK_TDI_BEHAVIOR Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WSK\_TDI\_BEHAVIOR


**Note**   The TDI feature is deprecated and will be removed in future versions of Microsoft Windows.

 

A WSK application uses the WSK\_TDI\_BEHAVIOR client control operation to control whether the WSK subsystem will divert network I/O to [TDI](https://msdn.microsoft.com/library/windows/hardware/ff565094) transports. A WSK application uses this client control operation only if it needs to override the default behavior of the WSK subsystem.

If a WSK application uses the WSK\_TDI\_BEHAVIOR client control operation, it must do so before it creates any sockets.

To control whether the WSK subsystem will divert network I/O to TDI transports, a WSK application calls the [**WskControlClient**](https://msdn.microsoft.com/library/windows/hardware/ff571126) function with the following parameters.

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
<td><p><em>ControlCode</em></p></td>
<td><p>WSK_TDI_BEHAVIOR</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>sizeof(ULONG)</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a ULONG typed variable that contains flags that control the behavior of the WSK subsystem.</p></td>
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
<td><p><em>Irp</em></p></td>
<td><p><strong>NULL</strong></p></td>
</tr>
</tbody>
</table>

The following flags are defined for the WSK\_TDI\_BEHAVIOR client control operation.

<a href="" id="wsk-tdi-behavior-bypass-tdi"></a>WSK\_TDI\_BEHAVIOR\_BYPASS\_TDI  
If a native WSK transport exists for the address family, socket type, and protocol that are specified when the WSK application creates a socket, then, if this flag is set, the WSK subsystem ignores any TDI filter drivers and always uses the native WSK transport.

The default behavior is that if a TDI filter driver is detected for the address family, socket type, and protocol that are specified when the WSK application creates a new socket, the WSK subsystem diverts the network I/O for the new socket to the TDI transport so that the network traffic and other socket operations pass through the TDI filter driver.

The *Irp* parameter must be **NULL** for this client control operation.

**Note**  TDI is not supported in Microsoft Windows versions after Windows Vista.

 

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

 

 




