---
title: Wave Filters
description: Wave Filters
ms.assetid: 9e364c8f-55c3-4ec9-a9ce-9ee0f6a0746b
keywords:
- audio filters WDK audio , wave
- wave filters WDK audio
- filters WDK audio , wave
- wave-rendering filters WDK audio
- wave-capture filters WDK audio
- rendering wave audio WDK audio
- capturing wave audio WDK audio
- WaveRT filters WDK audio
- WavePci filters WDK audio
- WaveCyclic filters WDK audio
- WaveRT, filter
- WavePci, filter
- audio devices, WaveCyclic
- WaveCyclic, filter
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# Wave Filters


## <span id="wave_filters"></span><span id="WAVE_FILTERS"></span>


Wave filters represent devices that render and/or capture wave-formatted digital audio data. Applications typically access the capabilities of these devices either through the DirectSound API or through the Microsoft Windows multimedia waveOut*Xxx* and waveIn*Xxx* functions. For information about the wave formats that WDM audio drivers can support, see [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) and [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802).

A *wave-rendering* filter receives as input a wave digital audio stream and outputs either an analog audio signal (to a set of speakers or external mixer) or a digital audio stream (to an S/PDIF connector, for example).

A *wave-capture* filter receives as input either an analog audio signal (from a microphone or input jack) or a digital stream (from an S/PDIF connector, for example). The same filter outputs a wave stream containing digital-audio data.

A single wave filter can perform both rendering and capture simultaneously. This type of filter might, for example, represent an audio device that can play audio through a set of speakers and record audio through a microphone at the same time. Alternately, the wave-rendering and wave-capture hardware might be represented as separate wave filters, as described in [Dynamic Audio Subdevices](dynamic-audio-subdevices.md).

An audio adapter driver forms a wave filter by binding a wave miniport driver, which the hardware vendor implements as part of the adapter driver, with a wave port driver, which the system implements. The miniport driver handles all the hardware-specific operations for the wave filter, and the port driver manages all the generic wave-filter functions.

The PortCls system driver (Portcls.sys) implements three wave port drivers: WaveRT, WavePci, and WaveCyclic.

The three types of wave filter operate as follows:

-   A *WaveRT* filter allocates a buffer for wave data and makes that buffer directly accessible to the user-mode client. The buffer can consist of contiguous or noncontiguous blocks of memory, depending on the hardware capabilities of the wave device. The client accesses the buffer as a contiguous block of virtual memory. The buffer is cyclic, which means that when the device's read (for rendering) or write (for capture) pointer reaches the end of the buffer, it automatically wraps around to the beginning of the buffer.

-   A *WavePci* filter directly accesses the client's buffer. Although the client accesses the buffer as a single, contiguous block of virtual memory, the WavePci filter must access the buffer as a series of possibly noncontiguous memory blocks. Blocks containing successive portions of the rendering or capture stream are queued up at the device. When the device's read or write pointer reaches the end of one block, it moves to the beginning of the next block in the queue.

-   A *WaveCyclic* filter allocates a buffer consisting of a single, contiguous block of memory for use as its output (for rendering) or input (for capture) buffer. This buffer is cyclic. Because the buffer is not directly accessible to the client, the driver must copy data between the driver's cyclic buffer and the client's user-mode buffer.

WaveRT is preferred over WavePci and WaveCyclic. WavePci and WaveCyclic were used with earlier versions of Windows.

A WaveRT filter can represent an audio device that resides on a system bus, such as PCI or PCI Express. The primary advantage of a WaveRT filter over a WaveCyclic or WavePci filter is that a WaveRT filter allows a user-mode client to exchange audio data directly with the audio hardware. In contrast, WaveCyclic and WavePci filters both require periodic software intervention by the driver, which increases the latency of the audio stream. In addition, audio devices both with and without scatter/gather DMA capabilities can be represented as WaveRT filters. For more information, see the [A Wave Port Driver for Real-Time Audio Streaming](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/WaveRTport.doc) white paper.


### <span id="wavert_filter"></span><span id="WAVERT_FILTER"></span>WaveRT Filters

A WaveRT filter is implemented as a port/miniport driver pair. In Windows Vista and later, a WaveRT filter factory creates a WaveRT filter as follows:

-   It instantiates a WaveRT miniport driver object.

