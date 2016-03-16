---
title: Framework Object Methods
description: Framework Object Methods
ms.assetid: f82275c5-15f9-43f5-91bb-b83446526c28
keywords: ["framework objects WDK KMDF methods"]
---

# Framework Object Methods


## <a href="" id="ddk-framework-object-methods-df"></a>


Each framework object exports a set of methods (functions). Each method serves one of two purposes:

-   It performs an action that is associated with the object.

    For example, the [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) method creates an I/O queue for a device.

    Methods that perform an action typically return an [NTSTATUS value](https://msdn.microsoft.com/library/windows/hardware/ff557697).

-   It retrieves or modifies a [property](framework-object-properties.md) that is associated with the object.

    For example, the [**WdfRequestGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549965) method returns information about an I/O request's completion status.

    Methods that retrieve a property typically return the property's value, while methods that modify a property typically do not return a value.

Each object method accepts an object handle as input. If a driver passes an invalid object handle to an object method, a system bug check occurs.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Object%20Methods%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




