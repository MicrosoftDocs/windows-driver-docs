---
title: Topology Miniport Driver
description: Topology Miniport Driver
ms.assetid: 3e0b797e-2fa5-499b-a465-0f51f5433177
keywords:
- audio miniport drivers WDK , Topology
- miniport drivers WDK audio , Topology
- Topology miniport drivers WDK audio
- Topology miniport interface WDK audio
- connection descriptors WDK audio
- from-node WDK audio
- in-node WDK audio
- distinguished node identifiers WDK audio
- mixing audio WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Topology Miniport Driver


## <span id="topology_miniport_driver"></span><span id="TOPOLOGY_MINIPORT_DRIVER"></span>


A Topology miniport driver manages the various hardware controls (for example, volume and muting) in the audio adapter's mixer circuitry. This driver enumerates the controls as *nodes* in the mixer topology, allowing clients to discover the interconnections between nodes, and to query and set the control parameters at each node.

The [SysAudio system driver](kernel-mode-wdm-audio-components.md#sysaudio_system_driver) looks at the adapter's topology when it builds an [audio filter graph](audio-filter-graphs.md). The mixer API (described in the Windows multimedia section of the Microsoft Windows SDK documentation) represents the topology nodes as mixer-line controls and exposes them to user-mode applications such as SndVol32. For more information, see [SysTray and SndVol32](systray-and-sndvol32.md).

A Topology miniport driver should implement a Topology miniport interface, which the port driver uses to initialize the miniport driver. The miniport interface, [IMiniportTopology](https://msdn.microsoft.com/library/windows/hardware/ff536712), inherits the methods in the [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698) interface; it provides no additional methods. An audio adapter driver forms a [topology filter](topology-filters.md) by binding a miniport object's IMiniportTopology interface to a port object's [IPortTopology](https://msdn.microsoft.com/library/windows/hardware/ff536896) interface.

Typically, a topology filter encompasses most of an adapter's topology nodes, although other devices within the adapter might contain additional topology nodes. For example, a wave device, which is represented as a wave filter, might contain DAC ([**KSNODETYPE\_DAC**](https://msdn.microsoft.com/library/windows/hardware/ff537158)) and ADC ([**KSNODETYPE\_ADC**](https://msdn.microsoft.com/library/windows/hardware/ff537153)) nodes.

The querying and setting of control parameters on topology nodes is accomplished through property requests. Each node type is associated with a specific property or set of properties. A node might support only one control value. For example, a volume node ([**KSNODETYPE\_VOLUME**](https://msdn.microsoft.com/library/windows/hardware/ff537208)) has a value indicating its current volume setting. Other nodes might support multiple control values. For example, a 3D node ([**KSNODETYPE\_3D\_EFFECTS**](https://msdn.microsoft.com/library/windows/hardware/ff537148)) supports a number of 3D buffer and 3D listener properties. A sum node ([**KSNODETYPE\_SUM**](https://msdn.microsoft.com/library/windows/hardware/ff537196)), on the other hand, has no control values.

A Topology miniport driver uses a *connection descriptor* ([**PCCONNECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537688)) to describe a connection between two topology nodes. Each connection is directed and specifies both a from-node and a to-node. A node might have several pins, and the function performed by one pin might differ from that of the other pins. To distinguish one pin from another, the miniport driver numbers the pins on a node. These pin numbers appear in the connection descriptors. For example, a state-variable filter might have three output pins - one each for the high, middle, and low frequencies - numbered 1, 2, and 3. Pin numbering allows clients of the miniport driver to determine which connections are associated with which pins.

A connection descriptor uses a *distinguished node identifier*, [**PCFILTER\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff537695), to distinguish a pin on the filter from a pin on a node within the filter. Each of the mixer circuitry's hardwired connections to the audio rendering and capture devices in the audio adapter is represented as a pin on the topology filter. Other topology filter pins represent external physical connections, such as a lineout jack on the adapter card. The pins on a topology filter represent physical, hardwired connections of the adapter hardware. Thus, the pins cannot provide explicit control over whether a connection is made, and they cannot be used to manage the flow of data over that connection.

A single connection descriptor can describe a connection between any two pin types in a topology. The pins on the two sides of a connection can both be pins on the filter or pins on nodes within the filter, or the connection can have a filter pin on one side and a node pin on the other. A miniport driver specifies its topology as an array of connection descriptors. A single pin can have more than one connection, which means that the same pin can appear in more than one connection descriptor in the array.

The topology description that a client obtains from a miniport driver is not designed to support open-ended discovery of how to interpret node types that are unknown to the client. Node pin numbering alone does not provide the client with the information needed to discover the functions of the pins. Although the miniport driver identifies the type of a node (by means of a GUID), it does not provide any standardized list of parameters for describing either the node type or the pins supported by the node type.

For example, if a client enumerates a node that uses the node-type GUID [**KSNODETYPE\_VOLUME**](https://msdn.microsoft.com/library/windows/hardware/ff537208) to identify itself, the client can make use of the node only if it knows the conventions for dealing with volume nodes. By convention, a volume node, for example, supports the [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff537309) property and assigns node pin numbers 0 and 1 to the output (source) pin and input (sink) pin, respectively. In addition, a client that is able to control a volume node usually performs a directed search that limits its exploration to a relatively small number of node types (volume and mute nodes, for example). The client typically explores only portions of a filter graph that are likely to contain volume nodes (for example, mixer lines).

The miniport interface supports the delivery of unsolicited control value changes from the miniport driver to the port driver. This feature accommodates devices with control knobs, sliders, or switches that can be physically manipulated by the user. Each time the user changes a node's control value, a hardware interrupt notifies the port driver that a [hardware event](hardware-events.md) has occurred.

 

 




