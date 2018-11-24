---
title: OID_TCP_OFFLOAD_PARAMETERS
description: This topic describes the OID_TCP_OFFLOAD_PARAMETERS object identifier (OID). 
ms.assetid: 5D9B5F62-E506-4983-B247-A93B81E70A43
keywords:
- OID_TCP_OFFLOAD_PARAMETERS, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# OID_TCP_OFFLOAD_PARAMETERS

Query requests are not supported.

As a set request, the OID_TCP_OFFLOAD_PARAMETERS OID sets the current TCP offload configuration of a miniport adapter. Protocol drivers or user-mode applications can set this OID to change the current TCP offload configuration. A system administrator can use this OID through the Microsoft Windows Management Instrumentation (WMI) interface.

## Remarks

OID_TCP_OFFLOAD_PARAMETERS is required for miniport drivers that support TCP offloads and optional for other miniport drivers. If a miniport driver does not support this OID, the driver should return NDIS_STATUS_NOT_SUPPORTED.

The **InformationBuffer** member of the [NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [NDIS_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure. If the contents of **InformationBuffer** are invalid, the miniport driver should return NDIS_STATUS_INVALID_DATA in response to this OID.

While NDIS processes this OID and before it passes the OID to the miniport driver, NDIS updates the miniport adapter's offload standardized keywords with the new settings.

Miniport drivers must use the contents of the [NDIS_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure to update the currently reported TCP offload capabilities. After the update, the miniport driver must report the current task offload capabilities with the [NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md) status indication. This status indication ensures that all of the overlying protocol drivers are updated with the new capabilities information.

This OID is a more comprehensive OID that instructs miniport drivers to turn certain offloads on or off. Most TCP/IP task offloads can be configured and activated with this OID. For some offloads, such as Rx Checksum or Rx IPSec, this OID serves as a configuration change and doesn't mean the offload will be operational immediately. To activate those offloads, the miniport driver must wait until it receives an [OID_OFFLOAD_ENCAPSULATION](oid-offload-encapsulation.md) Set request.

Before setting OID_TCP_OFFLOAD_PARAMETERS, the overlying applications or drivers can use the [OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](oid-tcp-offload-hardware-capabilities.md) OID to determine what capabilities a miniport adapter's hardware can support. Use OID_TCP_OFFLOAD_PARAMETERS to enable capabilities that are reported as not enabled by the [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md) OID.

### See also

[NDIS_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff566706)  
[NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)  
[NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md)  
[OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md)  
[OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](oid-tcp-offload-hardware-capabilities.md)

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

