---
title: Audio Stream Object Interfaces
description: Audio Stream Object Interfaces
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Stream Object Interfaces


## <span id="ddk_audio_stream_object_interfaces_ks"></span><span id="DDK_AUDIO_STREAM_OBJECT_INTERFACES_KS"></span>


This section describes audio stream object interfaces. These interfaces are associated with the wave and MIDI streams that flow into and from the pins of wave, MIDI, and DirectMusic filters. Some of these interfaces are implemented by the miniport driver and exposed to the port driver. Others are implemented by the port driver and exposed to the miniport driver.

This section discusses the following audio stream object interfaces:

Manages buffer storage for DirectMusic streams. Implemented by the DMus port driver.

Assigns [digital rights management (DRM)](./digital-rights-management.md) protection to the digital content in an audio stream. Implemented by a WaveCyclic, WavePci, or WaveRT miniport driver.

Represents the MIDI stream that flows through a pin on a MIDI filter. Implemented by a MIDI miniport driver.

Represents the wave stream that flows through a pin on a WaveCyclic filter. Implemented by a WaveCyclic miniport driver.

Represents the wave stream that flows through a pin on a WavePci filter. Implemented by a WavePci miniport driver.

Represents the wave stream that flows through a pin on a WaveRT filter. Implemented by a WaveRT miniport dirver.

Augments the **IMiniportWaveRTStream** interface, providing additional methods for DMA driver event notifications.

Represents the MIDI stream that flows through a MIDI or DirectMusic pin on a DirectMusic filter. Implemented by a DMus miniport driver.

Provides mapping services to a WavePci miniport driver's stream objects. Implemented by the WavePci port driver.

Handles wave output for a DirectMusic synthesizer device. Implemented by a DMus miniport driver and used by the DMus port driver's wave sink.

[IAllocatorMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iallocatormxf)

[IDrmAudioStream](/windows-hardware/drivers/ddi/drmk/nn-drmk-idrmaudiostream)

[IMiniportMidiStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidistream)

[IMiniportWaveCyclicStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavecyclicstream)

[IMiniportWavePciStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavepcistream)

[IMiniportWaveRTStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertstream)

[IMiniportWaveRTStreamNotofication](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertstreamnotification)

[IMXF](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-imxf)

[IPortWavePciStream](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavepcistream)

[ISynthSinkDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-isynthsinkdmus)

 

