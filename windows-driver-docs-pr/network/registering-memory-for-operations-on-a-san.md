---
title: Registering Memory for Operations on a SAN
description: Registering Memory for Operations on a SAN
ms.assetid: 5492466e-4765-4d43-b6bc-1d5bc74996ba
keywords:
- SAN connection setup WDK , registering memory
- registering memory for SANs
- data buffers WDK SANs
- buffers WDK SANs
- registering data buffers
- memory WDK SANs
- registered memory WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Memory for Operations on a SAN





The Windows Sockets switch calls a SAN service provider's extension functions to register all data buffers for sending and receiving messages and for RDMA operations on a system area network. These extension functions register a buffer to a region of physical memory for use on a particular SAN socket that is connected to a remote peer. For a description of these extension functions, see the [Windows Sockets SPI Extensions for SANs](windows-sockets-spi-extensions-for-sans.md).

### Registering Data Buffers

The switch calls a SAN service provider's [**WSPRegisterMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566311) extension function on behalf of an application that runs in a local process to register data buffers that can be accessed only by that process. The buffer handles that **WSPRegisterMemory** returns are valid only in the context of the local process that performed the registration. The switch calls **WSPRegisterMemory** to register buffers that serve as the message receiving buffer in a call to the [**WSPRecv**](https://msdn.microsoft.com/library/windows/hardware/ff566309) function or the message sending buffer in a call to the [**WSPSend**](https://msdn.microsoft.com/library/windows/hardware/ff566316) function. The switch also calls **WSPRegisterMemory** to register buffers that serve as the local receiving RDMA buffer in a call to the [**WSPRdmaRead**](https://msdn.microsoft.com/library/windows/hardware/ff566304) extension function or the local RDMA source in a call to the [**WSPRdmaWrite**](https://msdn.microsoft.com/library/windows/hardware/ff566306) extension function. After the local process finishes using buffers that were registered with **WSPRegisterMemory**, the switch calls the [**WSPDeregisterMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566279) extension function to release those buffers.

The switch calls the SAN service provider's [**WSPRegisterRdmaMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566313) extension function on behalf of an application that runs in a local process to register RDMA buffers that both local and remote processes can access. The buffer descriptors that **WSPRegisterRdmaMemory** returns are valid only for RDMA data transfer operations that a remote peer initiates in the context of the peer's connection to the SAN socket on which the registration was performed. The switch at the remote peer connection uses these RDMA buffers as either the target in a call to the **WSPRdmaWrite** extension function or the source in a call to the **WSPRdmaRead** extension function. After the local and remote processes finish using buffers that were registered with **WSPRegisterRdmaMemory**, the switch calls the [**WSPDeregisterRdmaMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566281) extension function to release those buffers.

### Managing Memory Access

A SAN service provider must prevent unauthorized access to registered memory.

Memory must be registered and accessible as follows:

Memory registered for local access should be available only to the process in which the switch called **WSPRegisterMemory**.

Memory registered for both local and remote access can be accessed by either the process in which the switch called **WSPRegisterRdmaMemory** to register memory, or by the remote peer that is connected to the SAN socket to which the memory is registered.

Memory must be accessible only while registered and while the connection is established. A SAN service provider must ensure that it does not inadvertently make such memory accessible to other processes running on the same computer or on other computers on the SAN.

Memory registered only for read access must not be available for write access. Memory registered only for write access must not be available for read access.

### Using Registered Memory

The switch registers two virtually contiguous regions of memory for each connected TCP socket to use for negotiating a data-transfer session. The switch uses one region of memory to provide message buffers containing send data when calling a SAN service provider's **WSPSend** function. The switch uses the other region of memory to post message buffers to receive data when calling a SAN service provider's **WSPRecv** function.

The switch typically registers RDMA buffers only if it transfers application data in RDMA operations.

Before the switch closes a socket, the switch calls either **WSPDeregisterMemory** or **WSPDeregisterRdmaMemory** functions of a SAN service provider to release any memory that a pending data transfer operation is not currently using. The SAN service provider must also release memory associated with outstanding data transfer operations.

 

 





