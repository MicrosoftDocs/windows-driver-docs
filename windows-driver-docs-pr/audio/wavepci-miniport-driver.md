---
title: WavePci Miniport Driver
description: WavePci Miniport Driver
ms.assetid: 8a166087-d158-4d49-a917-2a5a78b43cb4
keywords:
- audio miniport drivers WDK , WavePci
- miniport drivers WDK audio , WavePci
- WavePci miniport drivers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WavePci Miniport Driver


## <span id="wavepci_miniport_driver"></span><span id="WAVEPCI_MINIPORT_DRIVER"></span>


**Important**  The use of WavePci is no longer recommended, instead use WaverRT.

 

A WavePci miniport driver manages the hardware-dependent functions of a wave-rendering or wave-capture device that has scatter/gather DMA hardware that can transfer audio data to or from any location in physical memory. A wave device that lacks the ability to perform scatter/gather transfers or is able to access only restricted regions in physical memory should use a [WaveCyclic miniport driver](wavecyclic-miniport-driver.md) instead.

A WavePci miniport driver should implement two interfaces:

-   **The miniport interface** performs miniport driver initialization, channel enumeration, and stream creation.

-   **The stream interface** manages a wave stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536724), inherits the methods in the [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698) interface. IMiniportWavePci provides the following additional methods:

[**IMiniportWavePci::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536734)

Initializes the miniport object.

[**IMiniportWavePci::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536735)

Creates a new stream object.

[**IMiniportWavePci::Service**](https://msdn.microsoft.com/library/windows/hardware/ff536736)

Notifies the miniport driver of a request for service.

The stream interface, [IMiniportWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536725), inherits the methods from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. IMiniportWavePciStream provides the following additional methods:

[**IMiniportWavePciStream::GetAllocatorFraming**](https://msdn.microsoft.com/library/windows/hardware/ff536726)

Gets the miniport driver's preferred allocator-framing parameters for the wave stream.

[**IMiniportWavePciStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536727)

Gets the device's current position in the wave stream.

[**IMiniportWavePciStream::MappingAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff536728)

Indicates that a new mapping is available from the port driver.

[**IMiniportWavePciStream::NormalizePhysicalPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536729)

Converts a physical buffer position value into a time-based value.

[**IMiniportWavePciStream::RevokeMappings**](https://msdn.microsoft.com/library/windows/hardware/ff536730)

Revokes previously issued mappings.

[**IMiniportWavePciStream::Service**](https://msdn.microsoft.com/library/windows/hardware/ff536731)

Notifies the stream object of a request for service.

[**IMiniportWavePciStream::SetFormat**](https://msdn.microsoft.com/library/windows/hardware/ff536732)

Sets the data format of the wave stream.

[**IMiniportWavePciStream::SetState**](https://msdn.microsoft.com/library/windows/hardware/ff536733)

Sets the state of the wave stream.
 

 




