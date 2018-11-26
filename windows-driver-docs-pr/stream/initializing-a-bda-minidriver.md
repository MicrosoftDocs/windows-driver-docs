---
title: Initializing a BDA Minidriver
description: Initializing a BDA Minidriver
ms.assetid: 4df2efc6-e666-48d5-9a7b-cbf724c027f0
keywords:
- BDA minidrivers WDK AVStream , initializing
- initializing BDA minidrivers WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a BDA Minidriver





A BDA minidriver is initialized similarly to other AVStream minidrivers. The BDA minidriver's DriverEntry function calls the AVStream [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683) function to initialize the BDA minidriver's driver object. In this call, the BDA minidriver passes a pointer to a [**KSDEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff561691) structure that specifies characteristics of the device, which can include:

-   A pointer to a [**KSDEVICE\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff561693) structure that contains the dispatch table for the BDA device. At a minimum, the BDA minidriver should supply routines that create and start the device and specify these routines in the **Add** and **Start** members respectively of the KSDEVICE\_DISPATCH structure. The BDA minidriver's create routine should allocate memory for the device class and reference the pointer to the [**KSDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff561681) structure for the BDA device to this device class. The BDA minidriver's start routine should get information about the device from the registry, set information about the device, and then register a group of static template structures with the BDA support library. See [Starting a BDA Minidriver](starting-a-bda-minidriver.md) for more information.

-   An array of [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structures for the individual filter types supported by this device. This structure type describes the characteristics of a filter created by a given filter factory. You should specify members of structures of this type in this array if you create your BDA minidriver so that it does not use the BDA support library (*Bdasup.lib*) to handle your BDA minidriver's property and method sets. If you create your BDA minidriver so that it uses the BDA support library, then your BDA minidriver should instead call the [**BdaCreateFilterFactory**](https://msdn.microsoft.com/library/windows/hardware/ff556438) support function to add filter factory descriptors (KSFILTER\_DESCRIPTOR structures) for your device. See [Starting a BDA Minidriver](starting-a-bda-minidriver.md) for more information.

The following code snippet shows examples of an array of filter descriptors, a dispatch table for the BDA device, and the descriptor for the BDA device:

```cpp
//
//  Array containing descriptors for all filter factories
//  available on the device.
//
//  Note!  Only used when dynamic topology is not used (that is, 
//         only when filters and pins are fixed). Typically, this 
//         is when the network provider is not present.
//
DEFINE_KSFILTER_DESCRIPTOR_TABLE(FilterDescriptors)
{
    &TemplateTunerFilterDescriptor
};
//
//  Device Dispatch Table
//
//  Lists the dispatch routines for the major events related to 
//  the underlying device.
//
extern
const
KSDEVICE_DISPATCH
DeviceDispatch =
{
    CDevice::Create,    // Add
    CDevice::Start,     // Start
    NULL,               // PostStart
    NULL,               // QueryStop
    NULL,               // CancelStop
    NULL,               // Stop
    NULL,               // QueryRemove
    NULL,               // CancelRemove
    NULL,               // Remove
    NULL,               // QueryCapabilities
    NULL,               // SurpriseRemoval
    NULL,               // QueryPower
    NULL                // SetPower
};
//
//  Device Descriptor
//
//  Brings together the data structures that define the device and
//  the initial filter factories that can be created on it.
//  Note that because template topology structures are specific 
//  to BDA, the device descriptor does not include them.
//  Note also that if BDA dynamic topology is used, the device 
//  descriptor does not specify a list of filter factory descriptors.
//  If BDA dynamic topology is used, the BDA minidriver calls 
//  BdaCreateFilterFactory to add filter factory descriptors. 
extern
const
KSDEVICE_DESCRIPTOR
DeviceDescriptor =
{
    &DeviceDispatch,    // Dispatch
#ifdef DYNAMIC_TOPOLOGY // network provider is present
    0,    // FilterDescriptorsCount
    NULL, // FilterDescriptors
#else     // network provider is not present
    SIZEOF_ARRAY( FilterDescriptors), // FilterDescriptorsCount
    FilterDescriptors                 // FilterDescriptors
#endif // DYNAMIC_TOPOLOGY
```

 

 




