---
title: OID_WDI_SET_ASSOCIATION_PARAMETERS
ms.topic: reference
description: OID_WDI_SET_ASSOCIATION_PARAMETERS specifies parameters that the adapter can use during association to a set of BSSIDs.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_ASSOCIATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS specifies parameters that the adapter can use during association to a set of BSSIDs.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

This command replaces the previously configured list of BSSID-specific association parameters.

## Set property parameters


| TLV                                                                     | Multiple TLV instances allowed | Optional | Description                     |
|-------------------------------------------------------------------------|--------------------------------|----------|---------------------------------|
| [**WDI\_TLV\_CONNECT\_BSS\_ENTRY**](./wdi-tlv-connect-bss-entry.md) | X                              |          | The BSS entries and parameters. |

 

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

 

