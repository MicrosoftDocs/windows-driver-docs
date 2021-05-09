---
title: OID_WDI_TASK_CLOSE
description: OID_WDI_TASK_CLOSE requests that the IHV component closes the adapter. This includes disabling interrupts and shutting down hardware. During a halt, this task is passed to the IHV through the CloseAdapterHandler handler registered by the IHV.
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_CLOSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WDI\_TASK\_CLOSE


OID\_WDI\_TASK\_CLOSE requests that the IHV component closes the adapter. This includes disabling interrupts and shutting down hardware. During a halt, this task is passed to the IHV through the CloseAdapterHandler handler registered by the IHV.

| Object  | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|---------|---------------|---------------------------------------|---------------------------------|
| Adapter | No            | 1                                     | 5                               |

 

## Task parameters


None
## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_CLOSE\_COMPLETE](ndis-status-wdi-indication-close-complete.md)

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

 

 




