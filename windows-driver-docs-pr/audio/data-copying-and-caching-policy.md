---
Description: Data Copying and Caching Policy
MS-HAID: 'audio.data\_copying\_and\_caching\_policy'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Data Copying and Caching Policy
---

# Data Copying and Caching Policy


A WaveCyclic miniport driver copies audio data between the DMA buffer, which the HD Audio controller hardware accesses, and the client buffer, which the user-mode audio application accesses:

-   For a playback data stream, the driver copies data from the client buffer to the DMA buffer.

-   For a capture data stream, the driver copies data from the DMA buffer to the client buffer.

For both playback and capture streams, the driver can achieve the best performance by enabling caching of the DMA buffer memory (cache type **MmCached**) and relying on the PCI controller's bus-snooping mechanism to ensure cache coherency. However, some PCI Express controller implementations do not snoop the HD Audio controller's isochronous data transfers (such as Intel's initial PCI Express chipset).

The function driver cannot detect whether the PCI controller hardware supports snooping of DMA buffer transfers or performs isochronous data transfers. To avoid potential cache coherency problems, the driver disables caching of the DMA buffer memory by specifying the caching type for that memory as **MmWriteCombined**. (**MmNonCached** would also work, but might not perform as well.) If you write a custom adapter driver that is based on the sample function driver, your WaveCyclic miniport driver should behave similarly unless you can verify that the PCI controller does in fact support snooping of DMA buffer transfers.

To support devices and systems that do not perform bus snooping, a custom function driver must follow these rules:

-   For a playback stream, specify the DMA buffer's cache type as **MmWriteCombined**. After copying a block of data from the client buffer to the DMA buffer, call the [**KeMemoryBarrier**](kernel.kememorybarrier) function to make the data visible to the DMA engine. **KeMemoryBarrier** flushes the copied data to memory in an efficient way that leaves the processor's data caches largely undisturbed.

-   For a capture stream, specify the DMA buffer's cache type as either **MmWriteCombined** or **MmNonCached**. In addition, the function driver should avoid writing to the DMA buffer. If it must perform in-place processing of audio samples, it should first copy the data elsewhere.

The block of data that the function driver copies to or from the DMA buffer is not required to begin or end on a write-combining buffer boundary, and its size is not required to be a multiple of the write-combining buffer size (typically, 32 or 64 bytes).

For codec function drivers that use the [**HDAUDIO\_BUS\_INTERFACE\_BDL**](audio.hdaudio_bus_interface_bdl) version of the DDI, the [**AllocateContiguousDmaBuffer**](audio.allocatecontiguousdmabuffer) routine performs both the allocation and mapping of the DMA buffer memory. The routine always sets the buffer's cache type to **MmWriteCombined**.

For more information about write-combining, see the IA-32 Intel Architecture Software Developer's Manual at the [Intel](http://go.microsoft.com/fwlink/p/?linkid=38518) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Data%20Copying%20and%20Caching%20Policy%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



