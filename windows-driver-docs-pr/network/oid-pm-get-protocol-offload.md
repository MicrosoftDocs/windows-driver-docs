---
title: OID\_PM\_GET\_PROTOCOL\_OFFLOAD
author: windows-driver-content
description: An overlying driver issues an OID method request of OID\_PM\_GET\_PROTOCOL\_OFFLOAD to obtain parameter settings for a low power protocol offload from a network adapter.
ms.assetid: c14b9278-6f24-41a1-bc2e-536a75460ecd
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_PM_GET_PROTOCOL_OFFLOAD Network Drivers Starting with Windows Vista
---

# OID\_PM\_GET\_PROTOCOL\_OFFLOAD


An overlying driver issues an OID method request of OID\_PM\_GET\_PROTOCOL\_OFFLOAD to obtain parameter settings for a low power protocol offload from a network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure initially contains a pointer to a ULONG protocol offload identifier. After a successful return from the OID method request, the **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure contains a pointer to an [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](ndis-pm-protocol-offload.md) structure.

Remarks
-------

NDIS 6.20 and later protocol drivers use OID\_PM\_GET\_PROTOCOL\_OFFLOAD method OID to retrieve parameter settings for a low power protocol offload from a network adapter.

The information buffer must point to a ULONG-type protocol offload identifier. NDIS set this protocol offload identifier in the **ProtocolOffloadId** member of the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](ndis-pm-protocol-offload.md) structure when NDIS sent the prior [OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](oid-pm-add-protocol-offload.md) OID request to the underlying network adapter.

The miniport driver returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The requested data was retrieved successfully. The information buffer contains the corresponding NDIS\_PM\_PROTOCOL\_OFFLOAD structure.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. The final status code and results will be passed to the OID request completion handler of the caller.

<a href="" id="ndis-status-invalid-parameter"></a>NDIS\_STATUS\_INVALID\_PARAMETER  
The specified protocol offload identifier was not valid.

<a href="" id="ndis-status-buffer-too-short"></a>NDIS\_STATUS\_BUFFER\_TOO\_SHORT  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the NDIS\_OID\_REQUEST structure to the minimum buffer size that is required.

<a href="" id="ndis-status-not-supported"></a>NDIS\_STATUS\_NOT\_SUPPORTED  
The NDIS version of the miniport driver is below 6.20.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for reasons other than the preceding reasons.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.20 and later. Mandatory for miniport drivers. (See Remarks section.)</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_PROTOCOL\_OFFLOAD**](ndis-pm-protocol-offload.md)

[OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](oid-pm-add-protocol-offload.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PM_GET_PROTOCOL_OFFLOAD%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


