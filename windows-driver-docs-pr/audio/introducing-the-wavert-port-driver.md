---
title: Introducing the WaveRT Port Driver
description: Introducing the WaveRT Port Driver
ms.assetid: 48b2b59e-385e-4814-ac20-c4b1a08f32dc
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




