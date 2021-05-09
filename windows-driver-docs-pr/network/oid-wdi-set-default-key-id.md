---
title: OID_WDI_SET_DEFAULT_KEY_ID
description: OID_WDI_SET_DEFAULT_KEY_ID sets the default key ID for packet transmission on a port.
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_DEFAULT_KEY_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WDI\_SET\_DEFAULT\_KEY\_ID


OID\_WDI\_SET\_DEFAULT\_KEY\_ID sets the default key ID for packet transmission on a port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                             | Multiple TLV instances allowed | Optional | Description                                             |
|-------------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------|
| [**WDI\_TLV\_DEFAULT\_TX\_KEY\_ID\_PARAMETERS**](./wdi-tlv-default-tx-key-id-parameters.md) |                                |          | The default key ID for packet transmission on the port. |

 

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

 

