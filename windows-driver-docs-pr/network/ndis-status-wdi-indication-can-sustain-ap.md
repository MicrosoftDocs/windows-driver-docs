---
title: NDIS_STATUS_WDI_INDICATION_CAN_SUSTAIN_AP
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_CAN_SUSTAIN_AP to indicate that the port is ready to receive a OID_WDI_TASK_START_AP request, after previously indicating NDIS_STATUS_WDI_INDICATION_STOP_AP.
ms.assetid: 638822A9-4CED-4564-86B3-8BC9DBA05DD3
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_CAN_SUSTAIN_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP to indicate that the port is ready to receive a [OID\_WDI\_TASK\_START\_AP](oid-wdi-task-start-ap.md) request, after previously indicating [NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP](ndis-status-wdi-indication-stop-ap.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                     | Multiple TLV instances allowed | Optional | Description                                                     |
|------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------|
| [**WDI\_TLV\_INDICATION\_CAN\_SUSTAIN\_AP**](https://msdn.microsoft.com/library/windows/hardware/dn926317) |                                |          | The reason the adapter can now sustain 802.11 AP functionality. |

 

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

 

 




