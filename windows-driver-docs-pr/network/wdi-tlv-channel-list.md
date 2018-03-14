---
title: WDI_TLV_CHANNEL_LIST
author: windows-driver-content
description: WDI_TLV_CHANNEL_LIST is a TLV that contains one or more channel numbers.
ms.assetid: DBBA28C2-D80F-409B-BEE6-81B6FEDF7484
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_CHANNEL_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CHANNEL\_LIST


WDI\_TLV\_CHANNEL\_LIST is a TLV that contains one or more channel numbers.

## TLV Type


0x4

## Length


The size (in bytes) of the array of [**WDI\_CHANNEL\_MAPPING\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn897799) structures. The array must contain 1 or more structures.

## Values


| Type                                                                       | Description                          |
|----------------------------------------------------------------------------|--------------------------------------|
| [**WDI\_CHANNEL\_MAPPING\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn897799)\[\] | An array of channel mapping entries. |

 

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

 

 




