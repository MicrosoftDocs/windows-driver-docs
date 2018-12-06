---
title: Caching Registered Memory
description: Caching Registered Memory
ms.assetid: e1040f6a-6e65-462a-a79a-5d05d36787b0
keywords:
- SAN connection setup WDK , caching registered memory
- RDMA buffer caching WDK SANs
- cache RDMA buffers WDK SANs
- registered memory WDK SANs
- local access registered memory caching WDK SANs
- remote access registered memory caching WDK SANs
- memory WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Caching Registered Memory





SAN service providers can cache RDMA buffers that are exposed for either local or remote access to improve performance.

### Caching RDMA Buffers Exposed for Local Access

The Windows Sockets switch calls a SAN service provider's [**WSPRegisterMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566311) extension function on behalf of an application to register all data buffers that serve as either the local receiving RDMA buffer in a call to the [**WSPRdmaRead**](https://msdn.microsoft.com/library/windows/hardware/ff566304) extension function or the local RDMA source in a call to the [**WSPRdmaWrite**](https://msdn.microsoft.com/library/windows/hardware/ff566306) extension function. As part of this registration process, the SAN service provider must lock down these buffers to regions of physical memory and register them with the SAN NIC. Both of these operations are resource intensive. Therefore, the SAN service provider should use caching to reduce the overhead of these registrations. If the SAN service provider uses caching, the performance of applications that reuse buffers for data transfers improves.

SAN service providers should cache and release RDMA buffers that are exposed for local access as described in the following list:

1.  When the switch calls the [**WSPDeregisterMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566279) extension function to release a buffer, the SAN service provider should leave the buffer registered with the SAN NIC and locked down to a region of physical memory. The SAN service provider should also add the buffer to a cache of registered buffers, in case the buffer is used again in a subsequent RDMA operation, and secure possession of the buffer as described in the next list item.

2.  A SAN service provider caches memory registrations based on virtual addresses. When the SAN service provider caches a buffer's registration, the SAN service provider's proxy driver must call the [**MmSecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556374) function to secure possession of that registered buffer so that the operating system notifies the switch if the buffer is released (for example, if an application calls the **VirtualFree** function to release a virtual address range back to the operating system).

3.  When the switch subsequently calls **WSPRegisterMemory** to register a buffer, the SAN service provider should check its cache to determine if the buffer is already registered. If the SAN service provider finds the buffer in its cache, the SAN service provider should not perform any further registration action.

4.  Before the virtual-to-physical mappings of the registered buffer subsequently change, the switch calls each SAN service provider's [**WSPMemoryRegistrationCacheCallback**](https://msdn.microsoft.com/library/windows/hardware/ff566299) extension function. Each SAN service provider's proxy driver, in turn, must call the [**MmUnsecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556395) function to release ownership of the buffer. In addition, each SAN service provider must remove the buffer from its cache and must remove the buffer registration from the SAN NIC.

5.  Before the connection between a local SAN socket and a remote peer is closed, the SAN service provider should release any cached buffers.

**Note**  The proxy driver must use the **try/except** mechanism around code that accesses a user-mode buffer that was secured through a call to **MmSecureVirtualMemory** to prevent operating system crashes. For more information about how a proxy driver secures and releases buffers, see [Securing and Releasing Ownership of Virtual Addresses](securing-and-releasing-ownership-of-virtual-addresses.md). For more information about **try/except**, see the Visual C++ documentation. For information about **VirtualFree**, see the Microsoft Windows SDK documentation.

 

### Caching RDMA Buffers Exposed for Remote Access

The Windows Sockets switch calls a SAN service provider's [**WSPRegisterRdmaMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566313) extension function to register all data buffers that serve as either the remote RDMA target of a remote **WSPRdmaWrite** call or the remote RDMA source of a remote **WSPRdmaRead** call. That is, the switch exposes these buffers for access by a remote peer. After data transfers from these buffers are completed, the switch calls the SAN service provider's [**WSPDeregisterRdmaMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566281) extension function to release these buffers so that they are no longer accessible from the remote peer.

SAN service providers should cache RDMA buffers that are exposed for remote access as described in the following list:

1.  When the Switch calls **WSPDeregisterRdmaMemory** to release a buffer, the SAN service provider should leave the buffer locked in physical memory and registered with the SAN NIC. The SAN service provider should also add the buffer to a cache of registered buffers, in case the buffer is used again in a subsequent RDMA operation. However, the SAN service provider should take appropriate action to ensure that the remote peer can no longer access the buffer.
    **Note**  If the buffer can only be made inaccessible by the SAN service provider removing the buffer registration from the SAN NIC, the SAN service provider must do so. However, the SAN service provider should leave the buffer locked down to a region of physical memory. This scenario does not provide the best possible performance but is better than no caching.

     

2.  To cache RDMA buffers exposed for remote access, the SAN service provider and its proxy driver should use the caching techniques as described in the preceding list for RDMA buffers that are exposed for local access.

3.  When the switch subsequently calls **WSPRegisterRdmaMemory** to register a buffer, the SAN service provider should check its cache to determine if the buffer is already registered. If the SAN service provider finds the buffer in its cache, the SAN service provider should simply expose the buffer for remote access, no further registration action is required. However, if the buffer registration was previously removed from the SAN NIC, the SAN service provider should register the buffer again.

4.  To release RDMA buffers exposed for remote access, the SAN service provider and its proxy driver should use the techniques as described in the preceding list.

 

 





