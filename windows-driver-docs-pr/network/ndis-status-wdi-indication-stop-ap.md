---
title: NDIS_STATUS_WDI_INDICATION_STOP_AP
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_STOP_AP to indicate that the adapter cannot sustain 802.11 Access Point (AP) functionality on any of the PHYs.
ms.assetid: EF129BD3-6AA2-4F38-BECD-E9D526314A27
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_STOP_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP to indicate that the adapter cannot sustain 802.11 Access Point (AP) functionality on any of the PHYs. The adapter should send this indication only after the NIC has stopped any APs that are operating on the available PHYs. The host blocks all [OID\_WDI\_TASK\_START\_AP](oid-wdi-task-start-ap.md) requests until the adapter sends [NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP](ndis-status-wdi-indication-can-sustain-ap.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                      | Multiple TLV instances allowed | Optional | Description                                                                       |
|---------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------|
| [**WDI\_TLV\_INDICATION\_STOP\_AP**](https://msdn.microsoft.com/library/windows/hardware/dn926318) |                                |          | The reason the adapter cannot sustain 802.11 AP functionality on any of the PHYs. |

 

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


[OID\_WDI\_TASK\_START\_AP](oid-wdi-task-start-ap.md)

[NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP](ndis-status-wdi-indication-can-sustain-ap.md)

 

 




