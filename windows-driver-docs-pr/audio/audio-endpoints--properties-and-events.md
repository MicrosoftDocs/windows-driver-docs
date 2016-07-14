---
Description: 'Audio Endpoints, Properties and Events'
MS-HAID: 'audio.audio\_endpoints\_\_properties\_and\_events'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Audio Endpoints, Properties and Events'
---

# Audio Endpoints, Properties and Events


## <span id="audio_properties_and_events"></span><span id="AUDIO_PROPERTIES_AND_EVENTS"></span>


The PortCls system driver supports a subset of the intrinsic operations that are described in [KS Properties, Events, and Methods](stream.ks_properties__events__and_methods).

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

[KSPROPSETID\_AC3](audio.kspropsetid_ac3)

[KSPROPSETID\_Acoustic\_Echo\_Cancel](audio.kspropsetid_acoustic_echo_cancel)

[KSPROPSETID\_Audio](audio.kspropsetid_audio)

[KSPROPSETID\_DirectSound3DBuffer](audio.kspropsetid_directsound3dbuffer)

[KSPROPSETID\_DirectSound3DListener](audio.kspropsetid_directsound3dlistener)

[KSPROPSETID\_DrmAudioStream](audio.kspropsetid_drmaudiostream)

[KSPROPSETID\_General](stream.kspropsetid_general)

[KSPROPSETID\_Hrtf3d](audio.kspropsetid_hrtf3d)

[KSPROPSETID\_Jack](audio.kspropsetid_jack)

[KSPROPSETID\_Pin](stream.kspropsetid_pin)

[KSPROPSETID\_Synth](audio.kspropsetid_synth)

[KSPROPSETID\_Synth\_Dls](audio.kspropsetid_synth_dls)

[KSPROPSETID\_TopologyNode](audio.kspropsetid_topologynode)

All audio drivers support the **KSPROPSETID\_Audio** property set.

Some audio adapter drivers support the following event set:

[KSEVENTSETID\_AudioControlChange](audio.kseventsetid_audiocontrolchange)

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Endpoints,%20Properties%20and%20Events%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



