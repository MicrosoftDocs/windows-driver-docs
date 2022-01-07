---
title: Audio Data Formats and Data Ranges
description: Audio Data Formats and Data Ranges
ms.date: 04/20/2017
---

# Audio Data Formats and Data Ranges


## <span id="audio_data_formats_and_data_ranges"></span><span id="AUDIO_DATA_FORMATS_AND_DATA_RANGES"></span>


Audio drivers use the [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) and [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)) structures to specify audio stream formats:

-   The digital format of a KS data stream is specified by a KS format descriptor that begins with a KSDATAFORMAT structure.

-   The range of stream formats that a KS pin can support is specified by an array of KS data ranges; each array element is a range descriptor that begins with a KSDATARANGE structure.

For more information about these two structures, see [KS Data Formats and Data Ranges](../stream/ks-data-formats-and-data-ranges.md). For more information about KS data ranges, see [Data Range Intersections in AVStream](../stream/data-range-intersections-in-avstream.md).

The remainder of this section discusses the following topics:

[Audio Data Formats](audio-data-formats.md)

[Audio Data Ranges](audio-data-ranges.md)

[Extensible Wave-Format Descriptors](extensible-wave-format-descriptors.md)

[Multichannel Formats for Home-Theater Systems](multichannel-formats-for-home-theater-systems.md)

[Examples of Audio Data Formats and Data Ranges](examples-of-audio-data-formats-and-data-ranges.md)

 

