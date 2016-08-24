---
title: Determining the Controlling Pin of a Node
author: windows-driver-content
description: Determining the Controlling Pin of a Node
MS-HAID:
- 'bdadg\_7b99ef43-2b33-43f5-8ea6-006029145c23.xml'
- 'stream.determining\_the\_controlling\_pin\_of\_a\_node'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: be1236e2-c710-4833-863e-54e826e53f92
keywords: ["method sets WDK BDA , node controlling pin", "property sets WDK BDA , node controlling pin", "controlling pin WDK BDA", "node controlling pin WDK BDA", "arrays WDK BDA", "pin controller WDK BDA"]
---

# Determining the Controlling Pin of a Node


## <a href="" id="ddk-determining-the-controlling-pin-of-a-node-ksg"></a>


Unlike filters and pins, nodes do not have an associated file handle by which applications in Ring 3 can access them. Because nodes are internal components within a filter, they exist somewhere between the filter's input and output pins. The network provider must determine which filter pin to use, then use the pin to access a node. This filter pin is called the controlling pin for that node. To determine the controlling pin for each node in the BDA template connection list of a filter, the network provider queries the KSPROPERTY\_BDA\_CONTROLLING\_PIN\_ID property of the [KSPROPSETID\_BdaTopology](https://msdn.microsoft.com/library/windows/hardware/ff566561) property set. The BDA minidriver in turn calls the [**BdaPropertyGetControllingPinId**](https://msdn.microsoft.com/library/windows/hardware/ff556480) support function for each node. In this call, the minidriver passes a pointer to a [**KSP\_BDA\_NODE\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566716) structure. This structure identifies the property request to retrieve the controlling pin for a specific node type and a pair of the filter's input and output pins. The BDA support library returns the identifier of the controlling pin for the node type.

A BDA minidriver does not typically intercept the KSPROPERTY\_BDA\_CONTROLLING\_PIN\_ID property. The minidriver automatically dispatches the **BdaPropertyGetControllingPinId** support function from the KSPROPSETID\_BdaTopology property set. See [Determining BDA Device Topology](determining-bda-device-topology.md) for more information.

The support library is able to do all the work of determining the identifier of the controlling pin because the BDA minidriver provided the support library with a pointer to the [**BDA\_FILTER\_TEMPLATE**](https://msdn.microsoft.com/library/windows/hardware/ff556523) structure when the BDA minidriver started operating. See [Starting a BDA Minidriver](starting-a-bda-minidriver.md) for more information. A BDA minidriver informs the BDA support library how to determine controlling pins through information contained in BDA\_FILTER\_TEMPLATE. This information includes:

-   An array of connections. This array is a [**KSTOPOLOGY\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/ff567148) array that provides a representation of all the possible connections between node and pin types that can be made within a filter or between a filter and adjoining filters. See [Mapping Connection Topology](mapping-connection-topology.md) For more information about the KSTOPOLOGY\_CONNECTION array.

-   An array of joint values. A joint is a point in the topology where one input splits into one or more paths to different outputs, or one or more inputs join into a single output path. The value given to a joint corresponds to the index of an element in the KSTOPOLOGY\_CONNECTION array. Most topologies will have only one joint.

-   An array of [**BDA\_PIN\_PAIRING**](https://msdn.microsoft.com/library/windows/hardware/ff556544) structures. These structures identify input and output pin types, the maximum number of input-type instances that can be created on the filter, and the maximum number of output-type instances that can be created on the filter. These structures also contain a pointer to the array of joint values between the input and output pins. See [Starting a BDA Minidriver](starting-a-bda-minidriver.md) For more information about the BDA\_PIN\_PAIRING array.

The following figure shows how the support library determines the filter pin that controls a specific node:

![diagram illustrating how the support library determines the filter pin that controls a specific node](images/bdajoint.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Determining%20the%20Controlling%20Pin%20of%20a%20Node%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


