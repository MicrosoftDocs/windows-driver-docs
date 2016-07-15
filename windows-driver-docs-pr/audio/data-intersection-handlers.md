---
Description: 'Data-Intersection Handlers'
MS-HAID: 'audio.data\_intersection\_handlers'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Data-Intersection Handlers'
---

# Data-Intersection Handlers


## <span id="data_intersection_handlers"></span><span id="DATA_INTERSECTION_HANDLERS"></span>


This section discusses data-intersection handlers in Microsoft Windows Driver Model (WDM) audio drivers. For a broader discussion of data-intersection handling for KS filters in general, see [DataRange Intersections in AVStream](stream.data_range_intersections_in_avstream).

In older versions of Windows such as Windows XP, the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio-system-driver) constructs a [virtual audio device](virtual-audio-devices.md) by connecting together pairs of audio-filter pins to form an [audio filter graph](audio-filter-graphs.md). Before a source pin on one filter can be connected to a sink pin of another, SysAudio must negotiate a common format that the two pins can use to exchange data. The details of this negotiation are largely delegated to the data-intersection handlers that are implemented in the individual filters.

Similarly, in Windows Vista and later, the audio engine must negotiate a common stream format with the data-intersection handler in the wave filter that represents the audio rendering device.

An adapter driver creates a WaveRT filter for an audio device by binding one of its miniport drivers to the corresponding port driver from Portcls.sys. The port driver contains a default data-intersection handler, but the default handler always gives the miniport driver's proprietary data-intersection handler the first opportunity to determine a common format. If the proprietary handler declines this opportunity, however, the port driver's default handler determines the format.

The port driver's default data-intersection handler is designed to deal with the most common hardware features. For simple audio devices, the default handler provides a convenient alternative to implementing a proprietary handler in the adapter driver. However, adapters with more advanced features might need proprietary handlers in order to expose the full capabilities of the hardware.

The remainder of this section describes some of the limitations of the port driver's default data-intersection handler and presents the techniques that are needed to design a proprietary data-intersection handler for an adapter driver. The following topics are discussed:

[Data Intersection](data-intersection.md)

[Default Data-Intersection Handlers](default-data-intersection-handlers.md)

[Proprietary Data-Intersection Handlers](proprietary-data-intersection-handlers.md)

[Hardware Constraints on Sample Frequency](hardware-constraints-on-sample-frequency.md)

[Output Buffer Size](output-buffer-size.md)

[Data Ranges with Discrete Values](data-ranges-with-discrete-values.md)

[Wild Cards](wild-cards.md)

[Data-Range Properties](data-range-properties.md)

[KMixer Behavior](kmixer-behavior.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Data-Intersection%20Handlers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


