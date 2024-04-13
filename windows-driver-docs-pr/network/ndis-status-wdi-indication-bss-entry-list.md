---
title: NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST to inform the host about updates to the BSS entries. This is an unsolicited indication and can be sent at any time.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST to inform the host about updates to the BSS entries. This is an unsolicited indication and can be sent at any time.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                   | Multiple TLV instances allowed | Optional | Description                 |
|--------------------------------------------------------|--------------------------------|----------|-----------------------------|
| [**WDI\_TLV\_BSS\_ENTRY**](./wdi-tlv-bss-entry.md) | X                              | X        | The list of updated BSSIDs. |

 

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


[OID\_WDI\_TASK\_SCAN](oid-wdi-task-scan.md)

[OID\_WDI\_TASK\_P2P\_DISCOVER](oid-wdi-task-p2p-discover.md)

[OID\_WDI\_SET\_P2P\_START\_BACKGROUND\_DISCOVERY](oid-wdi-set-p2p-start-background-discovery.md)

 

