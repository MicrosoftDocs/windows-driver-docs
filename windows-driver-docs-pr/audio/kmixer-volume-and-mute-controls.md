---
Description: KMixer Volume and Mute Controls
MS-HAID: 'audio.kmixer\_volume\_and\_mute\_controls'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: KMixer Volume and Mute Controls
---

# KMixer Volume and Mute Controls


## <span id="kmixer_volume_and_mute_controls"></span><span id="KMIXER_VOLUME_AND_MUTE_CONTROLS"></span>


Changes made to volume-level and mute controls on KMixer inputs can affect audio data that was submitted to KMixer before the change was requested. Also, volume changes are abrupt, and KMixer does nothing to smooth out the transition from the old volume level to the new one.

KMixer wakes up approximately every 10 milliseconds to mix another 10 milliseconds of data from all its input streams into a 10-millisecond output buffer, which it submits to the audio driver to be played. (This timing is specific to the current implementation of KMixer and may change in future versions of Microsoft Windows.)

When an application program calls **IDirectSoundBuffer::SetVolume** on an unaccelerated DirectSound buffer, for example, the call generates a [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](audio.ksproperty_audio_volumelevel) set-property request to a KMixer sink (input) pin. KMixer applies the new volume setting just as soon as it wakes up and begins processing the next 10-millisecond buffer queued at the pin. Note that this buffer might have arrived at the pin before the volume-level property request but is still affected by the request. KMixer does not attempt to perform a gradual transition from the old volume setting to the new one. Instead, the full volume change takes effect with the very first sample that KMixer reads from the buffer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KMixer%20Volume%20and%20Mute%20Controls%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



