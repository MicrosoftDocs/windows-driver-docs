---
title: NDIS_STATUS_WDI_INDICATION_AP_ASSOCIATION_REQUEST_RECEIVED
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_AP_ASSOCIATION_REQUEST_RECEIVED to indicate that a Wi-Fi Association Request Frame has been received for an operational Wi-Fi Direct Group Owner.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_AP_ASSOCIATION_REQUEST_RECEIVED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_AP\_ASSOCIATION\_REQUEST\_RECEIVED

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_AP\_ASSOCIATION\_REQUEST\_RECEIVED to indicate that a Wi-Fi Association Request Frame has been received for an operational Wi-Fi Direct Group Owner. The host may issue an [OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE](oid-wdi-task-send-ap-association-response.md) for this request.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                                     | Multiple TLV instances allowed | Optional | Description                                   |
|----------------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------|
| [**WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO**](./wdi-tlv-incoming-association-request-info.md) |                                |          | The incoming Association Request information. |

 

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

 

