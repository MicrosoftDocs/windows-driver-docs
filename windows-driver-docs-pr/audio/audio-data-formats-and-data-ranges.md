---
Description: Audio Data Formats and Data Ranges
MS-HAID: 'audio.audio\_data\_formats\_and\_data\_ranges'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Audio Data Formats and Data Ranges
---

# Audio Data Formats and Data Ranges


## <span id="audio_data_formats_and_data_ranges"></span><span id="AUDIO_DATA_FORMATS_AND_DATA_RANGES"></span>


Audio drivers use the [**KSDATAFORMAT**](stream.ksdataformat) and [**KSDATARANGE**](stream.ksdatarange) structures to specify audio stream formats:

-   The digital format of a KS data stream is specified by a KS format descriptor that begins with a KSDATAFORMAT structure.

-   The range of stream formats that a KS pin can support is specified by an array of KS data ranges; each array element is a range descriptor that begins with a KSDATARANGE structure.

For more information about these two structures, see [KS Data Formats and Data Ranges](stream.ks_data_formats_and_data_ranges). For more information about KS data ranges, see [Data Range Intersections in AVStream](stream.data_range_intersections_in_avstream).

The remainder of this section discusses the following topics:

[Audio Data Formats](audio-data-formats.md)

[Audio Data Ranges](audio-data-ranges.md)

[Extensible Wave-Format Descriptors](extensible-wave-format-descriptors.md)

[Multichannel Formats for Home-Theater Systems](multichannel-formats-for-home-theater-systems.md)

[Examples of Audio Data Formats and Data Ranges](examples-of-audio-data-formats-and-data-ranges.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Data%20Formats%20and%20Data%20Ranges%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


