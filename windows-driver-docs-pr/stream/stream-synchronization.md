---
title: Stream Synchronization
author: windows-driver-content
description: Stream Synchronization
ms.assetid: bbf589f1-ca4b-41a2-970d-b31c7761eb1a
keywords:
- synchronization WDK DVD decoder
- stream synchronization WDK DVD decoder
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Stream Synchronization


## <a href="" id="ddk-stream-synchronization-ksg"></a>


DVD stream inputs may be composed of two or more streams. The stream class driver can handle synchronization transparently on behalf of the DVD decoder minidriver. For more information, see [Minidriver Synchronization](minidriver-synchronization.md). Programmers must still be aware of several factors affecting DVD streams, including:

-   The audio stream must provide the master clock, and must synthesize the clock when there is no data. When audio data stops, the audio stream uses the system clock based on rate matching and clock frequency as returned by [**KeQueryPerformanceCounter**](https://msdn.microsoft.com/library/windows/hardware/ff553053). All other streams must act as subordinates to audio. That is, they synchronize their performance to the audio stream.

-   Software audio decoders must be supported in user-mode. The clock forwarder DirectShow filter forwards the DirectShow clock to the minidriver. This is transparent to the minidriver.

-   The decoder should not use the time stamps in the primary elementary stream (PES) header.

-   System clock references (SCRs) are not used in synchronization. The SCR field of the DVD PACK is set to zero because Microsoft's DVD architecture uses the "master clock" paradigm for audio and video synchronization.

-   The minidriver does not see time stamp discontinuities. The DVD navigator/splitter makes all time stamps contiguous.

If a decoder provides decoding capabilities for both audio and video, the decoder may use hardware synchronization only when the audio stream is opened as the system master clock. If the audio stream is not the master clock, the video stream must synchronize video decoding to the stream class master clock.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Stream%20Synchronization%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


