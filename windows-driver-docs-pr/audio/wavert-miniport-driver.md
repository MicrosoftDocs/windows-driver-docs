---
title: WaveRT Miniport Driver
description: WaveRT Miniport Driver
ms.assetid: 154dc921-424f-4021-8f17-5482ceef99a8
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WaveRT Miniport Driver


The WaveRT miniport driver is supported in Windows Vista and later Windows operating systems, and it manages the hardware-dependent functions of a wave-rendering or wave-capture audio device. A WaveRT-friendly audio device has scatter/gather DMA hardware that can transfer audio data to or from any location in physical memory.

A WaveRT miniport driver must implement two interfaces:

-   [IMiniportWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536737). This interface performs miniport driver initialization, channel enumeration, and stream creation.

-   [IMiniportWaveRTStream](https://msdn.microsoft.com/library/windows/hardware/ff536738). This interface manages a wave stream and exposes most of the functionality of the miniport driver.

For information about how to design a WaveRT miniport driver that complements the WaveRT port driver, see the [Developing a WaveRT Miniport Driver](developing-a-wavert-miniport-driver.md) topic.

### <span id="iminiportwavert"></span><span id="IMINIPORTWAVERT"></span>IMiniportWaveRT

The [IMiniportWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536737) interface provides the following methods:

[**IMiniportWaveRT::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536759)

Initializes the miniport object.

[**IMiniportWaveRT::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536762)

Creates a new stream object.

[**IMiniportWaveRT::GetDeviceDescription**](https://msdn.microsoft.com/library/windows/hardware/ff536758)

Returns a pointer to a [**DEVICE\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff543107) structure describing the device.

### <span id="iminiportwavertstream"></span><span id="IMINIPORTWAVERTSTREAM"></span>IMiniportWaveRTStream

The [IMiniportWaveRTStream](https://msdn.microsoft.com/library/windows/hardware/ff536738) interface inherits the methods from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. IMiniportWaveRTStream provides the following additional methods:

[**IMiniportWaveRTStream::AllocateAudioBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536744)

Allocates a cyclic buffer for audio data.

[**IMiniportWaveRTStream::FreeAudioBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536745)

Frees an audio buffer previously allocated with a call to [**IMiniportWaveRTStream::AllocateAudioBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536744).

[**IMiniportWaveRTStream::GetClockRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536746)

Retrieves the information that the port driver must have to expose the clock register to the audio subsystem and its clients.

[**IMiniportWaveRTStream::GetHWLatency**](https://msdn.microsoft.com/library/windows/hardware/ff536747)

Retrieves information about sources of stream latency in the audio hardware.

[**IMiniportWaveRTStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536749)

Retrieves the current play or record position as a byte offset from the beginning of the buffer.

[**IMiniportWaveRTStream::GetPositionRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536752)

Retrieves the information that the port driver must have to expose the position register to the audio subsystem and its clients.

[**IMiniportWaveRTStream::SetFormat**](https://msdn.microsoft.com/library/windows/hardware/ff536753)

Sets the data format of the wave stream.

[**IMiniportWaveRTStream::SetState**](https://msdn.microsoft.com/library/windows/hardware/ff536756)

Changes the transport state of the audio stream.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20WaveRT%20Miniport%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


