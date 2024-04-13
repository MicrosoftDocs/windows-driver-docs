---
title: Windows Sockets SPI Extensions for SANs
description: Windows Sockets SPI Extensions for SANs
keywords:
- SAN service providers WDK , extensions
- extensions WDK SANs
ms.date: 04/20/2017
---

# Windows Sockets SPI Extensions for SANs





This section provides a brief description of the SAN extension functions that a SAN service provider DLL must supply. These functions extend the Windows Sockets SPI for use with a SAN. The extended functions are defined in Ws2san.h and are fully documented in the [Windows Sockets Direct Reference](/previous-versions/windows/hardware/network/ff565857(v=vs.85)) section.

Except for the **WSPStartupEx** function, the extended functions listed in this section are retrieved by the Windows Sockets switch. To retrieve the entry point to each of these extended functions, the Windows Sockets switch calls a SAN service provider's [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)) function and passes the SIO\_GET\_EXTENSION\_FUNCTION\_POINTER command code along with the GUID whose value identifies one of these extended functions.

A SAN service provider must implement all of the following extension functions with the exception of the **WSPRdmaRead** and **WSPMemoryRegistrationCacheCallback** functions. If a SAN service provider does not support either the **WSPRdmaRead** or **WSPMemoryRegistrationCacheCallback** extension function, its **WSPIoctl** function must return the error WSAEOPNOTSUPP when the Windows Sockets switch requests the entry point to either **WSPRdmaRead** or **WSPMemoryRegistrationCacheCallback**.

<a href="" id="wspstartupex"></a>[**WSPStartupEx**](/previous-versions/windows/hardware/network/ff566321(v=vs.85))  
Initiates the Windows Sockets switch's use of a SAN service provider.

<a href="" id="wspregistermemory"></a>[**WSPRegisterMemory**](/previous-versions/windows/hardware/network/ff566311(v=vs.85))  
Registers a buffer array that a socket uses as either the local source or the local target of a data transfer operation. Such a socket can use this buffer array as the source buffer in **WSPRdmaWrite** and **WSPSend** calls and the receiving buffer in **WSPRdmaRead** and **WSPRecv** calls.

<a href="" id="wspderegistermemory"></a>[**WSPDeregisterMemory**](/previous-versions/windows/hardware/network/ff566279(v=vs.85))  
Releases a buffer array that was registered by a previous call to the **WSPRegisterMemory** function.

<a href="" id="wspregisterrdmamemory"></a>[**WSPRegisterRdmaMemory**](/previous-versions/windows/hardware/network/ff566313(v=vs.85))  
Registers an RDMA buffer array that is exposed to a remote peer connection for transferring data to or from that peer connection. A socket at the remote peer can use this RDMA buffer array as the target buffer in a **WSPRdmaWrite** call and the source buffer in a **WSPRdmaRead** call.

<a href="" id="wspderegisterrdmamemory"></a>[**WSPDeregisterRdmaMemory**](/previous-versions/windows/hardware/network/ff566281(v=vs.85))  
Releases a buffer array that was registered by a previous call to the **WSPRegisterRdmaMemory** function.

<a href="" id="--------wspmemoryregistrationcachecallback"></a>[**WSPMemoryRegistrationCacheCallback**](/previous-versions/windows/hardware/network/ff566299(v=vs.85))  
Releases ownership of an application's buffer and the lock between the buffer and physical memory and removes the buffer from the SAN service provider's cache and the buffer registration from the SAN NIC.

<a href="" id="wsprdmaread"></a>[**WSPRdmaRead**](/previous-versions/windows/hardware/network/ff566304(v=vs.85))  
Transfers data from an RDMA buffer in the address space that a socket's remote peer can access to a buffer in the address space that the local socket can access.

<a href="" id="wsprdmawrite"></a>[**WSPRdmaWrite**](/previous-versions/windows/hardware/network/ff566306(v=vs.85))  
Transfers data from a source buffer in the address space that a local socket can access to a target RDMA buffer in the address space that the socket's remote peer can access.

 

