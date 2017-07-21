---
title: WSK_TDI_BEHAVIOR
author: windows-driver-content
description: WSK_TDI_BEHAVIOR
ms.assetid: 84e4c8c3-2c31-4db5-bb25-309c6bb176ff
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WSK_TDI_BEHAVIOR Network Drivers Starting with Windows Vista
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

 

```

```

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WSK_TDI_BEHAVIOR%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


