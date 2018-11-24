---
title: Synchronizing Two or More Streams
description: Synchronizing Two or More Streams
ms.assetid: c25f4ca2-8a9f-43bc-a1bf-b71826b446ff
keywords:
- HD Audio, synchronizing streams
- High Definition Audio (HD Audio), synchronizing streams
- synchronizing streams WDK audio
- stream synchronization WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Two or More Streams


The [**SetDmaEngineState**](https://msdn.microsoft.com/library/windows/hardware/ff537889) routine sets the state of one or more DMA engines to one of the following: running, paused, stopped, or reset. If a call to this routine specifies more than one DMA engine, then all of the DMA engines make the state transition synchronously.

The ability to synchronize a group of streams is required for some audio applications. For example, an audio driver might use codec-combining to create a logical surround-sound audio device that joins two audio codecs: one codec drives the front speakers and a second audio codec drives the back speakers. Depending on the capabilities of the codecs, the audio driver might be required to split the original surround-sound audio stream into two streams, one for each codec. By using the [**SetDmaEngineState**](https://msdn.microsoft.com/library/windows/hardware/ff537889) routine to start and stop the streams in unison, the two streams can remain synchronized.

Allowing the two streams to fall out of synchronization by even a few samples might cause undesirable audio artifacts.

The [**SetDmaEngineState**](https://msdn.microsoft.com/library/windows/hardware/ff537889) routine is available in both versions of the HD Audio DDI.

The UAA HD Audio class driver does not perform codec-combining.

 

 




