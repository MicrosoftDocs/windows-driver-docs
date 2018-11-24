---
title: WDI_TLV_P2P_INSTANCE_NAME_HASH
description: WDI_TLV_P2P_INSTANCE_NAME_HASH is a TLV that contains the hash of "Instance Name, Service Type".
ms.assetid: A29D0339-93A8-43EB-8C22-DD7A7DC2147C
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_INSTANCE_NAME_HASH Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INSTANCE\_NAME\_HASH


WDI\_TLV\_P2P\_INSTANCE\_NAME\_HASH is a TLV that contains the hash of "Instance Name, Service Type".

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x12C

## Length


The size (in bytes) of a [**WDI\_P2P\_SERVICE\_NAME\_HASH**](https://msdn.microsoft.com/library/windows/hardware/dn926103) structure.

## Values


| Type                                                                    | Description                                |
|-------------------------------------------------------------------------|--------------------------------------------|
| [**WDI\_P2P\_SERVICE\_NAME\_HASH**](https://msdn.microsoft.com/library/windows/hardware/dn926103) | The hash of "Instance Name, Service Type". |

 

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
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




