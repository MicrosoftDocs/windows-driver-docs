---
title: WDI_TLV_HESSID
description: WDI_TLV_HESSID is a TLV that contains a list of HESSIDs.
ms.assetid: 630A1824-7722-4B03-8073-EFC44E142400
ms.date: 07/18/2017
keywords:
 - WDI_TLV_HESSID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_HESSID


WDI\_TLV\_HESSID is a TLV that contains a list of HESSIDs.

## TLV Type


0xC8

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description        |
|-------------------------------------------------------|--------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)\[\] | A list of HESSIDs. |

 

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

 

 




