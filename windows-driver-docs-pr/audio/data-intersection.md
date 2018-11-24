---
title: Data Intersection
description: Data Intersection
ms.assetid: a1588ce0-a091-4bfd-98a9-4d78e2fc847f
keywords:
- data-intersection handlers WDK audio , about data intersection
- data intersections WDK audio
- intersections WDK audio
- data-range intersections WDK audio
- sink pins WDK audio
- source pins WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Intersection


## <span id="data_intersection"></span><span id="DATA_INTERSECTION"></span>


In an audio filter graph, an audio stream can flow from the source pin of one filter to the sink pin of another filter only if the two pins support a common format for the stream. Similarly, a client can send an audio stream to a sink pin on a filter or receive an audio stream from a source pin on a filter only if the client and pin support a common stream format. Audio filters use a technique called data intersection (short for data-range intersection) to identify a stream format that is common to two pins or to a client and a pin.

For example, in Windows Server 2003, Windows XP, Windows 2000, and Windows Me/98, the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) uses the data-intersection technique to construct an audio filter graph by connecting pairs of filter pins that support compatible audio data formats.

A [pin factory](pin-factories.md) specifies the set of formats that each pin supports as an array of data ranges, where each data range is a structure of type [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096). A data range specifies a general format type, which can be [**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) or [**KSDATAFORMAT\_DSOUND**](https://msdn.microsoft.com/library/windows/hardware/ff537094). In addition, the data range specifies a range of values for each of the following parameters:

-   Bits per sample

-   Sample frequency

-   Number of channels

The KSDATARANGE\_AUDIO structure specifies both minimum and maximum values for the bits-per-sample and sample-frequency ranges but only a maximum for the number-of-channels range. The minimum number of channels is implicitly one.

The job of negotiating a common data format for two pins consists of finding two data ranges--one from each pin--that intersect each other. A pair of data ranges intersect if:

-   They support the same general wave format (KSDATAFORMAT\_WAVEFORMATEX or KSDATAFORMAT\_DSOUND).

-   Their bits-per-sample ranges overlap.

-   Their sample-frequency ranges overlap.

As mentioned previously, the KSDATAFORMAT\_AUDIO structure implies a hardware model in which the minimum number of channels supported by a pin is always one. According to this model, the number-of-channels ranges for any two pins should always overlap because both pins support at least one channel. Obviously, a hardware adapter with a minimum number of channels greater than one does not conform to this model, but the adapter driver can include a proprietary data-intersection handler to deal with this type of issue (see the example in [Proprietary Data-Intersection Handlers](proprietary-data-intersection-handlers.md)).

Upon finding a pair of intersecting data ranges for the two pins, the handler selects a common data format from the region of intersection as follows:

-   The number of bits per sample is selected from the region in which the two bits-per-sample ranges overlap.

-   The sample frequency is selected from the region in which the two sample-frequency ranges overlap.

-   The number of channels is selected from the region in which the two number-of-channels ranges overlap.

For example, when negotiating a common format for an audio port driver's sink pin and the source pin of another filter (typically, the [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver)), SysAudio first obtains the source pin's data-range array. SysAudio then sends a [**KSPROPERTY\_PIN\_DATAINTERSECTION**](https://msdn.microsoft.com/library/windows/hardware/ff565198) request to the sink pin and includes the source pin's data-range array with this request. The kernel-streaming layer intercepts the request and iteratively calls the port driver's data-intersection handler once for each successive element in the source pin's data-range array, beginning with the first element, until the handler succeeds in finding a data intersection.

With each call that SysAudio makes to the port driver's data-intersection handler, the handler first obtains the sink pin's data-range array from the miniport driver. It then iterates through the array, beginning with the first element, until it succeeds in finding an intersection between a sink-pin data range and the current source-pin data range. The handler selects a common format that lies within the intersection and outputs this format to the caller.

At each step in the iteration, the port driver calls the miniport driver's proprietary data-intersection handler with the two data ranges--one for each of the two pins. If at any step the proprietary handler declines to handle a data-intersection check between the two data ranges, the port driver's data-intersection handler performs the check instead.

To summarize, the search for an intersection between a source-pin data range and a sink-pin data range is an iterative process:

-   In the outer loop, the kernel-streaming layer iterates through successive elements in the source pin's data-range array, beginning with the first array element.

-   In the inner loop, the port driver iterates through successive elements in the sink pin's data-range array, beginning with the first array element.

The search stops upon finding the first data intersection. This process tends to favor the elements toward the beginning of each pin's data-range array. When specifying an array of data ranges for a pin, an adapter driver should order the array elements by placing data ranges for preferred formats toward the beginning of the array.

 

 




