---
title: WDF_DECLARE_CUSTOM_TYPE macro
description: The WDF_DECLARE_CUSTOM_TYPE macro creates a name and an accessor method for a driver's custom type.
ms.assetid: DF496E17-B3D4-4983-8506-40810ECAEA3E
keywords:
 - WDF_DECLARE_CUSTOM_TYPE macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF_DECLARE_CUSTOM_TYPE macro


\[Applies to KMDF and UMDF\]

The **WDF_DECLARE_CUSTOM_TYPE** macro creates a name and an accessor method for a driver's custom type.

Syntax
------

```ManagedCPlusPlus
void WDF_DECLARE_CUSTOM_TYPE(
    _customtype
);
```

Parameters
----------

*_customtype*   
The driver-defined name of a custom type.

Return value
------------

This macro does not return a value.

Remarks
-------

When calling **WDF_DECLARE_CUSTOM_TYPE**, a driver defines its own custom type name. When selecting a custom type name, choose a name that is specific to the domain of the driver. As a convention, do not start your custom type name with the prefix *Wdf*.

For more information about object custom types, see [Framework Object Custom Types](https://msdn.microsoft.com/library/windows/hardware/hh406457).

Examples
--------

The following code example calls the **WDF_DECLARE_CUSTOM_TYPE** macro to declare the MY_CUSTOM_TYPE custom type name. The driver must put this line in an area of the driver that declares global data, typically a header file.

```cpp
WDF_DECLARE_CUSTOM_TYPE(MY_CUSTOM_TYPE)
```

The following code example creates a request object, and then it uses the [**WdfObjectAddCustomType**](wdfobjectaddcustomtype.md) method to associate the **MY_CUSTOM_TYPE** custom type with the request object.

```cpp
WDFREQUEST Request;
WDF_OBJECT_ATTRIBUTES MyRequestObjectAttributes;

WDF_OBJECT_ATTRIBUTES_INIT(&amp;MyRequestObjectAttributes);

status = WdfRequestCreate(
                          &amp;MyRequestObjectAttributes
                          NULL,
                          &amp;Request
                          );

if (!NT_SUCCESS(status)) {
    return status;
}

status = WdfObjectAddCustomType(
                          Request,
                          MY_CUSTOM_TYPE
                          );

if (!NT_SUCCESS(status)) {
    return status;
}
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" data-raw-source="[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)">Universal</a></td>
</tr>
<tr class="even">
<td><p>Minimum KMDF version</p></td>
<td><p>1.11</p></td>
</tr>
<tr class="odd">
<td><p>Minimum UMDF version</p></td>
<td><p>2.0</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdfobject.h (include Wdf.h)</td>
</tr>
</tbody>
</table>

## See also


[**WdfObjectAddCustomType**](wdfobjectaddcustomtype.md)

[**WdfObjectAddCustomTypeWithData**](wdfobjectaddcustomtypewithdata.md)

[**WdfObjectGetCustomTypeData**](wdfobjectgetcustomtypedata.md)

[**WdfObjectIsCustomType**](wdfobjectiscustomtype.md)

 

 






