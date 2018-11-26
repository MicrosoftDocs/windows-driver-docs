---
title: NDIS_STATUS_WDI_INDICATION_P2P_SEND_REQUEST_ACTION_FRAME_COMPLETE
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_P2P_SEND_REQUEST_ACTION_FRAME_COMPLETE to indicate information about the Request Action frame sent by OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME.
ms.assetid: 4c67b512-456f-48ed-bd1c-71a32bcf85f0
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_SEND_REQUEST_ACTION_FRAME_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_REQUEST\_ACTION\_FRAME\_COMPLETE


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_REQUEST\_ACTION\_FRAME\_COMPLETE to indicate information about the Request Action frame sent by [OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME](oid-wdi-task-p2p-send-request-action-frame.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                                       | Multiple TLV instances allowed | Optional                                            | Description                                                           |
|------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT**](https://msdn.microsoft.com/library/windows/hardware/dn897993) |                                | This TLV is only required if the status is success. | Information about the Request Action frame that was sent to the peer. |

 

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

 

 




