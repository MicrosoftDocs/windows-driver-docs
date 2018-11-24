---
title: WDI_TLV_IHV_DATA
description: WDI_TLV_IHV_DATA is a TLV that contains IHV-specific information that is used by the IHV extensibility module.
ms.assetid: 50D80D9E-C3FF-41E5-A054-A5A28ED499FD
ms.date: 07/18/2017
keywords:
 - WDI_TLV_IHV_DATA Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IHV\_DATA


WDI\_TLV\_IHV\_DATA is a TLV that contains IHV-specific information that is used by the IHV extensibility module.

## TLV Type


0xBD

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                            |
|-----------|------------------------------------------------------------------------|
| UINT8\[\] | IHV specific information that is used by the IHV extensibility module. |

 

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

 

 




