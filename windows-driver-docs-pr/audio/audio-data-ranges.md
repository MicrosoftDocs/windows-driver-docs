---
title: Audio Data Ranges
description: Audio Data Ranges
ms.assetid: 690fafda-fb35-43da-9de1-6cbc3bf8eb6c
keywords:
- data ranges WDK audio
- range values WDK audio
- KS data ranges WDK audio
- audio data ranges WDK
- KSDATARANGE structure
- WDM audio data ranges WDK
- data ranges WDK audio , about audio data ranges
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Audio Data Ranges


## <span id="audio_data_ranges"></span><span id="AUDIO_DATA_RANGES"></span>


Each pin on a KS filter declares which data formats it supports. The pin factory exposes this information as an array of data ranges. Unlike the format descriptors described previously, a data range describes a range of data formats. For example, the data range for a wave pin specifies the range of sample sizes, frequencies, and channels that the pin supports.

When the miniport driver instantiates a pin, it configures the pin to handle a stream with a particular data format that it selects from the pin's data ranges. This work is done by the miniport driver's data-intersection handler, which selects an audio data format that is common to two pins so that they can be connected. For more information, see [Data-Intersection Handlers](data-intersection-handlers.md).

For information about using property requests to query audio pins for their data ranges and select data intersections, see [Pin Data-Range and Intersection Properties](pin-data-range-and-intersection-properties.md).

To specify a data range for a wave pin, the [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structure is followed by information describing the range of sample sizes, frequencies, and channels that the pin supports. This information, including the KSDATARANGE structure itself, is encapsulated in the [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structure.

To specify a data range for a MIDI or DirectMusic pin, the KSDATARANGE structure is followed by additional information, including the maximum number of channels and notes that can be played at the same time. This information, along with the KSDATARANGE structure itself, is encapsulated in the [**KSDATARANGE\_MUSIC**](https://msdn.microsoft.com/library/windows/hardware/ff537097) structure.

This document presents several examples of data ranges that use the KSDATARANGE\_AUDIO and KSDATARANGE\_MUSIC structures:

-   For example declarations of wave and DirectSound data ranges, see [PCM Stream Data Range](pcm-stream-data-range.md) and [DirectSound Stream Data Range](directsound-stream-data-range.md).

-   For example declarations of MIDI and DirectMusic data ranges, see [MIDI Stream Data Range](midi-stream-data-range.md) and [DirectMusic Stream Data Range](directmusic-stream-data-range.md).

-   For example declarations of data ranges for non-PCM formats, see [Specifying AC-3 Data Ranges](specifying-ac-3-data-ranges.md) and [Specifying WMA Pro Data Ranges](specifying-wma-pro-data-ranges.md).

 

 




