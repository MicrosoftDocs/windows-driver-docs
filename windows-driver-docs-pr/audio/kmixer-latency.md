---
title: KMixer Latency
description: KMixer Latency
ms.assetid: 9781c145-e7c6-4933-a3e8-bdba39918636
keywords:
- KMixer system driver WDK audio , latency
- waveOut latency WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KMixer Latency


## <span id="kmixer_latency"></span><span id="KMIXER_LATENCY"></span>


The [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver) is the kernel-mode software component that mixes the output streams from the various audio sources in the system. Inserting KMixer into a wave audio stream adds KMixer's inherent latency to the total latency of that stream. KMixer introduces a latency of 30 milliseconds into an audio stream. This is usually sufficient to absorb jitter resulting from competition for CPU time with ISRs (interrupt service routines) and other high-priority operations. In contrast, hardware mixers are largely immune to these sources of delay.

DirectSound streams that feed into hardware mixer pins bypass KMixer and avoid the latency of software mixing in KMixer. DirectSound makes use of all of an audio device's available hardware-accelerated mixer pins as long as those pins have a topology that conforms to the [DirectSound node-ordering requirements](directsound-node-ordering-requirements.md).

In all current versions of Microsoft Windows, including Windows Me and Windows XP, the **waveOut** API has a limitation that prevents it from taking advantage of all available hardware acceleration. An audio stream that is output by the **waveOut** API always passes through KMixer, even if the audio device provides hardware-accelerated mixing. If **waveOut** and DirectSound audio streams are played concurrently, the DirectSound audio streams can still use any available hardware-mixing pins, although the **waveOut** streams all pass through KMixer and go to a single hardware buffer.

Other non-DirectSound stream sources have limitations similar to those of **waveOut** that prevent them from using hardware-accelerated mixing. These sources include:

-   Redbook CD digital audio (See [Redbook System Driver](kernel-mode-wdm-audio-components.md#redbook_system_driver).)

-   Sound Blaster emulator (See [SBEmul System Driver](kernel-mode-wdm-audio-components.md#sbemul_system_driver).)

-   Kernel-mode software synthesizers (See [SWMidi System Driver](kernel-mode-wdm-audio-components.md#swmidi_system_driver) and [DMusic System Driver](kernel-mode-wdm-audio-components.md#dmusic_system_driver).)

-   DRMK, the kernel-mode DRM-decryption module (See [DRMK System Driver](kernel-mode-wdm-audio-components.md#drmk_system_driver).)

Similar to **waveOut** streams, streams from these four sources always pass through KMixer but can play concurrently with hardware-accelerated DirectSound streams.

If an audio device performs hardware mixing, streams that feed directly into the hardware mixing pins bypass KMixer and avoid the KMixer latency. The SysAudio system driver always reserves one hardware pin for KMixer so that after the other (unreserved) hardware pins have all been allocated, any additional streams can be mixed by KMixer and fed into the reserved hardware pin.

In the case of a single-stream device, KMixer is always instantiated on the one available rendering pin.

KMixer's buffer-management policy determines its latency. Upon being instantiated, KMixer initially allocates three buffers for wave data. After that, KMixer makes sure that a minimum of two buffers are queued at the miniport driver at all times. At any moment, the miniport driver has access to at least two buffers: the buffer that the device is currently reading and a second buffer that the miniport driver can switch to immediately when the first buffer is exhausted. Meanwhile, KMixer can write new data into the third buffer.

If at any time the driver has less than two buffers, KMixer interprets this as a starvation condition and begins allocating additional buffers. If starvation continues, KMixer can allocate up to eight buffers, but it allocates no further buffers once this limit is reached. Consequently, a driver might find as many as eight buffers in its queue following a period of severe starvation.

The parameter values in the preceding discussion are specific to the current implementation of KMixer and may change in future versions of Windows.

 

 




