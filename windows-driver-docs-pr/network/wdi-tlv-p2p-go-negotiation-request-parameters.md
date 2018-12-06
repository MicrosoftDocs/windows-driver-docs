---
title: WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_PARAMETERS
description: WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_PARAMETERS is a TLV that contains Wi-Fi Direct Group Owner negotiation request parameters.
ms.assetid: C0B1832A-D315-47F8-87B8-73373CF55D44
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS


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
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Intended interface address. Specifies the local MAC address for future Wi-Fi Direct connections.                                                                                |
| UINT8                                             | Specifies the Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi P2P technical specification. |
| UINT8                                             | Specifies the bits set by the operating system in the Group capability bitmap above.                                                                                            |

 

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

 

 




