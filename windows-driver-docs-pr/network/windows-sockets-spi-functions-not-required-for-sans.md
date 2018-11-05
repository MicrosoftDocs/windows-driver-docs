---
title: Windows Sockets SPI Functions not Required for SANs
description: Windows Sockets SPI Functions not Required for SANs
ms.assetid: 995ff59e-8ee4-4468-914d-47c14d804c38
keywords:
- SAN service providers WDK , not required functions
- functions WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Sockets SPI Functions not Required for SANs





This section describes the functions of the Windows Sockets SPI that a SAN service provider is not required to implement. These functions are defined in Ws2spi.h.

<a href="" id="wspaddresstostring"></a>**WSPAddressToString**  
The Windows Sockets switch uses the TCP/IP provider to convert all components of a SOCKADDR structure into a human-readable numeric string that represents the IP address of a socket.

<a href="" id="wspasyncselect"></a>**WSPAsyncSelect**  
The Windows Sockets switch uses its session protocol internally to handle notification of network events for a socket, if necessary.

<a href="" id="wspcancelblockingcall"></a>**WSPCancelBlockingCall**  
The Windows Sockets switch internally handles the cancellation of blocking requests that are in progress. Therefore, it never issues cancel blocking calls to a SAN service provider DLL. The Windows Sockets switch can either:

Cancel an outstanding connect request by closing the SAN socket. The SAN service provider DLL should abort the connect request.

Cancel outstanding send and receive requests by discarding data for those requests if the switch buffers that data internally, or by waiting for those requests to complete if they are RDMA transfers to or from application buffers. For lengthy RDMA transfers, the switch can close the connection altogether.

The Windows Sockets SPI documentation in the Microsoft Windows SDK warns that if a blocking call is canceled, an application cannot rely on a connection being preserved. In this case, the only call that is guaranteed to succeed on the socket after the cancellation of a blocking request is **WSPCloseSocket**.

**WSPGetPeerName**
The Windows Sockets switch caches the IP address of a peer when the switch establishes a connection to the peer in a **WSPConnect** call or accepts a connection to the peer in a **WSPAccept** call. The switch provides this cached value to applications, if necessary.

**WSPGetSockName**
The Windows Sockets switch caches the local IP address for a socket when the switch associates the address with the socket in a **WSPBind** call or accepts a connection to a peer in a **WSPAccept** call. The switch provides this cached value to applications, if necessary.

**WSPJoinLeaf**
The Windows Sockets switch exclusively uses the TCP/IP provider to handle multipoint sessions.

**WSPRecvDisconnect**
The Windows Sockets switch internally handles termination of data reception on a socket and retrieves any incoming disconnect data from the remote party.

**WSPRecvFrom**
The current version of Windows Sockets Direct does not support SAN service providers handling sockets that receive datagrams with User Datagram Protocol (UDP) semantics. Therefore, the Windows Sockets switch calls a SAN service provider's **WSPRecv** function on a connected socket to receive stream data with Transmission Control Protocol (TCP) semantics.

**WSPSelect**
The Windows Sockets switch uses its session protocol internally in cooperation with the TCP/IP provider to determine the status of sockets, if necessary.

**WSPSendDisconnect**
The Windows Sockets switch internally handles termination of the connection for a socket and sends disconnect data to the remote party.

**WSPSendTo**
The current version of Windows Sockets Direct does not support SAN service providers handling sockets that send datagrams with User Datagram Protocol (UDP) semantics. Therefore, the Windows Sockets switch calls a SAN service provider's **WSPSend** function on a connected socket to send stream data with Transmission Control Protocol (TCP) semantics.

**WSPShutdown**
The Windows Sockets switch internally disables the reception and transmission of data on a socket.

**WSPStartup**
The Windows Sockets switch does not call **WSPStartup** to start the operation of a SAN service provider. The switch instead uses the SAN service provider's **WSPStatupEx** function.

**WSPStringToAddress**
The Windows Sockets switch uses the TCP/IP provider to convert a human-readable numeric string that represents the IP address of a socket into a socket address structure (SOCKADDR) that is suitable to pass to Windows Sockets routines that take such a structure.

 

 





