---
title: NDIS_STATUS_WDI_INDICATION_SCAN_COMPLETE
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_SCAN_COMPLETE to indicate the completion of OID_WDI_TASK_SCAN.
ms.assetid: ed4b53e2-889d-4ce6-b9ea-92a95af28a8a
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_SCAN_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_SCAN\_COMPLETE


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_SCAN\_COMPLETE to indicate the completion of [OID\_WDI\_TASK\_SCAN](oid-wdi-task-scan.md).

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

## See also


[OID\_WDI\_TASK\_SCAN](oid-wdi-task-scan.md)

 

 




