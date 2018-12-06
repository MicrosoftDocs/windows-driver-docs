---
title: WDI_TLV_SET_RECEIVE_COALESCING
description: WDI_TLV_SET_RECEIVE_COALESCING is a TLV that contains received packet coalescing parameters for OID_WDI_SET_RECEIVE_COALESCING.
ms.assetid: 7937517E-79E5-4BF6-9C22-79E1D73CA97C
ms.date: 07/18/2017
keywords:
 - WDI_TLV_SET_RECEIVE_COALESCING Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SET\_RECEIVE\_COALESCING


WDI\_TLV\_SET\_RECEIVE\_COALESCING is a TLV that contains received packet coalescing parameters for [OID\_WDI\_SET\_RECEIVE\_COALESCING](https://msdn.microsoft.com/library/windows/hardware/dn925941).

## TLV Type


0x64

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                               | Multiple TLV instances allowed | Optional | Description                                |
|------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------|
| [**WDI\_TLV\_RECEIVE\_COALESCING\_CONFIG**](wdi-tlv-receive-coalescing-config.md) |                                |          | Specifies coalescing filter configuration. |
| [**WDI\_TLV\_RECEIVE\_FILTER\_FIELD**](wdi-tlv-receive-filter-field.md)           | X                              | X        | Specifies a receive filter field.          |

 

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

 

 




