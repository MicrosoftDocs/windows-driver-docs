---
title: WDI_TLV_PRIVACY_EXEMPTION_ENTRY
description: WDI_TLV_PRIVACY_EXEMPTION_ENTRY is a TLV that contains a privacy exemption entry.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_PRIVACY_EXEMPTION_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY


WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY is a TLV that contains a privacy exemption entry.

## TLV Type


0x48

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                   | Description                                                 |
|------------------------------------------------------------------------|-------------------------------------------------------------|
| UINT16                                                                 | Specifies the IEEE EtherType in big-endian byte order.      |
| [**WDI\_EXEMPTION\_ACTION\_TYPE**](/windows-hardware/drivers/ddi/dot11wdi/ne-dot11wdi-_wdi_exemption_action_type) | Specifies the action type of the exemption.                 |
| [**WDI\_EXEMPTION\_PACKET\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_exemption_packet_type) | Specifies the type of packet that the exemption applies to. |

 

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

 

