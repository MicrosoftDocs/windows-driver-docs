---
title: KMixer Behavior
description: KMixer Behavior
ms.assetid: 1668176f-3d19-425f-85f5-e51fb1b40acb
keywords:
- KMixer system driver WDK audio , data intersection
- data-intersection handlers WDK audio , KMixer
- mixed streams WDK audio
- sink pins WDK audio
- source pins WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KMixer Behavior


## <span id="kmixer_behavior"></span><span id="KMIXER_BEHAVIOR"></span>


In Windows Server 2003, Windows XP, Windows 2000, and Windows Me/98, an audio adapter's sink pin typically connects to the source pin from the KMixer system filter during playback of a PCM stream. As wave streams are added to or removed from the audio mix, KMixer might need to call the miniport driver stream's **SetFormat** method (for example, see [**IMiniportWavePciStream::SetFormat**](https://msdn.microsoft.com/library/windows/hardware/ff536732)) to adjust the sink pin's sample frequency.

In order to preserve the quality of the wave-data streams that enter its sink pins, KMixer attempts to adjust the sample frequency at its source pin to match the highest sample frequency of the streams entering its sink pins. Accordingly, as new streams are added or removed from the mix entering its sink pins, KMixer might need to increase or decrease the sample frequency at its source pin in order to accommodate the new mix. KMixer attempts to change the sample frequency at the connection between its source pin and an adapter's sink pin by calling the adapter's **SetFormat** method to request the change. If KMixer's call to **SetFormat** requests a sample rate that is higher than the adapter can support, the adapter fails the call. In this case, KMixer responds by calling **SetFormat** with successively lower sample frequencies until the **SetFormat** call succeeds. KMixer then down-samples the higher-frequency streams at its sink pins as necessary to accommodate the lower sample frequency at its source pin.

When the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) first creates the connection between KMixer's source pin and an adapter's sink pin, the initial sample frequency at the connection might not match the highest sample frequency at KMixer's sink pins. In this case, KMixer attempts to adjust the connection's sample frequency by calling **SetFormat**, as described previously.

In the current KMixer implementation, KMixer's handling of the bits-per-sample and number-of-channels settings at its source pin differs from its handling of the sample frequency. Once SysAudio creates a connection between the KMixer source pin and an adapter sink pin, KMixer never modifies the connection's initial bits-per-sample or number-of-channels settings. Ideally, these settings should match the maximum settings in the data streams entering KMixer's sink pins in order to preserve the quality of the audio data. Therefore, the adapter's proprietary data-intersection handler should choose the format with the highest bits-per-sample and number-of-channels values that lies within the intersection of the data ranges for the two pins. Note that a proprietary handler that is written to work this way will not need to be rewritten if in the future KMixer's behavior changes to dynamically adjust the connection's bits-per-sample and number-of-channels settings to accommodate dynamic changes in the KMixer inputs.

For more information, see [How KMixer Handles Set-Format Requests](how-kmixer-handles-set-format-requests.md).

 

 




