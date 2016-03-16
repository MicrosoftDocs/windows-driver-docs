---
title: Framework Object Hierarchy
description: Framework Object Hierarchy
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: ffacca8f-4083-4998-83d2-7c31544eb497
keywords: ["UMDF objects WDK hierarchy", "framework objects WDK UMDF hierarchy", "hierarchy WDK UMDF"]
---

# Framework Object Hierarchy


\[This topic applies to UMDF 1.*x*.\]

The following figure shows the parent-child framework object hierarchy.

![umdf parent-child object hierarchy](images/umdfhierarchy.gif)

The lifetime scope of framework objects is determined by their location in the hierarchy and how the objects are created. The lifetime scope of framework objects falls into one of the following categories:

-   The framework controls the creation and destruction of the objects.

    The framework creates and destroys objects, such as the [driver object](framework-driver-object.md) and [device object](framework-device-object.md), in response to system events. When a user-mode driver calls the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method to create the device object, the driver can optionally register to be notified by the framework before the device object is destroyed.

-   The framework creates the object; however, the driver controls when the object is released.

    The [I/O request object](framework-i-o-request-object.md) follows this pattern when I/O is presented to the driver. The framework creates the request object, and the request object's lifetime is valid until the driver calls the [**IWDFIoRequest::Complete**](https://msdn.microsoft.com/library/windows/hardware/ff559070) method.

-   The driver creates the object and associates the object with another framework object.

    Some framework objects are created by a method that is exposed by a parent framework object instance that the objects are to be associated to for lifetime-management purposes. The [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) method is an example of this pattern. If a call to **IWDFDevice::CreateIoQueue** succeeds, the newly created I/O queue is associated with the device instance that the [IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface represents. When the parent object is destroyed, the framework automatically cleans up child instances. Drivers are notified of these events if the drivers register appropriate callback functions with the framework.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Object%20Hierarchy%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




