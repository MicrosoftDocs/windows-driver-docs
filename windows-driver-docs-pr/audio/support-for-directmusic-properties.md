---
title: Support for DirectMusic Properties
description: Support for DirectMusic Properties
keywords:
- hardware acceleration WDK audio
- miniport drivers WDK audio , kernel-mode hardware acceleration
- synthesizers WDK audio , kernel-mode hardware acceleration
- synthesizers WDK audio , property support
- IKsControl interface
- property-set GUIDs WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for DirectMusic Properties


## <span id="support_for_directmusic_properties"></span><span id="SUPPORT_FOR_DIRECTMUSIC_PROPERTIES"></span>


A DirectMusic-synthesis miniport driver specifies its hardware capabilities in the form of an array of property items. Each property item is a [**PCPROPERTY\_ITEM**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcproperty_item) structure that contains the following:

-   A property set GUID that defines a particular hardware feature that is defined by DirectMusic.

-   A pointer to a property-handler method that is implemented within the driver.

-   A set of flags that specify whether the handler can get the property, set the property, and indicate basic support for the property.

### <span id="property_set_guids"></span><span id="PROPERTY_SET_GUIDS"></span>Property Set GUIDs

The following property-set GUIDs are defined by DirectMusic:

-   GUID\_DMUS\_PROP\_DLS1

-   GUID\_DMUS\_PROP\_DLS2

-   GUID\_DMUS\_PROP\_Effects

-   GUID\_DMUS\_PROP\_GM\_Hardware

-   GUID\_DMUS\_PROP\_GS\_Capable

-   GUID\_DMUS\_PROP\_GS\_Hardware

-   GUID\_DMUS\_PROP\_INSTRUMENT2

-   GUID\_DMUS\_PROP\_LegacyCaps

-   GUID\_DMUS\_PROP\_MemorySize

-   GUID\_DMUS\_PROP\_SampleMemorySize

-   GUID\_DMUS\_PROP\_SamplePlaybackRate

-   GUID\_DMUS\_PROP\_SetSynthSink

-   GUID\_DMUS\_PROP\_SynthSink\_DSOUND

-   GUID\_DMUS\_PROP\_SynthSink\_WAVE

-   GUID\_DMUS\_PROP\_Volume

-   GUID\_DMUS\_PROP\_WavesReverb

-   GUID\_DMUS\_PROP\_WriteLatency

-   GUID\_DMUS\_PROP\_WritePeriod

-   GUID\_DMUS\_PROP\_XG\_Capable

-   GUID\_DMUS\_PROP\_XG\_Hardware

For definitions of the preceding property set GUIDs, see the description of the [**KSPROPERTY**](../stream/ksproperty-structure.md) structure in the DirectX 8.0 Programmer's Reference in the Microsoft Windows SDK. The property set for each of the preceding GUIDs consists of a single element that is identified by an index of zero.

### <span id="ikscontrol_interface"></span><span id="IKSCONTROL_INTERFACE"></span>IKsControl Interface

The [IKsControl](/windows-hardware/drivers/ddi/ksproxy/nn-ksproxy-ikscontrol) interface is used to get, set, or query for basic support of properties, events, and methods. This interface is part of the WDM kernel streaming (KS) architecture, but is also used by DirectMusic to expose properties of DirectMusic ports. To retrieve this interface, call the **IDirectMusicPort::QueryInterface** method (described in the Windows SDK documentation) with the *riid* parameter set to **IID\_IKsControl**.

The [IKsControl](/windows-hardware/drivers/ddi/ksproxy/nn-ksproxy-ikscontrol) interface has three methods: [**KsProperty**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-ikscontrol-ksproperty), [**KsEvent**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-ikscontrol-ksevent), and [**KsMethod**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-ikscontrol-ksmethod). At present, only **KsProperty** is supported by DirectMusic.

The [**IKsControl::KsProperty**](/windows-hardware/drivers/ddi/ks/nf-ks-ikscontrol-ksproperty) method gets or sets the value of a property. The manner in which a property item request is routed to a particular DirectMusic port depends on how the port is implemented:

-   No properties are supported by ports that represent DirectMusic emulation on top of the Microsoft Win32 handle-based multimedia calls (the midiOut and midiIn APIs). Use the **GUID\_DMUS\_PROP\_LegacyCaps** property set GUID to query a port for whether it is implemented with Win32 multimedia calls.

-   Property item requests to a port that represents a pluggable software synthesizer are handled entirely in user mode. The topology of this type of port is a synthesizer (represented by an [IDirectMusicSynth](/windows/win32/api/dmusics/nn-dmusics-idirectmusicsynth) interface) that is connected to a sink node (an [IDirectMusicSynthSink](/windows/win32/api/dmusics/nn-dmusics-idirectmusicsynthsink) interface). The property request is given first to the synthesizer node, and then to the sink node if it is not recognized by the synthesizer.

