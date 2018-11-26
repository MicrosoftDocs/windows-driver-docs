---
title: Video Capture Overview
description: Video Capture Overview
ms.assetid: 3f299905-beab-48e2-b5c9-9850452115c6
keywords:
- video capture WDK AVStream , about video capture
- capturing video WDK AVStream , about video capture
- video capture WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




