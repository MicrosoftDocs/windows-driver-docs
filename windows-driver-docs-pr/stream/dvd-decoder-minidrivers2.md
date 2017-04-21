---
title: DVD Decoder Minidrivers
author: windows-driver-content
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DVD Decoder Minidrivers


## <a href="" id="ddk-dvd-decoder-minidrivers-ksg"></a>


DVD provides digital data storage that encompasses audio, video, and other digital data. This documentation discusses the design of DVD decoder minidrivers that are used for movie playback (video and audio) from DVD. These minidrivers control DVD decoder adapter cards that read and decode DVD data stream formats such as MPEG-2 (video and audio), AC-3 and DTS.

DVD decoder minidrivers interface with the stream class driver. This allows developers creating drivers for multifunction devices to build on the stream class using a single driver model that works for all data types (MPEG-2, AC-3, DTS, and so on).

DVD decoder minidrivers are portable and have no multiprocessor issues if they use stream class driver provided synchronization. Previously, a developer would have to create separate drivers using various driver models for MPEG-2, audio, MIDI, and subpicture. For more information, see [Streaming Minidrivers](streaming-minidrivers2.md).

The following topics are discussed:

[DVD Decoder Support in Windows](dvd-decoder-support-in-windows.md)

[DVD Data Streams](dvd-data-streams.md)

[DVD Copyright Protection](dvd-copyright-protection.md)

[DVD Regionalization](dvd-regionalization.md)

[Master Clock](master-clock.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20DVD%20Decoder%20Minidrivers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


