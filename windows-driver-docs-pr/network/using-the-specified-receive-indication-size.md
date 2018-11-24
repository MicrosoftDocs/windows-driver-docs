---
title: Using the Specified Receive Indication Size
description: Using the Specified Receive Indication Size
ms.assetid: b6a53683-36da-4184-8154-c3d77b6daf8e
keywords:
- delivering received data WDK TCP chimney offload , indication size
- indication size WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the Specified Receive Indication Size


\[The TCP chimney offload feature is deprecated and should not be used.\]




In the **RcvIndicationSize** member of the [**TCP\_OFFLOAD\_STATE\_CACHED**](https://msdn.microsoft.com/library/windows/hardware/ff570937) structure, the host stack can specify the optimum number of data bytes that the offload target should supply in a single call to the [**NdisTcpOffloadReceiveHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564606) function. Typically, an application that uses the indicate-and-post model for receiving data (which is described in the following paragraphs) specifies a receive indication size to the host stack.

The scenarios in this topic illustrate how an offload target can use the receive indication size to optimize the delivery of receive data. This information can help you optimize commonly used application algorithms that process receive data. These scenarios, however, refer to only a small part of the entire [delivery algorithm](delivery-algorithm.md). An offload target must implement the entire delivery algorithm.

The following scenarios illustrate optional optimizations--not required implementations:

-   An application that uses the indicate-and-post model does not typically post receive requests to the offload target's [*MiniportTcpOffloadReceive*](https://msdn.microsoft.com/library/windows/hardware/ff559460) function until the offload target has indicated receive data by calling the **NdisTcpOffloadReceiveHandler** function. After indicating receive data, the offload target should buffer the remaining receive data in the network interface card (NIC), if possible. The application looks at the indicated receive data to find the application header. From the application header, the application determines the amount of remaining receive data that will eventually arrive and then posts a receive buffer to the offload target's *MiniportTcpOffloadReceive* function. If the offload target completes the receive request with all of the data that is requested, the application does not typically post any more receive requests until the offload target has made another receive indication. If the offload target completes the receive request without filling the entire buffer, the application might continue to post receive requests until it has received all of the data.

-   If an application never posts receive buffers, it does not specify a receive indication size, so the value of the **RcvIndicationSize** member is zero. The offload target should indicate as much data as possible when calling the [**NdisTcpOffloadReceiveHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564606) function.

-   If an application always preposts receive requests, it typically does not specify a receive indication size. If the application runs out of receive requests, the offload target might have to make a receive indication. If the value of **RcvIndicationSize** is unspecified (set to zero), the offload target should indicate as much data as possible when calling the *NdisTcpOffloadReceiveHandler* function.

 

 





