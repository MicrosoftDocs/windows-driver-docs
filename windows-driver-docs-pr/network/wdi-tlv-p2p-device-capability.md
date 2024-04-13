---
title: WDI_TLV_P2P_DEVICE_CAPABILITY
ms.topic: reference
description: WDI_TLV_P2P_DEVICE_CAPABILITY is a TLV that contains Wi-Fi Direct device capabilities.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_DEVICE_CAPABILITY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DEVICE\_CAPABILITY

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_DEVICE\_CAPABILITY is a TLV that contains Wi-Fi Direct device capabilities.

## TLV Type


0x84

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------|
| UINT8  | A bitmap of the Wi-Fi Direct device capabilities as defined in Table 12 of the Wi-Fi Direct technical specification.            |
| UINT8  | A bitmap of the Wi-Fi Direct capabilities in the above device capability bitmap that are currently set by the operating system. |
| UINT32 | A bitmask that indicates which WPS versions are enabled.                                                                        |

 

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

 

 




