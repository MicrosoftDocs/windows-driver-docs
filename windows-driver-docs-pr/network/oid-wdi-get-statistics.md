---
title: OID\_WDI\_GET\_STATISTICS
description: OID\_WDI\_GET\_STATISTICS requests that the IHV component returns MAC and PHY layer statistics.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 55c36869-ce85-42fe-877b-07aefb669b56
keywords: ["OID_WDI_GET_STATISTICS Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- OID_WDI_GET_STATISTICS
api_location:
- dot11wdi.h
api_type:
- HeaderDef
---

# OID\_WDI\_GET\_STATISTICS


OID\_WDI\_GET\_STATISTICS requests that the IHV component returns MAC and PHY layer statistics.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Set not supported        | 1                               |

 

The MAC statistics must all be maintained per port. PHY statistics must also be maintained per port unless exempted. If PHY statistics cannot be maintained per port (as allowed by exemption), the statistics can be maintained per "channel" (PHY statistics for two ports operating on the same port can be combined).

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                              | Multiple TLV instances allowed | Optional | Description              |
|------------------------------------------------------------------|--------------------------------|----------|--------------------------|
| [**WDI\_TLV\_MAC\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/dn897846) | X                              |          | Per-peer MAC statistics. |
| [**WDI\_TLV\_PHY\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/dn898025) | X                              |          | Per-port PHY statistics. |

 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_GET_STATISTICS%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




