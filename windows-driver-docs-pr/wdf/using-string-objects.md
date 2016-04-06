---
title: Using String Objects
description: This topic describes the support that Windows Driver Frameworks (WDF) provides for string objects. It applies to both Kernel-Mode Driver Framework (KMDF).
ms.assetid: b1d52a18-ebd5-4ba7-b5c7-3ef3d298c82e
keywords: ["string objects WDK KMDF", "framework objects WDK KMDF , string objects", "Unicode strings WDK KMDF"]
---

# Using String Objects


This topic describes the support that Windows Driver Frameworks (WDF) provides for string objects. It applies to both Kernel-Mode Driver Framework (KMDF) drivers and User-Mode Driver Framework (UMDF) drivers starting in version 2.

## <a href="" id="ddk-using-user-event-objects-df"></a>


WDF uses only Unicode strings. All of the methods that are defined by framework objects accept only Unicode strings.

The framework defines the *framework string object* that KMDF and UMDF drivers can use to represent Unicode strings.

Your driver can call [**WdfStringCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550046) to create a string object and to optionally assign a Unicode string to the object.

Some of the framework's object methods, such as [**WdfRegistryQueryString**](https://msdn.microsoft.com/library/windows/hardware/ff549923), accept a string object handle as input and assign a string to the string object.

To access the string that is assigned to a string object, your driver can call [**WdfStringGetUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff550049).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20String%20Objects%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




