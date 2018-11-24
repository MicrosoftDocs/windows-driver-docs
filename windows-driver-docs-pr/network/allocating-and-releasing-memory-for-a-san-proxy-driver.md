---
title: Allocating and Releasing Memory for a SAN Proxy Driver
description: Allocating and Releasing Memory for a SAN Proxy Driver
ms.assetid: c196f202-159c-4296-9888-818eaeaada73
keywords:
- proxy drivers WDK SANs , memory allocations
- SAN proxy drivers WDK , memory allocations
- memory allocations WDK SANs
- releasing memory for SAN proxy drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating and Releasing Memory for a SAN Proxy Driver





The proxy driver must set up access to user buffers so that the Windows Sockets switch can transfer control messages and perform RDMA operations. To request this type of buffer access, the proxy driver sets a bit in the **Flags** member of its device object to DO\_DIRECT\_IO. The proxy driver must also allocate or release memory that is used for message transfer and RDMA whenever requested to do so. When the Windows Sockets switch requests a SAN service provider to register or release memory, the SAN service provider requests its proxy driver to respectively allocate or release physical memory. For more information about setting up buffer access and allocating and releasing memory, see [Memory Management](https://msdn.microsoft.com/library/windows/hardware/ff554389) and [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).

### Allocating Low Memory for RDMA

A proxy driver must allocate memory that can be accessed for RDMA operations. The proxy driver can allocate low memory for RDMA operations even on an system that is configured so that no physical memory below 4 GB can be allocated. (This is called a NOLOWMEM configuration.) The proxy driver calls either the [**MmAllocateContiguousMemorySpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554464) function or its own DMA [**AllocateCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff540575) function to retrieve low memory.

To retrieve a pointer to its DMA **AllocateCommonBuffer** function, the proxy driver performs the following steps:

1.  Zero-initializes a [**DEVICE\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff543107) structure and then writes relevant information for its SAN NIC to this structure.

2.  Calls [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220) to retrieve a pointer to the DMA adapter structure for its SAN NIC. In this call, the driver passes a pointer to the filled-in DEVICE\_DESCRIPTION structure. **IoGetDmaAdapter** returns a pointer to a DMA adapter structure that contains a pointer to a [**DMA\_OPERATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff544071) structure. DMA\_OPERATIONS contains pointers to a system-defined set of DMA functions. One of these functions is **AllocateCommonBuffer**, which allocates a physically contiguous DMA buffer.

 

 





