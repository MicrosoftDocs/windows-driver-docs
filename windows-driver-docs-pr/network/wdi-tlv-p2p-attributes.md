---
title: WDI_TLV_P2P_ATTRIBUTES
ms.topic: reference
description: WDI_TLV_P2P_ATTRIBUTES is a TLV that contains Wi-Fi Direct attributes.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_ATTRIBUTES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_ATTRIBUTES


WDI\_TLV\_P2P\_ATTRIBUTES is a TLV that contains Wi-Fi Direct attributes.

## TLV Type


0x25

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                  | Multiple TLV instances allowed | Optional | Description                                       |
|---------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------|
| [**WDI\_TLV\_P2P\_CAPABILITIES**](wdi-tlv-p2p-capabilities.md)                       |                                |          | The Wi-Fi Direct capabilities.                    |
| [**WDI\_TLV\_P2P\_INTERFACE\_ADDRESS\_LIST**](wdi-tlv-p2p-interface-address-list.md) |                                |          | An array of Wi-Fi Direct interface MAC addresses. |

 

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

 

 




