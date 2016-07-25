---
title: Property-Data-Type Identifiers
description: Property-Data-Type Identifiers
ms.assetid: 8deb96d8-c18c-48f2-be5d-1a3fc8ba8508
keywords: ["device properties WDK device installations , property-data-type identifiers"]
---

# Property-Data-Type Identifiers


A property-data-type identifier is a [**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546)-typed value that represents the data format of a property. In general, a property-data-type identifier is a bitwise OR of a [**base-data-type identifier**](https://msdn.microsoft.com/library/windows/hardware/ff537793) and a [**property-data-type modifier**](https://msdn.microsoft.com/library/windows/hardware/ff549770). A property-data-type identifier can represent a single fixed-length base-data-type value, a single variable-length base-data-type value, an array of fixed-length base-data-type values, or a list of variable-length base-data-type values.

The system-supported base-data-type identifiers and property-data-type modifiers are defined in *Devpropdef.h*.

Windows enforces the following requirements on property-data-type identifiers:

-   The base-data-type identifier is one of the DEVPROP\_TYPE\_*Xxx* identifiers.

-   If the base-data-type identifier is [**DEVPROP\_TYPE\_EMPTY**](https://msdn.microsoft.com/library/windows/hardware/ff543585) or [**DEVPROP\_TYPE\_NULL**](https://msdn.microsoft.com/library/windows/hardware/ff543602), the property data-type identifier cannot include a property-data-type modifier.

-   If the property-data-type identifier includes a property-data-type modifier, the property-data-type modifier is one of the DEVPROP\_TYPEMOD\_*Xxx* identifiers.

-   The [**DEVPROP\_TYPEMOD\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff543556) property-data-type modifier can be combined only with the fixed-length base data types.

-   The [**DEVPROP\_TYPEMOD\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff543559) property-data-type modifier can be combined only with the variable-length base data types.

In addition to enforcing requirements on property data type identifiers, Windows also enforces [property value requirements](property-value-requirements.md) that depend on the property data type.

The SetupAPI property functions that retrieve and set a property value take a *PropertyType* parameter. For the functions that retrieve a property value, *PropertyType* is an output parameter that receives the property-data-type identifier for a property. For the functions that set a property value, *PropertyType* is an input parameter that supplies the property-data-type identifier for a device property.

For more information, see [Using SetupAPI to Access Device Properties (Windows Vista and Later)](using-setupapi-to-access-device-properties--windows-vista-and-later-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Property-Data-Type%20Identifiers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




