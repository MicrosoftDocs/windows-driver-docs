---
title: WDI_TLV_DISCONNECT_PARAMETERS
description: WDI_TLV_DISCONNECT_PARAMETERS is a TLV that contains parameters for OID_WDI_TASK_DISCONNECT.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_DISCONNECT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DISCONNECT\_PARAMETERS


WDI\_TLV\_DISCONNECT\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_DISCONNECT](./oid-wdi-task-disconnect.md).

## TLV Type


0x36

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | The MAC address of the peer to disassociate.                                                                                                                                        |
| UINT16                                            | The reason for the host-triggered disassociation. This value is provided in little endian byte order and should be appropriately copied into the reason code of the outgoing frame. |

 

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

 

