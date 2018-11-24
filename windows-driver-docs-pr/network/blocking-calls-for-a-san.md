---
title: Blocking Calls for a SAN
description: Blocking Calls for a SAN
ms.assetid: 93be861c-4cf1-48ea-ac69-a4a171ca9052
keywords:
- blocking calls WDK SANs
- Windows Sockets Direct WDK , blocking calls
- SAN blocking calls WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Blocking Calls for a SAN





The Windows Sockets switch handles blocking calls and the cancellation of such calls internally or forwards them to the TCP/IP service provider. The switch never calls a **WSPCancelBlockingCall** function for a SAN service provider to cancel a blocking request that is in progress. Therefore, a SAN service provider is not required to implement a **WSPCancelBlockingCall** function.

The switch handles the following blocking requests and corresponding cancellations in the following ways:

-   When an application requests to connect a SAN socket to a specific destination address in blocking mode, the switch receives a blocking **WSPConnect** call. The switch forwards the connect request in nonblocking mode to the appropriate SAN service provider's [**WSPConnect**](https://msdn.microsoft.com/library/windows/hardware/ff566275) function. If the switch must cancel this connection request for some reason, it calls the SAN service provider's [**WSPCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff566273) function. The SAN service provider must promptly abort the connection request and release resources for the socket.

-   When the switch receives a blocking request that was initiated by an application to perform a data transfer operation on a SAN socket, it forwards the data transfer request in an overlapped (nonblocking) manner to the appropriate SAN service provider. For example, if the switch receives a synchronous (blocking) **WSPSend** call, it calls the appropriate SAN service provider's [**WSPSend**](https://msdn.microsoft.com/library/windows/hardware/ff566316) function in an overlapped (nonblocking) manner. If the application later cancels the data transfer operation and the switch has control of the application's buffer, the switch completes the application's request with a failure status. If the application's buffer is involved in an outstanding RDMA operation, the switch waits for the operation to complete. If an RDMA transfer takes too long to complete, the switch calls the appropriate SAN service provider's **WSPCloseSocket** function to close the connection in an abortive manner, thereby forcing completion.

**Note**  If an application cancels a blocking call, it cannot rely on a connection being preserved. Only the **WSPCloseSocket** call is guaranteed to succeed on the socket after the cancellation of a blocking request. For more information, see the Windows Sockets SPI documentation in the Microsoft Windows SDK.

 

 

 





