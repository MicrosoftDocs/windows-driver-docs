---
title: WDI_TLV_COUNTRY_REGION_LIST
description: WDI_TLV_COUNTRY_REGION_LIST is a TLV that contains a list of country or region codes.
ms.assetid: 675C176F-EE7A-41E0-9770-4D810F29E7BF
ms.date: 07/18/2017
keywords:
 - WDI_TLV_COUNTRY_REGION_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_COUNTRY\_REGION\_LIST


WDI\_TLV\_COUNTRY\_REGION\_LIST is a TLV that contains a list of country or region codes.

## TLV Type


0x12

## Length


The size (in bytes) of the array of WDI\_COUNTRY\_REGION\_LIST elements. The array must contain 1 or more elements.

**Note**  WDI\_COUNTRY\_REGION\_LIST is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                           | Description                          |
|--------------------------------|--------------------------------------|
| WDI\_COUNTRY\_REGION\_LIST\[\] | An array of country or region codes. |

 

WDI\_COUNTRY\_REGION\_LIST consists of the following elements.

| Type       | Description               |
|------------|---------------------------|
| UINT8\[3\] | A country or region code. |

 

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

 

 




