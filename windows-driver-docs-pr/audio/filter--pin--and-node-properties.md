---
title: Filter, Pin, and Node Properties
description: Filter, Pin, and Node Properties
keywords:
- audio properties WDK , filters
- WDM audio properties WDK , filters
- audio properties WDK , pins
- WDM audio properties WDK , pins
- audio properties WDK , nodes
- WDM audio properties WDK , nodes
- filter properties WDK audio
- node properties WDK audio
- KS filters WDK audio , property requests
- filters WDK audio , property requests
- filters WDK audio , property overview
- nodes WDK audio , property overview
- pins WDK audio , property overview
ms.date: 04/20/2017
---

# Filter, Pin, and Node Properties

Microsoft Windows Driver Model (WDM) audio drivers represent an audio device as a KS filter, and they represent a hardware buffer on the device as a pin on the filter. When a client sends a property request to one of these filter or pin objects, the port driver receives the request and routes the request to the appropriate property handler in the port driver or miniport driver.

Audio devices support three kinds of properties:

- **Filter properties**

    A filter property is a property of the filter as a whole rather than a property of a particular pin or node within the filter. Requests for filter properties specify filter handles, but they do not specify node IDs.

- **Pin properties**

    A pin property is a property of a particular pin instance on the filter. Requests for these properties specify pin handles, but they do not specify node IDs.

- **Node properties**

    A node property is a property of a topology node within the filter. A request for a node property specifies a filter handle or pin handle, plus a node ID.

Whether a node-property request specifies a filter or pin handle depends on whether the node is unique to the filter. For more information, see the following Node Properties section.

The following figure shows these three kinds of property request: a pin-property request sent to a pin instance, a node-property request sent to a node (on a filter or pin instance), and a filter-property request sent to a filter instance.

:::image type="content" source="images/propreqs.png" alt-text="Diagram illustrating filter, pin, and node property requests.":::

Typically, the port driver handles most requests for filter and pin properties, and the miniport driver handles requests for node properties.

