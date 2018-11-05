---
title: KMixer Volume and Mute Controls
description: KMixer Volume and Mute Controls
ms.assetid: 4e6b9e84-42da-4614-b729-f8f2efb0ece2
keywords:
- KMixer system driver WDK audio , volume controls
- SRC WDK audio , volume controls
- sample-rate conversion WDK audio , volume controls
- KMixer system driver WDK audio , mute controls
- SRC WDK audio , mute controls
- sample-rate conversion WDK audio , mute controls
- volume control mixing WDK audio
- mute control WDK audio
- mixing volume changes WDK audio
- mixing mute changes WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KMixer Volume and Mute Controls


## <span id="kmixer_volume_and_mute_controls"></span><span id="KMIXER_VOLUME_AND_MUTE_CONTROLS"></span>


Changes made to volume-level and mute controls on KMixer inputs can affect audio data that was submitted to KMixer before the change was requested. Also, volume changes are abrupt, and KMixer does nothing to smooth out the transition from the old volume level to the new one.

KMixer wakes up approximately every 10 milliseconds to mix another 10 milliseconds of data from all its input streams into a 10-millisecond output buffer, which it submits to the audio driver to be played. (This timing is specific to the current implementation of KMixer and may change in future versions of Microsoft Windows.)

When an application program calls **IDirectSoundBuffer::SetVolume** on an unaccelerated DirectSound buffer, for example, the call generates a [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff537309) set-property request to a KMixer sink (input) pin. KMixer applies the new volume setting just as soon as it wakes up and begins processing the next 10-millisecond buffer queued at the pin. Note that this buffer might have arrived at the pin before the volume-level property request but is still affected by the request. KMixer does not attempt to perform a gradual transition from the old volume setting to the new one. Instead, the full volume change takes effect with the very first sample that KMixer reads from the buffer.

 

 




