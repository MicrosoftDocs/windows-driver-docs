---
title: WDF\_DECLARE\_CUSTOM\_TYPE macro
author: windows-driver-content
description: The WDF\_DECLARE\_CUSTOM\_TYPE macro creates a name and an accessor method for a driver's custom type.
ms.assetid: DF496E17-B3D4-4983-8506-40810ECAEA3E
keywords:
 - WDF_DECLARE_CUSTOM_TYPE macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDF\_DECLARE\_CUSTOM\_TYPE macro


\[Applies to KMDF and UMDF\]

The **WDF\_DECLARE\_CUSTOM\_TYPE** macro creates a name and an accessor method for a driver's custom type.

Syntax
------

```ManagedCPlusPlus
void WDF_DECLARE_CUSTOM_TYPE(
    _customtype
);
```

Parameters
----------

*\_customtype*   
The driver-defined name of a custom type.

Return value
------------

This macro does not return a value.

Remarks
-------

When calling **WDF\_DECLARE\_CUSTOM\_TYPE**, a driver defines its own custom type name. When selecting a custom type name, choose a name that is specific to the domain of the driver. As a convention, do not start your custom type name with the prefix *Wdf*.

For more information about object custom types, see [Framework Object Custom Types](https://msdn.microsoft.com/library/windows/hardware/hh406457).

Examples
--------

The following code example calls the **WDF\_DECLARE\_CUSTOM\_TYPE** macro to declare the MY\_CUSTOM\_TYPE custom type name. The driver must put this line in an area of the driver that declares global data, typically a header file.

```
WDF_DECLARE_CUSTOM_TYPE(MY_CUSTOM_TYPE)
```

The following code example creates a request object, and then it uses the [**WdfObjectAddCustomType**](wdfobjectaddcustomtype.md) method to associate the **MY\_CUSTOM\_TYPE** custom type with the request object.

```
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
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF_DECLARE_CUSTOM_TYPE%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


