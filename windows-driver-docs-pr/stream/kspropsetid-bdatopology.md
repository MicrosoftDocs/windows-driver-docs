---
title: KSPROPSETID\_BdaTopology
description: KSPROPSETID\_BdaTopology
ms.assetid: 26d67e68-56a9-4d36-9e33-6fb4486d7cd9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_BdaTopology


## <span id="ddk_kspropsetid_bdatopology_ks"></span><span id="DDK_KSPROPSETID_BDATOPOLOGY_KS"></span>


KSPROPSETID\_BdaTopology is the BDA topology property set. It is used for querying filters about their capabilities.

The following properties are available:

<span id="KSPROPERTY_BDA_NODE_TYPES"></span><span id="ksproperty_bda_node_types"></span>[**KSPROPERTY\_BDA\_NODE\_TYPES**](ksproperty-bda-node-types.md)  
Returns a list of the node types.

<span id="KSPROPERTY_BDA_PIN_TYPES"></span><span id="ksproperty_bda_pin_types"></span>[**KSPROPERTY\_BDA\_PIN\_TYPES**](ksproperty-bda-pin-types.md)  
Returns a list of the pin types.

<span id="KSPROPERTY_BDA_TEMPLATE_CONNECTIONS"></span><span id="ksproperty_bda_template_connections"></span>[**KSPROPERTY\_BDA\_TEMPLATE\_CONNECTIONS**](ksproperty-bda-template-connections.md)  
Returns a list of connections between pins and nodes in a template topology.

<span id="KSPROPERTY_BDA_NODE_METHODS"></span><span id="ksproperty_bda_node_methods"></span>[**KSPROPERTY\_BDA\_NODE\_METHODS**](ksproperty-bda-node-methods.md)  
Returns a list of methods supported on a node.

<span id="KSPROPERTY_BDA_NODE_PROPERTIES"></span><span id="ksproperty_bda_node_properties"></span>[**KSPROPERTY\_BDA\_NODE\_PROPERTIES**](ksproperty-bda-node-properties.md)  
Returns a list of properties supported on a node.

<span id="KSPROPERTY_BDA_NODE_EVENTS"></span><span id="ksproperty_bda_node_events"></span>[**KSPROPERTY\_BDA\_NODE\_EVENTS**](ksproperty-bda-node-events.md)  
Returns a list of events supported on a node.

<span id="KSPROPERTY_BDA_CONTROLLING_PIN_ID"></span><span id="ksproperty_bda_controlling_pin_id"></span>[**KSPROPERTY\_BDA\_CONTROLLING\_PIN\_ID**](ksproperty-bda-controlling-pin-id.md)  
Returns the controlling pin for a node in the BDA template connection list.

<span id="KSPROPERTY_BDA_NODE_DESCRIPTORS"></span><span id="ksproperty_bda_node_descriptors"></span>[**KSPROPERTY\_BDA\_NODE\_DESCRIPTORS**](ksproperty-bda-node-descriptors.md)  
Returns a list of nodes.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The BDA support library provides default methods to handle this property set. The network provider filter uses this property set to determine the template topology of the filter, and the methods, properties and events supported on each node and pin. The network provider filter uses this node and pin information to determine what kinds of operations the filter can perform on the signal and whether to add the filter to the graph. The actual topology of a filter refers to the pin and node connections that are actually made on the filter by the network provider.

The properties in this property set define what the filter can do. Typically, filters are not required to intercept any of these properties. For more information, see [Broadcast Driver Architecture Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff556588) on how the BDA minidriver for a filter can use the BDA support library of functions to provide default handling of these properties. A driver writer should create static structures that enable handling of this property set. Once these structures are created and registered with the BDA support library, the driver writer is not required to do anything further to support this property set.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaTopology%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




