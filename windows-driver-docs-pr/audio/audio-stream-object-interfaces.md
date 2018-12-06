---
title: Audio Stream Object Interfaces
description: Audio Stream Object Interfaces
ms.assetid: 9d68016a-ddb1-4fbb-b6cc-384f8c76552c
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





