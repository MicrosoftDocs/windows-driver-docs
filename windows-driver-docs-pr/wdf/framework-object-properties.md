---
title: Framework Object Properties
author: windows-driver-content
description: Framework Object Properties
ms.assetid: d95a7f51-fe22-4cd6-8c46-6d571f7d9169
keywords: ["framework objects WDK KMDF , properties", "properties WDK KMDF", "get method WDK KMDF", "set method WDK KMDF"]
---

# Framework Object Properties


## <a href="" id="ddk-framework-object-properties-df"></a>


Most framework objects contain sets of properties. Properties represent information that is available to a driver. From the driver's perspective, some properties are read-only and some are read/write.

For each readable property, the framework defines a "get" [method](framework-object-methods.md) that a driver can call to retrieve the property's value. Each "get" method returns the current value of the property.

For each writable property, the framework defines a "set" method that a driver can call to modify the property's value. The driver supplies the property's new value as an input parameter to the "set" method.

For example, the framework device object defines two methods, [**WdfDeviceGetDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff545994) and [**WdfDeviceSetDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff546884), that a driver can call to get or set a device's Plug and Play (PnP) state.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Object%20Properties%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




