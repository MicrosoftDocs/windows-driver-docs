---
title: OID_WDI_SET_P2P_WPS_ENABLED
ms.topic: reference
description: OID_WDI_SET_P2P_WPS_ENABLED requests that the adapter enables or disables Wi-Fi Protected Setup (WPS) on the NIC.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_P2P_WPS_ENABLED Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_P2P\_WPS\_ENABLED

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_SET\_P2P\_WPS\_ENABLED requests that the adapter enables or disables Wi-Fi Protected Setup (WPS) on the NIC.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                 | Multiple TLV instances allowed | Optional | Description                                 |
|---------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------|
| [**WDI\_TLV\_P2P\_WPS\_ENABLED**](./wdi-tlv-p2p-wps-enabled.md) |                                |          | Specifies whether to enable or disable WPS. |

 

## Set property results


No additional data. The data in the header is sufficient.

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

 

