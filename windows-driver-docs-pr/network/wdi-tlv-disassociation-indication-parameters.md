---
title: WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS
description: WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS is a TLV that contains disassociation indication parameters for NDIS_STATUS_WDI_INDICATION_DISASSOCIATION.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DISASSOCIATION\_INDICATION\_PARAMETERS


WDI\_TLV\_DISASSOCIATION\_INDICATION\_PARAMETERS is a TLV that contains disassociation indication parameters for [NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION](./ndis-status-wdi-indication-disassociation.md).

## TLV Type


0xBC

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                         | Description                                                                |
|--------------------------------------------------------------|----------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address)            | The MAC address of the peer associated with the disassociation indication. |
| [**WDI\_ASSOC\_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_assoc_status) (UINT32) | The trigger for the disassociation indication.                             |

 

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

 

