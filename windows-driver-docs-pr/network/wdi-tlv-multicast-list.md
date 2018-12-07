---
title: WDI_TLV_MULTICAST_LIST
description: WDI_TLV_MULTICAST_LIST is a TLV that contains an array of multicast MAC addresses.
ms.assetid: 5023557A-1BC5-4A4E-A77C-20353C0CA3FD
ms.date: 07/18/2017
keywords:
 - WDI_TLV_MULTICAST_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_MULTICAST\_LIST


WDI\_TLV\_MULTICAST\_LIST is a TLV that contains an array of multicast MAC addresses.

## TLV Type


0x6A

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                          |
|-------------------------------------------------------|--------------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)\[\] | An array of multicast MAC addresses. |

 

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

 

 




