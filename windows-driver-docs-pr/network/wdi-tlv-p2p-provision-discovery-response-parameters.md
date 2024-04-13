---
title: WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_PARAMETERS
ms.topic: reference
description: WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_PARAMETERS is a TLV that contains provision discovery response parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_PARAMETERS is a TLV that contains provision discovery response parameters.

## TLV Type


0x113

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | The Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi P2P technical specification. |
| UINT8 | The bits set by the operating system in the above Group capability bitmap.                                                                                            |

 

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

 

 




