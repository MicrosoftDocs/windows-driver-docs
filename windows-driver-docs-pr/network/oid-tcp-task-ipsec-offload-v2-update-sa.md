---
title: OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA
author: windows-driver-content
description: As a set, the TCP/IP transport uses the OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA OID to request that a miniport driver update the specified security associations (SAs) on a NIC.
ms.assetid: 22849103-9148-4621-b78f-b9f34f2c7ac1
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA Network Drivers Starting with Windows Vista
---

# OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA


\[The IPsec Task Offload feature is deprecated and should not be used.\]

As a set, the TCP/IP transport uses the OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA OID to request that a miniport driver update the specified security associations (SAs) on a NIC.

**Note**  NDIS supports this OID with the direct OID request interface. For more information about the direct OID request interface, see [NDIS 6.1 Direct OID Request Interface](ndis-6-1-direct-oid-request-interface.md).

 

Remarks
-------

All NDIS 6.1 miniport drivers that support IPsec offload version 2 (IPsecOV2) must support this OID.

When a miniport driver receives this request, the driver should update the specified SAs on the NIC. The miniport driver can fail this request if the SA is not found or the ESN is not supported. In this case, the returned status should be NDIS\_STATUS\_INVALID\_PARAMETER.

The miniport driver receives an [**IPSEC\_OFFLOAD\_V2\_UPDATE\_SA**](ipsec-offload-v2-update-sa.md) structure that contains information about the update and a pointer to the next IPSEC\_OFFLOAD\_V2\_UPDATE\_SA structure in a linked list.

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
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**IPSEC\_OFFLOAD\_V2\_UPDATE\_SA**](ipsec-offload-v2-update-sa.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


