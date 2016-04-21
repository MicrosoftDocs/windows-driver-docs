---
title: Creating Callback Objects
author: windows-driver-content
description: Creating Callback Objects
ms.assetid: bbae1458-911f-4a48-8bf2-0997e8f98826
keywords: ["callback objects WDK UMDF", "callback objects WDK UMDF , creating", "User-Mode Driver Framework WDK , objects", "user-mode drivers WDK UMDF , objects", "UMDF objects WDK , callback objects", "framework objects WDK UMDF , callback objects"]
---

# Creating Callback Objects


\[This topic applies to UMDF 1.*x*.\]

A UMDF driver can create *callback objects*, which consist of context data and interface methods. The framework accesses the driver's callback objects through the driver's callback interface methods.

The following figure shows how driver-implemented callback objects correspond to [framework objects](framework-objects.md).

![framework objects and vendor-supplied callback objects](images/correspond.gif)

A UMDF driver can create several types of callback objects, including the following:

-   Driver callback object

    The framework uses the driver callback object to initialize the driver and notify the driver of the arrival of a new device.

-   Device callback object

    The driver uses the device callback object to store device context and to handle the cleanup and closing of file objects and Plug and Play (PnP) and power management (PM) events.

-   Queue callback object

    The driver uses the queue callback object to process I/O.

The following figure shows how a UMDF driver creates a device callback object.

![call sequence for creating a umdf device callback object](images/callback.gif)

The following topics contain code examples that show how to create a callback object:

-   [Creating Callback Objects Example](creating-callback-objects-example.md)

-   [Defining Callback Objects Example](defining-callback-objects-example.md)

-   [Associating Callback Interfaces Example](associating-callback-interfaces-example.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20Callback%20Objects%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




