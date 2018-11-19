---
title: Stream Synchronization
description: Stream Synchronization
ms.assetid: bbf589f1-ca4b-41a2-970d-b31c7761eb1a
keywords:
- synchronization WDK DVD decoder
- stream synchronization WDK DVD decoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stream Synchronization





DVD stream inputs may be composed of two or more streams. The stream class driver can handle synchronization transparently on behalf of the DVD decoder minidriver. For more information, see [Minidriver Synchronization](minidriver-synchronization.md). Programmers must still be aware of several factors affecting DVD streams, including:

-   The audio stream must provide the master clock, and must synthesize the clock when there is no data. When audio data stops, the audio stream uses the system clock based on rate matching and clock frequency as returned by [**KeQueryPerformanceCounter**](https://msdn.microsoft.com/library/windows/hardware/ff553053). All other streams must act as subordinates to audio. That is, they synchronize their performance to the audio stream.

-   Software audio decoders must be supported in user-mode. The clock forwarder DirectShow filter forwards the DirectShow clock to the minidriver. This is transparent to the minidriver.

-   The decoder should not use the time stamps in the primary elementary stream (PES) header.

-   System clock references (SCRs) are not used in synchronization. The SCR field of the DVD PACK is set to zero because Microsoft's DVD architecture uses the "master clock" paradigm for audio and video synchronization.

-   The minidriver does not see time stamp discontinuities. The DVD navigator/splitter makes all time stamps contiguous.

If a decoder provides decoding capabilities for both audio and video, the decoder may use hardware synchronization only when the audio stream is opened as the system master clock. If the audio stream is not the master clock, the video stream must synchronize video decoding to the stream class master clock.

 

 




