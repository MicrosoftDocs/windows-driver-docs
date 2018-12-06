---
title: OID_TCP_TASK_OFFLOAD
description: This topic describes the OID_TCP_TASK_OFFLOAD object identifier (OID).
ms.assetid: 4e16cdb7-b899-43b6-a94b-d691622be105
keywords:
- OID_TCP_TASK_OFFLOAD
ms.date: 11/06/2017
ms.localizationpriority: medium
---

# OID_TCP_TASK_OFFLOAD

The host stack queries the OID_TCP_TASK_OFFLOAD OID to obtain the TCP offload capabilities of a miniport driver's NIC or of an offload target. After determining the offload capabilities that a NIC or an offload target supports, the host stack sets this OID to enable one or more of the reported capabilities. The host stack can also disable all of a NIC's or an offload target's TCP offload capabilities by setting OID_TCP_TASK_OFFLOAD. Only one protocol at a time can enable the TCP offload capabilities of a particular NIC.

## Querying offload capabilities

When the host stack queries OID_TCP_TASK_OFFLOAD, it supplies in the *InformationBuffer* an [NDIS_TASK_OFFLOAD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff559004) structure. This structure specifies the following:

- The offload version supported by the host stack.
- The encapsulation format for send and receive packets processed by the host stack.
- The size of the encapsulation header in such packets.

With this information, a miniport driver or its NIC can locate the beginning of the first IP header in a transmit packet, which is a prerequisite for performing an offload task. An offload target needs to know the encapsulation format to process receive packets. In response to a query of OID_TCP_TASK_OFFLOAD, a miniport driver or offload target returns, in the *InformationBuffer*, the NDIS_TASK_OFFLOAD_HEADER structure followed immediately by one or more [NDIS_TASK_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff558995) structures. Each NDIS_TASK_OFFLOAD structure describes an offload capability supported by the miniport driver's NIC or by the offload target. If the miniport driver's NIC or the offload target supports multiple versions of a particular offload capability, it should return one NDIS_TASK_OFFLOAD structure for each version.

Each NDIS_TASK_OFFLOAD structure has a **Task** member that specifies the particular offload capability to which the structure applies. Each NDIS_TASK_OFFLOAD structure also has a **TaskBuffer** that contains information pertinent to the specified offload capability. The information in the **TaskBuffer** is formatted as one of the following structures:

- [NDIS_TASK_TCP_IP_CHECKSUM](https://msdn.microsoft.com/library/windows/hardware/ff559004)  
    Specifies checksum offload capabilities.
- [NDIS_TASK_IPSEC](https://msdn.microsoft.com/library/windows/hardware/ff558990)  
    Specifies Internet Protocol security (IPsec) offload capabilities.
- [NDIS_TASK_TCP_LARGE_SEND](https://msdn.microsoft.com/library/windows/hardware/ff559008)  
    Specifies large TCP packet segmentation capabilities.
- [NDIS_TASK_TCP_CONNECTION_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff567873)  
    Specifies TCP chimney offload capabilities. For more information on NDIS_TASK_TCP_CONNECTION_OFFLOAD, see [TCP Chimney Offload](ndis-tcp-chimney-offload.md).

> [!NOTE]
> If an intermediate driver modifies the contents of packets that it forwards to an underlying miniport driver such that TCP offload functions cannot be performed on the packets, the intermediate driver should respond to OID_TCP_TASK_OFFLOAD queries with a status of NDIS_STATUS_NOT_SUPPORTED instead of passing the OID request to the underlying miniport driver or offload target.

## Enabling offload capabilities

After querying a NIC's or an offload target's offload capabilities, the host stack enables one or more of these capabilities by setting OID_TCP_TASK_OFFLOAD. When setting OID_TCP_TASK_OFFLOAD, the host stack supplies, in the *InformationBuffer*, an NDIS_TASK_OFFLOAD_HEADER structure followed immediately by an NDIS_TASK_OFFLOAD structure for each offload capability that the host stack is enabling.

The **Task** in each NDIS_TASK_OFFLOAD structure indicates the offload capability that the host stack is enabling. The host stack also enables specific aspects of a particular offload capability by setting members of the structure in the **TaskBuffer** of each NDIS_TASK_OFFLOAD structure.

## Changing offload capabilities 

To change the offload capabilities that are enabled for a NIC or an offload target, the host stack sets OID_TCP_TASK_OFFLOAD. The miniport driver or offload target must enable only those offload capabilities specified by the most recent set of OID_TCP_TASK_OFFLOAD. The miniport driver or offload target must disable all other offload capabilities. Note that before disabling a specific TCP chimney offload capability, the host stack terminates the offload of any offloaded TCP connections that use that capability.

An offload target can use pause or resume offload indications to change its reported TCP offload capabilities:

- An offload target makes a pause indication by calling the [NdisMIndicateStatusEx](https://msdn.microsoft.com/library/windows/hardware/ff563600) function with the NDIS_STATUS_INDICATION->**StatusCode** member set to NDIS_STATUS_OFFLOAD_PAUSE.
- An offload target makes a resume indication by calling the **NdisMIndicateStatusEx** function with the NDIS_STATUS_INDICATION->**StatusCode** member set to NDIS_STATUS_OFFLOAD_RESUME.

After an offload target requests the host stack to resume offloading state objects, the host stack queries OID_TCP_TASK_OFFLOAD again to obtain the offload target's TCP offload revised capabilities. For more information, see [NDIS_STATUS_OFFLOAD_RESUME](https://msdn.microsoft.com/library/windows/hardware/ff567405).

## Disabling offload capabilities

To disable all offload capabilities supported by a NIC or an offload target, the host stack sets OID_TCP_TASK_OFFLOAD. In the *InformationBuffer*, the host stack supplies an NDIS_TASK_OFFLOAD_HEADER structure with the **OffsetFirstTask** member of this structure set to zero.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

