---
title: DVD Decoder Minidrivers
description: DVD Decoder Minidrivers
ms.assetid: 1dec271d-47cf-4ab6-9149-7f5b9b92b189
keywords:
- Windows 2000 Kernel Streaming Model WDK , DVD decoder minidrivers
- Streaming Model WDK Windows 2000 Kernel , DVD decoder minidrivers
- Kernel Streaming Model WDK , DVD decoder minidrivers
- DVD decoder minidrivers WDK
- decoder minidrivers WDK DVD
- movie playbacks WDK DVD decoder
- audio playbacks WDK DVD decoder
- video playbacks WDK DVD decoder
- playback WDK DVD decoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DVD Decoder Minidrivers





DVD provides digital data storage that encompasses audio, video, and other digital data. This documentation discusses the design of DVD decoder minidrivers that are used for movie playback (video and audio) from DVD. These minidrivers control DVD decoder adapter cards that read and decode DVD data stream formats such as MPEG-2 (video and audio), AC-3 and DTS.

DVD decoder minidrivers interface with the stream class driver. This allows developers creating drivers for multifunction devices to build on the stream class using a single driver model that works for all data types (MPEG-2, AC-3, DTS, and so on).

DVD decoder minidrivers are portable and have no multiprocessor issues if they use stream class driver provided synchronization. Previously, a developer would have to create separate drivers using various driver models for MPEG-2, audio, MIDI, and subpicture. For more information, see [Streaming Minidrivers](streaming-minidrivers2.md).

The following topics are discussed:

[DVD Decoder Support in Windows](dvd-decoder-support-in-windows.md)

[DVD Data Streams](dvd-data-streams.md)

[DVD Copyright Protection](dvd-copyright-protection.md)

[DVD Regionalization](dvd-regionalization.md)

[Master Clock](master-clock.md)

 

 




