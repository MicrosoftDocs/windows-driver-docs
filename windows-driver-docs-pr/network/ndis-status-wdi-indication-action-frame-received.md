---
title: NDIS_STATUS_WDI_INDICATION_ACTION_FRAME_RECEIVED
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_ACTION_FRAME_RECEIVED to indicate that an Action Frame has been received.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_ACTION_FRAME_RECEIVED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_ACTION\_FRAME\_RECEIVED


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_ACTION\_FRAME\_RECEIVED to indicate that an Action Frame has been received.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                               | Multiple TLV instances allowed | Optional | Description                                               |
|------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](./wdi-tlv-bssid.md)                                      |                                |          | The BSSID of the source.                                  |
| [**WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO**](./wdi-tlv-bss-entry-channel-info.md) |                                |          | The logical channel number and band ID for the BSS entry. |
| [**WDI\_TLV\_ACTION\_FRAME\_BODY**](./wdi-tlv-action-frame-body.md)            |                                |          | The incoming Action Frame body.                           |

 

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


[OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION](oid-wdi-set-advertisement-information.md)

 

