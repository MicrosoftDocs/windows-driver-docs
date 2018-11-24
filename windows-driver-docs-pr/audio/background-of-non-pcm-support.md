---
title: Background of Non-PCM Support
description: Background of Non-PCM Support
ms.assetid: 4f0e1101-e4cc-4bde-a178-fb47fe24ae4d
keywords:
- non-PCM audio formats WDK , DirectSound
- non-PCM audio formats WDK , waveOut
- waveOut non-PCM support WDK audio
- DirectSound WDK audio , non-PCM support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Background of Non-PCM Support


## <span id="background_of_non_pcm_support"></span><span id="BACKGROUND_OF_NON_PCM_SUPPORT"></span>


Several issues prevented earlier versions of Microsoft Windows from supporting non-PCM formats through the waveOut and DirectSound APIs. These issues and how they have been resolved are discussed below.

### <span id="waveOut_API"></span><span id="waveout_api"></span><span id="WAVEOUT_API"></span>waveOut API

The software layer that separates waveOut applications from VxD wave drivers is fairly thin. Drivers and applications that support a custom wave format can stream data in that format regardless of whether the operating system understands the format.

However, in Windows 2000 and Windows 98, the WDM audio framework forces all the audio data that is processed by the waveOut API (and DirectShow's waveOut renderer) to pass through the [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver) (Kmixer.sys), which is the kernel audio mixer. A waveOutOpen call succeeds only if KMixer supports the format, regardless of whether the driver supports the format.

KMixer handles WAVE\_FORMAT\_PCM on all WDM operating systems. Windows 2000 and later, and Windows 98 SE, extend KMixer to support not only WAVE\_FORMAT\_IEEE\_FLOAT but also [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) variants of PCM and IEEE-float formats. Because KMixer supports no non-PCM formats, an attempt to pass non-PCM data through KMixer fails.

Windows XP and later, and Windows Me, support non-PCM formats by allowing non-PCM audio data to simply bypass KMixer. Specifically, waveOut non-PCM data flows directly to PortCls (or USBAudio) instead of first passing through KMixer. Any mixing of non-PCM data must be done in hardware, but applications that use non-PCM data in a format such as AC-3 or WMA Pro typically do not require mixing and drivers typically do not support hardware mixing in that format.

### <span id="DirectSound_API"></span><span id="directsound_api"></span><span id="DIRECTSOUND_API"></span>DirectSound API

On legacy waveOut drivers and VxD drivers, DirectSound supports [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) (but not WAVEFORMATEXTENSIBLE) PCM formats for both primary and secondary buffers, with 8 or 16 bits per sample, one or two channels, and a sampling rate between 100 Hz and 100 kHz. VxD drivers can further limit the formats allowed for primary buffers when the cooperative level is set to DSSCL\_WRITEPRIMARY (see the description of the **IDirectSoundBuffer::SetFormat** method in the DirectX SDK). These limitations have not changed in Windows Me or Windows XP.

WDM drivers can support PCM formats in both WAVEFORMATEX and WAVEFORMATEXTENSIBLE form. For Windows 2000 and later, Windows Me, and Windows 98 SE, drivers can also support the WAVE\_FORMAT\_IEEE\_FLOAT format for both primary and secondary DSBCAPS\_LOCSOFTWARE buffers (mixed by KMixer) in both WAVEFORMATEX and WAVEFORMATEXTENSIBLE form.

Calling **SetFormat** to specify the data format of a primary buffer has only an indirect effect on the final mixing format chosen by the sound card. The primary buffer object is used to obtain the **IDirectSound3DListener** interface and to set the device's global volume and pan, but does not represent the single output stream from the sound card. Instead, KMixer mixes the primary-buffer data in order to allow several DSSCL\_WRITEPRIMARY DirectSound clients to run simultaneously.

On Windows 2000 and Windows 98, DirectSound supports only PCM data. (The same is true of DirectShow, which uses DirectSound's renderer.) A call to **CreateSoundBuffer** with a non-PCM format always fails, even if the driver supports the format. Failure occurs for two reasons. First, whenever DirectSound creates a KS pin, it automatically specifies KSDATAFORMAT\_SUBTYPE\_PCM instead of deriving the subtype from the **wFormatTag** member of the WAVEFORMATEX structure that is used to create the **IDirectSoundBuffer** object. Second, DirectSound requires every data path to have volume and SRC (sample-rate conversion) nodes ([**KSNODETYPE\_VOLUME**](https://msdn.microsoft.com/library/windows/hardware/ff537208) and [**KSNODETYPE\_SRC**](https://msdn.microsoft.com/library/windows/hardware/ff537190)), regardless of whether the client requests pan, volume, or frequency controls on the DirectSound buffer. This requirement is met if either the data passes through KMixer or the device performs hardware mixing. For non-PCM formats, however, KMixer is not present in the data path and the drivers themselves typically fail when asked to perform hardware mixing.

Windows XP and later, and Windows Me, remove the limitations that prevented DirectSound applications from using non-PCM formats. DirectSound 8 (and later versions) uses the correct format subtype and no longer automatically requires volume and SRC nodes in every data path.

 

 




