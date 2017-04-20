---
title: WavePci Miniport Driver
description: WavePci Miniport Driver
ms.assetid: 8a166087-d158-4d49-a917-2a5a78b43cb4
keywords:
- audio miniport drivers WDK , WavePci
- miniport drivers WDK audio , WavePci
- WavePci miniport drivers WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20WavePci%20Miniport%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


