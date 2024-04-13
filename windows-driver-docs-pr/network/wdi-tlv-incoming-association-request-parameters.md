---
title: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS
ms.topic: reference
description: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS is a TLV that contains association request parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_PARAMETERS is a TLV that contains association request parameters.

## TLV Type


0x7D

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | The MAC address of the sender.                                                                                                |
| UINT8                                             | A bit that indicates whether or not it is a reassociation request. A value of 1 indicates that it is a reassociation request. |

 

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

 

