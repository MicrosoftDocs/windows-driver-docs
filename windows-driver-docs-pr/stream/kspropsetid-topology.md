---
title: KSPROPSETID\_Topology
description: KSPROPSETID\_Topology
ms.assetid: d0c51bcf-ced3-4863-9359-9fa326122262
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_Topology


## <span id="ddk_kspropsetid_topology_ks"></span><span id="DDK_KSPROPSETID_TOPOLOGY_KS"></span>


Clients use requests in the KSPROPSETID\_Topology property set to examine a KS filter's internal topology.

Each node in the topology has a zero-based node ID: KS filters with *n* nodes number them from 0 to *n-1*. The whole KS filter itself may be treated as a node and has the special node ID number KSFILTER\_NODE.

Stream minidrivers do not need to handle the properties in this property set. The stream class driver handles them on behalf of the minidriver.

Microsoft defines a standard set of node types of the form KSNODETYPE\_XXX in the *ksmedia.h* header file. When using the properties in this set, clients refer to a node by its zero-based index in this sequence.

The KSPROPSETID\_Topology property set includes:

[**KSPROPERTY\_TOPOLOGY\_CATEGORIES**](ksproperty-topology-categories.md)

[**KSPROPERTY\_TOPOLOGY\_CONNECTIONS**](ksproperty-topology-connections.md)

[**KSPROPERTY\_TOPOLOGY\_NAME**](ksproperty-topology-name.md)

[**KSPROPERTY\_TOPOLOGY\_NODES**](ksproperty-topology-nodes.md)

 

 





