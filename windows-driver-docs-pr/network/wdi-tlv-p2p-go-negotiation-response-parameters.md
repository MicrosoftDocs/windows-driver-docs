---
title: WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_PARAMETERS
description: WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_PARAMETERS is a TLV that contains incoming GO Negotiation Response parameters.
ms.assetid: 78C9B274-FAF0-4B2E-98A9-865A65105DA1
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_PARAMETERS


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_PARAMETERS is a TLV that contains incoming GO Negotiation Response parameters.

## TLV Type


0x71

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                             | Specifies the Wi-Fi Direct Status Code, as defined by the Wi-Fi Direct specification.                                                                                           |
| UINT8                                             | Specifies the local Wi-Fi Direct GO Intent. This is a value between 0 and 15.                                                                                                   |
| UINT8                                             | Specifies the tie-breaker field of the GO Intent.                                                                                                                               |
| UINT16                                            | Specifies the GO Configuration Timeout in milliseconds.                                                                                                                         |
| UINT16                                            | Specifies the Client Configuration Timeout in milliseconds.                                                                                                                     |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Intended interface address. Specifies the local MAC Address for future Wi-Fi Direct connection.                                                                                 |
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

 

 




