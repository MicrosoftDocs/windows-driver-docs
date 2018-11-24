---
title: Duplicating Socket Handles for a SAN
description: Duplicating Socket Handles for a SAN
ms.assetid: d8e8cb6d-fcdb-4121-9a44-a2bc884ab620
keywords:
- Windows Sockets Direct WDK , socket handles
- SAN sockets WDK , duplicating socket handles
- suspensions WDK Windows Sockets Direct
- duplicating socket handles WDK SANs
- shared underlying sockets WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Duplicating Socket Handles for a SAN





Multiple applications that run in different processes can use the Windows Sockets switch to perform operations on a shared underlying socket. However, only one application at a time can perform operations on that shared underlying socket.

To use a shared underlying socket, an application must retrieve a duplicate handle to that underlying socket in one of the following ways:

-   Directly, by calling the Windows Sockets **WSADuplicateSocket** function

    The call is made in the context of the controlling process (the process in which the socket was created).

-   Indirectly, by calling the Win32 DuplicateHandle function

    The call is made in the context of a noncontrolling process (other than the process in which the socket was created).

-   Using the handle inheritance mechanism

    A child process (the noncontrolling process) inherits all or some of the handles created in its parent process (the controlling process).

-   During graceful connection closure

    If an application in the controlling process closes a socket and exits while some data still remains to be sent, this remaining data is buffered in the Windows Sockets DLL. Another application in the context of the system service process (the noncontrolling process) subsequently sends this data.

The Windows Sockets switch, in conjunction with the TCP/IP provider, detects and handles each of the preceding conditions. The switch allows only one process at a time to execute operations that either transfer data or change state for an underlying shared socket. Processes dynamically swap control of the underlying socket, as required, to execute requested operations. The switch serializes operations that different processes request to perform on a shared socket and executes those operations in first-in-first-out (FIFO) order. The switch waits for all in-progress operations to complete before swapping control of an underlying socket to another process. Logically, the switch takes control of the underlying socket away from the controlling process as soon as a noncontrolling process requests a qualifying operation. After control is taken away, the switch treats the original controlling process like a noncontrolling process if the original controlling process requests qualifying operations. Note that the switch takes no action on a duplicate socket handle until the noncontrolling process actually uses the duplicate socket handle for a data transfer or state-change operation.

Both the switch and the appropriate SAN service provider are loaded into all processes that share access to a particular underlying socket. The switch maintains its own socket context and connection state information in all processes that share the socket. The SAN service provider is required to maintain its socket context and connection state information only in the process that has control of the underlying socket at any given point in time. The SAN service provider must swap control of its context and connection state information from the current controlling process to the next controlling process whenever the switch requires the swap as described in the following sequence. To minimize the amount of resources that are required for swapping, a SAN service provider can maintain its context and connection state information in all processes that share an underlying socket.

Because the switch does not create the SAN socket that corresponds to an application socket until an application calls either the **connect** or **listen** function, the switch cannot request that the SAN service provider perform a swap operation before the application socket is connected or listening. Even after the application socket is connected or listening, one of the following conditions must be met before the switch requests that the SAN service provider swap control of the socket:

-   A process that does not control the socket initiates a data transfer. The SAN service provider does not swap control of the socket until all data transfer operations that were initiated by the controlling process have completed.

-   A process that does not control the socket calls the **WSAAccept**, **WSPAccept**, or **AcceptEx** function to start a connection-acceptance operation on a listening socket. The SAN service provider does not swap control of the socket until all accept requests that were initiated by the controlling process have completed.

