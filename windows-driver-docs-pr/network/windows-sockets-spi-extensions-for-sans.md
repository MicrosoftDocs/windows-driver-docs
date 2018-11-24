---
title: Windows Sockets SPI Extensions for SANs
description: Windows Sockets SPI Extensions for SANs
ms.assetid: 08f51612-2e2b-439a-8318-43884086828c
keywords:
- SAN service providers WDK , extensions
- extensions WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Sockets SPI Extensions for SANs





This section provides a brief description of the SAN extension functions that a SAN service provider DLL must supply. These functions extend the Windows Sockets SPI for use with a SAN. The extended functions are defined in Ws2san.h and are fully documented in the [Windows Sockets Direct Reference](https://msdn.microsoft.com/library/windows/hardware/ff565857) section.

Except for the **WSPStartupEx** function, the extended functions listed in this section are retrieved by the Windows Sockets switch. To retrieve the entry point to each of these extended functions, the Windows Sockets switch calls a SAN service provider's [**WSPIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff566296) function and passes the SIO\_GET\_EXTENSION\_FUNCTION\_POINTER command code along with the GUID whose value identifies one of these extended functions.

A SAN service provider must implement all of the following extension functions with the exception of the **WSPRdmaRead** and **WSPMemoryRegistrationCacheCallback** functions. If a SAN service provider does not support either the **WSPRdmaRead** or **WSPMemoryRegistrationCacheCallback** extension function, its **WSPIoctl** function must return the error WSAEOPNOTSUPP when the Windows Sockets switch requests the entry point to either **WSPRdmaRead** or **WSPMemoryRegistrationCacheCallback**.

<a href="" id="wspstartupex"></a>[**WSPStartupEx**](https://msdn.microsoft.com/library/windows/hardware/ff566321)  
Initiates the Windows Sockets switch's use of a SAN service provider.

<a href="" id="wspregistermemory"></a>[**WSPRegisterMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566311)  
Registers a buffer array that a socket uses as either the local source or the local target of a data transfer operation. Such a socket can use this buffer array as the source buffer in **WSPRdmaWrite** and **WSPSend** calls and the receiving buffer in **WSPRdmaRead** and **WSPRecv** calls.

<a href="" id="wspderegistermemory"></a>[**WSPDeregisterMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566279)  
Releases a buffer array that was registered by a previous call to the **WSPRegisterMemory** function.

<a href="" id="wspregisterrdmamemory"></a>[**WSPRegisterRdmaMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566313)  
Registers an RDMA buffer array that is exposed to a remote peer connection for transferring data to or from that peer connection. A socket at the remote peer can use this RDMA buffer array as the target buffer in a **WSPRdmaWrite** call and the source buffer in a **WSPRdmaRead** call.

<a href="" id="wspderegisterrdmamemory"></a>[**WSPDeregisterRdmaMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566281)  
Releases a buffer array that was registered by a previous call to the **WSPRegisterRdmaMemory** function.

<a href="" id="--------wspmemoryregistrationcachecallback"></a>[**WSPMemoryRegistrationCacheCallback**](https://msdn.microsoft.com/library/windows/hardware/ff566299)  
Releases ownership of an application's buffer and the lock between the buffer and physical memory and removes the buffer from the SAN service provider's cache and the buffer registration from the SAN NIC.

<a href="" id="wsprdmaread"></a>[**WSPRdmaRead**](https://msdn.microsoft.com/library/windows/hardware/ff566304)  
Transfers data from an RDMA buffer in the address space that a socket's remote peer can access to a buffer in the address space that the local socket can access.

<a href="" id="wsprdmawrite"></a>[**WSPRdmaWrite**](https://msdn.microsoft.com/library/windows/hardware/ff566306)  
Transfers data from a source buffer in the address space that a local socket can access to a target RDMA buffer in the address space that the socket's remote peer can access.

 

 





