---
Description: 'Filter, Pin, and Node Properties'
MS-HAID: 'audio.filter\_\_pin\_\_and\_node\_properties'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Filter, Pin, and Node Properties'
---

# Filter, Pin, and Node Properties


## <span id="filter_pin_and_node_properties"></span><span id="FILTER_PIN_AND_NODE_PROPERTIES"></span>


Microsoft Windows Driver Model (WDM) audio drivers represent an audio device as a KS filter, and they represent a hardware buffer on the device as a pin on the filter. When a client sends a property request to one of these filter or pin objects, the port driver receives the request and routes the request to the appropriate property handler in the port driver or miniport driver.

Audio devices support three kinds of properties:

-   **Filter properties**

    A filter property is a property of the filter as a whole rather than a property of a particular pin or node within the filter. Requests for filter properties specify filter handles, but they do not specify node IDs.

-   **Pin properties**

    A pin property is a property of a particular pin instance on the filter. Requests for these properties specify pin handles, but they do not specify node IDs.

-   **Node properties**

    A node property is a property of a topology node within the filter. A request for a node property specifies a filter handle or pin handle, plus a node ID.

Whether a node-property request specifies a filter or pin handle depends on whether the node is unique to the filter. For more information, see the following Node Properties section.

The following figure shows these three kinds of property request: a pin-property request sent to a pin instance, a node-property request sent to a node (on a filter or pin instance), and a filter-property request sent to a filter instance.

![diagram illustrating filter-, pin-, and node-property requests](images/propreqs.png)

Typically, the port driver handles most requests for filter and pin properties, and the miniport driver handles requests for node properties.

