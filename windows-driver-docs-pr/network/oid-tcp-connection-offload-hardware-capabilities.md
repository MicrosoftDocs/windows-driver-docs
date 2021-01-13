---
title: OID_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES
description: This topic describes the OID_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES object identifier (OID). 
keywords:
- OID_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# OID_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES

As a query request, the OID_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES OID reports the current connection offload hardware capabilities of an underlying miniport adapter. User-mode applications (or possibly overlying drivers) can query this OID to determine the connection offload hardware capabilities of an underlying miniport adapter. A system administrator can use this OID through the Microsoft Windows Management Instrumentation (WMI) interface.

Set requests are not supported.

## Remarks

NDIS handles this OID for miniport drivers. Miniport drivers report miniport adapter connection offload hardware capabilities to NDIS. For information about passing connection offload hardware capabilities to NDIS from a miniport driver and from NDIS to overlying drivers, see [NDIS_TCP_CONNECTION_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_connection_offload).

The **InformationBuffer** member of the [NDIS_OID_REQUEST](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains an [NDIS_TCP_CONNECTION_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_connection_offload) structure.

In response to OID_TCP_CONNECTION_OFFLOAD_HARDWARE_CAPABILITIES, the **Encapsulation** member of NDIS_TCP_CONNECTION_OFFLOAD defines the current packet encapsulation hardware capabilities of the miniport adapter. NDIS provides a bitwise OR of the flags that are provided in the **Encapsulation** member. The other members of NDIS_TCP_CONNECTION_OFFLOAD contain settings for various connection offload services. For more information about encapsulation and other capabilities, see [NDIS_TCP_CONNECTION_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_connection_offload) and [NDIS_OFFLOAD_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload_parameters).


### See also

[NDIS_OFFLOAD_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload_parameters)  
[NDIS_OID_REQUEST](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)  
[NDIS_TCP_CONNECTION_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_connection_offload)

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
