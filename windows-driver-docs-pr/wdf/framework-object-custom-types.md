---
title: Framework Object Custom Types
description: Framework Object Custom Types
ms.date: 04/20/2017
---

# Framework Object Custom Types


Starting in KMDF version 1.11, the framework supports custom type names. A custom type name is a string that driver can associate with a WDFOBJECT instance. Drivers define their own custom type names. The driver specifies a custom type name for an object after the driver has called the object's creation method.

Use these macros to manipulate custom type names:

-   To define a custom type name, call [**WDF\_DECLARE\_CUSTOM\_TYPE**](./wdf-declare-custom-type.md) from an area of the driver that declares global data, such as a header file.
-   Call [**WdfObjectAddCustomType**](./wdfobjectaddcustomtype.md) or [**WdfObjectAddCustomTypeWithData**](./wdfobjectaddcustomtypewithdata.md) to associate a custom type with a framework object.
-   Call [**WdfObjectIsCustomType**](./wdfobjectiscustomtype.md) to determine whether a specified object is of a specified custom type.
-   After calling [**WdfObjectAddCustomTypeWithData**](./wdfobjectaddcustomtypewithdata.md), the driver can later call [**WdfObjectGetCustomTypeData**](./wdfobjectgetcustomtypedata.md) to retrieve the data.

A driver can associate multiple custom types with a single framework object. A driver can also associate multiple framework objects with a single custom type.

In output from KMDF debugger extensions, custom type names are displayed along with other WDF object information.

```cpp
WDF_Object_Name, [custom_Type1_Name, custom_Type2_Name]
```

 

