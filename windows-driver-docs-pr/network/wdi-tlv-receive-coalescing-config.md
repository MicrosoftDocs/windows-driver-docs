---
title: WDI_TLV_RECEIVE_COALESCING_CONFIG
description: WDI_TLV_RECEIVE_COALESCING_CONFIG is a TLV that contains receive coalescing configuration.
ms.assetid: 32542203-14DE-4F91-AB85-D2FA75ECAB9E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_RECEIVE_COALESCING_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_RECEIVE\_COALESCING\_CONFIG


WDI\_TLV\_RECEIVE\_COALESCING\_CONFIG is a TLV that contains receive coalescing configuration.

## TLV Type


0xDB

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                         |
|--------|---------------------------------------------------------------------|
| UINT32 | A unique queue ID to queue packets matching this filter.            |
| UINT32 | A filter ID with a value from 1 to the number of filters supported. |
| UINT32 | The maximum coalescing delay in milliseconds.                       |

 

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

## See also


[OID\_WDI\_SET\_RECEIVE\_COALESCING](https://msdn.microsoft.com/library/windows/hardware/dn925941)

 

 




