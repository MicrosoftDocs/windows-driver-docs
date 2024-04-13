---
title: WDI_TLV_P2P_DISCOVER_MODE
ms.topic: reference
description: WDI_TLV_P2P_DISCOVER_MODE is a TLV that contains Wi-Fi Direct discovery mode information for OID_WDI_TASK_P2P_DISCOVER.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_DISCOVER_MODE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DISCOVER\_MODE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_DISCOVER\_MODE is a TLV that contains Wi-Fi Direct discovery mode information for [OID\_WDI\_TASK\_P2P\_DISCOVER](./oid-wdi-task-p2p-discover.md).

## TLV Type


0xA9

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                                       | Description                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_DISCOVER\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_discover_type) (UINT32)                    | The type of discovery to be performed by the port.                                                                                                                                                                              |
| UINT8                                                                                      | A flag that indicates if a complete device discovery is required. Valid values are 0 (not required) and 1 (required). If this flag is set to 0, a partial discovery may be performed.                                           |
| [**WDI\_P2P\_SCAN\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_scan_type) (UINT32)                            | The type of scan to be performed by the port in scan phase.                                                                                                                                                                     |
| [**WDI\_P2P\_SERVICE\_DISCOVERY\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_service_discovery_type) (UINT32) | The type of Service Discovery to be performed.                                                                                                                                                                                  |
| UINT8                                                                                      | The scan repeat count. Specifies if the full scan procedure should be repeated. If set to 0, the scan should be repeated until the task is aborted by the host.                                                                 |
| UINT32                                                                                     | The time between scans. If the scan repeat count is not set to 1, this time specifies how long (in milliseconds) device should wait before repeating the scan procedure after completing a full scan of the requested channels. |

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

