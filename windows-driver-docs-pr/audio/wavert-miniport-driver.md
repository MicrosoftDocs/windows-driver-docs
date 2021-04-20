---
title: WaveRT Miniport Driver
description: WaveRT Miniport Driver
ms.date: 10/01/2020
ms.localizationpriority: medium
---

# WaveRT Miniport Driver


The WaveRT miniport driver is supported in Windows Vista and later Windows operating systems, and it manages the hardware-dependent functions of a wave-rendering or wave-capture audio device. A WaveRT-friendly audio device has scatter/gather DMA hardware that can transfer audio data to or from any location in physical memory.

A WaveRT miniport driver must implement two interfaces:

-   [IMiniportWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavert). This interface performs miniport driver initialization, channel enumeration, and stream creation.

-   [IMiniportWaveRTStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertstream). This interface manages a wave stream and exposes most of the functionality of the miniport driver.

For information about how to design a WaveRT miniport driver that complements the WaveRT port driver, see the [Developing a WaveRT Miniport Driver](developing-a-wavert-miniport-driver.md) topic.

### <span id="iminiportwavert"></span><span id="IMINIPORTWAVERT"></span>IMiniportWaveRT

The [IMiniportWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavert) interface provides the following methods:

[**IMiniportWaveRT::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavert-init)

Initializes the miniport object.

[**IMiniportWaveRT::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavert-newstream)

Creates a new stream object.

[**IMiniportWaveRT::GetDeviceDescription**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavert-getdevicedescription)

Returns a pointer to a [**DEVICE\_DESCRIPTION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_description) structure describing the device.

### <span id="iminiportwavertstream"></span><span id="IMINIPORTWAVERTSTREAM"></span>IMiniportWaveRTStream

The [IMiniportWaveRTStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertstream) interface inherits the methods from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. IMiniportWaveRTStream provides the following additional methods:

[**IMiniportWaveRTStream::AllocateAudioBuffer**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-allocateaudiobuffer) Allocates a cyclic buffer for audio data.

[**IMiniportWaveRTStream::FreeAudioBuffer**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-freeaudiobuffer)

Frees an audio buffer previously allocated with a call to [**IMiniportWaveRTStream::AllocateAudioBuffer**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-allocateaudiobuffer).

[**IMiniportWaveRTStream::GetClockRegister**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-getclockregister)

Retrieves the information that the port driver must have to expose the clock register to the audio subsystem and its clients.

[**IMiniportWaveRTStream::GetHWLatency**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-gethwlatency)

Retrieves information about sources of stream latency in the audio hardware.

[**IMiniportWaveRTStream::GetPosition**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-getposition)

Retrieves the current play or record position as a byte offset from the beginning of the buffer.

[**IMiniportWaveRTStream::GetPositionRegister**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-getpositionregister)

Retrieves the information that the port driver must have to expose the position register to the audio subsystem and its clients.

[**IMiniportWaveRTStream::SetFormat**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-setformat)

Sets the data format of the wave stream.

[**IMiniportWaveRTStream::SetState**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-setstate)

Changes the transport state of the audio stream.
