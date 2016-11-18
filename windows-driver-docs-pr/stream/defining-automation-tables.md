---
title: Defining Automation Tables
author: windows-driver-content
description: Defining Automation Tables
MS-HAID:
- 'bdadg\_3433fda8-0ba7-412f-b8cf-4d12ac590386.xml'
- 'stream.defining\_automation\_tables'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1c0dace6-b618-4705-bf5d-65457d14c072
keywords: ["BDA minidrivers WDK AVStream , automation tables", "automation tables WDK AVStream"]
---

# Defining Automation Tables


## <a href="" id="ddk-defining-automation-tables-ksg"></a>


An automation table for a filter, pin, or node is what describes the properties and methods supported by the filter, pin, or node. If a BDA minidriver supplies a property or method handler that is already implemented by AVStream, the BDA minidriver's implementation supersedes AVStream's.

A BDA minidriver should define arrays of property and method sets and then define automation tables for those set arrays so that the minidriver can automatically process requests. See the [Determining BDA Device Topology](determining-bda-device-topology.md) section for an example of how the minidriver also defines a property set to which this section refers.

The following code snippet shows examples of filter automation tables and arrays of property and method sets:

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Defining%20Automation%20Tables%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


