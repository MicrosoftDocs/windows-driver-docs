---
title: WDI_TLV_P2P_SERVICE_TYPE_HASH
description: WDI_TLV_P2P_SERVICE_TYPE_HASH is a TLV that contains the hash of Service Type.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_SERVICE_TYPE_HASH Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SERVICE\_TYPE\_HASH


WDI\_TLV\_P2P\_SERVICE\_TYPE\_HASH is a TLV that contains the hash of Service Type.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x12A

## Length


The size (in bytes) of a [**WDI\_P2P\_SERVICE\_NAME\_HASH**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_p2p_service_name_hash) structure.

## Values


| Type                                                                    | Description               |
|-------------------------------------------------------------------------|---------------------------|
| [**WDI\_P2P\_SERVICE\_NAME\_HASH**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_p2p_service_name_hash) | The hash of Service Type. |

 

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

 

