---
title: OID\_802\_3\_MULTICAST\_LIST
author: windows-driver-content
description: As a set request, NDIS and overlying protocol drivers use the OID\_802\_3\_MULTICAST\_LIST OID request to replace the current multicast address list on a miniport adapter.
ms.assetid: 601f38e1-26ae-4d72-9d72-91bd58f81bba
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_802_3_MULTICAST_LIST Network Drivers Starting with Windows Vista
---

# OID\_802\_3\_MULTICAST\_LIST


As a set request, NDIS and overlying protocol drivers use the OID\_802\_3\_MULTICAST\_LIST OID request to replace the current multicast address list on a miniport adapter. If an address is present in the list, that address is enabled to receive multicast packets.

As a query request, NDIS and protocol drivers use the OID\_802\_3\_MULTICAST\_LIST OID request to obtain the current multicast address list.

## <a href="" id="ddk-oid-802-3-multicast-list-nr"></a>


NDIS handles OID\_802\_3\_MULTICAST\_LIST query requests for miniport drivers, so miniport drivers never receive these query requests.

Miniport drivers that support multicast address lists must support OID\_802\_3\_MULTICAST\_LIST set requests.

For a set request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains the multicast address list as an array of addresses.

-   Each address is an array of 6 bytes.
-   The **InformationBufferLength** member contains the length, in bytes, of the **InformationBuffer** array.
-   If there are duplicate addresses in the list in the **InformationBuffer** member, NDIS removes the duplicates before sending the OID\_802\_3\_MULTICAST\_LIST set request to the miniport driver.
-   If the **InformationBufferLength** member is zero, the miniport driver must clear the multicast address list.
-   If the **InformationBufferLength** member is greater than zero, the miniport driver must replace any existing multicast address list with the list in the **InformationBuffer** member.

The miniport adapter's multicast address list is shared by all protocol drivers that are bound to the miniport adapter. NDIS controls access to this list. If multiple protocol drivers try to modify the list at the same time, NDIS combines their requests into a single OID\_802\_3\_MULTICAST\_LIST set request, which it sends to the miniport driver.

When a miniport adapter is initialized, it resets the NIC so the multicast address list is zero. NDIS also initializes the packet filter so it does not allow the protocol driver to receive multicast packets.

To receive a multicast packet, the protocol driver must later do one of the following:

-   Set the packet filter to include the **NDIS\_PACKET\_TYPE\_MULTICAST** flag. At any time, it can disable multicast packet reception by canceling this flag. The order in which the protocol driver enables reception for multicast packets is not important. For more information, see the [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md) OID request.
-   Set the packet filter to include the **NDIS\_PACKET\_TYPE\_ALL\_MULTICAST** flag, which enables all multicast packets, and do the filtering itself.

The miniport driver can set a limit on the number of multicast addresses that the multicast address list can contain. NDIS returns **NDIS\_STATUS\_MULTICAST\_FULL** if a protocol driver exceeds this limit or if it specifies an invalid multicast address.

For a query request, NDIS returns a multicast address list that is the union of all multicast address lists for all protocol bindings.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](oid-802-3-add-multicast-address.md)

[OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS](oid-802-3-delete-multicast-address.md)

[OID\_802\_3\_MAXIMUM\_LIST\_SIZE](oid-802-3-maximum-list-size.md)

[OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_802_3_MULTICAST_LIST%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


