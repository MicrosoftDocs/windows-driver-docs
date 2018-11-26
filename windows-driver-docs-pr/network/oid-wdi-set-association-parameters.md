---
title: OID_WDI_SET_ASSOCIATION_PARAMETERS
description: OID_WDI_SET_ASSOCIATION_PARAMETERS specifies parameters that the adapter can use during association to a set of BSSIDs.
ms.assetid: 86a6cc62-eaa4-435c-af6c-b76591d92c00
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_ASSOCIATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS


OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS specifies parameters that the adapter can use during association to a set of BSSIDs.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

This command replaces the previously configured list of BSSID-specific association parameters.

## Set property parameters


| TLV                                                                     | Multiple TLV instances allowed | Optional | Description                     |
|-------------------------------------------------------------------------|--------------------------------|----------|---------------------------------|
| [**WDI\_TLV\_CONNECT\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn926264) | X                              |          | The BSS entries and parameters. |

 

## Set property results


No additional data. The data in the header is sufficient.
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

 

 




