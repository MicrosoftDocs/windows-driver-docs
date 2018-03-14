---
title: KMixer Driver Sample Rate Conversion and Mixing Policy
description: KMixer Driver Sample Rate Conversion and Mixing Policy
ms.assetid: 713937da-ccdc-482e-9954-d6d714f33581
keywords:
- SRC WDK audio
- sample-rate conversion WDK audio
- WDM audio drivers WDK , sample-rate conversions
- audio drivers WDK , sample-rate conversions
- KMixer system driver WDK audio , sample-rate conversion
- KS stream mixing WDK audio
- combining audio streams WDK
- stream mixing WDK audio
- SRC WDK audio , about sample-rate conversion
- sample-rate conversion WDK audio , about sample-rate conversion
- kernel streaming WDK audio
- playback WDK audio
- mixing audio WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KMixer Driver Sample Rate Conversion and Mixing Policy


## <span id="kmixer_driver_sample_rate_conversion_and_mixing_policy"></span><span id="KMIXER_DRIVER_SAMPLE_RATE_CONVERSION_AND_MIXING_POLICY"></span>


This section describes the sample-rate conversion and mixing policy of the [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver). KMixer is the kernel-mode system component that performs mixing of kernel-streaming (KS) audio streams.

KMixer can mix playback audio streams from clients such as DirectSound or **waveOut** application programs. The streams can be in different wave PCM formats with a variety of sample rates, sample sizes, and channel counts. Samples can be expressed as integer or floating-point values. KMixer generates a mixed stream in a format that the downstream filter, which is typically an audio rendering device, can handle.

KMixer can also perform format conversion (but no mixing) of a capture stream. KMixer inputs the capture stream from an audio capture device and converts it to a format that a client such as a DirectSoundCapture or **waveIn** application program can handle.

This section discusses the following topics:

[Types of Sample Rate Conversion](types-of-sample-rate-conversion.md)

[Policy for Sample Rate Conversion of Audio Streams](policy-for-sample-rate-conversion-of-audio-streams.md)

[Policy for Mixing Audio Streams and Setting the Output Sample Rate](policy-for-mixing-audio-streams-and-setting-the-output-sample-rate.md)

[How KMixer Handles Set-Format Requests](how-kmixer-handles-set-format-requests.md)

[KMixer Volume and Mute Controls](kmixer-volume-and-mute-controls.md)

 

 




