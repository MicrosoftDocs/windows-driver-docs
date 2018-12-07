---
title: OID_IP4_OFFLOAD_STATS
description: This topic describes the OID_IP4_OFFLOAD_STATS object identifier (OID).
ms.assetid: 7ffe9703-5370-410f-bccd-4a430835edd0
keywords:
- OID_IP4_OFFLOAD_STATS
ms.date: 11/06/2017
ms.localizationpriority: medium
---

# OID_IP4_OFFLOAD_STATS

The host stack queries the OID_IP4_OFFLOAD_STATS OID to obtain statistics on IPv4 datagrams that an offload target has processed on offloaded TCP connections. The host stack sets this OID to cause an offload target to reset the counters for such statistics to zero.

In response to a query of OID_IP4_OFFLOAD_STATS, an offload target supplies a filled-in [IP_OFFLOAD_STATS](https://msdn.microsoft.com/library/windows/hardware/ff557022) structure. The IP_OFFLOAD_STATS structure contains the statistics for IPv4 datagrams processed on offloaded TCP connections.

In response to a set of OID_IP4_OFFLOAD_STATS, an offload target should reset all of its IPv4 statistics counters for offloaded TCP connections to zero.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

