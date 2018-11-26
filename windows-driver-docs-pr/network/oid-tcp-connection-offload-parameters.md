---
title: OID_TCP_CONNECTION_OFFLOAD_PARAMETERS
description: This topic describes the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS object identifier (OID). 
ms.assetid: 6481D565-900A-4B75-A60F-72701FB45FAD
keywords:
- OID_TCP_CONNECTION_OFFLOAD_PARAMETERS, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# OID_TCP_CONNECTION_OFFLOAD_PARAMETERS

As a query request, overlying drivers can use the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OID to determine the current connection offload settings of an underlying miniport adapter. NDIS handles this OID query for miniport drivers.

As a set request, NDIS and overlying drivers use the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OID to set the connection offload configuration parameters of an underlying miniport adapter. Miniport drivers that support connection offload must handle this OID set request. Otherwise, the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OID is optional for miniport drivers.

## Remarks

The **InformationBuffer** member of the [NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff567876) structure.

> [!NOTE]
> Do not confuse OID_TCP_CONNECTION_OFFLOAD_PARAMETERS with the [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md) OID that administrative applications use to enable or disable TCP offload features.

### See also

[NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)  
[OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md)

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

