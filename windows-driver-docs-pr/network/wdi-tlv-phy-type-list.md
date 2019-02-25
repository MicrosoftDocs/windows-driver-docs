---
title: WDI_TLV_PHY_TYPE_LIST
description: WDI_TLV_PHY_TYPE_LIST is a TLV that contains an array of PHY types.
ms.assetid: 4066E4CE-D63E-4499-AE27-11F6BD57795D
ms.date: 07/18/2017
keywords:
 - WDI_TLV_PHY_TYPE_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PHY\_TYPE\_LIST


WDI\_TLV\_PHY\_TYPE\_LIST is a TLV that contains an array of PHY types.

## TLV Type


0x19

## Length


The size (in bytes) of the array of [**WDI\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926105) values. The array must contain 1 or more values.

## Values


| Type                                            | Description                  |
|-------------------------------------------------|------------------------------|
| [**WDI\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926105)\[\] | An array of PHY type values. |

 

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

 

 




