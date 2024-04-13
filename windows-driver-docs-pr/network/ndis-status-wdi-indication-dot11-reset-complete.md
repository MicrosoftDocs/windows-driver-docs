---
title: NDIS_STATUS_WDI_INDICATION_DOT11_RESET_COMPLETE
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_DOT11_RESET_COMPLETE to indicate the completion of OID_WDI_TASK_DOT11_RESET.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_DOT11_RESET_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_DOT11\_RESET\_COMPLETE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_DOT11\_RESET\_COMPLETE to indicate the completion of [OID\_WDI\_TASK\_DOT11\_RESET](oid-wdi-task-dot11-reset.md).

| Object |
|--------|
| Port   |

 

## Payload data


This indication contains no additional data. The data in the header is sufficient.

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




