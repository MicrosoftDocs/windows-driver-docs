---
title: OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES
description: This topic describes the OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES object identifier (OID). 
keywords:
- OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES

As a query request, the OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES OID reports the task offload hardware capabilities of a miniport adapter's hardware. User-mode applications (or possibly overlying drivers) can query this OID to determine the task offload hardware capabilities of an underlying miniport adapter. A system administrator can use this OID through the Windows Management Instrumentation (WMI) interface.

Set requests are not supported.

## Remarks

NDIS handles this OID for miniport drivers. Miniport drivers report miniport adapter hardware capabilities to NDIS. For information about reporting task offload hardware capabilites to NDIS from a miniport driver and from NDIS to overlying drivers, see [NDIS_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload).

The **InformationBuffer** member of the [NDIS_OID_REQUEST](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains an [NDIS_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure. NDIS returns NDIS_STATUS_BUFFER_TOO_SHORT if the buffer is not big enough.

After determining the miniport adapter's hardware capabilities, the overlying applications or drivers can use the [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md) OID to enable capabilities that are currently reported as not enabled by the [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md) OID.

### See also

[NDIS_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload)  
[NDIS_OID_REQUEST](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)  
[OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md)  
[OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md)  

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
