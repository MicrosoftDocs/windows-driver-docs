---
title: KSPROPSETID\_BdaTopology
description: KSPROPSETID\_BdaTopology
ms.assetid: 26d67e68-56a9-4d36-9e33-6fb4486d7cd9
ms.date: 11/28/2017
ms.localizationpriority: medium
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

### Comments

The BDA support library provides default methods to handle this property set. The network provider filter uses this property set to determine the template topology of the filter, and the methods, properties and events supported on each node and pin. The network provider filter uses this node and pin information to determine what kinds of operations the filter can perform on the signal and whether to add the filter to the graph. The actual topology of a filter refers to the pin and node connections that are actually made on the filter by the network provider.

The properties in this property set define what the filter can do. Typically, filters are not required to intercept any of these properties. For more information, see [Broadcast Driver Architecture Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff556588) on how the BDA minidriver for a filter can use the BDA support library of functions to provide default handling of these properties. A driver writer should create static structures that enable handling of this property set. Once these structures are created and registered with the BDA support library, the driver writer is not required to do anything further to support this property set.

 

 





