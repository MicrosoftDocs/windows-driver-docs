---
title: Audio Filters, Pins, and Nodes
description: Audio Filters, Pins, and Nodes
ms.assetid: 5f30703c-bf33-49bb-bce2-990ad5b54a9c
keywords:
- WDM audio drivers WDK , filters
- audio drivers WDK , filters
- WDM audio drivers WDK , pins
- audio drivers WDK , pins
- WDM audio drivers WDK , nodes
- audio drivers WDK , nodes
- filters WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
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

For a more general discussion of kernel-streaming filters, pins, and nodes, see [KS Minidriver Architecture](https://msdn.microsoft.com/library/windows/hardware/ff567656).

 

 




