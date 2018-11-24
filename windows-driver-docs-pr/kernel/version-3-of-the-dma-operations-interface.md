---
title: Version 3 of the DMA Operations Interface
description: Version 3 of the DMA operations interface is available starting with Windows 8.
ms.assetid: EFB59930-7D58-4E6E-8242-66A326E239E5
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Version 3 of the DMA Operations Interface


Version 3 of the DMA operations interface is available starting with Windows 8. The **DMA\_OPERATIONS** structure for this interface contains a number of new routines that are not defined in previous versions of this interface. For a list of the routines in version 3, see [**DMA\_OPERATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff544071).

Although version 3 of the DMA operations interface is available across all Windows hardware platforms, this interface has many features to enable kernel-mode drivers to use the advanced capabilities of system DMA controllers in System on a Chip (SoC) integrated circuits. These capabilities typically include the ability to do scatter/gather DMA transfers. In contrast, previous versions of the DMA operations interface restrict scatter/gather DMA transfers to bus-master devices. The version-3 interface simplifies the management of scatter/gather lists and reduces the need for driver intervention during complex DMA transfers.

To use version 3 of the DMA operations interface to perform a DMA transfer, a driver typically calls the following routines:

<a href="" id="iogetdmaadapter"></a>[**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220)  
Allocates a DMA adapter object and returns a pointer to a [**DMA\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff544062) structure that contains the DMA operations interface.

<a href="" id="getdmatransferinfo"></a>[**GetDmaTransferInfo**](https://msdn.microsoft.com/library/windows/hardware/hh451125)  
Provides a description of the resources that are required to perform the DMA transfer that is described by the caller.

<a href="" id="allocateadapterchannelex"></a>[**AllocateAdapterChannelEx**](https://msdn.microsoft.com/library/windows/hardware/hh406340)  
Allocates the resources required for the DMA transfer and assigns these resources to the DMA adapter object.

<a href="" id="maptransferex"></a>[**MapTransferEx**](https://msdn.microsoft.com/library/windows/hardware/hh406521)  
Initializes the map registers and the scatter/gather buffer for the DMA transfer, and starts the transfer.

<a href="" id="flushadapterbuffersex"></a>[**FlushAdapterBuffersEx**](https://msdn.microsoft.com/library/windows/hardware/hh451102)  
Performs any cache operations that might be required at the end of the DMA transfer.

<a href="" id="freeadapterchannel"></a>[**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507)  
Frees the DMA channel and map registers.

<a href="" id="putdmaadapter"></a>[**PutDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff559965)  
Releases the adapter object.

These routines are used both for bus-master devices that use dedicated DMA controllers, and for subordinate devices that share a system DMA controller. For a step-by-step description of the calls that a driver makes during a typical DMA transfer, see [Basic Calling Pattern for Version-3 DMA Routines](basic-calling-pattern-for-version-3-dma-routines.md).

**Note**  
In version 3 of the DMA operations interface, calls to the [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041) routine are not required either before or after DMA transfers. The reason is that the following routines cover the need for flushing data caches on platforms that do not enforce cache coherency in hardware:

-   **MapTransferEx** ensures that processor data caches are flushed before write (memory-to-device) transfers.
-   **FlushAdapterBuffersEx** ensures that caches are invalidated after read (device-to-memory) transfers.

On an x86 or x64 processor, the **KeFlushIoBuffers** call performs no operations, and this call, while unnecessary, does not interfere with the operation of the hardware platform. On an ARM processor, calls to **KeFlushIoBuffers** during DMA transfers perform cache operations that are unnecessary and can degrade performance.

 

 

 




