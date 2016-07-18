---
title: Introducing the WaveRT Port Driver
description: Introducing the WaveRT Port Driver
ms.assetid: 48b2b59e-385e-4814-ac20-c4b1a08f32dc
---

# Introducing the WaveRT Port Driver


In Windows Vista and later operating systems, support is provided for a wave real-time (WaveRT) port driver that achieves improved performance but uses a simple cyclic buffer for rendering and capturing audio streams.

The improved performance of the WaveRT port driver includes the following characteristics:

-   Low-latency during wave-capture and wave-rendering

-   A glitch-resilient audio stream

Like the WaveCyclic and WavePci port drivers in earlier versions of Microsoft Windows, the WaveRT port driver provides the generic functionality for a [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff560842) (KS) filter. The WaveRT port driver provides support for audio devices that can do the following:

-   They can connect to a system bus, for example the PCI Express bus.

-   They can playback or record wave data (audio data that is described by a [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) or [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure).

-   They can use the improved scheduling support that is available in Windows Vista, to reduce the latency of an audio stream.

If you want your audio device to take advantage of the improvements in audio offered in Windows, your audio device must be able to play or capture audio data with little or no intervention by the driver software during streaming. A properly designed audio device that uses the WaveRT port driver requires little or no help from the driver software from the time the audio stream enters the *run* state until it exits from that state.

The main client of the WaveRT port driver is the audio engine running in shared mode. For more information about the Windows Vista audio engine, see the [Exploring the Windows Vista Audio Engine](exploring-the-windows-vista-audio-engine.md) topic.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Introducing%20the%20WaveRT%20Port%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


