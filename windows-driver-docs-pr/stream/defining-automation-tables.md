---
title: Defining Automation Tables
description: Defining Automation Tables
ms.assetid: 1c0dace6-b618-4705-bf5d-65457d14c072
keywords:
- BDA minidrivers WDK AVStream , automation tables
- automation tables WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining Automation Tables





An automation table for a filter, pin, or node is what describes the properties and methods supported by the filter, pin, or node. If a BDA minidriver supplies a property or method handler that is already implemented by AVStream, the BDA minidriver's implementation supersedes AVStream's.

A BDA minidriver should define arrays of property and method sets and then define automation tables for those set arrays so that the minidriver can automatically process requests. See the [Determining BDA Device Topology](determining-bda-device-topology.md) section for an example of how the minidriver also defines a property set to which this section refers.

The following code snippet shows examples of filter automation tables and arrays of property and method sets:

```cpp
//
//  Filter Level Property Set supported
//
//  This array defines a property set supported by the
//  filter that is exposed by the minidriver.
//
DEFINE_KSPROPERTY_SET_TABLE(FilterPropertySets)
{
    DEFINE_KSPROPERTY_SET
    (
        &KSPROPSETID_BdaTopology,                   // Set
        SIZEOF_ARRAY(FilterTopologyProperties),     // PropertiesCount
        FilterTopologyProperties,                   // PropertyItems
        0,                                          // FastIoCount
        NULL                                        // FastIoTable
    )
};
//
//  Filter Level Method Sets supported
//
//  This array defines method sets supported by the
//  filter that is exposed by the minidriver.
//
DEFINE_KSMETHOD_SET_TABLE(FilterMethodSets)
{
    DEFINE_KSMETHOD_SET
    (
        &KSMETHODSETID_BdaChangeSync,               // Set
        SIZEOF_ARRAY(BdaChangeSyncMethods),         // MethodsCount
        BdaChangeSyncMethods,                       // MethodItems
        0,                                          // FastIoCount
        NULL                                        // FastIoTable
    ),
    DEFINE_KSMETHOD_SET
    (
        &KSMETHODSETID_BdaDeviceConfiguration,      // Set
        SIZEOF_ARRAY(BdaDeviceConfigurationMethods),// MethodsCount
        BdaDeviceConfigurationMethods,              // MethodItems
        0,                                          // FastIoCount
        NULL                                        // FastIoTable
    )
};
//
//  Filter Automation Table
//
//  Lists all arrays of property and method sets for the filter that 
//  is exposed by the minidriver.
//
DEFINE_KSAUTOMATION_TABLE(FilterAutomation) {
    DEFINE_KSAUTOMATION_PROPERTIES(FilterPropertySets),
    DEFINE_KSAUTOMATION_METHODS(FilterMethodSets),
    DEFINE_KSAUTOMATION_EVENTS_NULL
};
```

The following code snippet shows an example of a node automation table and an array of property sets:

```cpp
//
//  RF tuner node property set supported
//
//  This array defines a property set supported by the
//  RF Tuner Node associated with the antenna input pin.
//
DEFINE_KSPROPERTY_SET_TABLE(RFNodePropertySets)
{
    DEFINE_KSPROPERTY_SET
    (
        &KSPROPSETID_BdaFrequencyFilter,            // Set
        SIZEOF_ARRAY(RFNodeFrequencyProperties),    // PropertiesCount
        RFNodeFrequencyProperties,                  // PropertyItems
        0,                                          // FastIoCount
        NULL                                        // FastIoTable
    )
};
//
//  Radio frequency tuner node automation table
//
//
DEFINE_KSAUTOMATION_TABLE(RFTunerNodeAutomation) {
    DEFINE_KSAUTOMATION_PROPERTIES( RFNodePropertySets),
    DEFINE_KSAUTOMATION_METHODS_NULL,
    DEFINE_KSAUTOMATION_EVENTS_NULL
};
```

 

 




