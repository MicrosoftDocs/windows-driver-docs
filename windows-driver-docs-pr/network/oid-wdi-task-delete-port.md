---
title: OID_WDI_TASK_DELETE_PORT
description: OID_WDI_TASK_DELETE_PORT requests that the IHV component releases all resources (including MAC and PHY) allocated to the specified port.
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_DELETE_PORT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WDI\_TASK\_DELETE\_PORT


OID\_WDI\_TASK\_DELETE\_PORT requests that the IHV component releases all resources (including MAC and PHY) allocated to the specified port.

| Object  | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|---------|---------------|---------------------------------------|---------------------------------|
| Adapter | No            | 6                                     | 1                               |

 

## Task parameters


| TLV                                                                               | Multiple TLV instances allowed | Optional | Description                 |
|-----------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------|
| [**WDI\_TLV\_DELETE\_PORT\_PARAMETERS**](./wdi-tlv-delete-port-parameters.md) |                                |          | The delete port parameters. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_DELETE\_PORT\_COMPLETE](ndis-status-wdi-indication-delete-port-complete.md)

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

 

