---
title: Understanding the WaveRT Port Driver
description: Understanding the WaveRT Port Driver
ms.assetid: 2627615a-3fde-4ed6-9f7f-f6d7e5d82b3b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Understanding the WaveRT Port Driver


The WaveRT port driver combines the simplicity of the previous WaveCyclic port driver with the hardware-accelerated performance of the WavePci port driver.

The WaveRT port driver eliminates the need to continually map and copy audio data by providing its main client (typically, the audio engine) with direct access to the data buffer. This direct access also eliminates the need for the driver to manipulate the data in the audio stream. The WaveRT port driver thus accommodates the needs of the direct memory access (DMA) controllers that some audio devices have.

To distinguish itself from other wave-render and wave-capture devices, the WaveRT port driver registers itself under [**KSCATEGORY\_REALTIME**](https://msdn.microsoft.com/library/windows/hardware/ff548485) in addition to [**KSCATEGORY\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff548261), [**KSCATEGORY\_RENDER**](https://msdn.microsoft.com/library/windows/hardware/ff548493) and [**KSCATEGORY\_CAPTURE**](https://msdn.microsoft.com/library/windows/hardware/ff548325). This self-registration occurs during the installation of the adapter driver.

In Windows Vista and later operating systems, when the operating system starts and the audio engine is initialized, the audio engine enumerates the KS filters that represent the audio devices. During the enumeration, the audio engine instantiates the drivers for the audio devices that it finds. This process results in the creation of filter objects for these devices. For WaveRT audio devices, the resulting filter object has the following components:

-   An instance of the WaveRT port driver to manage the generic system functions for the filter

-   An instance of the WaveRT miniport driver to handle all the hardware-specific functions of the filter

After the filter object is created, the audio engine and the WaveRT miniport driver are ready to open an audio stream for the type of audio processing needed. To prepare the KS filter for audio rendering (playback), for example, the audio engine and the WaveRT miniport driver do the following to open a playback stream:

1.  The audio engine opens a pin on the KS filter, and the WaveRT miniport driver creates an instance of the pin. When the audio engine opens the pin, it also passes the wave format of the stream to the driver. The driver uses the wave format information to select the proper buffer size in the next step.

2.  The audio engine sends a request to the miniport driver for a cyclic buffer of a particular size to be created. The term *cyclic buffer* refers to the fact that when the buffer position register reaches the end of the buffer in a playback or record operation, the position register can automatically wrap around to the beginning of the buffer. Unlike the WaveCyclic miniport driver that sets up a contiguous block of physical memory, the WaveRT miniport driver does not need a buffer that is contiguous in physical memory. The driver uses the [**KSPROPERTY\_RTAUDIO\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff537370) property to allocate space for the buffer. If the hardware of the audio device cannot stream from a buffer of the requested size, the driver works within the resource limitations of the audio device to create a buffer that is the closest in size to the originally requested size. The driver then maps the buffer into the DMA engine of the audio device and makes the buffer accessible to the audio engine in user-mode.

3.  The audio engine schedules a thread to periodically write audio data to the cyclic buffer.

4.  If the hardware of the audio device does not provide direct support for cyclic buffers, the miniport driver periodically reprograms the audio device to keep using the same buffer. For example, if the hardware does not support buffer looping, the driver must set the DMA address back to the start of the buffer each time it reaches the end of the buffer. This update can be done in either an interrupt service routine (ISR) or a high-priority thread.

The resulting configuration supplies a glitch-resilient audio signal on audio device hardware that either supports cyclic buffers or works with the miniport driver to regularly update its hardware.

To prepare a KS filter for audio capture (recording), the audio engine and the WaveRT miniport driver use similar steps to open a record stream.

One of the performance improvements provided by the WaveRT port driver is a reduction in the delay in the end-to-end processing of the audio stream during wave-render or wave-capture. This delay is referred to as stream latency.

For more information about these two types of stream latency, see the following topics.

-   [Stream Latency during Playback](stream-latency-during-playback.md)

-   [Stream Latency during Recording](stream-latency-during-recording.md)

For information about how to develop a WaveRT miniport driver that complements the WaveRT port driver, see the [Developing a WaveRT Miniport Driver](developing-a-wavert-miniport-driver.md) topic.

 

 




