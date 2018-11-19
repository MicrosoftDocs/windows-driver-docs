---
title: WDI_TLV_AUTH_ALGO_LIST
description: WDI_TLV_AUTH_ALGO_LIST is a TLV that contains a list of authentication algorithms.
ms.assetid: 6F5EC21B-C923-45ED-B62E-302D916AABE5
ms.date: 07/18/2017
keywords:
 - WDI_TLV_AUTH_ALGO_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_AUTH\_ALGO\_LIST


WDI\_TLV\_AUTH\_ALGO\_LIST is a TLV that contains a list of authentication algorithms.

## TLV Type


0x3C

## Length


The size (in bytes) of the array of [**WDI\_AUTH\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897792) structures. The array must contain 1 or more elements.

## Values


| Type                                                        | Description                            |
|-------------------------------------------------------------|----------------------------------------|
| [**WDI\_AUTH\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897792)\[\] | An array of authentication algorithms. |

 

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

 

 




