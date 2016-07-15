---
Description: 'Audio Filters, Pins, and Nodes'
MS-HAID: 'audio.audio\_filters\_\_pins\_\_and\_nodes'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Audio Filters, Pins, and Nodes'
---

# Audio Filters, Pins, and Nodes


## <span id="audio_filters_pins_and_nodes"></span><span id="AUDIO_FILTERS_PINS_AND_NODES"></span>


A Microsoft Windows Driver Model (WDM) adapter driver exposes its audio hardware as a collection of filter factories, each of which can create one or more filter instances. A kernel streaming (KS) filter object can encapsulate an audio hardware function that performs some type of digital processing of the wave audio data that streams through the filter. For example, the filter might do rendering or synthesis of a stream, or it might add reverb to a stream.

A filter instance exposes pin factories, each of which can create one or more pin instances. These pins can be connected to the pins of other filters to produce filter graphs. To be part of an audio filter graph, a filter must have one or more pin instances.

A pin represents an input or output connection point through which a data stream enters or exits the filter. Each pin specifies the range of data formats that it can support, and only a stream with a compatible format can flow through the pin.

A filter for a WDM audio device exposes its internal topology in the form of nodes and connections.

Topology nodes lie on the data paths that pass through the filter. A node represents a point of control within the filter. Each node logically encapsulates a modular chunk of the filter's functionality and performs digital-signal processing on the data stream that passes through the node. A node might represent a volume control, for example, that can be adjusted under software control.

The filter object also specifies the connections between its various pins and nodes. Implicit in these connections is the ordering of nodes along each data path through the filter.

This section presents the features of filters, pins, and nodes that are specific to WDM audio drivers. The following topics are discussed:

[Audio Filters](audio-filters.md)

[Filter Factories](filter-factories.md)

[Pin Factories](pin-factories.md)

[Nodes and Connections](nodes-and-connections.md)

[Audio Filter Graphs](audio-filter-graphs.md)

[Wave Filters](wave-filters.md)

[MIDI and DirectMusic Filters](midi-and-directmusic-filters.md)

[Topology Filters](topology-filters.md)

For a more general discussion of kernel-streaming filters, pins, and nodes, see [KS Minidriver Architecture](stream.ks_minidriver_architecture).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Filters,%20Pins,%20and%20Nodes%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


