---
title: NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST to request that the Microsoft component queue an IHV task.ObjectPort .
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST to request that the Microsoft component queue an IHV task.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                         | Multiple TLV instances allowed | Optional | Description                                                                                                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_IHV\_TASK\_REQUEST\_PARAMETERS**](./wdi-tlv-ihv-task-request-parameters.md) |                                |          | The IHV-requested priority for this task. Refer to the [**WDI\_IHV\_TASK\_PRIORITY**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_ihv_task_priority) enum for valid values. |
| [**WDI\_TLV\_IHV\_TASK\_DEVICE\_CONTEXT**](./wdi-tlv-ihv-task-device-context.md)         |                                | X        | The IHV-provided context information that is forwarded to [OID\_WDI\_TASK\_IHV](oid-wdi-task-ihv.md).                                       |

 

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

## See also


[OID\_WDI\_TASK\_IHV](oid-wdi-task-ihv.md)

 

