---
title: OID_WDI_TASK_STOP_AP
ms.topic: reference
description: OID_WDI_TASK_STOP_AP requests that the IHV component disconnects all connected clients on the specified port and stops beaconing and responding to probe requests. AP configuration and MIB attributes are preserved.
ms.date: 03/02/2023
keywords:
 - OID_WDI_TASK_STOP_AP Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_TASK\_STOP\_AP

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_TASK\_STOP\_AP requests that the IHV component disconnects all connected clients on the specified port and stops beaconing and responding to probe requests. AP configuration and MIB attributes are preserved.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 2                                     | 1                               |

 

## Task parameters


None
## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP\_COMPLETE](ndis-status-wdi-indication-stop-ap-complete.md)

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

 

 




