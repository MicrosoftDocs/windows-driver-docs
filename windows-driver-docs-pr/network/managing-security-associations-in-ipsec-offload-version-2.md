---
title: Managing Security Associations in IPsec Offload Version 2
description: Managing Security Associations in IPsec Offload Version 2
ms.assetid: aaa352c1-fb70-4c96-adda-9710347e2442
keywords:
- IPsecOV2 WDK TCP/IP transport , security associations
- security associations WDK IPsec offload
- SAs WDK IPsec offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Security Associations in IPsec Offload Version 2

\[The IPsec Task Offload feature is deprecated and should not be used.\]




After the TCP/IP transport determines that a NIC can perform IPsec offload version 2 (IPsecOV2) operations (see [Reporting a NIC's IPsec Offload Version 2 Capabilities](reporting-a-nic-s-ipsec-offload-version-2-capabilities.md)), the transport requests that the NIC's miniport driver add one or more security associations (SAs) to the NIC before the transport can offload IPsec tasks to the NIC. After adding SAs, the TCP/IP transport can also delete or update them. The IPsecOV2 interface requires the NDIS direct OID interface for add, delete, and update OIDs.

**Note**  NDIS provides a direct OID request interface for NDIS 6.1 and later drivers. The [direct OID request path](https://msdn.microsoft.com/library/windows/hardware/ff564736) supports OID requests that are queried or set frequently.

 

To request that a miniport driver add one or more SAs to a NIC, the TCP/IP transport sets the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812) OID. The miniport driver receives an [**IPSEC\_OFFLOAD\_V2\_ADD\_SA**](https://msdn.microsoft.com/library/windows/hardware/ff556977) structure and configures the NIC for IPsecOV2 processing on an SA. With a successful set to OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA, the miniport driver initializes a handle that identifies the offloaded SA in the IPSEC\_OFFLOAD\_V2\_ADD\_SA structure. The transport uses this handle in subsequent requests to the miniport driver (that is, on the send path or in the calls to modify or delete the SA). For more information about using the SA handle in the send path, see [Sending Network Data with IPsec Offload Version 2](sending-network-data-with-ipsec-offload-version-2.md).

The miniport driver reports the number of SAs that a NIC can support in the **SaOffloadCapacity** member of the [**NDIS\_IPSEC\_OFFLOAD\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff565808) structure.

The miniport driver can set the **SaDeleteReq** flag in the [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818) structure for a receive packet. The TCP/IP transport subsequently issues [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569813) one time to delete the inbound SA that the packet was received over and one time again to delete the outbound SA that corresponds to the deleted inbound SA.

The TCP/IP transport issues [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569813) to delete an inbound SAs over which a packet was received and to delete the outbound SAs that correspond to the deleted inbound SAs. A NIC must not remove these SAs before it receives the corresponding OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA request.

The TCP/IP transport sets the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569814) OID to request that a miniport driver update a NIC with the higher order bits for an SA with extended sequence numbers (ESN). For NICs that support ESN, when the miniport driver receives this request, the driver should update the sequence number of the specified SA in the NIC in accordance with the [**IPSEC\_OFFLOAD\_V2\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff556984) enumeration value that is specified in the **Operation** member of the [**IPSEC\_OFFLOAD\_V2\_UPDATE\_SA**](https://msdn.microsoft.com/library/windows/hardware/ff556990) structure.

 

 





