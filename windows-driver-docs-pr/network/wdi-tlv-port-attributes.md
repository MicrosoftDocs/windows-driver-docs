---
title: WDI_TLV_PORT_ATTRIBUTES
ms.topic: reference
description: WDI_TLV_PORT_ATTRIBUTES is a TLV that contains port attributes.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PORT_ATTRIBUTES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PORT\_ATTRIBUTES


WDI\_TLV\_PORT\_ATTRIBUTES is a TLV that contains port attributes.

## TLV Type


0x29

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                         |
|---------------------------------------------------|-----------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | Specifies the MAC address associated with the port. |
| UINT16                                            | Specifies the port number.                          |

 

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

 

