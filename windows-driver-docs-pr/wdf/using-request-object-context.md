---
title: Using Request Object Context
description: Using Request Object Context
ms.assetid: befb4a22-0640-45e3-890e-6ff17969b017
keywords: ["request objects WDK KMDF , context space", "context space WDK KMDF"]
---

# Using Request Object Context


## <a href="" id="ddk-using-request-object-context-df"></a>


Every framework request object, whether created by the framework or by a driver, can contain driver-defined context space. When a framework-based driver initializes a framework device object, the driver can call [**WdfDeviceInitSetRequestAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff546786) to specify a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that describes context space for the device's request objects.

The framework allocates context space for request objects as follows:

-   When the framework creates request objects for your driver, it allocates context space with the size that your driver specified when it called **WdfDeviceInitSetRequestAttributes**.

-   If your driver creates additional request objects by calling [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951), you can specify a context size by providing a WDF\_OBJECT\_ATTRIBUTES structure.

For more information about allocating and accessing context space for framework objects, see [Framework Object Context Space](framework-object-context-space.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20Request%20Object%20Context%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




