---
title: WDI_TLV_DISALLOWED_BSSIDS_LIST
author: windows-driver-content
description: WDI_TLV_DISALLOWED_BSSIDS_LIST is a TLV that contains a list of BSSIDs that are not allowed to be used for association.
ms.assetid: A65A6C05-C4E1-4880-BF83-48B62D0C2FD3
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_DISALLOWED_BSSIDS_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_DISALLOWED\_BSSIDS\_LIST


WDI\_TLV\_DISALLOWED\_BSSIDS\_LIST is a TLV that contains a list of BSSIDs that are not allowed to be used for association.

## TLV Type


0xC3

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                                                                                                                                               |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)\[\] | A list of BSSIDs that are not allowed to be used for association. If this is specified, the adapter must not associate to any AP that is not in this list |

 

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

 

 




