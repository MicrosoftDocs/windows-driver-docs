---
title: OID_TCP_TASK_IPSEC_ADD_SA
author: windows-driver-content
description: This topic describes the OID_TCP_TASK_IPSEC_ADD_SA object identifier (OID).
ms.assetid: 7062c0df-627c-4110-a69f-ebad60f4e3b8
keywords:
- OID_TCP_TASK_IPSEC_ADD_SA
ms.author: windowsdriverdev
ms.date: 11/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_TCP_TASK_IPSEC_ADD_SA

The OID_TCP_TASK_IPSEC_ADD_SA OID is set by the transport protocol to request that a miniport driver add one or more security associations (SAs) to a NIC.

The information for each SA is formatted as an [OFFLOAD_IPSEC_ADD_SA](https://msdn.microsoft.com/library/windows/hardware/ff569056) structure.

The first seven members of the OFFLOAD_IPSEC_ADD_SA structure (**SrcAddr**, **SrcMask**, **DestAddr**, **DestMask**, **Protocol**, **SrcPort**, and **DestPort**) constitute a filter that specifies the source and destination, as well as the IP protocols, to which the SAs apply. This filter pertains to a transport-mode connection--that is, an end-to-end connection between two hosts. If the specified connection is made through a tunnel, the source and destination addresses of the tunnel are specified by **SrcTunnelAddr** and **DestTunnelAddr**, respectively.

If a filter parameter is set to zero, that parameter is not used to filter packets for the specified SAs. For example, if **SrcAddr** is set to zero, the specified SAs can apply to a packet that contains any source address. To take this to the extreme, if all the filter parameters are set to zero, the specified SAs apply to any source host sending any type of packet to any destination host.

The TCP/IP transport can specify an IP protocol in the **Protocol** member to indicate that the specified SAs apply only to packets of the specified protocol type. If **Protocol** is set to zero, the specified SAs apply to all packets sent from the specified source to the specified destination.

## OFFLOAD_SECURITY_ASSOCIATION structure

An [OFFLOAD_SECURITY_ASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff569061) structure specifies a single security association (SA). The OFFLOAD_SECURITY_ASSOCIATION structure is an element in the **SecAssoc** variable-length array. **SecAssoc** contains one or two OFFLOAD_SECURITY_ASSOCIATION structures.

An SA specified for use in processing authentication headers (AH) will have an operation type of **AUTHENTICATE** and will have an **IntegrityAlgo** (integrity algorithm). The SA will not have an a **ConfAlgo** (confidentiality algorithm). In this case, **ConfAlgo** will contain zeros.

An SA specified for use in processing encapsulating security payloads (ESPs) will have an operation type of **ENCRYPT** and may have an **IntegrityAlgo** (integrity algorithm) and/or a **ConfAlgo** (confidentiality algorithm).

## OFFLOAD_ALGO_INFO structure

The [OFFLOAD_ALGO_INFO](https://msdn.microsoft.com/library/windows/hardware/ff568842) structure, which is a member of an [OFFLOAD_SECURITY_ASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff569061) structure, specifies an algorithm used for a security association (SA).

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")