---
title: WDI_TLV_P2P_INTERFACE_ADDRESS_LIST
description: WDI_TLV_P2P_INTERFACE_ADDRESS_LIST is a TLV that contains an address list for a Wi-Fi Direct interface.
ms.assetid: B7FCB047-28D2-43E2-B4D6-B24E7BC74D47
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_INTERFACE_ADDRESS_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INTERFACE\_ADDRESS\_LIST


WDI\_TLV\_P2P\_INTERFACE\_ADDRESS\_LIST is a TLV that contains an address list for a Wi-Fi Direct interface.

## TLV Type


0x18

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                      |
|-------------------------------------------------------|----------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)\[\] | An array of Wi-Fi MAC addresses. |

 

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

 

 




