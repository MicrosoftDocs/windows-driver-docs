---
title: AVStream Descriptors
description: AVStream Descriptors
ms.assetid: fd436406-311b-4537-994d-fbd8d92d4673
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
ms.localizationpriority: medium
---

# AVStream Descriptors





An AVStream minidriver describes itself and the filter types it supports by providing nested descriptor structures in the call to [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683). Each key component -- the device, the [filter factory](https://msdn.microsoft.com/library/windows/hardware/ff536385), and the [pin factory](https://msdn.microsoft.com/library/windows/hardware/ff537747) -- has an associated descriptor.

As shown in [AVStream Object Hierarchy](avstream-object-hierarchy.md), the highest level descriptor for an AVStream minidriver is the device descriptor, [**KSDEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff561691).

In the device descriptor, the **FilterDescriptors** member points to an array of KSFILTER\_DESCRIPTOR structures that describe the types of filters this device can create. AVStream clients can call [**KsCreateFilterFactory**](https://msdn.microsoft.com/library/windows/hardware/ff561650) to dynamically add filter factories.

A KSFILTER\_DESCRIPTOR indicates how many pin types the filter supports, the KS categories under which the filter is to be registered, and the topology of the filter. Inside each filter descriptor, the minidriver provides a pointer to an array of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structures. Each of these pin descriptors describes a pin type that this filter can instantiate. You can create additional pin factories by calling [**KsFilterCreatePinFactory**](https://msdn.microsoft.com/library/windows/hardware/ff562529).

Typically, AVStream minidrivers lay out static descriptor tables in their source and call [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683) to perform the setup work. For more information about initializing your driver, see [Initializing an AVStream Minidriver](initializing-an-avstream-minidriver.md).

There are other types of descriptors as well, such as the node descriptor [**KSNODE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563473), which describes a given topology node.

The dispatch table is common to each of the three main descriptor types. See [AVStream Dispatch Tables](avstream-dispatch-tables.md).

 

 




