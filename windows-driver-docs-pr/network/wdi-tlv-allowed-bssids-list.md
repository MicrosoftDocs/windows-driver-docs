---
title: WDI_TLV_ALLOWED_BSSIDS_LIST
description: WDI_TLV_ALLOWED_BSSIDS_LIST is a TLV that contains a list of BSSIDs that are allowed to be used for association.
ms.assetid: A53C5EB2-1D77-4380-86C7-291D2BF4FCFC
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ALLOWED_BSSIDS_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ALLOWED\_BSSIDS\_LIST


WDI\_TLV\_ALLOWED\_BSSIDS\_LIST is a TLV that contains a list of BSSIDs that are allowed to be used for association.

## TLV Type


0xC2

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                                                   |
|-------------------------------------------------------|---------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)\[\] | A list of BSSIDs that are allowed to be used for association. |

 

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

 

 




