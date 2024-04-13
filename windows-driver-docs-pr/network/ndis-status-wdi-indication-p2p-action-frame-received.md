---
title: NDIS_STATUS_WDI_INDICATION_P2P_ACTION_FRAME_RECEIVED
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_P2P_ACTION_FRAME_RECEIVED to indicate that a Wi-Fi Direct Action Frame has been received.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_ACTION_FRAME_RECEIVED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_ACTION\_FRAME\_RECEIVED

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_ACTION\_FRAME\_RECEIVED to indicate that a Wi-Fi Direct Action Frame has been received.

| Object |
|--------|
| Port   |

 

The host may issue an [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md) for this request.

The port must indicate these packets in any of the following situations:

-   The port is in listen state.
-   The port has a GO in operational state.
-   The port is dwelling on a remote listen channel when an [OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME](oid-wdi-task-p2p-send-request-action-frame.md) or [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md) has been recently issued.

## Payload data


| Type                                                                                               | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_INCOMING\_FRAME\_INFORMATION**](./wdi-tlv-p2p-incoming-frame-information.md) |                                |          | The incoming Wi-Fi Direct Action Frame information. This information is forwarded back to the port when the host issues [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md). |

 

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

## See also


[OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME](oid-wdi-task-p2p-send-request-action-frame.md)

[OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md)

 

