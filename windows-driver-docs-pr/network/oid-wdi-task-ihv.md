---
title: OID_WDI_TASK_IHV
ms.topic: reference
description: OID_WDI_TASK_IHV is used to start an IHV-initiated task.
ms.date: 03/02/2023
keywords:
 - OID_WDI_TASK_IHV Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_TASK\_IHV

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_TASK\_IHV is used to start an IHV-initiated task.

| Object | Abort capable                                           | Default priority (host driver policy)       | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | Priority depends on IHV-requested settings. | 10                              |

 

The task is initiated by the sending [NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST](ndis-status-wdi-indication-ihv-task-request.md), and is prioritized based on the value requested by the IHV.

## Task parameters


| TLV                                                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                   |
|--------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_IHV\_TASK\_DEVICE\_CONTEXT**](./wdi-tlv-ihv-task-device-context.md) |                                | X        | The context data provided by the IHV component. This is forwarded from [NDIS\_STATUS\_WDI\_INDICATION\_IHV\_ TASK\_REQUEST](ndis-status-wdi-indication-ihv-task-request.md). |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_COMPLETE](ndis-status-wdi-indication-ihv-task-complete.md)

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

 

