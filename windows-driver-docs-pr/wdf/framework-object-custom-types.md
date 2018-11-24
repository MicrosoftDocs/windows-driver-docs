---
title: Framework Object Custom Types
description: Framework Object Custom Types
ms.assetid: E00393ED-7285-4354-9E1B-D9ABDB7DC9F2
ms.date: 04/20/2017
ms.localizationpriority: medium
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

```cpp
WDF_Object_Name, [custom_Type1_Name, custom_Type2_Name]
```

 

 





