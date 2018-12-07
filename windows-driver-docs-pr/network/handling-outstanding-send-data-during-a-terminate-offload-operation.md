---
title: Handling Outstanding Send Data During a Terminate Offload Operation
description: Handling Outstanding Send Data During a Terminate Offload Operation
ms.assetid: 34a3e464-5ea6-4021-9a52-59f691ce3ffb
keywords:
- terminating offload state WDK TCP chimney offload , outstanding send data during
- outstanding send data during termination WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Outstanding Send Data During a Terminate Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




When the offload of a TCP connection is terminated, outstanding send data might exist on the connection. This data can include:

-   Data that the offload target has sent but that has not yet been acknowledged by the remote host

-   Data that the offload target has not yet sent

The offload target can handle such data in either of the following ways or in a combination of these two ways:

-   The offload target can complete outstanding send requests by calling the [**NdisTcpOffloadSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff564609) function before terminating the offload of the connection.

-   The offload target can pass outstanding send data to the host in the call to the [**NdisMTerminateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563685) function.

When passing outstanding send data to the host, the offload target does the following:

-   Chains together [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures that the host stack passed to the offload target's [*MiniportTcpOffloadSend*](https://msdn.microsoft.com/library/windows/hardware/ff559464) function. These NET\_BUFFER\_LIST structures must be chained together in the same order that they were in when passed to the offload target.

-   Specifies a pointer in the **NetBufferListChain** member of the [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure that the offload target passes in the call to the **NdisMTerminateOffloadComplete** function. The value of **NetBufferListChain** points to the first NET\_BUFFER\_LIST structure in the linked list.

-   Specifies pointers in the **SendDataHead** and **SendDataTail** members of the [**TCP\_OFFLOAD\_STATE\_DELEGATED**](https://msdn.microsoft.com/library/windows/hardware/ff570939) structure that the offload target passes in the call to the **NdisMTerminateOffloadComplete** function.

 

 





