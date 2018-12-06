---
title: Maintaining and Reporting Chimney-Specific Statistics
description: Maintaining and Reporting Chimney-Specific Statistics
ms.assetid: b50b70e4-70a7-4c4e-860a-af70dab01d38
keywords:
- TCP chimney offload WDK networking , statistics
- chimney offload WDK networking , statistics
- statistics WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Maintaining and Reporting Chimney-Specific Statistics


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target must maintain and, when queried, report the TCP chimney-related statistics about:

-   IPv4 datagrams that the offload target has processed on offloaded TCP connections.

-   IPv6 datagrams that the offload target has processed on offloaded TCP connections.

-   TCP segments that the offload target has processed on offloaded TCP connections that convey IPv4 datagrams.

-   TCP segments that the offload target has processed on offloaded TCP connections that convey IPv6 datagrams.

In response to a query of [OID\_IP4\_OFFLOAD\_STATS](https://msdn.microsoft.com/library/windows/hardware/ff569758) or [OID\_IP6\_OFFLOAD\_STATS](https://msdn.microsoft.com/library/windows/hardware/ff569759), an offload target returns IPv4 or IPv6 statistics in an [**IP\_OFFLOAD\_STATS**](https://msdn.microsoft.com/library/windows/hardware/ff557022) structure.

In response to a query of [OID\_TCP4\_OFFLOAD\_STATS](https://msdn.microsoft.com/library/windows/hardware/ff569800) or [OID\_TCP6\_OFFLOAD\_STATS](https://msdn.microsoft.com/library/windows/hardware/ff569801), an offload target returns TCP statistics in a [**TCP\_OFFLOAD\_STATS**](https://msdn.microsoft.com/library/windows/hardware/ff570940) structure.

 

 





