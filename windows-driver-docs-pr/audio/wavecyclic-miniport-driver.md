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

The miniport interface, [IMiniportWaveCyclic](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiportwavecyclic), inherits the methods in the [IMiniport](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiport) interface. IMiniportWaveCyclic provides the following additional methods:

[**IMiniportWaveCyclic::Init**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavecyclic-init)

Initializes the miniport object.

[**IMiniportWaveCyclic::NewStream**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavecyclic-newstream)

Creates a new stream object.

The stream interface, [IMiniportWaveCyclicStream](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiportwavecyclicstream), inherits the methods in the [**IUnknown**](https://docs.microsoft.com/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. IMiniportWaveCyclicStream provides the following additional methods:

[**IMiniportWaveCyclicStream::GetPosition**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavecyclicstream-getposition)

Gets the device's current position in the wave stream.

[**IMiniportWaveCyclicStream::NormalizePhysicalPosition**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavecyclicstream-normalizephysicalposition)

Converts a physical buffer position value into a time-based value.

[**IMiniportWaveCyclicStream::SetFormat**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavecyclicstream-setformat)

Sets the data format of the wave stream.

[**IMiniportWaveCyclicStream::SetNotificationFreq**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavecyclicstream-setnotificationfreq)

Sets the frequency at which notification interrupts occur.

[**IMiniportWaveCyclicStream::SetState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavecyclicstream-setstate)

Sets the state of the wave stream.

[**IMiniportWaveCyclicStream::Silence**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavecyclicstream-silence)

Copies silence into a buffer.
 

 




