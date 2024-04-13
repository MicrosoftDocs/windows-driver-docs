---
title: OID_TCP6_OFFLOAD_STATS
ms.topic: reference
description: This topic describes the OID_TCP6_OFFLOAD_STATS object identifier (OID).
keywords:
- OID_TCP6_OFFLOAD_STATS
ms.date: 11/06/2017
---

# OID_TCP6_OFFLOAD_STATS

The host stack queries the OID_TCP6_OFFLOAD_STATS OID to obtain statistics on TCP segments that an offload target has processed on offloaded TCP connections that convey IPv6 datagrams. The host stack sets this OID to cause an offload target to reset the counters for such statistics to zero.

In response to a query of OID_TCP6_OFFLOAD_STATS, an offload target supplies a filled-in [TCP_OFFLOAD_STATS](/windows-hardware/drivers/ddi/ndischimney/ns-ndischimney-_tcp_offload_stats) structure.

In response to a set of OID_TCP6_OFFLOAD_STATS, an offload target should reset to zero all of its TCP statistics counters for offloaded TCP connections that convey IPv6 datagrams.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
