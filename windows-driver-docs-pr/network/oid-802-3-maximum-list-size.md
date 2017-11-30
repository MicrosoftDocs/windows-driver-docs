---
title: OID_802_3_MAXIMUM_LIST_SIZE
author: windows-driver-content
description: OID_802_3_MAXIMUM_LIST_SIZE
ms.assetid: e4288fb3-6bb3-415c-b150-1f258a2fa1a0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_802_3_MAXIMUM_LIST_SIZE Network Drivers Starting with Windows Vista
---

# OID\_802\_3\_MAXIMUM\_LIST\_SIZE


## <a href="" id="ddk-oid-802-3-maximum-list-size-nr"></a>


NDIS and overlying protocol drivers use the OID\_802\_3\_MAXIMUM\_LIST\_SIZE OID request to query or set the maximum number of 6-byte multicast addresses that the miniport adapter's multicast address list can hold.

This multicast address list is shared by all protocol drivers that are bound to the miniport adapter. Because it is a shared resource, a protocol driver can receive **NDIS\_STATUS\_MULTICAST\_FULL** from the miniport adapter in response to an [OID\_802\_3\_MULTICAST\_LIST](oid-802-3-multicast-list.md) OID set request, even if the number of elements in the list is less than the number that NDIS previously returned for an OID\_802\_3\_MAXIMUM\_LIST\_SIZE OID query request.

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

[OID\_802\_3\_MULTICAST\_LIST](oid-802-3-multicast-list.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_802_3_MAXIMUM_LIST_SIZE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


