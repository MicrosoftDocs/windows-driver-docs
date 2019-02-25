---
title: Audio Data Formats and Data Ranges
description: Audio Data Formats and Data Ranges
ms.assetid: 85aa74b4-8e33-49f4-82e7-561baa55c265
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Audio Data Formats and Data Ranges


## <span id="audio_data_formats_and_data_ranges"></span><span id="AUDIO_DATA_FORMATS_AND_DATA_RANGES"></span>


Audio drivers use the [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) and [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures to specify audio stream formats:

-   The digital format of a KS data stream is specified by a KS format descriptor that begins with a KSDATAFORMAT structure.

-   The range of stream formats that a KS pin can support is specified by an array of KS data ranges; each array element is a range descriptor that begins with a KSDATARANGE structure.

For more information about these two structures, see [KS Data Formats and Data Ranges](https://msdn.microsoft.com/library/windows/hardware/ff567632). For more information about KS data ranges, see [Data Range Intersections in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff558680).

The remainder of this section discusses the following topics:

[Audio Data Formats](audio-data-formats.md)

[Audio Data Ranges](audio-data-ranges.md)

[Extensible Wave-Format Descriptors](extensible-wave-format-descriptors.md)

[Multichannel Formats for Home-Theater Systems](multichannel-formats-for-home-theater-systems.md)

[Examples of Audio Data Formats and Data Ranges](examples-of-audio-data-formats-and-data-ranges.md)

 

 




