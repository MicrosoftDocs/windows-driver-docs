---
title: Windows Sockets SPI Functions Required for SANs
description: Windows Sockets SPI Functions Required for SANs
ms.assetid: b41bd7e0-bb6c-4933-a5d0-18e4d067601b
keywords:
- SAN service providers WDK , required functions
- functions WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Sockets SPI Functions Required for SANs





This section describes the functions of the Windows Sockets SPI that a SAN service provider DLL must supply. These functions are defined in Ws2spi.h and are fully documented in the [Windows Sockets Direct Reference](https://msdn.microsoft.com/library/windows/hardware/ff565857) section:

<a href="" id="wspaccept"></a>[**WSPAccept**](https://msdn.microsoft.com/library/windows/hardware/ff566266)  
Conditionally accepts a connection for a socket that is listening for connections, based on the return value of a supplied condition function.

<a href="" id="wspbind"></a>[**WSPBind**](https://msdn.microsoft.com/library/windows/hardware/ff566268)  
Associates the local IP address, or name, of a network interface with a socket. This network interface is serviced by the SAN service provider.

<a href="" id="wspcleanup"></a>[**WSPCleanup**](https://msdn.microsoft.com/library/windows/hardware/ff566270)  
Terminates use of the SAN service provider DLL.

<a href="" id="wspclosesocket"></a>[**WSPCloseSocket**](https://msdn.microsoft.com/library/windows/hardware/ff566273)  
Closes a socket.

<a href="" id="wspconnect"></a>[**WSPConnect**](https://msdn.microsoft.com/library/windows/hardware/ff566275)  
Establishes the connection of a socket to a peer, exchanges connect data, and specifies required quality of service (QoS) based on the supplied flow specification.

<a href="" id="wspduplicatesocket"></a>[**WSPDuplicateSocket**](https://msdn.microsoft.com/library/windows/hardware/ff566282)  
Retrieves a WSAPROTOCOL\_INFOW structure that can be used to create a new socket descriptor for a shared socket in the context of another process.

<a href="" id="wspenumnetworkevents"></a>[**WSPEnumNetworkEvents**](https://msdn.microsoft.com/library/windows/hardware/ff566284)  
Reports occurrences of network events for a socket.

<a href="" id="wspeventselect"></a>[**WSPEventSelect**](https://msdn.microsoft.com/library/windows/hardware/ff566287)  
Specifies an event object for a socket. This event object is subsequently set by the occurrence of the supplied set of network events.

<a href="" id="wspgetoverlappedresult"></a>[**WSPGetOverlappedResult**](https://msdn.microsoft.com/library/windows/hardware/ff566288)  
Returns the results of an asynchronous (overlapped) operation on a socket. This operation previously indicated that it was pending completion.

<a href="" id="wspgetqosbyname"></a>[**WSPGetQOSByName**](https://msdn.microsoft.com/library/windows/hardware/ff566290)  
Initializes a QoS structure based on a named template, or retrieves an enumeration of the available template names.

A SAN service provider DLL that supports QoS must fully implement **WSPGetQOSByName**. If the SAN service provides does not support QoS, its **WSPGetQOSByName** function must at least return the error WSAEOPNOTSUPP.

<a href="" id="wspgetsockopt"></a>[**WSPGetSockOpt**](https://msdn.microsoft.com/library/windows/hardware/ff566292)  
Retrieves the current value of an option for a socket.

<a href="" id="wspioctl"></a>[**WSPIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff566296)  
Sets or retrieves operating parameters associated with a socket.

<a href="" id="wsplisten"></a>[**WSPListen**](https://msdn.microsoft.com/library/windows/hardware/ff566297)  
Establishes a socket to listen for incoming connections.

<a href="" id="wsprecv"></a>[**WSPRecv**](https://msdn.microsoft.com/library/windows/hardware/ff566309)  
Receives data on a connected socket.

<a href="" id="wspsend"></a>[**WSPSend**](https://msdn.microsoft.com/library/windows/hardware/ff566316)  
Sends data on a connected socket.

<a href="" id="wspsetsockopt"></a>[**WSPSetSockOpt**](https://msdn.microsoft.com/library/windows/hardware/ff566318)  
Sets the value of an option for a socket.

<a href="" id="wspsocket"></a>[**WSPSocket**](https://msdn.microsoft.com/library/windows/hardware/ff566319)  
Creates a socket that uses the TCP/IP protocol and asynchronous (overlapped) data transfer.

 

 





