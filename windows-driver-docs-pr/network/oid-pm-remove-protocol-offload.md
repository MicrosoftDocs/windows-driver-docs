---
title: OID_PM_REMOVE_PROTOCOL_OFFLOAD
description: As a set request, NDIS and protocol drivers use the OID_PM_REMOVE_PROTOCOL_OFFLOAD OID to remove a power management protocol offload from a network adapter.
ms.assetid: efca3018-28bf-4d91-b698-4b1c9e02f6e3
ms.date: 08/08/2017
keywords: 
 -OID_PM_REMOVE_PROTOCOL_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PM\_REMOVE\_PROTOCOL\_OFFLOAD


As a set request, NDIS and protocol drivers use the OID\_PM\_REMOVE\_PROTOCOL\_OFFLOAD OID to remove a power management protocol offload from a network adapter. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a **ULONG** protocol offload identifier.

Remarks
-------

NDIS and protocol drivers use the OID\_PM\_REMOVE\_PROTOCOL\_OFFLOAD OID to remove a protocol offload from the underlying network adapter.

The **DATA.SET\_INFORMATION.InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure must point to a **ULONG** value for a previously added protocol offload identifier. NDIS sets this protocol offload identifier in the **ProtocolOffloadId** member of the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure when NDIS sent the prior [OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](oid-pm-add-protocol-offload.md) OID request to the underlying network adapter.

### Remarks for miniport driver writers

NDIS ensures that the buffer size is at least **sizeof**(**ULONG**) and contains a valid protocol offload ID. Therefore, a miniport driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function should return NDIS\_STATUS\_SUCCESS for this request.

**Note**  If the miniport driver is resetting, its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function should return NDIS\_STATUS\_NOT\_ACCEPTED.

 

### Return status codes

NDIS returns one of the following status codes for this request:

<a href="" id="ndis-status-success"></a>**NDIS\_STATUS\_SUCCESS**  
The protocol offload was removed successfully.

<a href="" id="ndis-status-pending"></a>**NDIS\_STATUS\_PENDING**  
The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-invalid-length"></a>**NDIS\_STATUS\_INVALID\_LENGTH**  
The information buffer is too small. NDIS sets the **DATA.SET\_INFORMATION.BytesNeeded** member in the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required, in bytes.

<a href="" id="ndis-status-file-not-found"></a>**NDIS\_STATUS\_FILE\_NOT\_FOUND**  
The protocol offload identifier in the OID request is not valid.

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
<td><p>Supported in NDIS 6.20 and later. Mandatory for miniport drivers.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760)

[OID\_PM\_ADD\_PROTOCOL\_OFFLOAD](oid-pm-add-protocol-offload.md)

 

 




