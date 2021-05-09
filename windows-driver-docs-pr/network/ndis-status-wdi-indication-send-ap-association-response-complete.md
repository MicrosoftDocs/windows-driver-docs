---
title: NDIS_STATUS_WDI_INDICATION_SEND_AP_ASSOCIATION_RESPONSE_COMPLETE
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_SEND_AP_ASSOCIATION_RESPONSE_COMPLETE to indicate information about the AP association response sent by OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_SEND_AP_ASSOCIATION_RESPONSE_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_SEND\_AP\_ASSOCIATION\_RESPONSE\_COMPLETE


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_SEND\_AP\_ASSOCIATION\_RESPONSE\_COMPLETE to indicate information about the AP association response sent by [OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE](oid-wdi-task-send-ap-association-response.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [**WDI\_TLV\_ASSOCIATION\_RESPONSE\_RESULT\_PARAMETERS**](./wdi-tlv-association-response-result-parameters.md) |   |   | The association response parameters. |
| [**WDI\_TLV\_ASSOCIATION\_RESPONSE\_FRAME**](./wdi-tlv-association-response-frame.md) |   |   | The received association response. This does not include the 802.11 MAC header. |
| [**WDI\_TLV\_BEACON\_IES**](./wdi-tlv-beacon-ies.md) |   |   | The beacon IEs from the association. |
| [**WDI\_TLV\_PHY\_TYPE\_LIST**](./wdi-tlv-phy-type-list.md) |   |   | The list of PHY types. |
 

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

 

