---
title: OID_802_3_DELETE_MULTICAST_ADDRESS
description: As a set request, NDIS and overlying protocol drivers use the OID_802_3_DELETE_MULTICAST_ADDRESS OID to delete a previously added multicast address from the multicast address list of a miniport adapter.
ms.assetid: 5efaa724-80b4-4721-a1b0-8ba67c03bb32
ms.date: 08/08/2017
keywords: 
 -OID_802_3_DELETE_MULTICAST_ADDRESS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS


As a set request, NDIS and overlying protocol drivers use the OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS OID to delete a previously added multicast address from the multicast address list of a miniport adapter. The multicast address is an array of 6 bytes. Deleting an address disables that address so that it can no longer receive multicast packets.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

Remarks
-------

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains the 6-byte address to be deleted from the multicast address list.

The OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS OID request can delete only one address. To delete more than one address, the protocol driver must issue multiple OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS OID requests.

NDIS miniport drivers do not receive this OID request directly. Instead, NDIS consolidates each sequence of [OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](oid-802-3-add-multicast-address.md) and OID\_802\_3\_DELETE\_MULTICAST\_ADDRESS OID requests into a single [OID\_802\_3\_MULTICAST\_LIST](oid-802-3-multicast-list.md) OID request.

To replace or delete the entire multicast list, the protocol driver can use the [OID\_802\_3\_MULTICAST\_LIST](oid-802-3-multicast-list.md) OID request.

To add an address to the list, the protocol driver can use the [OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](oid-802-3-add-multicast-address.md) OID request.

The overlying protocol driver can add a given multicast address multiple times by sending multiple [OID\_802\_3\_ADD\_MULTICAST\_ADDRESS](oid-802-3-add-multicast-address.md) OID requests. If NDIS succeeds the first add request for a given multicast address, NDIS will succeed all subsequent add requests for that address. To delete a multicast address that was added more than once, the overlying driver must delete the address the same number of times that it added the address.

### Return status codes

The miniport driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function returns one of the following values for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The miniport driver completed the request successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The miniport driver will complete the request asynchronously. After the miniport driver has completed all processing, it must succeed the request by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563622" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563622)"><strong>NdisMOidRequestComplete</strong></a> function, passing <strong>NDIS_STATUS_SUCCESS</strong> for the <em>Status</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_ACCEPTED</strong></p></td>
<td><p>The miniport driver is resetting.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_REQUEST_ABORTED</strong></p></td>
<td><p>The miniport driver stopped processing the request. For example, NDIS called the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559432" data-raw-source="[&lt;em&gt;MiniportResetEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559432)"><em>MiniportResetEx</em></a> function.</p></td>
</tr>
</tbody>
</table>

 

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

[OID\_802\_3\_MAXIMUM\_LIST\_SIZE](oid-802-3-maximum-list-size.md)

[OID\_802\_3\_MULTICAST\_LIST](oid-802-3-multicast-list.md)

 

 




