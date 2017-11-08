---
title: OID_TCP6_OFFLOAD_STATS
author: windows-driver-content
description: This topic describes the OID_TCP6_OFFLOAD_STATS object identifier (OID).
ms.assetid: d7da8dd0-8de0-4283-9ecf-94e3d1503abe
keywords:
- OID_TCP6_OFFLOAD_STATS
ms.author: windowsdriverdev
ms.date: 11/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_TCP6_OFFLOAD_STATS

The host stack queries the OID_TCP6_OFFLOAD_STATS OID to obtain statistics on TCP segments that an offload target has processed on offloaded TCP connections that convey IPv6 datagrams. The host stack sets this OID to cause an offload target to reset the counters for such statistics to zero.

In response to a query of OID_TCP6_OFFLOAD_STATS, an offload target supplies a filled-in [TCP_OFFLOAD_STATS](https://msdn.microsoft.com/library/windows/hardware/ff570940) structure.

In response to a set of OID_TCP6_OFFLOAD_STATS, an offload target should reset to zero all of its TCP statistics counters for offloaded TCP connections that convey IPv6 datagrams.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")