---
title: Windows Sockets SPI Functions Required for SANs
description: Windows Sockets SPI Functions Required for SANs
keywords:
- SAN service providers WDK , required functions
- functions WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Sockets SPI Functions Required for SANs





This section describes the functions of the Windows Sockets SPI that a SAN service provider DLL must supply. These functions are defined in Ws2spi.h and are fully documented in the [Windows Sockets Direct Reference](/previous-versions/windows/hardware/network/ff565857(v=vs.85)) section:

<a href="" id="wspaccept"></a>[**WSPAccept**](/previous-versions/windows/hardware/network/ff566266(v=vs.85))  
Conditionally accepts a connection for a socket that is listening for connections, based on the return value of a supplied condition function.

<a href="" id="wspbind"></a>[**WSPBind**](/previous-versions/windows/hardware/network/ff566268(v=vs.85))  
Associates the local IP address, or name, of a network interface with a socket. This network interface is serviced by the SAN service provider.

<a href="" id="wspcleanup"></a>[**WSPCleanup**](/previous-versions/windows/hardware/network/ff566270(v=vs.85))  
Terminates use of the SAN service provider DLL.

<a href="" id="wspclosesocket"></a>[**WSPCloseSocket**](/previous-versions/windows/hardware/network/ff566273(v=vs.85))  
Closes a socket.

<a href="" id="wspconnect"></a>[**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85))  
Establishes the connection of a socket to a peer, exchanges connect data, and specifies required quality of service (QoS) based on the supplied flow specification.

<a href="" id="wspduplicatesocket"></a>[**WSPDuplicateSocket**](/previous-versions/windows/hardware/network/ff566282(v=vs.85))  
Retrieves a WSAPROTOCOL\_INFOW structure that can be used to create a new socket descriptor for a shared socket in the context of another process.

<a href="" id="wspenumnetworkevents"></a>[**WSPEnumNetworkEvents**](/previous-versions/windows/hardware/network/ff566284(v=vs.85))  
Reports occurrences of network events for a socket.

<a href="" id="wspeventselect"></a>[**WSPEventSelect**](/previous-versions/windows/hardware/network/ff566287(v=vs.85))  
Specifies an event object for a socket. This event object is subsequently set by the occurrence of the supplied set of network events.

<a href="" id="wspgetoverlappedresult"></a>[**WSPGetOverlappedResult**](/previous-versions/windows/hardware/network/ff566288(v=vs.85))  
Returns the results of an asynchronous (overlapped) operation on a socket. This operation previously indicated that it was pending completion.

<a href="" id="wspgetqosbyname"></a>[**WSPGetQOSByName**](/previous-versions/windows/hardware/network/ff566290(v=vs.85))  
Initializes a QoS structure based on a named template, or retrieves an enumeration of the available template names.

A SAN service provider DLL that supports QoS must fully implement **WSPGetQOSByName**. If the SAN service provides does not support QoS, its **WSPGetQOSByName** function must at least return the error WSAEOPNOTSUPP.

<a href="" id="wspgetsockopt"></a>[**WSPGetSockOpt**](/previous-versions/windows/hardware/network/ff566292(v=vs.85))  
Retrieves the current value of an option for a socket.

<a href="" id="wspioctl"></a>[**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85))  
Sets or retrieves operating parameters associated with a socket.

<a href="" id="wsplisten"></a>[**WSPListen**](/previous-versions/windows/hardware/network/ff566297(v=vs.85))  
Establishes a socket to listen for incoming connections.

<a href="" id="wsprecv"></a>[**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85))  
Receives data on a connected socket.

<a href="" id="wspsend"></a>[**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85))  
Sends data on a connected socket.

<a href="" id="wspsetsockopt"></a>[**WSPSetSockOpt**](/previous-versions/windows/hardware/network/ff566318(v=vs.85))  
Sets the value of an option for a socket.

<a href="" id="wspsocket"></a>[**WSPSocket**](/previous-versions/windows/hardware/network/ff566319(v=vs.85))  
Creates a socket that uses the TCP/IP protocol and asynchronous (overlapped) data transfer.

 

