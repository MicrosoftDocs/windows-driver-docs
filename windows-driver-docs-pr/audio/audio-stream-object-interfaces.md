---
title: Audio Stream Object Interfaces
description: Audio Stream Object Interfaces
ms.assetid: 9d68016a-ddb1-4fbb-b6cc-384f8c76552c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Audio Stream Object Interfaces


## <span id="ddk_audio_stream_object_interfaces_ks"></span><span id="DDK_AUDIO_STREAM_OBJECT_INTERFACES_KS"></span>


This section describes audio stream object interfaces. These interfaces are associated with the wave and MIDI streams that flow into and from the pins of wave, MIDI, and DirectMusic filters. Some of these interfaces are implemented by the miniport driver and exposed to the port driver. Others are implemented by the port driver and exposed to the miniport driver.

This section discusses the following audio stream object interfaces:

Manages buffer storage for DirectMusic streams. Implemented by the DMus port driver.

Assigns [digital rights management (DRM)](https://msdn.microsoft.com/library/windows/hardware/ff536260) protection to the digital content in an audio stream. Implemented by a WaveCyclic, WavePci, or WaveRT miniport driver.

Represents the MIDI stream that flows through a pin on a MIDI filter. Implemented by a MIDI miniport driver.

Represents the wave stream that flows through a pin on a WaveCyclic filter. Implemented by a WaveCyclic miniport driver.

Represents the wave stream that flows through a pin on a WavePci filter. Implemented by a WavePci miniport driver.

Represents the wave stream that flows through a pin on a WaveRT filter. Implemented by a WaveRT miniport dirver.

Augments the **IMiniportWaveRTStream** interface, providing additional methods for DMA driver event notifications.

Represents the MIDI stream that flows through a MIDI or DirectMusic pin on a DirectMusic filter. Implemented by a DMus miniport driver.

Provides mapping services to a WavePci miniport driver's stream objects. Implemented by the WavePci port driver.

Handles wave output for a DirectMusic synthesizer device. Implemented by a DMus miniport driver and used by the DMus port driver's wave sink.

[IAllocatorMXF](https://msdn.microsoft.com/library/windows/hardware/ff536491)

[IDrmAudioStream](https://msdn.microsoft.com/library/windows/hardware/ff536568)

[IMiniportMidiStream](https://msdn.microsoft.com/library/windows/hardware/ff536704)

[IMiniportWaveCyclicStream](https://msdn.microsoft.com/library/windows/hardware/ff536715)

[IMiniportWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536725)

[IMiniportWaveRTStream](https://msdn.microsoft.com/library/windows/hardware/ff536738)

[IMiniportWaveRTStreamNotofication](https://msdn.microsoft.com/library/windows/hardware/ff536739)

[IMXF](https://msdn.microsoft.com/library/windows/hardware/ff536782)

[IPortWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536907)

[ISynthSinkDMus](https://msdn.microsoft.com/library/windows/hardware/ff537011)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Stream%20Object%20Interfaces%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




