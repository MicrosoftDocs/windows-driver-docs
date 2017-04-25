---
title: Specifying Pin Data Ranges
description: Specifying Pin Data Ranges
ms.assetid: bef74cd1-d2be-402d-be7f-acc7d8cbf392
keywords:
- pins WDK audio , data ranges
- WDM audio drivers WDK , pin data ranges
- audio drivers WDK , pin data ranges
- data ranges WDK audio , pins
- configurable pins WDK audio drivers
- formats WDK audio , pin data ranges
- intersections WDK audio drivers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying Pin Data Ranges


After defining a topology to represent the data paths and control nodes in your devices, the next step is to define the [data ranges](audio-data-ranges.md) for each configurable pin. A configurable pin can be created, configured, and connected to a wave or MIDI stream under software control. In contrast, a physical connection or bridge pin exists implicitly and can neither be created nor configured under software control.

Before connecting a configurable pin to serve as a sink or source for a wave or MIDI stream, the pin must be configured to handle the data format for the stream. Typically, the pin can be configured to accept one of several stream formats. For example, a PCM wave-output pin might accept the following ranges of PCM stream parameters:

-   Sample rates of 11.025 kHz, 22.05 kHz, 44.1 kHz, and 48 kHz

-   Sample sizes of 8, 16, 24, and 32 bits

-   Any number of channels from 1 through 8

For each type of configurable pin, a miniport driver describes the various stream data formats that the pin can handle. These parameter ranges can be specified as an array of data-range descriptors, as shown in the following code example.

```
static KSDATARANGE_AUDIO PinDataRangesPcm[] =
{
    {
        {
            sizeof(KSDATARANGE_AUDIO),
            0,
            0,
            0,
            STATICGUIDOF(KSDATAFORMAT_TYPE_AUDIO),
            STATICGUIDOF(KSDATAFORMAT_SUBTYPE_PCM),
            STATICGUIDOF(KSDATAFORMAT_SPECIFIER_WAVEFORMATEX)
        },
        8,       // Maximum number of channels
        8,       // Minimum number of bits-per-sample
        32,      // Maximum number of bits-per-channel
        11025,   // Minimum rate
        48000    // Maximum rate
    }
};
```

Note that the `PinDataRangesPcm` array in the preceding example contains a single data-range descriptor of type [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096). More generally, a data-range array can contain an arbitrary number of descriptors. For example, a non-PCM wave-output pin might support both AC-3-over-S/PDIF and WMA Pro-over-S/PDIF formats. Each of these two formats is specified by a separate data-range descriptor. Thus, the pin's data-range array would contain at least two KSDATARANGE\_AUDIO structures.

A configurable pin that supports the music stream format from an application that uses DirectMusic or the Windows multimedia midiIn*Xxx* and midiOut*Xxx* functions uses a data-range descriptor of type [**KSDATARANGE\_MUSIC**](https://msdn.microsoft.com/library/windows/hardware/ff537097).

The port driver obtains the data-range information from the miniport driver and uses this information, wherever possible, to handle requests for information about the data formats that each pin can support. In the case of a pin with a simple PCM data range, the port driver is able to handle the intersection requests for that pin. In an intersection request, a client supplies a set of data ranges that represent possible data formats for a stream. If possible, the port driver's intersection handler picks a particular data format from the data ranges in the request that also falls within its pin's data ranges. This format represents an intersection of the two sets of data ranges. Hence, both the client and the pin can process a stream with this format. For more complex data ranges, the miniport driver can provide its own intersection handler, which the port driver then uses instead of its own, default handler. The intersection handler of the miniport driver can allow for any format requirements that might be difficult to express to the port driver as an array of data ranges. For more information, see [Data-Intersection Handlers](data-intersection-handlers.md). Additional information is available in the white paper titled *Multiple Channel Audio Data and WAVE Files* at the [audio technology](http://go.microsoft.com/fwlink/p/?linkid=8751) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Specifying%20Pin%20Data%20Ranges%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


