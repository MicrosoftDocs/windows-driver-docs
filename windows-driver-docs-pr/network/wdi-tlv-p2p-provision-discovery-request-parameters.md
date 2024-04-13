---
title: WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_PARAMETERS
ms.topic: reference
description: WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_PARAMETERS is a TLV that contains Wi-Fi Provision Discovery Request parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS is a TLV that contains Wi-Fi Provision Discovery Request parameters.

## TLV Type


0x85

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi Direct technical specification. |
| UINT8 | The bits in the Group capability bitmap above that are set by the operating system.                                                                                  |

 

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

 

 




