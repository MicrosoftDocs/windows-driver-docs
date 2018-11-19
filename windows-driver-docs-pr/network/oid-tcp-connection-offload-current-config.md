---
title: OID_TCP_CONNECTION_OFFLOAD_CURRENT_CONFIG
description: This topic describes the OID_TCP_CONNECTION_OFFLOAD_CURRENT_CONFIG object identifier (OID). 
ms.assetid: 29CB74B1-8D7F-4EC2-AAAC-93D454824031
keywords:
- OID_TCP_CONNECTION_OFFLOAD_CURRENT_CONFIG, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# OID_TCP_CONNECTION_OFFLOAD_CURRENT_CONFIG

As a query request, administrative applications (or possibly overlying drivers) can use the OID_TCP_CONNECTION_OFFLOAD_CURRENT_CONFIG OID to determine the currently-enabled connection offload capabilities of an underlying miniport adapter. A system administrator can use this OID through the Microsoft Windows Management Instrumentation (WMI) interface.

Set requests are not supported.

## Remarks

NDIS handles this OID for miniport drivers. Miniport drivers report miniport adapter connection offload settings to NDIS. For information about passing connection offload configuration settings to NDIS from a miniport driver and from NDIS to overlying drivers, see [NDIS_TCP_CONNECTION_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff567875).

The **InformationBuffer** member of the [NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [NDIS_TCP_CONNECTION_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff567875) structure.

In response to OID_TCP_CONNECTION_OFFLOAD_CURRENT_CONFIG, the **Encapsulation** member of NDIS_TCP_CONNECTION_OFFLOAD defines the current packet encapsulation configuration of the miniport adapter. NDIS provides a bitwise OR of the flags that are provided in the **Encapsulation** member. The other members of NDIS_TCP_CONNECTION_OFFLOAD contain settings for various connection offload services. For more information about encapsulation and other capabilities, see [NDIS_TCP_CONNECTION_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff567875) and [NDIS_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff566706).


### See also

[NDIS_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff566706)  
[NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)  
[NDIS_TCP_CONNECTION_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff567875)

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

