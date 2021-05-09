---
title: WDI_TLV_ROAMING_NEEDED_PARAMETERS
description: WDI_TLV_ROAMING_NEEDED_PARAMETERS is a TLV that contains the reason for a roam trigger. This is used in the NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED payload.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ROAMING_NEEDED_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ROAMING\_NEEDED\_PARAMETERS


WDI\_TLV\_ROAMING\_NEEDED\_PARAMETERS is a TLV that contains the reason for a roam trigger. This is used in the [NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](./ndis-status-wdi-indication-roaming-needed.md) payload.

## TLV Type


0x55

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                | Description                                                                                                                                      |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_ASSOC\_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_assoc_status) | Specifies the reason for a roam trigger. When a [OID\_WDI\_TASK\_ROAM](./oid-wdi-task-roam.md) is triggered, this reason is forwarded to it. |

 

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

 

