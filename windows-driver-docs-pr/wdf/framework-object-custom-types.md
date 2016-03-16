---
title: Framework Object Custom Types
description: Framework Object Custom Types
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: E00393ED-7285-4354-9E1B-D9ABDB7DC9F2
---

# Framework Object Custom Types


Starting in KMDF version 1.11, the framework supports custom type names. A custom type name is a string that driver can associate with a WDFOBJECT instance. Drivers define their own custom type names. The driver specifies a custom type name for an object after the driver has called the object's creation method.

Use these macros to manipulate custom type names:

-   To define a custom type name, call [**WDF\_DECLARE\_CUSTOM\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/hh439486) from an area of the driver that declares global data, such as a header file.
-   Call [**WdfObjectAddCustomType**](https://msdn.microsoft.com/library/windows/hardware/hh439344) or [**WdfObjectAddCustomTypeWithData**](https://msdn.microsoft.com/library/windows/hardware/hh439350) to associate a custom type with a framework object.
-   Call [**WdfObjectIsCustomType**](https://msdn.microsoft.com/library/windows/hardware/hh439362) to determine whether a specified object is of a specified custom type.
-   After calling [**WdfObjectAddCustomTypeWithData**](https://msdn.microsoft.com/library/windows/hardware/hh439350), the driver can later call [**WdfObjectGetCustomTypeData**](https://msdn.microsoft.com/library/windows/hardware/hh439356) to retrieve the data.

A driver can associate multiple custom types with a single framework object. A driver can also associate multiple framework objects with a single custom type.

In output from KMDF debugger extensions, custom type names are displayed along with other WDF object information.

``` syntax
WDF_Object_Name, [custom_Type1_Name, custom_Type2_Name]
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Object%20Custom%20Types%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




