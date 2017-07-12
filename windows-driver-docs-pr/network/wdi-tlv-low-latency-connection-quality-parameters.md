---
title: WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS
description: WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS is a TLV that contains low latency connection quality parameters.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: F6C26267-AC6F-4810-913B-46DA99498BE2
keywords: ["WDI_TLV_LOW_LATENCY_CONNECTION_QUALITY_PARAMETERS Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_LOW_LATENCY_CONNECTION_QUALITY_PARAMETERS
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS


WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS is a TLV that contains low latency connection quality parameters.

## TLV Type


0xF6

## Length


The size (in bytes) of the array of all contained elements.

## Values


| Type  | Description                                                                                                                                                                                                                                                                            |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | Specifies the maximum number of milliseconds that the port can be on a different channel during Active Scan or other multi-channel operations. The only instance in which this off-channel can be higher is if the adapter needs to do a passive scan.                                 |
| UINT8 | Specifies the link quality threshold for [NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](https://msdn.microsoft.com/library/windows/hardware/dn925648). When the link quality is below this threshold, it is acceptable for the adapter to send NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED. |

 

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


[OID\_WDI\_SET\_CONNECTION\_QUALITY](https://msdn.microsoft.com/library/windows/hardware/dn925927)

[NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](https://msdn.microsoft.com/library/windows/hardware/dn925648)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_LOW_LATENCY_CONNECTION_QUALITY_PARAMETERS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





