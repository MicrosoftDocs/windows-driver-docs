---
title: OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA
description: As a set, the TCP/IP transport uses the OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA OID to request that a miniport driver update the specified security associations (SAs) on a NIC.
ms.assetid: 22849103-9148-4621-b78f-b9f34f2c7ac1
ms.date: 08/08/2017
keywords: 
 -OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA


\[The IPsec Task Offload feature is deprecated and should not be used.\]

As a set, the TCP/IP transport uses the OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA OID to request that a miniport driver update the specified security associations (SAs) on a NIC.

**Note**  NDIS supports this OID with the direct OID request interface. For more information about the direct OID request interface, see [NDIS 6.1 Direct OID Request Interface](https://msdn.microsoft.com/library/windows/hardware/ff564736).

 

Remarks
-------

All NDIS 6.1 miniport drivers that support IPsec offload version 2 (IPsecOV2) must support this OID.

When a miniport driver receives this request, the driver should update the specified SAs on the NIC. The miniport driver can fail this request if the SA is not found or the ESN is not supported. In this case, the returned status should be NDIS\_STATUS\_INVALID\_PARAMETER.

The miniport driver receives an [**IPSEC\_OFFLOAD\_V2\_UPDATE\_SA**](https://msdn.microsoft.com/library/windows/hardware/ff556990) structure that contains information about the update and a pointer to the next IPSEC\_OFFLOAD\_V2\_UPDATE\_SA structure in a linked list.

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


[**IPSEC\_OFFLOAD\_V2\_UPDATE\_SA**](https://msdn.microsoft.com/library/windows/hardware/ff556990)

 

 




