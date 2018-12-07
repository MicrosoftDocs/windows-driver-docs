---
title: OID_WDI_TASK_STOP_AP
description: OID_WDI_TASK_STOP_AP requests that the IHV component disconnects all connected clients on the specified port and stops beaconing and responding to probe requests. AP configuration and MIB attributes are preserved.
ms.assetid: b7df1d2f-fed4-4079-8a2d-3f691a52ad52
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_STOP_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_STOP\_AP


OID\_WDI\_TASK\_STOP\_AP requests that the IHV component disconnects all connected clients on the specified port and stops beaconing and responding to probe requests. AP configuration and MIB attributes are preserved.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 2                                     | 1                               |

 

## Task parameters


None
## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP\_COMPLETE](ndis-status-wdi-indication-stop-ap-complete.md)
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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