The switch performs the following steps to swap control of a connected SAN socket from the controlling process to the next-controlling process (For an overview of the swapping process, see the table in the Remarks section of the documentation for the [**WSPDuplicateSocket**](https://msdn.microsoft.com/library/windows/hardware/ff566282) function.):

1.  The switch suspends processing of new requests from the application in the controlling process. When all send and RDMA operations in progress on the SAN socket have completed, the switch calls the SAN service provider's [**WSPSend**](https://msdn.microsoft.com/library/windows/hardware/ff566316) function to send a message to a connected peer to request a suspension of the session and calls the SAN service provider's [**WSPDeregisterMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566279) function to release all local buffers used for send operations. As a result, the switch at the peer connection suspends processing of new application requests, waits for all send and RDMA operations in progress on the SAN socket to complete, and releases all RDMA memory. The peer connection next sends a reply message indicating that the session is suspended. On receiving this confirmation message, the switch at the local endpoint calls the SAN service provider's **WSPDeregisterRdmaMemory** function to release all RDMA memory. At this point, SAN sockets at both endpoints of the connection can only have receive requests pending. These receive requests remain pending on the remote peer's SAN socket to permit reactivation of the session. The receive requests on the local SAN socket in the controlling process are completed in the next step. While the connection is suspended, the switch at the remote peer connection queues new blocking or overlapped requests, buffers new nonblocking sends up to the SO\_SNDBUF setting, fails new nonblocking sends after the buffer limit is reached, and fails all new nonblocking receives with WSAEWOULDBLOCK. The local switch in the controlling process handles new requests on the application socket as if the process did not have control of the socket.

2.  After the session is suspended, the switch calls the SAN service provider's **WSPDuplicateSocket** function in the controlling process to direct the SAN service provider to transfer the socket context into the address space of the next-controlling process. The switch specifies the next-controlling process in the *dwProcessId* parameter of **WSPDuplicateSocket**. The **WSPDuplicateSocket** function must call the **WPUCompleteOverlappedRequest** function to complete all outstanding receive requests on the socket with a success status and zero bytes. The SAN service provider must also automatically release all buffers associated with these requests. The SAN service provider releases all buffers since the switch does not request any more operations on the SAN socket after **WSPDuplicateSocket** returns. The only possible exception is a **WSPCloseSocket** function call, as described in the next step. After **WSPDuplicateSocket** returns, the switch saves the value in the **dwProviderReserved** member of the WSAPROTOCOL\_INFOW structure to which the *lpProtocolInfo* output parameter points. The switch uses this value to identify the underlying socket in the context of the next-controlling process. Therefore, the value in **dwProviderReserved** must uniquely identify the underlying socket and the connection for that socket across all processes on the system. In addition, this value must be valid only in the context of the process that the switch specified in the *dwProcessId* parameter of **WSPDuplicateSocket**.

3.  After the socket context is transferred into the address space of the next-controlling process, the switch calls the SAN service provider's [**WSPSocket**](https://msdn.microsoft.com/library/windows/hardware/ff566319) function in the context of the next-controlling process. In this call, the switch passes the value for the underlying socket that was returned in the **WSPDuplicateSocket** call to the **dwProviderReserved** member of the WSAPROTOCOL\_INFOW structure to which the *lpProtocolInfo* input parameter points. If the next-controlling process did not request the creation of the SAN socket, the SAN service provider must create a new socket and call the **WPUCreateSocketHandle** function to obtain a handle, as required for any new socket. If the SAN socket was created in the context of the next-controlling process, the SAN service provider can reactivate the former socket and return the same descriptor for the socket that was used previously. In this case, the SAN service provider should not call **WPUCreateSocketHandle**, but should continue to use the original socket handle that the switch provided. Alternatively, the SAN service provider can create a new socket, regardless of whether a socket previously existed in the process. In this case, the switch must call the SAN service provider's [**WSPCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff566273) function in the context of the next-controlling process to dispose of the former socket descriptor.

4.  The switch restarts processing of new requests from the application in the next-controlling process.

The switch duplicates a listening socket in a similar manner, except that the switch is not required to suspend a session. The switch waits until it completes all **WSPAccept** calls that were initiated by an application's **accept** and **AcceptEx** calls before calling the SAN service provider's **WSPDuplicateSocket** function in the controlling process.

Because the switch suspends processing of new requests on a SAN socket prior to calling the SAN service provider's **WSPDuplicateSocket** function, the SAN service provider can release all resources associated with a local endpoint in the controlling process. The SAN service provider can even terminate an underlying connection. If the SAN service provider closes an underlying connection in the controlling process, the SAN service provider must reestablish the connection after the switch calls the SAN service provider's **WSPSocket** function within the next-controlling process. After the **WSPSocket** call returns, the SAN socket within the next-controlling process must be in the same state, from the switch's perspective, as the SAN socket in the controlling process was prior to the switch calling the SAN service provider's **WSPDuplicateSocket** function.

If a SAN NIC supports sharing resources between endpoints that run in different processes, the SAN service provider does not have to release resources for a local endpoint in the controlling process prior to receiving a **WSPDuplicateSocket** call. In such a case, the SAN socket associated with a local endpoint remains inactive in the former-controlling process until the switch either swaps the socket context back from the next-controlling process or calls the SAN service provider's **WSPCloseSocket** function to explicitly close the socket. Because most applications perform their final access to the socket in the process that originally created it--generally to close the connection--the SAN service provider can improve performance if the SAN service provider preserves the socket context in the controlling process after the switch swaps control of the socket to the next-controlling process.

Note that, in all cases, a SAN socket descriptor must remain valid until the switch calls the SAN service provider's **WSPCloseSocket** function to explicitly close the socket. Even if the SAN service provider releases all resources for the socket in a particular process prior to receiving a **WSPDuplicateSocket** call, the SAN service provider must not reuse the descriptor for the socket until the switch calls **WSPCloseSocket** on that descriptor.

An unexpected process exit or some other error condition can interrupt a SAN service provider's socket-duplication operation. For example, a shortage of resources can cause such an interruption. The switch treats such error conditions as it does any other error situation. If necessary, the switch closes all descriptors that are associated with the underlying socket in all processes to forcefully terminate the socket's connection. If at all possible, the SAN service provider at the remote peer should complete [**WSPRecv**](https://msdn.microsoft.com/library/windows/hardware/ff566309) calls that receive incoming data with an appropriate error code, such as WSAECONNRESET. This error code informs the remote peer of the connection termination. If the switch at the remote peer does not receive this connection-termination indication, the switch at the remote peer times out a suspended connection if the system that requested the suspension fails.

 

 





