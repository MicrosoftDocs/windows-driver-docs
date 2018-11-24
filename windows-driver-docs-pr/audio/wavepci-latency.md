---
title: WavePci Latency
description: WavePci Latency
ms.assetid: 6d83c015-cf8f-40b4-bf28-de865a5bfe2d
keywords:
- WavePci latency WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WavePci Latency


## <span id="wavepci_latency"></span><span id="WAVEPCI_LATENCY"></span>


The WavePci port driver handles buffering of an audio stream differently from the WaveCyclic driver.

If your WavePci miniport driver provides hardware mixing, DirectSound submits an IRP to the WavePci port driver that contains the entire DirectSound wave stream in a single cyclic buffer. DirectSound allocates the buffer as a contiguous block of virtual memory. To avoid copying the DirectSound buffer, the kernel-streaming layer maps the buffer into kernel-mode virtual memory and generates a MDL (memory descriptor list) that specifies both the virtual and physical addresses of the memory pages in the cyclic buffer. The WavePci port driver partitions the cyclic buffer into a sequence of allocator frames (see [KS Allocators](https://msdn.microsoft.com/library/windows/hardware/ff567257)). The miniport driver specifies its preferred allocator-frame size when its [**IMiniportWavePciStream::GetAllocatorFraming**](https://msdn.microsoft.com/library/windows/hardware/ff536726) method is called by the port driver during stream initialization. However, SysAudio, the system graph builder, can override the miniport driver's preferences in order to accommodate the requirements of the other components in the audio filter graph.

The WavePci port driver exposes the cyclic buffer to the miniport driver as a sequence of mappings. A mapping is either an entire allocation frame or a portion of a frame. If a particular allocation frame lies completely within a page, the port driver presents that frame to the miniport driver as a single mapping. If an allocation frame straddles one or more page boundaries, the port driver splits the frame at each page boundary and presents it as two or more mappings. Each call to [**IPortWavePciStream::GetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff536909) yields the next successive mapping in the sequence.

In contrast to the WaveCyclic case, where the miniport driver has little control over how many milliseconds of data are buffered at the hardware, the WavePci miniport driver has considerable control over the number of mappings that it has open at any time. The number of open mappings increases by one with each call to [**GetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff536909) and decreases by one with each call to [**ReleaseMapping**](https://msdn.microsoft.com/library/windows/hardware/ff536911). (A **GetMapping** call can fail, of course, so the driver has less than total control over the number of mappings.) By controlling the number of open mappings and keeping track of the cumulative the size of the mappings, the miniport driver can determine (within a tolerance dependent on the mapping size) the number of milliseconds of buffering that are available to the hardware. Your WavePci miniport driver should request enough page mappings to reduce the chances of starvation to acceptable levels.

If your miniport driver's policy is to buffer up to 50 milliseconds of data, for example, between the read and write pointers, remember that this limit represents the maximum amount of data that your driver will accumulate, but it does not and should not represent your driver's contribution to the latency of the stream. Your driver should be designed to keep its latency as small as possible. When a miniport driver obtains its initial set of mappings before starting to play a new stream, the miniport driver can continue to request mappings until it either reaches its buffer limit (50 milliseconds in this example) or no more mappings are immediately available. In the latter case, however, the miniport driver must not wait until more mappings become available before it begins playing the stream. Instead, the driver should immediately begin playing the mappings it has already obtained. Later, as more mappings become available, the driver can continue to acquire additional mappings until either it reaches its buffer-size limit or no more mappings are immediately available.

In general, a WavePci device's DMA hardware should be designed to directly access audio frames that are stored at arbitrary byte alignments and that straddle boundaries between noncontiguous pages of physical memory. If you have a device that requires that the mappings be an integral number of audio frames, that device is limited in the kinds of audio formats that it supports. Of course, a device with this limitation should still be able to handle an audio frame size that is a power of two.

For example, a device with four channels and a 16-bit sample size requires an audio-frame size of eight bytes. An integral number of audio frames fits neatly within a page (or any other allocation-frame size that is a multiple of eight bytes). However, in the case of a 5.1-channel stream with 16-bit samples, the audio frame size is 12 bytes and a stream that exceeds the size of a single page necessarily contains audio frames that straddle page boundaries. (The figures in [Wave Filters](wave-filters.md) illustrate this problem.) Hardware that cannot handle arbitrary byte alignments and arbitrary byte-length mappings must depend on the driver to perform an intermediate copy, which degrades performance.

The Ac97 sample adapter driver in the Microsoft Windows Driver Kit (WDK) implements a [**GetAllocatorFraming**](https://msdn.microsoft.com/library/windows/hardware/ff536726) method. The miniport driver uses this method to communicate its preferred frame-allocation size. In Windows 2000 and Windows Me, the port driver calls this method only when the [Splitter system driver](kernel-mode-wdm-audio-components.md#splitter_system_driver) (Splitter.sys) is instantiated above the output pin. In Windows XP and later, the port driver calls this method for input streams as well. Remember that SysAudio might choose to ignore the miniport driver's preferences when deciding on a frame-allocation size.

 

 




