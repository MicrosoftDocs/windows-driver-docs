---
title: NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST to inform the host about updates to the BSS entries. This is an unsolicited indication and can be sent at any time.
ms.assetid: 5b9fd7b1-0817-4b86-9acc-b4f99cb7ae9a
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST to inform the host about updates to the BSS entries. This is an unsolicited indication and can be sent at any time.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                   | Multiple TLV instances allowed | Optional | Description                 |
|--------------------------------------------------------|--------------------------------|----------|-----------------------------|
| [**WDI\_TLV\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn926162) | X                              | X        | The list of updated BSSIDs. |

 

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

## See also


[OID\_WDI\_TASK\_SCAN](oid-wdi-task-scan.md)

[OID\_WDI\_TASK\_P2P\_DISCOVER](oid-wdi-task-p2p-discover.md)

[OID\_WDI\_SET\_P2P\_START\_BACKGROUND\_DISCOVERY](oid-wdi-set-p2p-start-background-discovery.md)

 

 




