---
title: KSPROPSETID\_TopologyNode
description: KSPROPSETID\_TopologyNode
keywords: ["KSPROPSETID_TopologyNode"]
ms.date: 03/06/2023
ms.topic: reference
---


# KSPROPSETID\_TopologyNode


## <span id="ddk_kspropsetid_topologynode_ks"></span><span id="DDK_KSPROPSETID_TOPOLOGYNODE_KS"></span>


The `KSPROPSETID_TopologyNode` property set provides generic control over the various topology nodes. For a list of topology node types, see [Audio Topology Nodes](audio-topology-nodes.md). The properties in this set can be used to enable, disable, and reset topology nodes.

To expose AEC (acoustic echo cancellation) hardware acceleration to the system, an audio driver must implement AEC and noise-suppression nodes ([**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md) and [**KSNODETYPE\_NOISE\_SUPPRESS**](ksnodetype-noise-suppress.md)), and must support enabling and disabling of these nodes through the `KSPROPSETID_TopologyNode` properties. For more information, see [Exposing Hardware-Accelerated Capture Effects](./exposing-hardware-accelerated-capture-effects.md).

A [**KSNODETYPE\_PROLOGIC\_ENCODER**](ksnodetype-prologic-encoder.md) node must also support the `KSPROPSETID_TopologyNode` properties.

The `KSPROPSETID_TopologyNode` property set contains the following properties:

[**KSPROPERTY\_TOPOLOGYNODE\_ENABLE**](ksproperty-topologynode-enable.md)

[**KSPROPERTY\_TOPOLOGYNODE\_RESET**](ksproperty-topologynode-reset.md)

 

