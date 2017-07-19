---
title: WDI\_TLV\_RECEIVE\_COALESCING\_CONFIG
author: windows-driver-content
description: WDI\_TLV\_RECEIVE\_COALESCING\_CONFIG is a TLV that contains receive coalescing configuration.
ms.assetid: 32542203-14DE-4F91-AB85-D2FA75ECAB9E
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_RECEIVE_COALESCING_CONFIG Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_RECEIVE_COALESCING_CONFIG%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


