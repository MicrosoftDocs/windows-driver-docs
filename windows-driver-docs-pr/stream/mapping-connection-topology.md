---
title: Mapping Connection Topology
description: Mapping Connection Topology
ms.assetid: f11ffc48-a117-4b75-bc19-7a3762e6ba19
keywords:
- method sets WDK BDA , mapping connection topology
- property sets WDK BDA , mapping connection topology
- topology WDK BDA
- mapping connection topology
- connection topology mapping WDK BDA
- BDA_TEMPLATE_CONNECTION
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping Connection Topology





In order for the BDA support library to provide properties and methods to applications in Ring 3 on behalf of a BDA minidriver, the BDA minidriver must provide a mapping of its connection topology to the BDA support library. The BDA minidriver provides this mapping in an array of [**BDA\_TEMPLATE\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/ff556558) structures. The BDA minidriver passes this BDA\_TEMPLATE\_CONNECTION array in an array of [**KSTOPOLOGY\_CONNECTION**](https://msdn.microsoft.com/library/windows/hardware/ff567148) structures when it calls the [**BdaCreateFilterFactory**](https://msdn.microsoft.com/library/windows/hardware/ff556438) support function. See [Starting a BDA Minidriver](starting-a-bda-minidriver.md) for more information. This array provides a representation of all the possible connections between node and pin types that can be made within a filter or between a filter and adjoining filters.

The network provider filter can subsequently make a KSPROPERTY\_BDA\_TEMPLATE\_CONNECTIONS property request of the [KSPROPSETID\_BdaTopology](https://msdn.microsoft.com/library/windows/hardware/ff566561) property set on a filter instance of the BDA minidriver to retrieve the minidriver's connection topology. The BDA minidriver in turn calls the [**BdaPropertyTemplateConnections**](https://msdn.microsoft.com/library/windows/hardware/ff556501) support function, which returns the list of the filter's template connections (BDA\_TEMPLATE\_CONNECTION structures) in an array of KSTOPOLOGY\_CONNECTION structures. The members of a BDA\_TEMPLATE\_CONNECTION structure identify the following pairs of node and pin types of a connection:

-   node and pin types where the connection begins

-   node and pin types where the connection ends

Setting the node type to a value of −1 indicates that the connection begins or ends at a pin of either an upstream or downstream filter respectively. Otherwise, the value of the node type corresponds to the index of the element in the zero-based array of internal node types. This array is an array of [**KSNODE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563473) structures. The value of the pin type corresponds to the index of the element in the zero-based array of pin types that are available in the template filter descriptor for the BDA minidriver. This array is an array of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structures.

The following code snippet shows example arrays of node types and pin types that are available in the template filter descriptor for the BDA minidriver:

```cpp
//
//  Template Node Descriptors
//
//  This array describes all Node Types available in the template
//  topology of the filter.
//
const
KSNODE_DESCRIPTOR
NodeDescriptors[] =
{
    {   // 0 node type
        &RFTunerNodeAutomation,// PKSAUTOMATION_TABLE AutomationTable;
        &KSNODE_BDA_RF_TUNER,  // Type
        NULL                   // Name
    },
    {   // 1 node type
        &VSB8DemodulatorNodeAutomation, // PKSAUTOMATION_TABLE 
                                        // AutomationTable;
        &KSNODE_BDA_8VSB_DEMODULATOR,   // Type
        NULL                            // Name
    }
};
//
//  Template Pin Descriptors
//
//  This data structure defines the pin types available in the filters
//  template topology. These structures will be used to create a
//  pin factory ID for a pin type when BdaMethodCreatePin is called.
//
const
KSPIN_DESCRIPTOR_EX
TemplatePinDescriptors[] =
{
    //  Antenna Pin
    //  0 pin type
    {
        &AntennaPinDispatch,
        &AntennaAutomation,   // AntennaPinAutomation
        {
            0,  // Interfaces
            NULL,
            0,  // Mediums
            NULL,
            SIZEOF_ARRAY(AntennaPinRanges),
            AntennaPinRanges,
            KSPIN_DATAFLOW_IN,
            KSPIN_COMMUNICATION_BOTH,
            NULL,   // Name
            NULL,   // Category
            0
        },
        KSPIN_FLAG_DO_NOT_USE_STANDARD_TRANSPORT | 
        KSPIN_FLAG_FRAMES_NOT_REQUIRED_FOR_PROCESSING | 
        KSPIN_FLAG_FIXED_FORMAT,
        1,      // InstancesPossible
        0,      // InstancesNecessary
        NULL,   // Allocator Framing
        NULL    // PinIntersectHandler
    },

    //  Transport Pin
    //  1 pin type
    {
        &TransportPinDispatch,
        &TransportAutomation,   // TransportPinAutomation
        {
            0,  // Interfaces
            NULL,
            1,  // Mediums
            &TransportPinMedium,
            SIZEOF_ARRAY(TransportPinRanges),
            TransportPinRanges,
            KSPIN_DATAFLOW_OUT,
            KSPIN_COMMUNICATION_BOTH,
            (GUID *) &PINNAME_BDA_TRANSPORT,   // Name
            (GUID *) &PINNAME_BDA_TRANSPORT,   // Category
            0
        },
        KSPIN_FLAG_DO_NOT_USE_STANDARD_TRANSPORT | 
        KSPIN_FLAG_FRAMES_NOT_REQUIRED_FOR_PROCESSING | 
        KSPIN_FLAG_FIXED_FORMAT,
        1,
        1,      // InstancesNecessary
        NULL,   // Allocator Framing
        NULL    // PinIntersectHandler
    }
};
```

The following code snippet shows examples of arrays of template connections and joints:

```cpp
//
//  BDA Template Topology Connections
//
//  Lists the possible connections between pin types and
//  node types. This structure along with the BDA_FILTER_TEMPLATE, 
//  KSFILTER_DESCRIPTOR, and BDA_PIN_PAIRING structures 
//  describe how topologies are created in the filter.
//
const
KSTOPOLOGY_CONNECTION TemplateTunerConnections[] =
{
    { -1,  0,  0,  0}, // from upstream filter to 0 pin of 0 node 
    {  0,  1,  1,  0}, // from 1 pin of 0 node to 0 pin of 1 node 
    {  1,  1,  -1, 1}, // from 1 pin of 1 node to downstream filter 
};
//
//  Lists the template joints between antenna (input) and transport 
//  (output) pin types. Values given to joints correspond to indexes 
//  of elements in the preceding KSTOPOLOGY_CONNECTION array.
// 
//  For this template topology, the RF node (0) belongs to the antenna 
//  pin and the 8VSB demodulator node (1) belongs to the transport pin
//
const
ULONG   AntennaTransportJoints[] =
{
    1  // Second element in the preceding KSTOPOLOGY_CONNECTION array.
};
```

 

 