-   It instantiates a WaveRT port driver object by calling [**PcNewPort**](https://msdn.microsoft.com/library/windows/hardware/ff537715) with GUID value **CLSID\_PortWaveRT**.

-   It calls the port driver's [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method to bind the miniport driver to the port driver.

The code example in [Subdevice Creation](subdevice-creation.md) illustrates this process. The port and miniport drivers communicate with each other through their [IPortWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536920) and [IMiniportWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536737) interfaces.

For more information, see the [A Wave Port Driver for Real-Time Audio Streaming](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/WaveRTport.doc) white paper.

### <span id="Information_for_previous_versions_of_Windows"></span><span id="information_for_previous_versions_of_windows"></span><span id="INFORMATION_FOR_PREVIOUS_VERSIONS_OF_WINDOWS"></span>Information for previous versions of Windows

**WaveCyclic Information for previous versions of Windows**

A WaveCyclic filter can represent an audio device that connects to a system bus, such as ISA, PCI, PCI Express, or PCMCIA. As the name "WavePci" implies, a WavePci filter usually represents a device that connects to a PCI bus, although, in principle, a WavePci device might instead connect to an ISA bus, for example. Unlike the simpler devices that are supported by WaveCyclic, a device supported by WavePci must have scatter/gather DMA capabilities. An audio device that resides on PCI bus but lacks scatter/gather DMA can be represented as a WaveCyclic filter but not as a WavePci filter.

**WavePci Information for previous versions of Windows**

A WavePci device is able to perform scatter/gather DMA transfers to or from buffers that can be located at arbitrary memory addresses and that begin and end with arbitrary byte alignments. In contrast, the DMA hardware for a WaveCyclic device requires only the ability to move data to or from a single buffer that the device's miniport driver allocates. A WaveCyclic miniport driver is free to allocate a cyclic buffer that meets the limited capabilities of its DMA channel. For example, the DMA channel for a typical WaveCyclic device might require a buffer that satisfies the following restrictions:

-   The buffer is located in a certain region of the physical address space.

-   The buffer is contiguous in physical as well as in virtual address space.

-   The buffer begins and ends on even four- or eight-byte boundaries.

In return for this simplicity, however, a WaveCyclic device must rely on software copying of data to or from the cyclic buffer, whereas a WavePci device relies on the scatter/gather capabilities of its DMA hardware to avoid such copying. The IRPs that deliver wave audio data to a rendering device or retrieve data from a capture device are accompanied by data buffers, and each of these buffers contains a portion of the audio stream that is being rendered or captured. A WavePci device is able to access these buffers directly through its scatter/gather DMA engine, whereas a WaveCyclic device requires that the data be copied to its cyclic buffer from the IRP, or vice versa.

### <span id="wavepci_filter"></span><span id="WAVEPCI_FILTER"></span>WavePci Filters

**Note: WavePci Information for previous versions of Windows**

A WavePci filter is implemented as a port/miniport driver pair. A WavePci filter factory creates a WavePci filter as follows:

-   It instantiates a WavePci miniport driver object.

-   It instantiates a WavePci port driver object by calling [**PcNewPort**](https://msdn.microsoft.com/library/windows/hardware/ff537715) with GUID value **CLSID\_PortWavePci**.

-   It calls the port driver's [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method to bind the miniport driver to the port driver.

The code example in [Subdevice Creation](subdevice-creation.md) illustrates this process. The port and miniport drivers communicate with each other through their [IPortWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536905) and [IMiniportWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536724) interfaces.

For more information, see [Implementation Issues for WavePci Devices](implementation-issues-for-wavepci-devices.md).

### <span id="wavecyclic_filter"></span><span id="WAVECYCLIC_FILTER"></span>WaveCyclic Filters

**Note: WaveCyclic Information for previous versions of Windows**

A WaveCyclic filter is implemented as a port/miniport driver pair. A WaveCyclic filter factory creates a WaveCyclic filter as follows:

-   It instantiates a WaveCyclic miniport driver object.

-   It instantiates a WaveCyclic port driver object by calling [**PcNewPort**](https://msdn.microsoft.com/library/windows/hardware/ff537715) with GUID value **CLSID\_PortWaveCyclic**.

-   It calls the port driver's [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method to bind the miniport driver to the port driver.

The code example in [Subdevice Creation](subdevice-creation.md) illustrates this process. The port and miniport drivers communicate with each other through their [IPortWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536899) and [IMiniportWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536714) interfaces.

The WaveCyclic filter's cyclic buffer always consists of a contiguous block of virtual memory. The port driver's implementation of the [**IDmaChannel::AllocateBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536553) method always allocates a buffer that is contiguous in both physical and virtual memory address space. If, as mentioned previously, the WaveCyclic device's DMA engine imposes additional constraints on the buffer memory, the miniport driver is free to implement its own buffer-allocation method to meet these constraints.

A WaveCyclic miniport driver that asks for a large buffer (for example, eight physically contiguous memory pages) should be prepared to settle for a smaller buffer size if the operating system denies the original request. An audio device might occasionally be unloaded and reloaded to rebalance system resources (see [Stopping a Device to Rebalance Resources](https://msdn.microsoft.com/library/windows/hardware/ff563877)).

A WaveCyclic device with built-in, bus-mastering DMA hardware is called a *master device*. Alternatively, a WaveCyclic device can be a *subordinate device* with no built-in DMA-hardware capabilities. A subordinate device has to rely on the system DMA controller to perform any data transfers that it requires. For more information about master and subordinate devices, see [IDmaChannel](https://msdn.microsoft.com/library/windows/hardware/ff536547) and [IDmaChannelSlave](https://msdn.microsoft.com/library/windows/hardware/ff536548).

A WaveCyclic miniport driver can implement its own DMA-channel object instead of using the default DMA-channel object, which is created by one of the port driver's New*Xxx*DmaChannel methods:

[**IPortWaveCyclic::NewMasterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536900)

[**IPortWaveCyclic::NewSlaveDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536902)

The adapter driver's custom [IDmaChannel](https://msdn.microsoft.com/library/windows/hardware/ff536547) implementation can perform custom handling of data to meet special hardware constraints. For example, the Windows Multimedia functions use wave formats in which 16-bit samples are always signed values, but the audio-rendering hardware might be designed to use unsigned 16-bit values instead. In this case, the driver's custom [**IDmaChannel::CopyTo**](https://msdn.microsoft.com/library/windows/hardware/ff536558) method can be written to convert the signed source values to the unsigned destination values that the hardware requires. Although this technique can be useful for working around hardware-design flaws, it can also incur a significant cost in software overhead.

For an example of a driver that implements its own DMA-channel object, see the Sb16 sample audio adapter in the WDK. If the constant OVERRIDE\_DMA\_CHANNEL is defined to be **TRUE**, the conditional compilation statements in the source code enable the implementation of a proprietary [IDmaChannel](https://msdn.microsoft.com/library/windows/hardware/ff536547) object, which the driver uses in place of the default IDmaChannel object from the IPortWaveCyclic::New*Xxx*DmaChannel call.

 

 




