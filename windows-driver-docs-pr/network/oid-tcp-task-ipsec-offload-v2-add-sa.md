---
title: OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA
description: As a set, the TCP/IP transport uses the OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA OID to request that a miniport driver add the specified security associations (SAs) to a NIC.
ms.assetid: bd1d0cf2-234d-4c06-904e-fe2de6022981
ms.date: 08/08/2017
keywords: 
 -OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA


\[The IPsec Task Offload feature is deprecated and should not be used.\]

As a set, the TCP/IP transport uses the OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA OID to request that a miniport driver add the specified security associations (SAs) to a NIC.

**Note**  NDIS supports this OID with the direct OID request interface. For more information about the direct OID request interface, see [NDIS 6.1 Direct OID Request Interface](https://msdn.microsoft.com/library/windows/hardware/ff564736).

 

**Note**  This OID is supported in NDIS 6.1 and 6.20. For NDIS 6.30 and later drivers see [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA\_EX](oid-tcp-task-ipsec-offload-v2-add-sa-ex.md).

 

Remarks
-------

All NDIS 6.1 and 6.20 miniport drivers that support IPsec offload version 2 (IPsecOV2) must support this OID.

After TCP/IP transport determines that a NIC can perform IPsecOV2 operations, the TCP/IP transport requests the miniport driver to add SAs. The transport cannot offload IPsecOV2 operations to the NIC before the transport adds an SA.

The miniport driver receives an [**IPSEC\_OFFLOAD\_V2\_ADD\_SA**](https://msdn.microsoft.com/library/windows/hardware/ff556977) structure that contains a pointer to the next IPSEC\_OFFLOAD\_V2\_ADD\_SA structure in a linked list. The miniport driver configures the NIC for IPsecOV2 processing on the SAs. With a successful set to OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA, the miniport driver supplies the handles that identify the offloaded SAs in the **OffloadHandle** member of IPSEC\_OFFLOAD\_V2\_ADD\_SA. (For example, the transport uses the handle in the send path to indicate which offloaded SA to use). If any of the SAs in the linked list were offloaded, the set request is successful.

The miniport driver can return a failure status for the OID request, for example, when the NIC runs out of capacity to offload more SAs. Also, the miniport driver might return a failure status because it needs to avoid a race condition. In this case, the NIC configuration changes and excludes a particular algorithm.

If the request fails, none of the SAs in the linked list were offloaded. If failure occurs for a particular SA in the linked list, the miniport driver should set the **OffloadHandle** member in the corresponding IPSEC\_OFFLOAD\_V2\_ADD\_SA structure to **NULL**.

The miniport driver reports the maximum number of SAs that a NIC can support in the **SaOffloadCapacity** member of the [**NDIS\_IPSEC\_OFFLOAD\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff565808) structure during initialization. If necessary, the TCP/IP transport can set the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA](oid-tcp-task-ipsec-offload-v2-delete-sa.md) OID to request that the miniport driver delete an SA from the NIC.

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
<td><p>Supported in NDIS 6.1 and 6.20. For NDIS 6.30 and later, use <a href="oid-tcp-task-ipsec-offload-v2-add-sa-ex.md" data-raw-source="[OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA_EX](oid-tcp-task-ipsec-offload-v2-add-sa-ex.md)">OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA_EX</a>.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**IPSEC\_OFFLOAD\_V2\_ADD\_SA**](https://msdn.microsoft.com/library/windows/hardware/ff556977)

[**NDIS\_IPSEC\_OFFLOAD\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff565808)

[OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA\_EX](oid-tcp-task-ipsec-offload-v2-add-sa-ex.md)

[OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA](oid-tcp-task-ipsec-offload-v2-delete-sa.md)

 

 




