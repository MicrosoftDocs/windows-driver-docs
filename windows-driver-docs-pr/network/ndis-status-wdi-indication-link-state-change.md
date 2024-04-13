---
title: NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE to indicate any of the following situations
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_LINK\_STATE\_CHANGE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_LINK\_STATE\_CHANGE to indicate any of the following situations:

-   The link speed changed.
-   The link quality changed by more than a threshold value. The threshold is 1 if the connection quality hint is set to WDI\_CONNECTION\_QUALITY\_LOW\_LATENCY (defined in [**WDI\_CONNECTION\_QUALITY\_HINT**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_connection_quality_hint)). Otherwise, the threshold is 5.

| Object |
|--------|
| Port   |

 

This information from this indication is used by the host to keep track of metadata about the current link, and it may be propagated to the user.

In Station and P2P Client cases, the Peer MAC Address is set to the BSSID of the connected network. In AP/P2P GO cases, the Peer MAC Address is set to the MAC address of a given connected device.

## Payload data


| Type                                                                                           | Multiple TLV instances allowed | Optional | Description                       |
|------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------|
| [**WDI\_TLV\_LINK\_STATE\_CHANGE\_PARAMETERS**](./wdi-tlv-link-state-change-parameters.md) |                                |          | The link state change parameters. |

 

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

 

