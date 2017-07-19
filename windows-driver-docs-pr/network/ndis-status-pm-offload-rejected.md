---
title: NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED
author: windows-driver-content
description: The NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED status indicates to overlying drivers that a power management protocol offload was rejected.
ms.assetid: 54922e70-2b56-4141-b79b-73418c7553e3
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_PM_OFFLOAD_REJECTED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED


The NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED status indicates to overlying drivers that a power management protocol offload was rejected.

Remarks
-------

NDIS or miniport drivers can generate the NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED status indication when either of them removes an offloaded protocol. The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains a ULONG for the protocol offload identifier of the rejected protocol offload. NDIS provided the protocol offload identifier in the **ProtocolOffloadId** member of the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure.

NDIS generates an NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED status indication when it has to remove a previously offloaded protocol from a network adapter. For example, NDIS might remove the protocol offload to free resources for a higher priority protocol offload. NDIS sends the status indication to the binding that offloaded the rejected protocol offload, but does not send it to other bindings.

Miniport drivers report this status indication to reject a previously accepted protocol offload. For example, for a WiFi WOL case, the miniport driver must make an NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED status indication when PTK/GTK rotation is not required to support WOL (due to vendor specific infrastructure support).

For wireless network adapters that use infrastructure elements to offload protocols and roam across the infrastructure, it is possible that a new infrastructure element might not support the same capabilities as the previous one. In this case, the miniport driver can issue a status indication to NDIS, and NDIS will issue NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED with a specific error code.

A WiFi driver might cache protocol offload requests locally. When the driver processes an OID for adding or deleting a protocol offload, the driver can choose to only update its local cache. The driver can defer the update of the infrastructure until it receives the [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768) OID.

The infrastructure might not have enough resources to accommodate all of the protocol offloads. In this case, the infrastructure can accept a partial list of the protocol offloads. When the miniport driver completes the OID\_PM\_PARAMETERS set request, the miniport driver must make NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED status indications for each of the protocol offloads that the AP rejects.

For example, a network adapter can use the AP's proxy ARP to support ARP offload.

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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_PM_OFFLOAD_REJECTED%20%20RELEASE:%20%287/6/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


