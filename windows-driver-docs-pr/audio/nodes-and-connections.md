---
title: Nodes and Connections
description: Nodes and Connections
ms.assetid: 829b1067-8246-49fc-94f1-4988e61defac
keywords: ["audio filters WDK audio , nodes", "audio filters WDK audio , connections", "audio topology nodes WDK", "topology nodes WDK audio", "connections WDK audio"]
---

# Nodes and Connections


## <span id="nodes_and_connections"></span><span id="NODES_AND_CONNECTIONS"></span>


The filter provides a description of its topology nodes in the form of an array of node descriptors ([**PCNODE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537720) structures). Each descriptor in the array describes a single node and contains a GUID that specifies the node type (for example, [**KSNODETYPE\_REVERB**](https://msdn.microsoft.com/library/windows/hardware/ff537189)). For a list of the standard node types that are defined for audio devices, see [Audio Topology Nodes](https://msdn.microsoft.com/library/windows/hardware/ff536219).

The filter identifies each of its nodes by the node's index in the descriptor array. For example, when sending a node-specific property request to a filter or to a particular pin on a filter, a client includes the node ID (the array index) in the request in order to identify the target node.

The filter provides a description of its internal connections in the form of an array of connection descriptors ([**PCCONNECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537688) structures). Each descriptor describes one of the filter's internal connections. A descriptor can either describe a connection between a pin and a node or a connection between two nodes.

The nodes and connections that the filter exposes together define the filter's internal topology. The topology is a map of the audio device's internal layout and should accurately reflect the organization of the hardware that it represents. The Microsoft Windows Multimedia mixer API, for example, translates the filter's internal connections into mixer lines and its nodes into controls on the mixer lines (see [Kernel Streaming Topology to Audio Mixer API Translation](kernel-streaming-topology-to-audio-mixer-api-translation.md)). Any inaccuracies in the filter's internal topology are reflected in the mixer-line representation and may cause errors or unexpected behavior in an application that uses the mixer API.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Nodes%20and%20Connections%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


