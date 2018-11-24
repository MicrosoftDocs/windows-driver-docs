---
title: OID_IP6_OFFLOAD_STATS
description: This topic describes the OID_IP6_OFFLOAD_STATS object identifier (OID).
ms.assetid: 94bfc254-bc83-481f-a2d7-46c1e31e23a7
keywords:
- OID_IP6_OFFLOAD_STATS
ms.date: 11/06/2017
ms.localizationpriority: medium
---

# OID_IP6_OFFLOAD_STATS

The host stack queries the OID_IP6_OFFLOAD_STATS OID to obtain statistics on IPv6 datagrams that an offload target has processed on offloaded TCP connections. The host stack sets this OID to cause an offload target to reset the counters for such statistics to zero.

In response to a query of OID_IP6_OFFLOAD_STATS, an offload target supplies a filled-in [IP_OFFLOAD_STATS](https://msdn.microsoft.com/library/windows/hardware/ff557022) structure. The IP_OFFLOAD_STATS structure contains the statistics for IPv6 datagrams processed on offloaded TCP connections.

In response to a set of OID_IP6_OFFLOAD_STATS, an offload target should reset all of its IPv6 statistics counters for offloaded TCP connections to zero.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

