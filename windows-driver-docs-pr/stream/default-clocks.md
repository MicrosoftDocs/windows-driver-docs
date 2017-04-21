---
title: Default Clocks
author: windows-driver-content
description: Default Clocks
ms.assetid: 8c1a51e5-238b-446a-8f20-3fe1b82020b5
keywords:
- default clocks WDK kernel streaming
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Default Clocks


## <a href="" id="ddk-default-clocks-ksg"></a>


Kernel streaming minidrivers can call [**KsAllocateDefaultClockEx**](https://msdn.microsoft.com/library/windows/hardware/ff560955) to allocate and initialize a default clock structure. Alternatively, they can call [**KsAllocateDefaultClock**](https://msdn.microsoft.com/library/windows/hardware/ff560952), which is a wrapper for **KsAllocateDefaultClockEx** with default parameters for the nonclock members. Call [**KsCreateDefaultClock**](https://msdn.microsoft.com/library/windows/hardware/ff561644) after using **KsAllocateDefaultClockEx** to initialize the default clock.

The default clock supports [KSPROPSETID\_Clock](https://msdn.microsoft.com/library/windows/hardware/ff566564), and may be accessed just as any other clock presented by a filter pin. The underlying data structure, however, is created by the filter pin, and shared by that pin and any instances of the clock that are created. The clock relies on the pin to update the current state and other elements in the shared structure. The default clock handles notification requests and clock queries.

When a pin on the filter that provides this clock is assigned a master clock, the pin owns this clock. The pin should reference the clock file object, just as if it was assigned some other clock implementation. The default clock does not reference the pin's file object when an instance is created. Instead, it keeps an internal reference count based on the initial allocation of the common clock structure, and on each file object opened on the clock. Even if the clock's owner frees the clock structure, it remains in place until all file objects are closed. The pin can directly access the default clock object, rather than go through the standard clock interface.

Minidrivers can support the [**KSPROPERTY\_CLOCK\_FUNCTIONTABLE**](https://msdn.microsoft.com/library/windows/hardware/ff564466) property to provide user-mode clients with a mechanism to check reference clock time. This property fills in a structure with function pointers that enable this, thereby supporting precise rate matching.

In addition, minidrivers support the [**KSPROPERTY\_STREAM\_RATE**](https://msdn.microsoft.com/library/windows/hardware/ff565752) property if a specified pin allows rate changes.

Applications that use the kernel streaming proxy interface call methods in the [IKsClockPropertySet](https://msdn.microsoft.com/library/windows/hardware/ff559728) interface to get and set time on physical clocks that may be used elsewhere for rate matching.

See [Quality Management](quality-management.md) for related information.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Default%20Clocks%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


