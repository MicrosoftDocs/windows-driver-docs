---
title: OID_WDI_TASK_OPEN
ms.topic: reference
description: OID_WDI_TASK_OPEN requests that the IHV component initializes the adapter.
ms.date: 03/02/2023
keywords:
 - OID_WDI_TASK_OPEN Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_TASK\_OPEN


OID\_WDI\_TASK\_OPEN requests that the IHV component initializes the adapter.

| Object  | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|---------|---------------|---------------------------------------|---------------------------------|
| Adapter | No            | 1                                     | 2                               |

 

Adapter initialization includes downloading firmware to the adapter, and setting up interrupts and other hardware resources. During initialization, this task is passed to the IHV using the OpenAdapterHandler handler registered by the IHV. On resume from low power state, this is passed to the IHV using OID\_WDI\_TASK\_OPEN.

## Task parameters


None
## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_OPEN\_COMPLETE](ndis-status-wdi-indication-open-complete.md)

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

 

 




