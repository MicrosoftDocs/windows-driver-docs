---
title: Audio Endpoints, Properties and Events
description: Audio Endpoints, Properties and Events
ms.assetid: ffc5834f-30c8-40b5-b57b-fe784331690c
keywords:
- audio events WDK
- audio properties WDK
- port drivers WDK audio , properties
- port drivers WDK audio , events
- adapter drivers WDK audio , events
- adapter drivers WDK audio , properties
- audio properties WDK , about audio properties
- audio events WDK , about audio events
- WDM audio properties WDK
- WDM audio events WDK
- WDM audio properties WDK , about audio properties
- KS properties WDK audio
- KS events WDK audio
- properties WDK audio
- pins WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Audio Endpoints, Properties and Events


## <span id="audio_properties_and_events"></span><span id="AUDIO_PROPERTIES_AND_EVENTS"></span>


The PortCls system driver supports a subset of the intrinsic operations that are described in [KS Properties, Events, and Methods](https://docs.microsoft.com/windows-hardware/drivers/stream/ks-properties--events--and-methods).

The port drivers in Portcls.sys support properties and events by providing handlers for some property and event requests and by forwarding other requests to the miniport drivers' handlers.

The current implementations of the WaveCyclic, WavePci, MIDI, and DMus port drivers provide the following:

-   Support for properties on a filter and its pins and nodes

-   Support for events on pins and nodes but not for events on the filter

A client can specify the handle to a filter or pin instance as the target for a property or event request. A request for a node property or event specifies a node ID in addition to a filter or pin handle. For more information, see [Filter, Pin, and Node Properties](filter--pin--and-node-properties.md).

The Topology port driver provides the following:

-   Support for properties on a filter and its nodes

-   Support for events on nodes

The pins on a topology filter represent hardwired connections that exist permanently and thus cannot be instantiated or deleted.

None of the port drivers provide support for methods on either the filter or its pins and nodes. The port drivers never handle method requests, and they never forward these requests to miniport drivers for handling.

Audio adapter drivers support some or all of the following standard property sets:

[KSPROPSETID\_AC3](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-ac3)

[KSPROPSETID\_Acoustic\_Echo\_Cancel](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-acoustic-echo-cancel)

[KSPROPSETID\_Audio](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-audio)

[KSPROPSETID\_DirectSound3DBuffer](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-directsound3dbuffer)

[KSPROPSETID\_DirectSound3DListener](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-directsound3dlistener)

[KSPROPSETID\_DrmAudioStream](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-drmaudiostream)

[KSPROPSETID\_General](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropsetid-general)

[KSPROPSETID\_Hrtf3d](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-hrtf3d)

[KSPROPSETID\_Jack](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-jack)

[KSPROPSETID\_Pin](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropsetid-pin)

[KSPROPSETID\_Synth](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-synth)

[KSPROPSETID\_Synth\_Dls](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-synth-dls)

[KSPROPSETID\_TopologyNode](https://docs.microsoft.com/windows-hardware/drivers/audio/kspropsetid-topologynode)

All audio drivers support the **KSPROPSETID\_Audio** property set.

Some audio adapter drivers support the following event set:

[KSEVENTSETID\_AudioControlChange](https://docs.microsoft.com/windows-hardware/drivers/audio/kseventsetid-audiocontrolchange)

In addition, audio adapter drivers are free to provide property handlers for other property sets that are defined in header file Ksmedia.h. Drivers can also define and support their own custom property and event sets, but only an application that knows about a custom property or event will be able to use it.

This section discusses audio-specific properties and events. It contains the following topics:

[Audio Property Requests](audio-property-requests.md)

[Filter, Pin, and Node Properties](filter--pin--and-node-properties.md)

[Audio Property Handlers](audio-property-handlers.md)

[Basic Support Queries for Audio Properties](basic-support-queries-for-audio-properties.md)

[Audio Endpoint Builder Algorithm](audio-endpoint-builder-algorithm.md)

[Dynamic Subdevice Registration and Unregistration](dynamic-subdeviceregistration-and-unregistration.md)

[Exposing Multichannel Nodes](exposing-multichannel-nodes.md)

[Pin Category Property](pin-category-property.md)

[Friendly Names for Audio Endpoint Devices](friendly-names-for-audio-endpoint-devices.md)

[Audio Position Property](audio-position-property.md)

[Pin Data-Range and Intersection Properties](pin-data-range-and-intersection-properties.md)

[Jack Description Property](jack-description-property.md)

[Microphone Array Geometry Property](microphone-array-geometry-property.md)

[Hardware Events](hardware-events.md)

 

 