The port driver supplies its own built-in handlers for the filter and pin properties that are used by the [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) (see [KSPROPSETID\_Sysaudio](./kspropsetid-sysaudio.md) and [KSPROPSETID\_Sysaudio\_Pin](./kspropsetid-sysaudio-pin.md)) and [WDMAud system driver](user-mode-wdm-audio-components.md#wdmaud_system_driver). A miniport driver does not need to implement handlers for properties that the port driver handles. A typical miniport driver provides few, if any, handlers for filter and pin properties. The miniport driver supplies the handlers for node properties that represent hardware-dependent features of the audio device. The port drivers supply no built-in handling of node properties, with the exception of [**KSPROPERTY\_TOPOLOGY\_NAME**](../stream/ksproperty-topology-name.md).

When both the port driver and miniport driver supply handlers for the same property, the port driver uses its own handler and ignores the miniport driver's handler.

## Filter Descriptors

The port driver obtains pointers to the miniport driver's property handlers by calling the [**IMiniport::GetDescription**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiport-getdescription) method. Through this method, the port driver retrieves a pointer to the miniport driver's filter descriptor, which is a structure of type [**PCFILTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcfilter_descriptor). This structure specifies the miniport driver's property handlers for filter, pin, and node properties:

- The PCFILTER\_DESCRIPTOR structure's **AutomationTable** member points to the automation table for the filter. This table specifies the miniport driver's property handlers for filter properties.

- The PCFILTER\_DESCRIPTOR structure's **Pins** member contains the automation tables for the pins. Each table specifies the property handlers for the pin properties of a particular pin type.

- The PCFILTER\_DESCRIPTOR structure's **Nodes** member contains the automation tables for the topology nodes inside the filter. Each table specifies the property handlers for the node properties of a particular node type.

## Filter Properties

The port driver accesses the miniport driver's filter-property handlers through the **AutomationTable** member of PCFILTER\_DESCRIPTOR. Typically, this automation table contains few handlers because the port driver supplies its own built-in handlers for all the filter properties that SysAudio and WDMAud use to query and configure audio devices.

However, the miniport driver can supply handlers for filter properties such as [**KSPROPERTY\_GENERAL\_COMPONENTID**](../stream/ksproperty-general-componentid.md) that provide hardware-dependent information that is not available to the port driver. Two of the sample audio drivers in the Microsoft Windows Driver Kit (WDK) handle the KSPROPERTY\_GENERAL\_COMPONENTID property. For more information, see the miniport driver implementations in the Sysvad sample driver, which is discussed in [Sample Audio Drivers](sample-audio-drivers.md).

All the port drivers in Portcls.sys provide handling for the [KSPROPSETID\_Pin](../stream/kspropsetid-pin.md) and [KSPROPSETID\_Topology](../stream/kspropsetid-topology.md) property sets. All the properties in these sets are filter properties, with the exception of [**KSPROPERTY\_TOPOLOGY\_NAME**](../stream/ksproperty-topology-name.md), which is a node property (that uses a filter handle, not a pin handle, to specify the target for the request). The port drivers support the following subset of the KSPROPSETID\_Pin properties:

[**KSPROPERTY\_PIN\_CATEGORY**](../stream/ksproperty-pin-category.md)

[**KSPROPERTY\_PIN\_CINSTANCES**](../stream/ksproperty-pin-cinstances.md)

[**KSPROPERTY\_PIN\_COMMUNICATION**](../stream/ksproperty-pin-communication.md)

[**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](../stream/ksproperty-pin-constraineddataranges.md)

[**KSPROPERTY\_PIN\_CTYPES**](../stream/ksproperty-pin-ctypes.md)

[**KSPROPERTY\_PIN\_DATAFLOW**](../stream/ksproperty-pin-dataflow.md)

[**KSPROPERTY\_PIN\_DATAINTERSECTION**](../stream/ksproperty-pin-dataintersection.md)

[**KSPROPERTY\_PIN\_DATARANGES**](../stream/ksproperty-pin-dataranges.md)

[**KSPROPERTY\_PIN\_GLOBALCINSTANCES**](../stream/ksproperty-pin-globalcinstances.md)

[**KSPROPERTY\_PIN\_INTERFACES**](../stream/ksproperty-pin-interfaces.md)

[**KSPROPERTY\_PIN\_MEDIUMS**](../stream/ksproperty-pin-mediums.md)

[**KSPROPERTY\_PIN\_NAME**](../stream/ksproperty-pin-name.md)

[**KSPROPERTY\_PIN\_NECESSARYINSTANCES**](../stream/ksproperty-pin-necessaryinstances.md)

[**KSPROPERTY\_PIN\_PHYSICALCONNECTION**](../stream/ksproperty-pin-physicalconnection.md)

[**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT**](../stream/ksproperty-pin-proposedataformat.md)

[**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2**](../stream/ksproperty-pin-proposedataformat2.md)

These properties provide information about the pin factories belonging to a filter. Typically, clients query the filter for these properties before creating pin instances. The port drivers support all four of the KSPROPSETID\_Topology properties, which provide information about the filter's internal topology.

In addition, the DMus port driver provides a handler for the [**KSPROPERTY\_SYNTH\_MASTERCLOCK**](/previous-versions/ff537403(v=vs.85)) property, which is a get-only property of a DirectMusic filter. KSPROPERTY\_SYNTH\_MASTERCLOCK is a member of the [KSPROPSETID\_SynthClock](./kspropsetid-synthclock.md) property set.

### <span id="Pin_Properties"></span><span id="pin_properties"></span><span id="PIN_PROPERTIES"></span>Pin Properties

The port driver accesses the miniport driver's pin-property handlers through the **Pins** member of PCFILTER\_DESCRIPTOR. This member points to an array of pin descriptors, and each descriptor points to the automation table for a pin type (identified by a pin ID, which is simply the array index).

Typically, these automation tables contain few entries because the port driver supplies its own handlers for all the pin properties that SysAudio and WDMAud use. A miniport driver has the option of supplying handlers for one or more pin properties that the port driver does not handle, but only clients that know about these properties can send property requests for them.

With the exception of the Topology port driver, all the port drivers in Portcls.sys supply built-in handlers for the following pin properties:

[**KSPROPERTY\_CONNECTION\_STATE**](../stream/ksproperty-connection-state.md)

[**KSPROPERTY\_CONNECTION\_DATAFORMAT**](../stream/ksproperty-connection-dataformat.md)

[**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING**](../stream/ksproperty-connection-allocatorframing.md)

[**KSPROPERTY\_STREAM\_ALLOCATOR**](../stream/ksproperty-stream-allocator.md)

[**KSPROPERTY\_STREAM\_MASTERCLOCK**](../stream/ksproperty-stream-masterclock.md)

[**KSPROPERTY\_AUDIO\_POSITION**](./ksproperty-audio-position.md)

[**KSPROPERTY\_DRMAUDIOSTREAM\_CONTENTID**](/previous-versions/ff537351(v=vs.85))

Some of the properties in this list require hardware-dependent information from the miniport driver. When the port driver receives an IRP containing a request for one of these properties, it does not pass the IRP to the miniport driver. Instead, the port driver handles the request itself, but its handler obtains the information it needs by calling an entry point in the miniport driver. For example, the port driver supplies its own property handler for KSPROPERTY\_AUDIO\_POSITION requests. This handler simply calls the miniport driver stream's **GetPosition** method (for example, [**IMiniportWavePciStream::GetPosition**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-getposition)) to get the current position.

### <span id="Node_Properties"></span><span id="node_properties"></span><span id="NODE_PROPERTIES"></span>Node Properties

The port driver accesses the miniport driver's node-property handlers through the **Nodes** member of PCFILTER\_DESCRIPTOR. This member points to an array of node descriptors, and each descriptor points to the automation table for a node type (identified by a node ID, which is simply the array index). Typically, all or most of the property handlers belonging to a miniport driver reside in the **Nodes** array. An audio driver represents the hardware controls in an audio device as topology nodes, and it uses the property mechanism to provide clients with access to the hardware-dependent control settings.

As described previously, a client sends a filter-property request to a filter handle, and a pin-property request to a pin handle. Unlike a filter or pin instance, a node is not a kernel object and does not have a handle. A client sends a node-property request to either a pin handle or a filter handle, but the request also specifies a node ID to indicate that the request is for a node property rather than a pin or filter property.

The following are general rules for determining whether a node property should use a filter handle or pin handle:

-   If a filter contains several instances of a particular pin type, and each pin of that type contains a node with a particular node ID, then each pin instance contains an instance of the node. In this case, a node-property request must specify a pin handle (rather than just a filter handle) to distinguish among several instances of the same node type. The combination of pin handle and node ID unambiguously identifies a particular node instance as the target for the request.

-   If a filter contains only one instance of a particular node, a node property request specifies a filter handle. The combination of filter handle and node ID is sufficient to unambiguously identify the node that is the target for the request.

Before implementing a handler for a particular node property, however, the driver writer should refer to [Audio Drivers Property Sets](./audio-drivers-property-sets.md) to check whether the target for the property should be specified as a filter handle or pin handle.

The port drivers in Portcls.sys currently do not provide built-in handling of node properties, with the exception of KSPROPERTY\_TOPOLOGY\_NAME.

### <span id="Overspecified_and_Underspecified_Property_Requests"></span><span id="overspecified_and_underspecified_property_requests"></span><span id="OVERSPECIFIED_AND_UNDERSPECIFIED_PROPERTY_REQUESTS"></span>Overspecified and Underspecified Property Requests

Drivers should be prepared to deal with property requests from clients that do not follow the preceding rules. Requests can be either overspecified or underspecified:

-   **Overspecified requests**

    If a property request requires only a filter handle, but the client sends the request to a pin handle instead, the target for the request is overspecified. However, drivers typically treat the request as valid; that is, they treat the request as though it had been sent to the filter containing the pin.

-   **Underspecified requests**

    If a property request requires a pin handle, but a client sends the request to a filter handle instead, the target for the request is underspecified. For example, if a filter contains several pin instances with the same node type, and a client sends a request for a property of that node type to a filter handle rather than a pin handle, the driver has no way to determine which node instance should receive the request. In this case, the behavior depends on the driver. Instead of automatically failing all underspecified requests, some drivers treat an underspecified set-property request as valid. In this case, the interpretation is that the request sets the default value for the specified node ID. When a pin factory creates a new node instance, the property belonging to the new node is initialized to the default value. A request that changes the default value has no effect on node instances created before the request. In addition, drivers uniformly fail underspecified get-property requests because the handler has no way to determine which node instance to query for the property.

### <span id="Exceptions_to_the_Rules"></span><span id="exceptions_to_the_rules"></span><span id="EXCEPTIONS_TO_THE_RULES"></span>Exceptions to the Rules

For historical reasons, a few audio properties have behavioral quirks that violate these general rules. The following are examples:

-   As described in [Applying Speaker-Configuration Settings](applying-speaker-configuration-settings.md), a client can change an audio device's speaker configuration by setting the [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](./ksproperty-audio-channel-config.md) property of a 3-D node ([**KSNODETYPE\_3D\_EFFECTS**](./ksnodetype-3d-effects.md)). The speaker-configuration setting is global because it changes the speaker configuration for all streams that are part of the mix that the device plays through the speakers. According to the general rule, a node-property request that affects the filter as a whole should specify a filter handle (plus a node ID). However, this particular property requires a pin handle instead of a filter handle. The pin handle designates the pin instance containing the 3-D node that is the target for the request.

-   [**KSPROPERTY\_SYNTH\_VOLUME**](/previous-versions/ff537409(v=vs.85)) and [**KSPROPERTY\_SYNTH\_MASTERCLOCK**](/previous-versions/ff537403(v=vs.85)) are properties of a synth node ([**KSNODETYPE\_SYNTHESIZER**](./ksnodetype-synthesizer.md)). Although both are node properties, requests for these properties do not include node IDs. (Note that the property descriptor for the request is a structure of type [**KSPROPERTY**](../stream/ksproperty-structure.md), not [**KSNODEPROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty).) This behavior violates the general rule that a node property requires a node ID. Despite this discrepancy, a miniport driver that supports either property should supply the property handler through the **Nodes** member of PCFILTER\_DESCRIPTOR (instead of the **Pins** member).

