---
title: NDIS_STATUS_WDI_INDICATION_P2P_SEND_RESPONSE_ACTION_FRAME_COMPLETE
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_P2P_SEND_RESPONSE_ACTION_FRAME_COMPLETE to indicate information about the Response Action frame sent by OID_WDI_TASK_P2P_SEND_RESPONSE_ACTION_FRAME.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_SEND_RESPONSE_ACTION_FRAME_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME\_COMPLETE


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME\_COMPLETE to indicate information about the Response Action frame sent by [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                                       | Multiple TLV instances allowed | Optional                                            | Description                                                            |
|------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------|------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT**](./wdi-tlv-p2p-send-action-frame-result-parameters.md) |                                | This TLV is only required if the status is success. | Information about the Response Action frame that was sent to the peer. |

 

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

 

