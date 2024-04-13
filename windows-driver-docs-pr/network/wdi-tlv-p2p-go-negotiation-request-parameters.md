---
title: WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_PARAMETERS
ms.topic: reference
description: WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_PARAMETERS is a TLV that contains Wi-Fi Direct Group Owner negotiation request parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS is a TLV that contains Wi-Fi Direct Group Owner negotiation request parameters.

## TLV Type


0x6E

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                             | Specifies the local Wi-Fi Direct GO Intent. Valid values are between 0 and 15.                                                                                                  |
| UINT8                                             | Specifies the tie-breaker field of GO Intent.                                                                                                                                   |
| UINT16                                            | Specifies the GO Configuration Timeout in milliseconds.                                                                                                                         |
| UINT16                                            | Specifies the Client Configuration Timeout in milliseconds.                                                                                                                     |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | Intended interface address. Specifies the local MAC address for future Wi-Fi Direct connections.                                                                                |
| UINT8                                             | Specifies the Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi P2P technical specification. |
| UINT8                                             | Specifies the bits set by the operating system in the Group capability bitmap above.                                                                                            |

 

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

 

