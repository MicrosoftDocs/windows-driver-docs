---
title: Property-Data-Type Identifiers
description: Property-Data-Type Identifiers
ms.assetid: 8deb96d8-c18c-48f2-be5d-1a3fc8ba8508
keywords:
- device properties WDK device installations , property-data-type identifiers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property-Data-Type Identifiers


A property-data-type identifier is a [**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546)-typed value that represents the data format of a property. In general, a property-data-type identifier is a bitwise OR of a [**base-data-type identifier**](https://msdn.microsoft.com/library/windows/hardware/ff537793) and a [**property-data-type modifier**](https://msdn.microsoft.com/library/windows/hardware/ff549770). A property-data-type identifier can represent a single fixed-length base-data-type value, a single variable-length base-data-type value, an array of fixed-length base-data-type values, or a list of variable-length base-data-type values.

The system-supported base-data-type identifiers and property-data-type modifiers are defined in *Devpropdef.h*.

Windows enforces the following requirements on property-data-type identifiers:

-   The base-data-type identifier is one of the DEVPROP_TYPE_*Xxx* identifiers.

-   If the base-data-type identifier is [**DEVPROP_TYPE_EMPTY**](https://msdn.microsoft.com/library/windows/hardware/ff543585) or [**DEVPROP_TYPE_NULL**](https://msdn.microsoft.com/library/windows/hardware/ff543602), the property data-type identifier cannot include a property-data-type modifier.

-   If the property-data-type identifier includes a property-data-type modifier, the property-data-type modifier is one of the DEVPROP_TYPEMOD_*Xxx* identifiers.

-   The [**DEVPROP_TYPEMOD_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff543556) property-data-type modifier can be combined only with the fixed-length base data types.

-   The [**DEVPROP_TYPEMOD_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff543559) property-data-type modifier can be combined only with the variable-length base data types.

In addition to enforcing requirements on property data type identifiers, Windows also enforces [property value requirements](property-value-requirements.md) that depend on the property data type.

The SetupAPI property functions that retrieve and set a property value take a *PropertyType* parameter. For the functions that retrieve a property value, *PropertyType* is an output parameter that receives the property-data-type identifier for a property. For the functions that set a property value, *PropertyType* is an input parameter that supplies the property-data-type identifier for a device property.

For more information, see [Using SetupAPI to Access Device Properties (Windows Vista and Later)](using-setupapi-to-access-device-properties--windows-vista-and-later-.md).

 

 





