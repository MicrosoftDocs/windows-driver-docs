---
title: WSK_TDI_DEVICENAME_MAPPING
description: WSK_TDI_DEVICENAME_MAPPING
ms.date: 07/18/2017
keywords:
 - WSK_TDI_DEVICENAME_MAPPING Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WSK\_TDI\_DEVICENAME\_MAPPING


A WSK application uses the WSK\_TDI\_DEVICENAME\_MAPPING client control operation to map combinations of address family, socket type, and protocol to device names of [TDI](/previous-versions/windows/hardware/network/ff565094(v=vs.85)) transports. A WSK application uses this client control operation only if it requires support for TDI transports. When a WSK application creates a socket, the WSK subsystem refer to the list of mappings only if there is no native support for the combination of address family, socket type, and protocol specified by the WSK application.

If a WSK application uses the WSK\_TDI\_DEVICENAME\_MAPPING client control operation to map combinations of address family, socket type, and protocol to device names of TDI transports, it must do so before it creates any sockets.

To map combinations of address family, socket type, and protocol to device names of TDI transports, a WSK application calls the [**WskControlClient**](/windows-hardware/drivers/ddi/wsk/nc-wsk-pfn_wsk_control_client) function with the following parameters.

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
<td><p>A pointer to a <a href="/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_tdi_map_info" data-raw-source="[&lt;strong&gt;WSK_TDI_MAP_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/wsk/ns-wsk-_wsk_tdi_map_info)"><strong>WSK_TDI_MAP_INFO</strong></a> structure that contains a list of mappings of combinations of address family, socket type, and protocol to <a href="/previous-versions/windows/hardware/network/ff565091(v=vs.85)" data-raw-source="[TDI](/previous-versions/windows/hardware/network/ff565091(v=vs.85))">TDI</a> device names.</p></td>
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

For more information about using TDI transports, see [Using TDI Transports](./using-tdi-transports.md).

The *Irp* parameter must be **NULL** for this client control operation.

**Note**  TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](./introduction-to-windows-filtering-platform-callout-drivers.md) or [Winsock Kernel](/windows-hardware/drivers/ddi/_netvista/) instead.

 

## Requirements

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

