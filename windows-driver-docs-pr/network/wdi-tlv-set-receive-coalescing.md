---
title: WDI\_TLV\_SET\_RECEIVE\_COALESCING
author: windows-driver-content
description: WDI\_TLV\_SET\_RECEIVE\_COALESCING is a TLV that contains received packet coalescing parameters for OID\_WDI\_SET\_RECEIVE\_COALESCING.
ms.assetid: 7937517E-79E5-4BF6-9C22-79E1D73CA97C
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_SET_RECEIVE_COALESCING Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_SET_RECEIVE_COALESCING%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


