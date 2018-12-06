---
title: OID_802_3_ADD_MULTICAST_ADDRESS
description: As a set request, NDIS and overlying protocol drivers use the OID_802_3_ADD_MULTICAST_ADDRESS OID request to add an 802.3 multicast address to the multicast address list of a miniport adapter.
ms.assetid: e3e6defe-e65f-46bb-9cd6-cb65ffa7d7f0
ms.date: 08/08/2017
keywords: 
 -OID_802_3_ADD_MULTICAST_ADDRESS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_802\_3\_ADD\_MULTICAST\_ADDRESS


As a set request, NDIS and overlying protocol drivers use the OID\_802\_3\_ADD\_MULTICAST\_ADDRESS OID request to add an 802.3 multicast address to the multicast address list of a miniport adapter. The multicast address is an array of 6 bytes. Adding an address enables that address to receive multicast packets.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

Remarks
-------

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains the 6-byte address to be added to the multicast address list.

The OID\_802\_3\_ADD\_MULTICAST\_ADDRESS OID request can add only one address. To add more than one address, the overlying driver must issue multiple OID\_802\_3\_ADD\_MULTICAST\_ADDRESS OID requests.

NDIS miniport drivers do not receive this OID request directly. Instead, NDIS consolidates each sequence of OID\_802\_3\_ADD\_MULTICAST\_ADDRESS and [OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS](oid-802-3-delete-multicast-address.md) OID requests into a single [OID\_802\_3\_MULTICAST\_LIST](oid-802-3-multicast-list.md) OID request, which it sends to the miniport driver.

To receive multicast packets, the overlying driver must use the [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md) OID to set the packet filter **NDIS\_PACKET\_TYPE\_MULTICAST** flag.

The miniport driver can set a limit on the number of multicast addresses that the multicast address list can contain. To specify the maximum number of multicast addresses, the miniport driver sets the **MaxMulticastListSize** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure that it passes to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function. For miniport drivers that are based on NDIS versions before NDIS 6.0, NDIS queries the maximum number of multicast addresses by sending an [OID\_802\_3\_MAXIMUM\_LIST\_SIZE](oid-802-3-maximum-list-size.md) OID request. NDIS returns **NDIS\_STATUS\_MULTICAST\_FULL** if an OID\_802\_3\_ADD\_MULTICAST\_ADDRESS request exceeds this limit.

To delete a previously added multicast address, make a set request with the [OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS](oid-802-3-delete-multicast-address.md) OID. The overlying driver can add a given multicast address multiple times. If NDIS succeeds the first add request for a given multicast address, NDIS will succeed all subsequent add requests for that address. To delete a multicast address that was added more than once, the overlying driver must delete the address the same number of times that it added the address.

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


[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

[OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS](oid-802-3-delete-multicast-address.md)

[OID\_802\_3\_MAXIMUM\_LIST\_SIZE](oid-802-3-maximum-list-size.md)

[OID\_802\_3\_MULTICAST\_LIST](oid-802-3-multicast-list.md)

[OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md)

 

 




