---
title: WSK_TDI_DEVICENAME_MAPPING
description: WSK_TDI_DEVICENAME_MAPPING
ms.assetid: 7636fa80-3908-4808-8fb8-6227ec6e023b
ms.date: 07/18/2017
keywords:
 - WSK_TDI_DEVICENAME_MAPPING Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WSK\_TDI\_DEVICENAME\_MAPPING


A WSK application uses the WSK\_TDI\_DEVICENAME\_MAPPING client control operation to map combinations of address family, socket type, and protocol to device names of [TDI](https://msdn.microsoft.com/library/windows/hardware/ff565094) transports. A WSK application uses this client control operation only if it requires support for TDI transports. When a WSK application creates a socket, the WSK subsystem refer to the list of mappings only if there is no native support for the combination of address family, socket type, and protocol specified by the WSK application.

If a WSK application uses the WSK\_TDI\_DEVICENAME\_MAPPING client control operation to map combinations of address family, socket type, and protocol to device names of TDI transports, it must do so before it creates any sockets.

To map combinations of address family, socket type, and protocol to device names of TDI transports, a WSK application calls the [**WskControlClient**](https://msdn.microsoft.com/library/windows/hardware/ff571126) function with the following parameters.

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
<td><p>WSK_TDI_DEVICENAME_MAPPING</p></td>
</tr>
<tr class="even">
<td><p><em>InputSize</em></p></td>
<td><p>sizeof(WSK_TDI_MAP_INFO)</p></td>
</tr>
<tr class="odd">
<td><p><em>InputBuffer</em></p></td>
<td><p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff571192" data-raw-source="[&lt;strong&gt;WSK_TDI_MAP_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff571192)"><strong>WSK_TDI_MAP_INFO</strong></a> structure that contains a list of mappings of combinations of address family, socket type, and protocol to <a href="https://msdn.microsoft.com/library/windows/hardware/ff565091" data-raw-source="[TDI](https://msdn.microsoft.com/library/windows/hardware/ff565091)">TDI</a> device names.</p></td>
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

For more information about using TDI transports, see [Using TDI Transports](https://msdn.microsoft.com/library/windows/hardware/ff571015).

The *Irp* parameter must be **NULL** for this client control operation.

**Note**  TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/hardware/ff571068) or [Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083) instead.

 

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

 

 




