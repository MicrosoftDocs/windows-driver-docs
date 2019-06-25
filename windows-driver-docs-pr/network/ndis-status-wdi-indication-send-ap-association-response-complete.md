---
title: NDIS_STATUS_WDI_INDICATION_SEND_AP_ASSOCIATION_RESPONSE_COMPLETE
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_SEND_AP_ASSOCIATION_RESPONSE_COMPLETE to indicate information about the AP association response sent by OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE.
ms.assetid: c8bfa3b3-5d22-4831-9355-94c62fed7fd4
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
| [**WDI\_TLV\_ASSOCIATION\_RESPONSE\_RESULT\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-association-response-result-parameters) |   |   | The association response parameters. |
| [**WDI\_TLV\_ASSOCIATION\_RESPONSE\_FRAME**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-association-response-frame) |   |   | The received association response. This does not include the 802.11 MAC header. |
| [**WDI\_TLV\_BEACON\_IES**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-beacon-ies) |   |   | The beacon IEs from the association. |
| [**WDI\_TLV\_PHY\_TYPE\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-phy-type-list) |   |   | The list of PHY types. |
 

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

 

 




