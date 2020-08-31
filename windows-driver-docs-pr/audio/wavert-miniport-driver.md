---
title: WaveRT Miniport Driver
description: WaveRT Miniport Driver
ms.assetid: 154dc921-424f-4021-8f17-5482ceef99a8
ms.date: 04/20/2017
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

The [IMiniportWaveRTStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertstream) interface inherits the methods from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. IMiniportWaveRTStream provides the following additional methods:

[**IMiniportWaveRTStream::AllocateAudioBuffer**](/previous-versions/windows/hardware/drivers/ff536744(v=vs.85))

Allocates a cyclic buffer for audio data.

[**IMiniportWaveRTStream::FreeAudioBuffer**](/previous-versions/windows/hardware/drivers/ff536745(v=vs.85))

Frees an audio buffer previously allocated with a call to [**IMiniportWaveRTStream::AllocateAudioBuffer**](/previous-versions/windows/hardware/drivers/ff536744(v=vs.85)).

[**IMiniportWaveRTStream::GetClockRegister**](/previous-versions/windows/hardware/drivers/ff536746(v=vs.85))

Retrieves the information that the port driver must have to expose the clock register to the audio subsystem and its clients.

[**IMiniportWaveRTStream::GetHWLatency**](/previous-versions/windows/hardware/drivers/ff536747(v=vs.85))

Retrieves information about sources of stream latency in the audio hardware.

[**IMiniportWaveRTStream::GetPosition**](/previous-versions/windows/hardware/drivers/ff536749(v=vs.85))

Retrieves the current play or record position as a byte offset from the beginning of the buffer.

[**IMiniportWaveRTStream::GetPositionRegister**](/previous-versions/windows/hardware/drivers/ff536752(v=vs.85))

Retrieves the information that the port driver must have to expose the position register to the audio subsystem and its clients.

[**IMiniportWaveRTStream::SetFormat**](/previous-versions/windows/hardware/drivers/ff536753(v=vs.85))

Sets the data format of the wave stream.

[**IMiniportWaveRTStream::SetState**](/previous-versions/windows/hardware/drivers/ff536756(v=vs.85))

Changes the transport state of the audio stream.

 

