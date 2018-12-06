---
title: WDI_TLV_CONFIGURED_MAC_ADDRESS
description: WDI_TLV_CONFIGURED_MAC_ADDRESS is a TLV that contains a custom MAC address.
ms.assetid: 2AB4AFF3-70E9-4E4B-885D-2578A5810A38
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CONFIGURED_MAC_ADDRESS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CONFIGURED\_MAC\_ADDRESS


WDI\_TLV\_CONFIGURED\_MAC\_ADDRESS is a TLV that contains a custom MAC address.

## TLV Type


0x99

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) structure.

## Values


| Type                                              | Description                                       |
|---------------------------------------------------|---------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | The MAC address that should be used for the port. |

 

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

 

 




