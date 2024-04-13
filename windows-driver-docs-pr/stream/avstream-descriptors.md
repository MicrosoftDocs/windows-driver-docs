---
title: AVStream Descriptors
description: AVStream Descriptors
keywords:
- AVStream descriptors WDK
- descriptors WDK AVStream
- nested descriptor structures WDK AVStream
- AVStream object hierarchy WDK
- objects WDK AVStream
- hierarchy WDK AVStream
- static descriptor tables WDK AVStream
- KSFILTER_DESCRIPTOR
- device descriptors WDK AVStream
- filter factories WDK AVStream
- filter types WDK AVStream
- pin types WDK AVStream
ms.date: 04/20/2017
---

# AVStream Descriptors





An AVStream minidriver describes itself and the filter types it supports by providing nested descriptor structures in the call to [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver). Each key component -- the device, the [filter factory](../audio/filter-factories.md), and the [pin factory](../audio/pin-factories.md) -- has an associated descriptor.

As shown in [AVStream Object Hierarchy](avstream-object-hierarchy.md), the highest level descriptor for an AVStream minidriver is the device descriptor, [**KSDEVICE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice_descriptor).

In the device descriptor, the **FilterDescriptors** member points to an array of KSFILTER\_DESCRIPTOR structures that describe the types of filters this device can create. AVStream clients can call [**KsCreateFilterFactory**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatefilterfactory) to dynamically add filter factories.

A KSFILTER\_DESCRIPTOR indicates how many pin types the filter supports, the KS categories under which the filter is to be registered, and the topology of the filter. Inside each filter descriptor, the minidriver provides a pointer to an array of [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structures. Each of these pin descriptors describes a pin type that this filter can instantiate. You can create additional pin factories by calling [**KsFilterCreatePinFactory**](/windows-hardware/drivers/ddi/ks/nf-ks-ksfiltercreatepinfactory).

Typically, AVStream minidrivers lay out static descriptor tables in their source and call [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver) to perform the setup work. For more information about initializing your driver, see [Initializing an AVStream Minidriver](initializing-an-avstream-minidriver.md).

There are other types of descriptors as well, such as the node descriptor [**KSNODE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksnode_descriptor), which describes a given topology node.

The dispatch table is common to each of the three main descriptor types. See [AVStream Dispatch Tables](avstream-dispatch-tables.md).

 

