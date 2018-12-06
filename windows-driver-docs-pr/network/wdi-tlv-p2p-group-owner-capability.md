---
title: WDI_TLV_P2P_GROUP_OWNER_CAPABILITY
description: WDI_TLV_P2P_GROUP_OWNER_CAPABILITY is a TLV that contains Wi-Fi Direct Group Owner capability information.
ms.assetid: 3F07665C-0212-465C-9118-CC213198EFB7
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_GROUP_OWNER_CAPABILITY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY


WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY is a TLV that contains Wi-Fi Direct Group Owner capability information.

## TLV Type


0x77

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8  | Specifies the Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi P2P technical specification. |
| UINT8  | Specifies the bits set by the operating system in the Group capability bitmap above.                                                                                            |
| UINT32 | Maximum client count for this Group Owner.                                                                                                                                      |

 

Requirements
------------

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

 

 




