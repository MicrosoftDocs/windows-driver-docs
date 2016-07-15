---
Description: Audio Data Ranges
MS-HAID: 'audio.audio\_data\_ranges'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Audio Data Ranges
---

# Audio Data Ranges


## <span id="audio_data_ranges"></span><span id="AUDIO_DATA_RANGES"></span>


Each pin on a KS filter declares which data formats it supports. The pin factory exposes this information as an array of data ranges. Unlike the format descriptors described previously, a data range describes a range of data formats. For example, the data range for a wave pin specifies the range of sample sizes, frequencies, and channels that the pin supports.

When the miniport driver instantiates a pin, it configures the pin to handle a stream with a particular data format that it selects from the pin's data ranges. This work is done by the miniport driver's data-intersection handler, which selects an audio data format that is common to two pins so that they can be connected. For more information, see [Data-Intersection Handlers](data-intersection-handlers.md).

For information about using property requests to query audio pins for their data ranges and select data intersections, see [Pin Data-Range and Intersection Properties](pin-data-range-and-intersection-properties.md).

To specify a data range for a wave pin, the [**KSDATARANGE**](stream.ksdatarange) structure is followed by information describing the range of sample sizes, frequencies, and channels that the pin supports. This information, including the KSDATARANGE structure itself, is encapsulated in the [**KSDATARANGE\_AUDIO**](audio.ksdatarange_audio) structure.

To specify a data range for a MIDI or DirectMusic pin, the KSDATARANGE structure is followed by additional information, including the maximum number of channels and notes that can be played at the same time. This information, along with the KSDATARANGE structure itself, is encapsulated in the [**KSDATARANGE\_MUSIC**](audio.ksdatarange_music) structure.

This document presents several examples of data ranges that use the KSDATARANGE\_AUDIO and KSDATARANGE\_MUSIC structures:

-   For example declarations of wave and DirectSound data ranges, see [PCM Stream Data Range](pcm-stream-data-range.md) and [DirectSound Stream Data Range](directsound-stream-data-range.md).

-   For example declarations of MIDI and DirectMusic data ranges, see [MIDI Stream Data Range](midi-stream-data-range.md) and [DirectMusic Stream Data Range](directmusic-stream-data-range.md).

-   For example declarations of data ranges for non-PCM formats, see [Specifying AC-3 Data Ranges](specifying-ac-3-data-ranges.md) and [Specifying WMA Pro Data Ranges](specifying-wma-pro-data-ranges.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Data%20Ranges%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


