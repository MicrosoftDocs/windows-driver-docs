---
title: Kernel Streaming Topology to Audio Mixer API Translation
description: Kernel Streaming Topology to Audio Mixer API Translation
ms.assetid: ee89dc67-c9f3-41cd-8a09-0c46d636fe64
keywords:
- mixer API WDK audio
- kernel streaming WDK audio
- audio mixer lines WDK audio
- source mixer lines WDK audio
- destination mixer lines WDK audio
- translating KS topology to mixer lines WDK audio
- mixer lines WDK audio
- KS stream mixing WDK audio
- KS topology WDK audio
- sink pins WDK audio
- source pins WDK audio
- KS pins WDK audio , translating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel Streaming Topology to Audio Mixer API Translation


## <span id="kernel_streaming_topology_to_audio_mixer_api_translation"></span><span id="KERNEL_STREAMING_TOPOLOGY_TO_AUDIO_MIXER_API_TRANSLATION"></span>


The **mixer** API is a set of Windows multimedia functions that are used to retrieve information about audio-mixer devices. The **mixer** API classifies audio-mixer lines as source and destination lines. *Source lines* are inputs into the audio card (for example, CD, microphone, line-in, and wave). *Destination lines* are outputs from the card (for example, speakers, headphones, phone line, and wave in). For a source line to be valid, it should have a unique path from the source to a destination. A single source line might map to more than one destination, but no more than a single path can connect a source line to a destination line. For more information about the **mixer** API, see the Microsoft Windows SDK documentation.

The WDM driver for an audio adapter exposes a KS-filter topology that represents the data paths through the hardware and the functions that are available on those paths. The [WDMAud system driver](user-mode-wdm-audio-components.md#wdmaud_system_driver) (in the Wdmaud.sys and Wdmaud.drv files) should interpret the KS-filter topology and generate the corresponding source and destination mixer lines that are exposed through the **mixer** API. WDMAud also handles the **mixer** API calls and translates them into the equivalent property calls on the filter pins and nodes that are managed by the adapter driver.

The [KMixer system driver](kernel-mode-wdm-audio-components.md#kmixer_system_driver) (Kmixer.sys) and [SWMidi system driver](kernel-mode-wdm-audio-components.md#swmidi_system_driver) (Swmidi.sys) are integral components of the kernel audio stack. KMixer provides system-wide audio mixing, bit-depth conversion, sample-rate conversion, and channel-to-speaker configuration (supermix) translation for PCM audio streams. SWMidi provides high-quality software synthesis of MIDI streams. The system audio driver, SysAudio (Sysaudio.sys; see [SysAudio System Driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver)), combines the capabilities of KMixer and SWMidi with the installed audio adapter drivers to form functionally enhanced [virtual audio devices](virtual-audio-devices.md).

WDMAud manages the interface between the KS portion and the legacy (see [WinMM System Component](user-mode-wdm-audio-components.md#winmm_system_component)) portion of the audio stack. WDMAud translates the pins on the SysAudio-virtualized filters into the legacy mixer lines that are presented in applications such as SndVol32. The translation from KS topology to mixer lines is performed as follows:

-   Source pins (KSPIN\_DATAFLOW\_OUT) in the KS topology are exposed as destination mixer lines (MIXERLINE\_COMPONENTTYPE\_DST\_*XXX*).

-   Sink pins (KSPIN\_DATAFLOW\_IN) in the KS topology are exposed as source mixer lines (MIXERLINE\_COMPONENTTYPE\_SRC\_*XXX*).

-   WDMAud walks the KS filter graph beginning at the source pin that lies at the endpoint of the filter graph and traverses the graph in the direction opposite to data flow until a sink pin is reached.

-   The properties that are supported on each KS node that is encountered during the traversal are exposed as controls on the source mixer line.

In the first two items above, the mapping of KS source and sink pins to destination and source mixer lines is potentially confusing because of the differences in terminology. In KS, a device is wrapped in a filter that has sink (input) pins and source (output) pins. The terms "sink" and "source" refer not to the filter but rather to the (typically buffered) connection between two filters:

-   The upstream filter's source pin is the source of the data stream that enters the connection.

-   The data stream exits the connection through the downstream filter's sink pin.

In contrast, the mixer-line terminology is device-centric:

-   A source mixer line is the source of a stream that enters the device.

-   A destination mixer line is the destination of a stream that exits the device.

Also, the KS terminology is somewhat inconsistent in the stream-flow direction that it assigns to a pin on a KS filter. The pin descriptor uses a [**KSPIN\_DATAFLOW**](https://msdn.microsoft.com/library/windows/hardware/ff563532) enumeration value to specify the direction:

-   A stream that enters the filter through a sink pin has a direction of KSPIN\_DATAFLOW\_IN.

-   A stream that exits the filter through a source pin has a direction of KSPIN\_DATAFLOW\_OUT.

The directions "in" and "out" are clearly filter-centric, whereas the terms "sink" and "source" are connection-centric.

For more information about the topology parsing algorithm used by WDMAud, see [WDMAud Topology Parsing](wdmaud-topology-parsing.md).

This section also includes:

[Topology Pins](topology-pins.md)

[Topology Nodes](topology-nodes.md)

[SysTray and SndVol32](systray-and-sndvol32.md)

[Exposing Filter Topology](exposing-filter-topology.md)

 

 




