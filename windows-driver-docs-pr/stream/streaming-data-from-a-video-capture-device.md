---
title: Streaming Data from a Video Capture Device
description: Streaming Data from a Video Capture Device
ms.assetid: c83aae8e-70a7-4d65-a888-00a7c21eebdd
keywords:
- video capture WDK AVStream , streaming data from
- capturing video WDK AVStream , streaming data from
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Streaming Data from a Video Capture Device


Video streams are composed of time-stamped, digitized video and related information, such as vertical blanking interval (VBI) data and timecode. Streams can be paused, started, and stopped independently of one another. Stream samples are time stamped with a 100-nanosecond resolution clock.

A video capture minidriver can support multiple, simultaneous streams of compressed and uncompressed video, timecode, closed captioning, raw and decoded VBI data, and custom data formats. The minidriver should create a new stream for each data type that can be produced simultaneously with other data types. The AVStream or Stream class interfaces expose a separate pin for each new stream. These pins are mirrored by KsProxy and appear in user mode as a Microsoft DirectShow filter. A DirectShow filter is not a WDM filter driver. For more information about pins and streaming, see [Kernel Streaming](kernel-streaming.md).

Each video streaming pin can support a variety of different data formats. For example, a single pin could support RGB16, RGB24, YUV9, and JPEG digital video. Most devices support only a few of these formats. For more information about stream formats and specifying a range of supported formats, see [Specifying Stream Formats](specifying-stream-formats.md).

### Vertical Blanking Interval (VBI) Data

When capturing vertical blanking interval (VBI) streams, the capture device should provide raw, undecoded VBI samples, so that downstream filters and codecs can extract closed captioning (CC), North American Broadcast Teletext Standard (NABTS), Teletext, and other proprietary data from the raw samples.

VBI decoders must be immediately informed of tuning changes. For example, when the tuner switches from one channel to another, a VBI decoder must be notified at the beginning of the tuning operation so it can temporarily stop decoding during the period of signal instability. When the tuning operation completes, the VBI decoder must be notified of the new channel and any video standard or country/region code changes that may have occurred.

A minidriver must propagate a tuning packet from its tuner filter, through the crossbar filter, and then into the analog video input pin on its capture filter. This packet is only available in user mode until it reaches the capture filter. The minidriver receives this tuning packet as a [**KS\_TVTUNER\_CHANGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567691) structure on the analog video input pin of the minidriver's capture filter.

The minidriver must also propagate the tuning packet to the VBI output pins of its capture filter using the [video stream extended header](video-stream-extended-headers.md). VBI decoders that operate as a chain must similarly propagate the extended header information from their input pins to their output pins.

 

 




