---
title: WDI_TLV_P2P_INVITATION_RESPONSE_PARAMETERS
ms.topic: reference
description: WDI_TLV_P2P_INVITATION_RESPONSE_PARAMETERS is a TLV that contains Wi-Fi Direct Invitation Response parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_INVITATION_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_INVITATION\_RESPONSE\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_INVITATION\_RESPONSE\_PARAMETERS is a TLV that contains Wi-Fi Direct Invitation Response parameters.

## TLV Type


0x80

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                    |
|--------|--------------------------------------------------------------------------------|
| UINT8  | The Wi-Fi Direct Status Code, as specified by the Wi-Fi Direct specification.. |
| UINT16 | The GO Configuration Timeout, in milliseconds.                                 |
| UINT16 | The Client Configuration Timeout, in milliseconds.                             |

 

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

 

 




