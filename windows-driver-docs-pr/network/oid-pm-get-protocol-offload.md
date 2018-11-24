---
title: OID_PM_GET_PROTOCOL_OFFLOAD
description: An overlying driver issues an OID method request of OID_PM_GET_PROTOCOL_OFFLOAD to obtain parameter settings for a low power protocol offload from a network adapter.
ms.assetid: c14b9278-6f24-41a1-bc2e-536a75460ecd
ms.date: 08/08/2017
keywords: 
 -OID_PM_GET_PROTOCOL_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PM\_GET\_PROTOCOL\_OFFLOAD


An overlying driver issues an OID method request of OID\_PM\_GET\_PROTOCOL\_OFFLOAD to obtain parameter settings for a low power protocol offload from a network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure initially contains a pointer to a ULONG protocol offload identifier. After a successful return from the OID method request, the **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure contains a pointer to an [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure.

Remarks
-------

NDIS 6.20 and later protocol drivers use OID\_PM\_GET\_PROTOCOL\_OFFLOAD method OID to retrieve parameter settings for a low power protocol offload from a network adapter.

The information buffer must point to a ULONG-type protocol offload identifier. NDIS set this protocol offload identifier in the **ProtocolOffloadId** member of the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure when NDIS sent the prior [OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](oid-pm-add-protocol-offload.md) OID request to the underlying network adapter.

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


[**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760)

[OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](oid-pm-add-protocol-offload.md)

 

 




