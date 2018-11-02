---
title: Pin Factories
description: Pin Factories
ms.assetid: 1399b8e1-bd73-4052-afa5-3e992be8789b
keywords:
- audio filters WDK audio , pin factories
- pin factories WDK audio
- pins WDK audio , factories
- filters WDK audio , pin factories
- multiple pin factories WDK audio
- data formats WDK audio , pin factories
- formats WDK audio , pin factories
- multiple pin instances WDK audio
- identifying pin factories
- KSPIN_DESCRIPTOR structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pin Factories


## <span id="pin_factories"></span><span id="PIN_FACTORIES"></span>


An audio filter's pin factories describe all of the pins that the filter can instantiate. As mentioned previously, an audio miniport driver stores pin information in an array of [**PCPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537721) structures. Each structure specifies a pin factory, and a pin factory is identified by its index in the array. This index is frequently referred to as the *pin ID*.

A PCPIN\_DESCRIPTOR structure contains an automation table and a [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure.

The KSPIN\_DESCRIPTOR structure contains the following information about the pins in the pin factory:

-   Filter-relative direction of data flow

-   Filter-relative direction of communication flow (In all current Windows versions, KS filters use IRPs for communication.)

-   Pin category

-   Friendly name

-   Instance capabilities

-   Data-format capabilities

The structure's **Category** and **Name** members specify the pin factory's pin category and friendly name. For each pin factory in the filter, the miniport driver specifies a combination of **Category** and **Name** GUIDs that together uniquely identify the pin factory. If two or more pin factories share the same **Category** value, each pin factory has a **Name** value that distinguishes it from the others. If only a single pin factory has a particular **Category** value, that value is sufficient to identify the pin factory, and the **Name** value for that pin factory can be set to **NULL**. For a coding example, see [Exposing Filter Topology](exposing-filter-topology.md). For information about pin categories, see [Pin Category Property](pin-category-property.md).

A pin factory specifies the range of data formats that it supports as an array of extended [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures:

-   A pin factory that supports a range of wave or DirectSound data formats for its input or output stream specifies an array of [**KSDATARANGE\_AUDIO**](https://msdn.microsoft.com/library/windows/hardware/ff537096) structures.

-   A pin factory that supports a range of MIDI or DirectMusic data formats for its input or output stream specifies an array of [**KSDATARANGE\_MUSIC**](https://msdn.microsoft.com/library/windows/hardware/ff537097) structures.

KSDATARANGE\_AUDIO and KSDATARANGE\_MUSIC are extended versions of KSDATARANGE. For examples of both types of data ranges, see [Audio Data Formats and Data Ranges](audio-data-formats-and-data-ranges.md).

Before connecting a sink pin on one filter to a source pin on another filter, a graph builder (for example, the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver)) can search the data ranges for a compatible format. The graph builder typically calls the filter's [data-intersection handler](data-intersection-handlers.md), which allows the filter itself to choose a compatible format.

A filter can have multiple pin factories, and a pin factory can support multiple pin instances.

-   Having multiple pin factories on a filter is useful for distinguishing separate data paths for the different types of data that flow through the filter. For example, one pin factory might support PCM data streams, and another pin factory might support AC-3 streams.

-   A single filter can support rendering and capture streams simultaneously. The rendering and capture paths have separate sets of filter factories.

-   Having multiple pin instances on a sink-pin factory frequently implies mixing, in which case the filter contains a SUM node ([**KSNODETYPE\_SUM**](https://msdn.microsoft.com/library/windows/hardware/ff537196)).

Like filters, pins are kernel objects and are identified by kernel handles. The handle for a pin instance is created by calling [**KsCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff561652). As a kernel object, a pin can be specified as the target of an IRP. A client of the driver specifies the pin handle when sending an IOCTL request to a pin.

When building an [audio filter graph](audio-filter-graphs.md), SysAudio links one filter to another by connecting their pins. A source pin from one filter can be connected to the sink pin of another filter. Data and IRPs from the source pin flow into the sink pin through this connection. To make the connection, a graph builder (typically SysAudio) creates the source pin first by calling [**KsCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff561652) and then creates the sink pin by calling **KsCreatePin** again. In the second call, however, the client specifies that the new sink pin is to be connected to the source pin that was created in the first call.

 

 




