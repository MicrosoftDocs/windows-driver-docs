---
title: OID_WDI_SET_PRIVACY_EXEMPTION_LIST
description: OID_WDI_SET_PRIVACY_EXEMPTION_LIST is used by the host to provide the list of exemptions for packet description. The adapter applies these exemptions to packets it receives that match the IEEE EtherType value specified for the exemption.
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_PRIVACY_EXEMPTION_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WDI\_SET\_PRIVACY\_EXEMPTION\_LIST


OID\_WDI\_SET\_PRIVACY\_EXEMPTION\_LIST is used by the host to provide the list of exemptions for packet description. The adapter applies these exemptions to packets it receives that match the IEEE EtherType value specified for the exemption.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                 | Multiple TLV instances allowed | Optional | Description                        |
|-------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------|
| [**WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY**](./wdi-tlv-privacy-exemption-entry.md) | X                              | X        | List of privacy exemption entries. |

 

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

 

