---
title: OID\_WDI\_SET\_RECEIVE\_COALESCING
description: OID\_WDI\_SET\_RECEIVE\_COALESCING is used by the host to add a packet filter for packet coalescing.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c8856813-0d81-4735-95cc-d9b5dc6ede87
keywords: ["OID_WDI_SET_RECEIVE_COALESCING Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- OID_WDI_SET_RECEIVE_COALESCING
api_location:
- dot11wdi.h
api_type:
- HeaderDef
---

# OID\_WDI\_SET\_RECEIVE\_COALESCING


OID\_WDI\_SET\_RECEIVE\_COALESCING is used by the host to add a packet filter for packet coalescing.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

When the host receives a request from the OS to set packet coalescing filters, it uses this command to add a packet filter for packet coalescing. To clear a packet filter for packet coalescing, see [OID\_WDI\_SET\_CLEAR\_RECEIVE\_COALESCING](oid-wdi-set-clear-receive-coalescing.md).

## Set property parameters


| TLV                                                                               | Multiple TLV instances allowed | Optional | Description                                 |
|-----------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------|
| [**WDI\_TLV\_SET\_RECEIVE\_COALESCING**](https://msdn.microsoft.com/library/windows/hardware/dn898061) |                                |          | The packet coalescing parameters to be set. |

 

## Set property results


No additional parameters. The data in the header is sufficient.
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

## See also


[OID\_WDI\_SET\_CLEAR\_RECEIVE\_COALESCING](oid-wdi-set-clear-receive-coalescing.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_SET_RECEIVE_COALESCING%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





