---
title: OID_WDI_TASK_CHANGE_OPERATION_MODE
description: OID_WDI_TASK_CHANGE_OPERATION_MODE configures the operation mode for the port.
ms.assetid: 84be0658-104d-4336-bc2f-6f2624f33857
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_CHANGE_OPERATION_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_CHANGE\_OPERATION\_MODE


OID\_WDI\_TASK\_CHANGE\_OPERATION\_MODE configures the operation mode for the port.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 4                                     | 1                               |

 

## Task parameters


| TLV                                                              | Multiple TLV instances allowed | Optional | Description                 |
|------------------------------------------------------------------|--------------------------------|----------|-----------------------------|
| [**WDI\_TLV\_OPERATION\_MODE**](https://msdn.microsoft.com/library/windows/hardware/dn897856) |                                |          | The desired operation mode. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_CHANGE\_OPERATION\_MODE\_COMPLETE](ndis-status-wdi-indication-change-operation-mode-complete.md)
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

 

 




