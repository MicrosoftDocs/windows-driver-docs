---
title: OID\_WDI\_SET\_MULTICAST\_LIST
description: OID\_WDI\_SET\_MULTICAST\_LIST specifies the multicast address list for a given port. This command can be set at any time.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dee41a49-2be2-4364-877c-b2b3bf29e78d
keywords: ["OID_WDI_SET_MULTICAST_LIST Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- OID_WDI_SET_MULTICAST_LIST
api_location:
- dot11wdi.h
api_type:
- HeaderDef
---

# OID\_WDI\_SET\_MULTICAST\_LIST


OID\_WDI\_SET\_MULTICAST\_LIST specifies the multicast address list for a given port. This command can be set at any time.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

The IHV component should only fail the command if the list size exceeds the limit specified in [**WDI\_TLV\_INTERFACE\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn897835).

After the host enables multicast packet filtering on the port using [OID\_WDI\_SET\_RECEIVE\_PACKET\_FILTER](oid-wdi-set-receive-packet-filter.md), the device must indicate received multicast frames with a destination address matching an address in the port’s multicast list to the host. The device must clear the multicast list as part of processing of [OID\_WDI\_TASK\_DOT11\_RESET](oid-wdi-task-dot11-reset.md). When the command is sent with no multicast list specified, the driver must clear its multicast list. In this case, no packets should be indicated up unless OID\_WDI\_SET\_RECEIVE\_PACKET\_FILTER has the WDI\_PACKET\_FILTER\_ALL\_MULTICAST bit set.

## Set property parameters


| TLV                                                              | Multiple TLV instances allowed | Optional | Description                                                  |
|------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------|
| [**WDI\_TLV\_MULTICAST\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn897849) |                                | X        | List of multicast MAC addresses. The list must not be empty. |

 

## Set property results


No additional data. The data in the header is sufficient.
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_SET_MULTICAST_LIST%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




