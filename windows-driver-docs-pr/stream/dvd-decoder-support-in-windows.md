---
title: DVD Decoder Support in Windows
description: DVD Decoder Support in Windows
ms.assetid: 3a77b6d1-6095-4cf8-8cd4-2e6d80d171c8
keywords:
- DVD decoder minidrivers WDK , Windows support
- decoder minidrivers WDK DVD , Windows support
- DVD decoder minidrivers WDK , writing
- decoder minidrivers WDK DVD , writing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DVD Decoder Support in Windows





**Note**   This topic is intended for developers. For general information about DVD decoders for Windows, including a list of software decoders, see article Q306331, "[Supported software MPEG-2 DVD decoders in Windows Media Player for Windows XP and Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=3100&ID=306331)," in the Microsoft Knowledge Base.

 

DVD decoders are supported in Windows 98/Me and later as well as Windows 2000 and later.

To write a DVD decoder minidriver, the minidriver must include the *ksmedia.h* and *ntddcdvd.h* header files that are provided in the WDK. The minidriver must also link to the *stream.lib*, *ks.lib*, *ksguid.lib*, and *dxapi.lib* libraries.

Under Windows XP, the following components support DVD decoding and playback:

-   **WDM Stream Class Driver**

    The WDM stream class driver supports streaming data types and MPEG-2 and AC-3 hardware decoders. For more information, see [Streaming Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff568275).

**Note**   Microsoft does not provide MPEG-2 or AC-3 software/hardware decoder filters with Windows XP. Vendors must supply either a DirectShow-compatible software decoder for each required DVD data stream, or provide a WDM streaming-compatible DVD decoder minidriver to support their DVD hardware decoders.

 

-   **DVD-ROM Class Driver**

    Support for the DVD-ROM command set, including commands for copyright protection and regionalization, is provided in Windows XP by an updated CD-ROM class driver. This class driver provides the ability to read data sectors from a DVD-ROM drive.

-   **UDF File System**

    NT-based operating systems provide a UDF-installable file system, similar to FAT and NTFS. This installable file system supports UDF-formatted DVD discs.

-   Microsoft **DirectShow**

    DirectShow filters and related support include a DVD navigator/splitter, proxy filters for interfacing with the hardware decoder minidrivers for video, subpicture and audio streams, line21 decoder (closed caption), a video mixer, video renderer, and an audio renderer.

    -   DirectShow DVD Navigator/Splitter Filter

        The DVD navigator/splitter filter interprets the programming language embedded in DVD movies, parental control, multiple languages, and processes most DVD-specific data structures. This filter reads the DVD stream directly from a DVD disc and produces individual media type outputs, such as audio, video, and subpicture. The filter responds to commands in the stream and handles all user input.

    -   DirectShow Proxy Filter

        This filter converts DirectShow interfaces to WDM connection and streaming architecture properties. It creates (that is, instantiates) a device object for each data type to be decoded in hardware, such as audio and video data types. This filter supports plug-ins that allow expansion for new interfaces.

    -   DirectShow Closed-Caption Decoding Filter

        This filter converts closed-caption data in a DVD video stream into text images.

    -   DirectShow Video Port Manager and Rendering Filters

        These filters enable playback of video using hardware video ports, and provide support for blending low-bandwidth video streams, such as the closed caption decoder output stream.

-   Microsoft **DirectDraw HAL with VPE**

Dedicated buses transfer decoded video streams from an MPEG-2 decoder to the display card. Microsoft provides software support for these interfaces by using the DirectDraw hardware abstraction layer (HAL) with video port extensions (VPE) to pass video that was decoded in hardware to the video graphics array (VGA). For software decoders, the accelerated graphics port (AGP) bus can be used to transfer the decoded video to the VGA.

-   **Copyright Protection**

    Copyright protection for DVD is provided by encrypting sectors on a disc and then decrypting those sectors before decoding them. Microsoft supports both software and hardware decrypters by way of the DVD navigator/splitter, which oversees the authentication sequence between the decoders and the DVD-ROM drives in a computer. The key exchange sequence is implemented through properties sent to the DVD decoder minidriver's input pins.

There are two primary forms of DVD playback:

[Hardware-based DVD Decoding](hardware-based-dvd-decoding.md)

[Software-based DVD Decoding](software-based-dvd-decoding.md)

The following topics summarize the DVD decoder related kernel streaming properties and events:

[DVD Decoder Related KS Properties](dvd-decoder-related-ks-properties.md)

[DVD Decoder Related KS Events](dvd-decoder-related-ks-events.md)

 

 




