---
title: Video Capture Overview
author: windows-driver-content
description: Video Capture Overview
ms.assetid: 3f299905-beab-48e2-b5c9-9850452115c6
keywords: ["video capture WDK AVStream , about video capture", "capturing video WDK AVStream , about video capture", "video capture WDK AVStream"]
---

# Video Capture Overview


Video capture minidrivers interact with either the AVStream of Stream class interfaces to control hardware devices that primarily produce streams of video data, along with ancillary data such as TV audio, or AM/FM tuner functionality. Vendors write a video capture minidriver to:

-   Capture compressed and uncompressed video streams from digital and analog video sources, such as IEEE 1394, USB, S-Video, and RCA video-in jacks.

-   Capture vertical blanking interval (VBI) data.

-   Capture ancillary data streams, such as TV audio or AM/FM tuner audio.

-   Capture timecode.

-   Control video ports and capture video from video port streams.

-   Control devices associated with video streams such as TV/radio tuners, signal routing devices (crossbars), TV audio control, and video compressors.

-   Control camera properties such as zoom, pan, and focus.

-   Control video properties such as hue, saturation, brightness, and sharpness.

-   Provide WDM streaming (for kernel mode) and DirectShow (for user mode) compatibility.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Capture%20Overview%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


