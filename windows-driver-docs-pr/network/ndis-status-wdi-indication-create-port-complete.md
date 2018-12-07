---
title: NDIS_STATUS_WDI_INDICATION_CREATE_PORT_COMPLETE
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_CREATE_PORT_COMPLETE to indicate the completion of OID_WDI_TASK_CREATE_PORT.
ms.assetid: 8d3cdac1-06d3-4a21-ac13-e6d789c6922e
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_CREATE_PORT_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_CREATE\_PORT\_COMPLETE


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_CREATE\_PORT\_COMPLETE to indicate the completion of [OID\_WDI\_TASK\_CREATE\_PORT](oid-wdi-task-create-port.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                               | Multiple TLV instances allowed | Optional | Description                         |
|--------------------------------------------------------------------|--------------------------------|----------|-------------------------------------|
| [**WDI\_TLV\_PORT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn898038) |                                |          | The attributes of the created port. |

 

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

 

 




