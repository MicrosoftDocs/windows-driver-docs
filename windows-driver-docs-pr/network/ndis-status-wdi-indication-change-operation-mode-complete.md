---
title: NDIS_STATUS_WDI_INDICATION_CHANGE_OPERATION_MODE_COMPLETE
author: windows-driver-content
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_CHANGE_OPERATION_MODE_COMPLETE to indicate the completion of OID_WDI_TASK_CHANGE_OPERATION_MODE.
ms.assetid: fa2a6544-c3ef-4a20-9182-f3678488053d
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WDI_INDICATION_CHANGE_OPERATION_MODE_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_CHANGE\_OPERATION\_MODE\_COMPLETE


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_CHANGE\_OPERATION\_MODE\_COMPLETE to indicate the completion of [OID\_WDI\_TASK\_CHANGE\_OPERATION\_MODE](oid-wdi-task-change-operation-mode.md).

| Object |
|--------|
| Port   |

 

## Payload data


This indication contains no additional data. The data in the header is sufficient.

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

 

 




