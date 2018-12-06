---
title: Handling Segments Received During a Terminate Offload Operation
description: Handling Segments Received During a Terminate Offload Operation
ms.assetid: 19924d55-80c0-4cb3-bce2-cf0e2fc0758d
keywords:
- terminating offload state WDK TCP chimney offload , segments received during
- out-of-order segments WDK TCP chimney offload
- segments received during termination WDK TCP chimney offload
- TCP SACK WDK TCP chimney offload
- selective acknowledgment for out-of-order segments WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Segments Received During a Terminate Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




If the offload target receives any segments on an offloaded TCP connection that is being terminated, it should not process the segments. Instead, it should indicate the received data through the non-offload NDIS interface by calling the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. The host stack will not forward such indicated receive data back to the offload target.

After the offload of a TCP connection has been terminated, the offload target continues to use the non-offload NDIS interface to indicate receive segments on the connection. Before completing a terminate offload operation, the offload target must send any delayed acknowledgments to the remote host.

If the offload target supports TCP SACK (that is, selective acknowledgment for out-of-order segments), it should drop any receive segments that it has not yet acknowledged with a TCP acknowledgment--not just a SACK acknowledgment. The offload target should not indicate the received SACK data to the local host, and it should not acknowledge such data to the remote host.

 

 





