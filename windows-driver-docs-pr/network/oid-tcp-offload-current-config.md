---
title: OID_TCP_OFFLOAD_CURRENT_CONFIG
description: This topic describes the OID_TCP_OFFLOAD_CURRENT_CONFIG object identifier (OID). 
keywords:
- OID_TCP_OFFLOAD_CURRENT_CONFIG, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.date: 02/27/2020
ms.localizationpriority: medium
---

# OID_TCP_OFFLOAD_CURRENT_CONFIG

As a query request, administrative applications (or possibly overlying drivers) use the OID_TCP_OFFLOAD_CURRENT_CONFIG OID to determine the current task offload configuration settings of an underlying miniport adapter. A system administrator can use this OID through the Microsoft Windows Management Instrumentation (WMI) interface.

Set requests are not supported.

## Remarks

NDIS handles this OID for miniport drivers. Miniport drivers report miniport adapter offload capabilities to NDIS. For information about passing task offload configuration settings to NDIS from a miniport driver and from NDIS to overlying drivers, see NDIS_OFFLOAD.

The **InformationBuffer** member of the [NDIS_OID_REQUEST](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains an [NDIS_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure. The **NDIS_OFFLOAD** structure includes the following miniport adapter capabilities:

- The header information, which includes the task offload version.
- The checksum offload information, in an [NDIS_TCP_IP_CHECKSUM_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_ip_checksum_offload) structure.
- The large send offload version 1 (LSOV1) information, in an [NDIS_TCP_LARGE_SEND_OFFLOAD_V1](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_large_send_offload_v1) structure.
- The Internet protocol security (IPsec) information, in an [NDIS_IPSEC_OFFLOAD_V1](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ipsec_offload_v1) structure.
- The large send offload version 2 (LSOV2) information, in an [NDIS_TCP_LARGE_SEND_OFFLOAD_V2](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_large_send_offload_v2) structure.

In response to OID_TCP_OFFLOAD_CURRENT_CONFIG, the **Encapsulation** members of the structures in the preceding list define the packet encapsulation capabilities of the miniport adapter. NDIS provides a bitwise OR of the flags that are provided in the **Encapsulation** members of these structures. The other structure members contain settings for various offload services. For more information about encapsulation and other capabilities, see [NDIS_TCP_IP_CHECKSUM_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_ip_checksum_offload), [NDIS_TCP_LARGE_SEND_OFFLOAD_V1](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_large_send_offload_v1), [NDIS_IPSEC_OFFLOAD_V1](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ipsec_offload_v1), and [NDIS_TCP_LARGE_SEND_OFFLOAD_V2](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_large_send_offload_v2).

Miniport adapters must support Ethernet encapsulation for all of the types of task offload that they support. The other types of encapsulation are optional.

Miniport drivers should automatically enable all of the task offload capabilities during initialization.

### See also

[NDIS_IPSEC_OFFLOAD_V1](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ipsec_offload_v1)  
[NDIS_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload)  
[NDIS_OID_REQUEST](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)  
[NDIS_TCP_IP_CHECKSUM_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_ip_checksum_offload)  
[NDIS_TCP_LARGE_SEND_OFFLOAD_V2](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_large_send_offload_v2)
[NDIS_IPSEC_OFFLOAD_V1](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ipsec_offload_v1)  

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
