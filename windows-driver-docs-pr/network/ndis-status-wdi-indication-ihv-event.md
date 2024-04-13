---
title: NDIS_STATUS_WDI_INDICATION_IHV_EVENT
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_IHV_EVENT to pass IHV specific information to the IHV extensibility module.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_IHV_EVENT Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_IHV\_EVENT

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_IHV\_EVENT to pass IHV specific information to the IHV extensibility module.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                 | Multiple TLV instances allowed | Optional | Description                                           |
|------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------|
| [**WDI\_TLV\_IHV\_DATA**](./wdi-tlv-ihv-data.md) |                                | X        | The event to be sent to the IHV extensibility module. |

 

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

 

