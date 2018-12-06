---
title: Allocating Buffer Pools
description: Allocating Buffer Pools
ms.assetid: 9bbf2636-9cfb-40ea-b67c-c4315a3fbc7a
keywords:
- TCP chimney offload WDK networking , buffer pools
- chimney offload WDK networking , buffer pools
- buffer pools WDK TCP chimney offload
- allocating buffer pools
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating Buffer Pools


\[The TCP chimney offload feature is deprecated and should not be used.\]

During initialization (that is, in the context of its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function), an offload target typically creates two buffers pools, each of which contains [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) and [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. The offload target uses one buffer pool for making receive indications through the TCP chimney when calling the [**NdisTcpOffloadReceiveHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564606) function. The offload target uses the other buffer pool for making receive indications through the nonoffload NDIS interface when calling the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. Using two buffer pools in this way improves performance and makes debugging easier.

Note that each allocated NET\_BUFFER\_LIST structure must have only one NET\_BUFFER structure associated with it. The number of NET\_BUFFER\_LIST structures that the offload target allocates in each pool depends on the implementation.

For more information about creating buffer pools, see [Miniport Driver Buffer Management](miniport-driver-buffer-management.md).

 

 





