---
title: WavePci Miniport Driver
description: WavePci Miniport Driver
keywords:
- audio miniport drivers WDK , WavePci
- miniport drivers WDK audio , WavePci
- WavePci miniport drivers WDK audio
ms.date: 04/20/2017
---

# WavePci Miniport Driver


## <span id="wavepci_miniport_driver"></span><span id="WAVEPCI_MINIPORT_DRIVER"></span>


**Important**  The use of WavePci is no longer recommended, instead use WaverRT.

 

A WavePci miniport driver manages the hardware-dependent functions of a wave-rendering or wave-capture device that has scatter/gather DMA hardware that can transfer audio data to or from any location in physical memory. A wave device that lacks the ability to perform scatter/gather transfers or is able to access only restricted regions in physical memory should use a [WaveCyclic miniport driver](wavecyclic-miniport-driver.md) instead.

A WavePci miniport driver should implement two interfaces:

-   **The miniport interface** performs miniport driver initialization, channel enumeration, and stream creation.

-   **The stream interface** manages a wave stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportWavePci](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavepci), inherits the methods in the [IMiniport](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiport) interface. IMiniportWavePci provides the following additional methods:

[**IMiniportWavePci::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-init)

Initializes the miniport object.

[**IMiniportWavePci::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-newstream)

Creates a new stream object.

[**IMiniportWavePci::Service**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-service)

Notifies the miniport driver of a request for service.

The stream interface, [IMiniportWavePciStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavepcistream), inherits the methods from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. IMiniportWavePciStream provides the following additional methods:

[**IMiniportWavePciStream::GetAllocatorFraming**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-getallocatorframing)

Gets the miniport driver's preferred allocator-framing parameters for the wave stream.

[**IMiniportWavePciStream::GetPosition**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-getposition)

Gets the device's current position in the wave stream.

[**IMiniportWavePciStream::MappingAvailable**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-mappingavailable)

Indicates that a new mapping is available from the port driver.

[**IMiniportWavePciStream::NormalizePhysicalPosition**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-normalizephysicalposition)

Converts a physical buffer position value into a time-based value.

[**IMiniportWavePciStream::RevokeMappings**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-revokemappings)

Revokes previously issued mappings.

[**IMiniportWavePciStream::Service**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-service)

Notifies the stream object of a request for service.

[**IMiniportWavePciStream::SetFormat**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-setformat)

Sets the data format of the wave stream.

[**IMiniportWavePciStream::SetState**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-setstate)

Sets the state of the wave stream.
 

