---
title: WaveCyclic Miniport Driver
description: WaveCyclic Miniport Driver
ms.assetid: 8a4811e9-e52b-4183-8d11-482883500f82
keywords:
- audio miniport drivers WDK , WaveCyclic
- miniport drivers WDK audio , WaveCyclic
- WaveCyclic miniport drivers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WaveCyclic Miniport Driver


## <span id="wavecyclic_miniport_driver"></span><span id="WAVECYCLIC_MINIPORT_DRIVER"></span>


**Important**  The use of WavePci is no longer recommended, instead use WaverRT.

 

A WaveCyclic miniport driver manages the hardware-dependent functions of a wave-rendering or wave-capture device that uses a cyclic buffer for audio data. The cyclic buffer is typically a single block of contiguous physical memory and can be located in a region of memory of the driver's choosing. A device with any of the following limitations should provide a WaveCyclic miniport driver rather than a [WavePci miniport driver](wavepci-miniport-driver.md):

-   The device lacks DMA hardware.

-   The device's DMA hardware can access data only in a buffer that occupies a single block of contiguous physical memory.

-   The device's DMA hardware is unable to access data in all regions of physical memory.

A WaveCyclic miniport driver should implement two interfaces:

-   **The miniport interface** supports miniport driver initialization and stream creation.

-   **The stream interface** manages a wave stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536714), inherits the methods in the [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698) interface. IMiniportWaveCyclic provides the following additional methods:

[**IMiniportWaveCyclic::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536722)

Initializes the miniport object.

[**IMiniportWaveCyclic::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536723)

Creates a new stream object.

The stream interface, [IMiniportWaveCyclicStream](https://msdn.microsoft.com/library/windows/hardware/ff536715), inherits the methods in the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. IMiniportWaveCyclicStream provides the following additional methods:

[**IMiniportWaveCyclicStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536716)

Gets the device's current position in the wave stream.

[**IMiniportWaveCyclicStream::NormalizePhysicalPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536717)

Converts a physical buffer position value into a time-based value.

[**IMiniportWaveCyclicStream::SetFormat**](https://msdn.microsoft.com/library/windows/hardware/ff536718)

Sets the data format of the wave stream.

[**IMiniportWaveCyclicStream::SetNotificationFreq**](https://msdn.microsoft.com/library/windows/hardware/ff536719)

Sets the frequency at which notification interrupts occur.

[**IMiniportWaveCyclicStream::SetState**](https://msdn.microsoft.com/library/windows/hardware/ff536720)

Sets the state of the wave stream.

[**IMiniportWaveCyclicStream::Silence**](https://msdn.microsoft.com/library/windows/hardware/ff536721)

Copies silence into a buffer.
 

 




