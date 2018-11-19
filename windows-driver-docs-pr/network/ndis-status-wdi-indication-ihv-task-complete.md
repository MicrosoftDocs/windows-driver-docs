---
title: NDIS_STATUS_WDI_INDICATION_IHV_TASK_COMPLETE
description: NDIS_STATUS_WDI_INDICATION_IHV_TASK_COMPLETE indicates the completion of OID_WDI_TASK_IHV.
ms.assetid: 03EA1580-110D-483B-BD4D-9275A7AC18A8
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_IHV_TASK_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_COMPLETE


NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_COMPLETE indicates the completion of [OID\_WDI\_TASK\_IHV](oid-wdi-task-ihv.md).

| Object |
|--------|
| Port   |

 

## Payload data


This indication contains no additional data. The data in the header is sufficient. The completion status from the message is not forwarded to anyone.

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

 

 