The port driver supplies its own built-in handlers for the filter and pin properties that are used by the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio-system-driver) (see [KSPROPSETID\_Sysaudio](audio.kspropsetid_sysaudio) and [KSPROPSETID\_Sysaudio\_Pin](audio.kspropsetid_sysaudio_pin)) and [WDMAud system driver](user-mode-wdm-audio-components.md#wdmaud-system-driver). A miniport driver does not need to implement handlers for properties that the port driver handles. A typical miniport driver provides few, if any, handlers for filter and pin properties. The miniport driver supplies the handlers for node properties that represent hardware-dependent features of the audio device. The port drivers supply no built-in handling of node properties, with the exception of [**KSPROPERTY\_TOPOLOGY\_NAME**](stream.ksproperty_topology_name).

When both the port driver and miniport driver supply handlers for the same property, the port driver uses its own handler and ignores the miniport driver's handler.

### <span id="Filter_Descriptors"></span><span id="filter_descriptors"></span><span id="FILTER_DESCRIPTORS"></span>Filter Descriptors

The port driver obtains pointers to the miniport driver's property handlers by calling the [**IMiniport::GetDescription**](audio.iminiport_getdescription) method. Through this method, the port driver retrieves a pointer to the miniport driver's filter descriptor, which is a structure of type [**PCFILTER\_DESCRIPTOR**](audio.pcfilter_descriptor). This structure specifies the miniport driver's property handlers for filter, pin, and node properties:

-   The PCFILTER\_DESCRIPTOR structure's **AutomationTable** member points to the automation table for the filter. This table specifies the miniport driver's property handlers for filter properties.

-   The PCFILTER\_DESCRIPTOR structure's **Pins** member contains the automation tables for the pins. Each table specifies the property handlers for the pin properties of a particular pin type.

-   The PCFILTER\_DESCRIPTOR structure's **Nodes** member contains the automation tables for the topology nodes inside the filter. Each table specifies the property handlers for the node properties of a particular node type.

### <span id="Filter_Properties"></span><span id="filter_properties"></span><span id="FILTER_PROPERTIES"></span>Filter Properties

The port driver accesses the miniport driver's filter-property handlers through the **AutomationTable** member of PCFILTER\_DESCRIPTOR. Typically, this automation table contains few handlers because the port driver supplies its own built-in handlers for all the filter properties that SysAudio and WDMAud use to query and configure audio devices.

However, the miniport driver can supply handlers for filter properties such as [**KSPROPERTY\_GENERAL\_COMPONENTID**](stream.ksproperty_general_componentid) that provide hardware-dependent information that is not available to the port driver. Two of the sample audio drivers in the Microsoft Windows Driver Kit (WDK) handle the KSPROPERTY\_GENERAL\_COMPONENTID property. For more information, see the miniport driver implementations in the Msvad and Sb16 samples.

All the port drivers in Portcls.sys provide handling for the [KSPROPSETID\_Pin](stream.kspropsetid_pin) and [KSPROPSETID\_Topology](stream.kspropsetid_topology) property sets. All the properties in these sets are filter properties, with the exception of [**KSPROPERTY\_TOPOLOGY\_NAME**](stream.ksproperty_topology_name), which is a node property (that uses a filter handle, not a pin handle, to specify the target for the request). The port drivers support the following subset of the KSPROPSETID\_Pin properties:

[**KSPROPERTY\_PIN\_CATEGORY**](stream.ksproperty_pin_category)

[**KSPROPERTY\_PIN\_CINSTANCES**](stream.ksproperty_pin_cinstances)

[**KSPROPERTY\_PIN\_COMMUNICATION**](stream.ksproperty_pin_communication)

[**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](stream.ksproperty_pin_constraineddataranges)

[**KSPROPERTY\_PIN\_CTYPES**](stream.ksproperty_pin_ctypes)

[**KSPROPERTY\_PIN\_DATAFLOW**](stream.ksproperty_pin_dataflow)

[**KSPROPERTY\_PIN\_DATAINTERSECTION**](stream.ksproperty_pin_dataintersection)

[**KSPROPERTY\_PIN\_DATARANGES**](stream.ksproperty_pin_dataranges)

[**KSPROPERTY\_PIN\_GLOBALCINSTANCES**](stream.ksproperty_pin_globalcinstances)

[**KSPROPERTY\_PIN\_INTERFACES**](stream.ksproperty_pin_interfaces)

[**KSPROPERTY\_PIN\_MEDIUMS**](stream.ksproperty_pin_mediums)

[**KSPROPERTY\_PIN\_NAME**](stream.ksproperty_pin_name)

[**KSPROPERTY\_PIN\_NECESSARYINSTANCES**](stream.ksproperty_pin_necessaryinstances)

[**KSPROPERTY\_PIN\_PHYSICALCONNECTION**](stream.ksproperty_pin_physicalconnection)

[**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT**](stream.ksproperty_pin_proposedataformat)

[**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2**](stream.ksproperty_pin_proposedataformat2)

These properties provide information about the pin factories belonging to a filter. Typically, clients query the filter for these properties before creating pin instances. The port drivers support all four of the KSPROPSETID\_Topology properties, which provide information about the filter's internal topology.

In addition, the DMus port driver provides a handler for the [**KSPROPERTY\_SYNTH\_MASTERCLOCK**](audio.ksproperty_synth_masterclock) property, which is a get-only property of a DirectMusic filter. KSPROPERTY\_SYNTH\_MASTERCLOCK is a member of the [KSPROPSETID\_SynthClock](audio.kspropsetid_synthclock) property set.

### <span id="Pin_Properties"></span><span id="pin_properties"></span><span id="PIN_PROPERTIES"></span>Pin Properties

The port driver accesses the miniport driver's pin-property handlers through the **Pins** member of PCFILTER\_DESCRIPTOR. This member points to an array of pin descriptors, and each descriptor points to the automation table for a pin type (identified by a pin ID, which is simply the array index).

Typically, these automation tables contain few entries because the port driver supplies its own handlers for all the pin properties that SysAudio and WDMAud use. A miniport driver has the option of supplying handlers for one or more pin properties that the port driver does not handle, but only clients that know about these properties can send property requests for them.

With the exception of the Topology port driver, all the port drivers in Portcls.sys supply built-in handlers for the following pin properties:

[**KSPROPERTY\_CONNECTION\_STATE**](stream.ksproperty_connection_state)

[**KSPROPERTY\_CONNECTION\_DATAFORMAT**](stream.ksproperty_connection_dataformat)

[**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING**](stream.ksproperty_connection_allocatorframing)

[**KSPROPERTY\_STREAM\_ALLOCATOR**](stream.ksproperty_stream_allocator)

[**KSPROPERTY\_STREAM\_MASTERCLOCK**](stream.ksproperty_stream_masterclock)

[**KSPROPERTY\_AUDIO\_POSITION**](audio.ksproperty_audio_position)

[**KSPROPERTY\_DRMAUDIOSTREAM\_CONTENTID**](audio.ksproperty_drmaudiostream_contentid)

Some of the properties in this list require hardware-dependent information from the miniport driver. When the port driver receives an IRP containing a request for one of these properties, it does not pass the IRP to the miniport driver. Instead, the port driver handles the request itself, but its handler obtains the information it needs by calling an entry point in the miniport driver. For example, the port driver supplies its own property handler for KSPROPERTY\_AUDIO\_POSITION requests. This handler simply calls the miniport driver stream's **GetPosition** method (for example, [**IMiniportWavePciStream::GetPosition**](audio.iminiportwavepcistream_getposition)) to get the current position.

### <span id="Node_Properties"></span><span id="node_properties"></span><span id="NODE_PROPERTIES"></span>Node Properties

The port driver accesses the miniport driver's node-property handlers through the **Nodes** member of PCFILTER\_DESCRIPTOR. This member points to an array of node descriptors, and each descriptor points to the automation table for a node type (identified by a node ID, which is simply the array index). Typically, all or most of the property handlers belonging to a miniport driver reside in the **Nodes** array. An audio driver represents the hardware controls in an audio device as topology nodes, and it uses the property mechanism to provide clients with access to the hardware-dependent control settings.

As described previously, a client sends a filter-property request to a filter handle, and a pin-property request to a pin handle. Unlike a filter or pin instance, a node is not a kernel object and does not have a handle. A client sends a node-property request to either a pin handle or a filter handle, but the request also specifies a node ID to indicate that the request is for a node property rather than a pin or filter property.

The following are general rules for determining whether a node property should use a filter handle or pin handle:

-   If a filter contains several instances of a particular pin type, and each pin of that type contains a node with a particular node ID, then each pin instance contains an instance of the node. In this case, a node-property request must specify a pin handle (rather than just a filter handle) to distinguish among several instances of the same node type. The combination of pin handle and node ID unambiguously identifies a particular node instance as the target for the request.

-   If a filter contains only one instance of a particular node, a node property request specifies a filter handle. The combination of filter handle and node ID is sufficient to unambiguously identify the node that is the target for the request.

Before implementing a handler for a particular node property, however, the driver writer should refer to [Audio Drivers Property Sets](audio.audio_drivers_property_sets) to check whether the target for the property should be specified as a filter handle or pin handle.

The port drivers in Portcls.sys currently do not provide built-in handling of node properties, with the exception of KSPROPERTY\_TOPOLOGY\_NAME.

### <span id="Overspecified_and_Underspecified_Property_Requests"></span><span id="overspecified_and_underspecified_property_requests"></span><span id="OVERSPECIFIED_AND_UNDERSPECIFIED_PROPERTY_REQUESTS"></span>Overspecified and Underspecified Property Requests

Drivers should be prepared to deal with property requests from clients that do not follow the preceding rules. Requests can be either overspecified or underspecified:

-   **Overspecified requests**

    If a property request requires only a filter handle, but the client sends the request to a pin handle instead, the target for the request is overspecified. However, drivers typically treat the request as valid; that is, they treat the request as though it had been sent to the filter containing the pin.

-   **Underspecified requests**

    If a property request requires a pin handle, but a client sends the request to a filter handle instead, the target for the request is underspecified. For example, if a filter contains several pin instances with the same node type, and a client sends a request for a property of that node type to a filter handle rather than a pin handle, the driver has no way to determine which node instance should receive the request. In this case, the behavior depends on the driver. Instead of automatically failing all underspecified requests, some drivers treat an underspecified set-property request as valid. In this case, the interpretation is that the request sets the default value for the specified node ID. When a pin factory creates a new node instance, the property belonging to the new node is initialized to the default value. A request that changes the default value has no effect on node instances created before the request. In addition, drivers uniformly fail underspecified get-property requests because the handler has no way to determine which node instance to query for the property.

### <span id="Exceptions_to_the_Rules"></span><span id="exceptions_to_the_rules"></span><span id="EXCEPTIONS_TO_THE_RULES"></span>Exceptions to the Rules

For historical reasons, a few audio properties have behavioral quirks that violate these general rules. The following are examples:

-   As described in [Applying Speaker-Configuration Settings](applying-speaker-configuration-settings.md), a client can change an audio device's speaker configuration by setting the [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](audio.ksproperty_audio_channel_config) property of a 3-D node ([**KSNODETYPE\_3D\_EFFECTS**](audio.ksnodetype_3d_effects)). The speaker-configuration setting is global because it changes the speaker configuration for all streams that are part of the mix that the device plays through the speakers. According to the general rule, a node-property request that affects the filter as a whole should specify a filter handle (plus a node ID). However, this particular property requires a pin handle instead of a filter handle. The pin handle designates the pin instance containing the 3-D node that is the target for the request.

-   [**KSPROPERTY\_SYNTH\_VOLUME**](audio.ksproperty_synth_volume) and [**KSPROPERTY\_SYNTH\_MASTERCLOCK**](audio.ksproperty_synth_masterclock) are properties of a synth node ([**KSNODETYPE\_SYNTHESIZER**](audio.ksnodetype_synthesizer)). Although both are node properties, requests for these properties do not include node IDs. (Note that the property descriptor for the request is a structure of type [**KSPROPERTY**](stream.ksproperty), not [**KSNODEPROPERTY**](audio.ksnodeproperty).) This behavior violates the general rule that a node property requires a node ID. Despite this discrepancy, a miniport driver that supports either property should supply the property handler through the **Nodes** member of PCFILTER\_DESCRIPTOR (instead of the **Pins** member).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Filter,%20Pin,%20and%20Node%20Properties%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


