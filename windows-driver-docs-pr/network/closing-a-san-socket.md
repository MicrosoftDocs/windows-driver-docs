---
title: Closing a SAN Socket
description: Closing a SAN Socket
ms.assetid: 49224987-ed46-4631-a47b-70cd855cfa40
keywords:
- SAN sockets WDK , closing
- closing SAN sockets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing a SAN Socket





After the Windows Sockets switch on either side of a connection calls a SAN service provider's [**WSPCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff566273) function, the SAN service provider performs the following procedure to close a SAN socket:

1.  Each SAN service provider on either side of the connection tears down the connection and completes receive requests-- [**WSPRecv**](https://msdn.microsoft.com/library/windows/hardware/ff566309) function calls--by returning the appropriate error code at the *lpErrno* parameter. For example, a SAN service provider returns WSAECONNRESET to indicate that the remote peer reset the connection.

    Each SAN service provider also signals completion of pending overlapped operations for the SAN socket to be closed. The SAN service provider calls the **WPUCompleteOverlappedRequest** function to signal completion of an overlapped operation. In this call, the SAN service provider passes a pointer to the [**WSAOVERLAPPED**](https://msdn.microsoft.com/library/windows/hardware/ff565952) structure that is associated with the overlapped operation. The SAN service provider also passes the WSA\_OPERATION\_ABORTED error code to specify that the overlapped operation was canceled because the SAN socket was closed. Before signaling completion of an overlapped operation, the SAN service provider should release any memory that was required for the operation.

2.  After the SAN service provider is done making up-calls--calls to functions that are prefixed with **WPU**--to the switch using the handle to the SAN socket that was obtained through a **WPUCreateSocketHandle** up-call, the SAN service provider must make a final up-call to the switch by calling the **WPUCloseSocketHandle** function to close the socket handle. The SAN service provider then cleans up everything related to the SAN socket. Up-calls are function calls from the switch's up-call dispatch table. The switch provides a pointer to this up-call dispatch table when it calls the SAN service provider's [**WSPStartupEx**](https://msdn.microsoft.com/library/windows/hardware/ff566321) function to start using the provider. For more information about these up-call functions, see the Microsoft Windows SDK documentation.

As long as a SAN service provider performs the preceding procedure to close a SAN socket, the switch takes care of everything else.

To prevent race conditions between a SAN service provider and the switch initiating socket closures, the SAN service provider should never release data structures related to a SAN socket until the switch calls **WSPCloseSocket**.

 

 





