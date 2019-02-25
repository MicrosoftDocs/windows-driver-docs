---
title: WDI_TLV_IHV_NON_WDI_OIDS_LIST
description: WDI_TLV_IHV_NON_WDI_OIDS_LIST is a TLV that contains a list of non-WDI OIDs that the adapter wants to advertise to the operating system.
ms.assetid: 84929276-F098-4C24-A499-E252D5FB71A6
ms.date: 07/18/2017
keywords:
 - WDI_TLV_IHV_NON_WDI_OIDS_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IHV\_NON\_WDI\_OIDS\_LIST


WDI\_TLV\_IHV\_NON\_WDI\_OIDS\_LIST is a TLV that contains a list of non-WDI OIDs that the adapter wants to advertise to the operating system.

## TLV Type


0x104

## Length


The size (in bytes) of the array of UINT32 elements. The array must contain 1 or more elements.

## Values


| Type       | Description                                                                                                                                                                                       |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32\[\] | A list of non-WDI OIDs that the adapter wants to advertise to the operating system. The adapter should not assume that the operating system has already filtered non-WDI OIDs to match this list. |

 

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

 

 




