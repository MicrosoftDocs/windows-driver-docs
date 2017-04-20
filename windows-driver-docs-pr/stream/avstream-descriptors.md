---
title: AVStream Descriptors
author: windows-driver-content
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AVStream Descriptors


## <a href="" id="ddk-avstream-descriptors-ksg"></a>


An AVStream minidriver describes itself and the filter types it supports by providing nested descriptor structures in the call to [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683). Each key component -- the device, the [filter factory](https://msdn.microsoft.com/library/windows/hardware/ff536385), and the [pin factory](https://msdn.microsoft.com/library/windows/hardware/ff537747) -- has an associated descriptor.

As shown in [AVStream Object Hierarchy](avstream-object-hierarchy.md), the highest level descriptor for an AVStream minidriver is the device descriptor, [**KSDEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff561691).

In the device descriptor, the **FilterDescriptors** member points to an array of KSFILTER\_DESCRIPTOR structures that describe the types of filters this device can create. AVStream clients can call [**KsCreateFilterFactory**](https://msdn.microsoft.com/library/windows/hardware/ff561650) to dynamically add filter factories.

A KSFILTER\_DESCRIPTOR indicates how many pin types the filter supports, the KS categories under which the filter is to be registered, and the topology of the filter. Inside each filter descriptor, the minidriver provides a pointer to an array of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structures. Each of these pin descriptors describes a pin type that this filter can instantiate. You can create additional pin factories by calling [**KsFilterCreatePinFactory**](https://msdn.microsoft.com/library/windows/hardware/ff562529).

Typically, AVStream minidrivers lay out static descriptor tables in their source and call [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683) to perform the setup work. For more information about initializing your driver, see [Initializing an AVStream Minidriver](initializing-an-avstream-minidriver.md).

There are other types of descriptors as well, such as the node descriptor [**KSNODE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563473), which describes a given topology node.

The dispatch table is common to each of the three main descriptor types. See [AVStream Dispatch Tables](avstream-dispatch-tables.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVStream%20Descriptors%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


