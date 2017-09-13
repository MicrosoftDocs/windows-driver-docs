---
title: OID\_PM\_REMOVE\_PROTOCOL\_OFFLOAD
author: windows-driver-content
description: As a set request, NDIS and protocol drivers use the OID\_PM\_REMOVE\_PROTOCOL\_OFFLOAD OID to remove a power management protocol offload from a network adapter.
ms.assetid: efca3018-28bf-4d91-b698-4b1c9e02f6e3
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_PM_REMOVE_PROTOCOL_OFFLOAD Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PM_REMOVE_PROTOCOL_OFFLOAD%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


