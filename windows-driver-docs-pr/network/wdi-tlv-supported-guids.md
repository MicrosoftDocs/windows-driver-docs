---
title: WDI_TLV_SUPPORTED_GUIDS
ms.topic: reference
description: WDI_TLV_SUPPORTED_GUIDS is a TLV that contains a supported NDIS GUID.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_SUPPORTED_GUIDS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_SUPPORTED\_GUIDS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_SUPPORTED\_GUIDS is a TLV that contains a supported NDIS GUID.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x130

## Length


The size (in bytes) of a [NDIS\_GUID](./filling-in-an-ndis-guid-structure.md) structure.

## Values


| Type       | Description            |
|------------|------------------------|
| NDIS\_GUID | A supported NDIS GUID. |

 

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
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

## See also


[OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](./oid-wdi-get-adapter-capabilities.md)

 

