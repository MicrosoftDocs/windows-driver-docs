---
title: NDIS_STATUS_WDI_INDICATION_CREATE_PORT_COMPLETE
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_CREATE_PORT_COMPLETE to indicate the completion of OID_WDI_TASK_CREATE_PORT.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_CREATE_PORT_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_CREATE\_PORT\_COMPLETE


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_CREATE\_PORT\_COMPLETE to indicate the completion of [OID\_WDI\_TASK\_CREATE\_PORT](oid-wdi-task-create-port.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                               | Multiple TLV instances allowed | Optional | Description                         |
|--------------------------------------------------------------------|--------------------------------|----------|-------------------------------------|
| [**WDI\_TLV\_PORT\_ATTRIBUTES**](./wdi-tlv-port-attributes.md) |                                |          | The attributes of the created port. |

 

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

 

