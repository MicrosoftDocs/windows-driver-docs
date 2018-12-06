---
title: Querying and setting TCP chimney offload for an offload target
description: Querying and Setting an Offload Target's TCP Chimney Offload Capabilities
ms.assetid: e4e6dc5f-0cf6-4de6-9402-4ce8c8cba942
keywords:
- TCP chimney offload WDK networking , capabilities
- chimney offload WDK networking , capabilities
- capabilities WDK TCP chimney offload
- querying TCP chimney offload capabilities
- target capabilities WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying and Setting an Offload Target's TCP Chimney Offload Capabilities


\[The TCP chimney offload feature is deprecated and should not be used.\]

If the offload target's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function returns NDIS\_STATUS\_SUCCESS, NDIS and the host stack query the operational characteristics of the offload target.

In particular, the host stack queries the [OID\_TCP\_TASK\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569815) OID to determine an offload target's task offload and TCP chimney offload capabilities. In response to this query, an offload target returns an [**NDIS\_TASK\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567873) structure that specifies the offload target's TCP chimney offload capabilities, in addition to other information. After querying the target's task offload and TCP chimney offload capabilities, the host stack sets OID\_TCP\_TASK\_OFFLOAD to enable the offload target's task offload and TCP chimney offload capabilities.

 

 





