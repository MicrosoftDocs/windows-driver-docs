---
title: Data Copying and Caching Policy
description: Data Copying and Caching Policy
ms.assetid: 1867f2bd-240c-4525-9f02-98b8f1d54b17
keywords:
- HD Audio, caching
- High Definition Audio (HD Audio), caching
- cache WDK audio
- bus snooping WDK audio
- snooping WDK audio
- memory WDK audio
- copying audio data
- data copying WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Copying and Caching Policy


A WaveCyclic miniport driver copies audio data between the DMA buffer, which the HD Audio controller hardware accesses, and the client buffer, which the user-mode audio application accesses:

-   For a playback data stream, the driver copies data from the client buffer to the DMA buffer.

-   For a capture data stream, the driver copies data from the DMA buffer to the client buffer.

For both playback and capture streams, the driver can achieve the best performance by enabling caching of the DMA buffer memory (cache type **MmCached**) and relying on the PCI controller's bus-snooping mechanism to ensure cache coherency. However, some PCI Express controller implementations do not snoop the HD Audio controller's isochronous data transfers (such as Intel's initial PCI Express chipset).

The function driver cannot detect whether the PCI controller hardware supports snooping of DMA buffer transfers or performs isochronous data transfers. To avoid potential cache coherency problems, the driver disables caching of the DMA buffer memory by specifying the caching type for that memory as **MmWriteCombined**. (**MmNonCached** would also work, but might not perform as well.) If you write a custom adapter driver that is based on the sample function driver, your WaveCyclic miniport driver should behave similarly unless you can verify that the PCI controller does in fact support snooping of DMA buffer transfers.

To support devices and systems that do not perform bus snooping, a custom function driver must follow these rules:

-   For a playback stream, specify the DMA buffer's cache type as **MmWriteCombined**. After copying a block of data from the client buffer to the DMA buffer, call the [**KeMemoryBarrier**](https://msdn.microsoft.com/library/windows/hardware/ff552971) function to make the data visible to the DMA engine. **KeMemoryBarrier** flushes the copied data to memory in an efficient way that leaves the processor's data caches largely undisturbed.

-   For a capture stream, specify the DMA buffer's cache type as either **MmWriteCombined** or **MmNonCached**. In addition, the function driver should avoid writing to the DMA buffer. If it must perform in-place processing of audio samples, it should first copy the data elsewhere.

The block of data that the function driver copies to or from the DMA buffer is not required to begin or end on a write-combining buffer boundary, and its size is not required to be a multiple of the write-combining buffer size (typically, 32 or 64 bytes).

For codec function drivers that use the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) version of the DDI, the [**AllocateContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536178) routine performs both the allocation and mapping of the DMA buffer memory. The routine always sets the buffer's cache type to **MmWriteCombined**.

For more information about write-combining, see the IA-32 Intel Architecture Software Developer's Manual at the [Intel](https://go.microsoft.com/fwlink/p/?linkid=38518) website.

 

 




