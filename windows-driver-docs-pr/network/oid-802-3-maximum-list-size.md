---
title: OID_802_3_MAXIMUM_LIST_SIZE
description: OID_802_3_MAXIMUM_LIST_SIZE
ms.assetid: e4288fb3-6bb3-415c-b150-1f258a2fa1a0
ms.date: 08/08/2017
keywords: 
 -OID_802_3_MAXIMUM_LIST_SIZE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_802\_3\_MAXIMUM\_LIST\_SIZE





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

 

 




