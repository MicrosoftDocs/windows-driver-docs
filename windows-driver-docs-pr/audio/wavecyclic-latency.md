---
title: WaveCyclic Latency
description: WaveCyclic Latency
ms.assetid: 6de639c6-ddd5-4013-8d67-00731c328f47
keywords:
- WaveCyclic latency WDK audio
- silence intervals WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WaveCyclic Latency


## <span id="wavecyclic_latency"></span><span id="WAVECYCLIC_LATENCY"></span>


If your WaveCyclic miniport driver provides hardware mixing of an audio playback stream, DirectSound submits an IRP to the WaveCyclic port driver that contains the entire DirectSound wave stream in a single cyclic buffer. The WaveCyclic port driver receives the IRP and feeds the wave data piece-by-piece into the DMA buffer that your driver exposes. WaveCyclic attempts to keep the DMA buffer's write pointer about 40 milliseconds ahead of the read pointer. Even when your driver is doing hardware mixing with DirectSound, it can expect about 40 milliseconds of extra data in the DMA buffer.

The fact that the WaveCyclic port driver tries to accumulate up to 40 milliseconds of data in the cyclic buffer does not mean that the WaveCyclic port driver adds 40 milliseconds to the latency of the stream. In fact, the port driver adds very little latency. Just before a new stream begins playing, while the port driver is still writing the initial data into the beginning of the cyclic buffer, the port driver continues writing until either no more data is available or the buffer contains a full 40 milliseconds of data. However, if less than this amount of data is immediately available, the port driver will not force the miniport driver to wait. Instead, it allows the miniport driver to begin playing the already buffered data immediately. Later, as more data becomes available, the port driver continues writing the data to the buffer until either no more data is available or the amount of data buffered between the read and write pointers reaches 40 milliseconds.

After a period of near starvation, a KMixer stream can contain intervals of silence. If WaveCyclic has received only enough wave data from KMixer to maintain thirty rather than forty milliseconds of extra data in the DMA buffer, WaveCyclic begins writing silence into the DMA buffer following the end of the valid data from KMixer. This policy ensures that if starvation occurs and the device reads past the end of the valid data, the audio device renders silence instead of stale or uninitialized data.

The amount of silence written to the DMA buffer is kept fairly small, and if KMixer does succeed in supplying the WaveCyclic port driver with additional data before the silence has been played, that data overwrites the silence in the buffer. In the absence of starvation, the audio device receives a continuous stream of mixed data without intervals of forced silence. When you are debugging your driver, however, you might see your miniport driver's [**IMiniportWaveCyclicStream::Silence**](https://msdn.microsoft.com/library/windows/hardware/ff536721) method being called even though your audio renderer is not starving.

 

 




