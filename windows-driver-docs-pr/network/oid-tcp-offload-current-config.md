---
title: OID_TCP_OFFLOAD_CURRENT_CONFIG
description: This topic describes the OID_TCP_OFFLOAD_CURRENT_CONFIG object identifier (OID). 
ms.assetid: 8DC81A41-1E4D-4F78-80D1-54C79F974CE3
keywords:
- OID_TCP_OFFLOAD_CURRENT_CONFIG, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# OID_TCP_OFFLOAD_CURRENT_CONFIG

As a query request, administrative applications (or possibly overlying drivers) use the OID_TCP_OFFLOAD_CURRENT_CONFIG OID to determine the current task offload configuration settings of an underlying miniport adapter. A system administrator can use this OID through the Microsoft Windows Management Instrumentation (WMI) interface.

Set requests are not supported.

## Remarks

NDIS handles this OID for miniport drivers. Miniport drivers report miniport adapter offload capabilities to NDIS. For information about passing task offload configuration settings to NDIS from a miniport driver and from NDIS to overlying drivers, see NDIS_OFFLOAD.

The **InformationBuffer** member of the [NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure. The **NDIS_OFFLOAD** structure includes the following miniport adapter capabilities:

- The header information, which includes the task offload version.
- The checksum offload information, in an [NDIS_TCP_IP_CHECKSUM_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff567878) structure.
- The large send offload version 1 (LSOV1) information, in an [NDIS_TCP_LARGE_SEND_OFFLOAD_V1](https://msdn.microsoft.com/library/windows/hardware/ff567883) structure.
- The Internet protocol security (IPsec) information, in an [NDIS_IPSEC_OFFLOAD_V1](https://msdn.microsoft.com/library/windows/hardware/ff565796) structure.
- The large send offload version 2 (LSOV2) information, in an [NDIS_TCP_LARGE_SEND_OFFLOAD_V2](https://msdn.microsoft.com/library/windows/hardware/ff567884) structure.

In response to OID_TCP_OFFLOAD_CURRENT_CONFIG, the **Encapsulation** members of the structures in the preceding list define the packet encapsulation capabilities of the miniport adapter. NDIS provides a bitwise OR of the flags that are provided in the **Encapsulation** members of these structures. The other structure members contain settings for various offload services. For more information about encapsulation and other capabilities, see [NDIS_TCP_IP_CHECKSUM_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff567878), [NDIS_TCP_LARGE_SEND_OFFLOAD_V1](https://msdn.microsoft.com/library/windows/hardware/ff567883), [NDIS_IPSEC_OFFLOAD_V1](https://msdn.microsoft.com/library/windows/hardware/ff565796), and [NDIS_TCP_LARGE_SEND_OFFLOAD_V2](https://msdn.microsoft.com/library/windows/hardware/ff567884).

Miniport adapters must support Ethernet encapsulation for all of the types of task offload that they support. The other types of encapsulation are optional.

Miniport drivers should automatically enable all of the task offload capabilities during initialization.

### See also

[NDIS_IPSEC_OFFLOAD_V1](https://msdn.microsoft.com/library/windows/hardware/ff565796)  
[NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599)  
[NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)  
[NDIS_TCP_IP_CHECKSUM_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff567878)  
[NDIS_TCP_LARGE_SEND_OFFLOAD_V2](https://msdn.microsoft.com/library/windows/hardware/ff567884)    
[NDIS_IPSEC_OFFLOAD_V1](https://msdn.microsoft.com/library/windows/hardware/ff565796)  

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

