---
title: NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_DISASSOCIATION to indicate that the host should try to find a better peer to connect to.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION to indicate that the host should try to find a better peer to connect to. This notification is used when the link quality with the currently connected peer falls below a certain threshold. On sending this notification, the host may trigger a roam scan and/or a roam operation. The Microsoft component does not perform a disconnect before it starts the roam operation.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                    | Multiple TLV instances allowed | Optional | Description                                                                                                                         |
|-----------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_ROAMING\_NEEDED\_PARAMETERS**](./wdi-tlv-roaming-needed-parameters.md) |                                |          | The reason for the roam trigger. When a [OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md) is triggered, this reason is forwarded to it. |

 

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


[OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md)

 

