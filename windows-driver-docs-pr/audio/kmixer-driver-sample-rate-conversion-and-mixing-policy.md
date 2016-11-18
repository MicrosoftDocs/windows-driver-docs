---
title: KMixer Driver Sample Rate Conversion and Mixing Policy
description: KMixer Driver Sample Rate Conversion and Mixing Policy
ms.assetid: 713937da-ccdc-482e-9954-d6d714f33581
keywords: ["SRC WDK audio", "sample-rate conversion WDK audio", "WDM audio drivers WDK , sample-rate conversions", "audio drivers WDK , sample-rate conversions", "KMixer system driver WDK audio , sample-rate conversion", "KS stream mixing WDK audio", "combining audio streams WDK", "stream mixing WDK audio", "SRC WDK audio , about sample-rate conversion", "sample-rate conversion WDK audio , about sample-rate conversion", "kernel streaming WDK audio", "playback WDK audio", "mixing audio WDK"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KMixer%20Driver%20Sample%20Rate%20Conversion%20and%20Mixing%20Policy%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


