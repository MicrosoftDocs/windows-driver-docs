---
title: WDF_DECLARE_CONTEXT_TYPE_WITH_NAME macro
description: The WDF_DECLARE_CONTEXT_TYPE_WITH_NAME macro creates an accessor method with a specified name for a driver's object-specific context space.
ms.assetid: e5911bd2-6976-4a91-b9ba-befa7ec93103
keywords:
 - WDF_DECLARE_CONTEXT_TYPE_WITH_NAME macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF_DECLARE_CONTEXT_TYPE_WITH_NAME macro


\[Applies to KMDF and UMDF\]

The WDF_DECLARE_CONTEXT_TYPE_WITH_NAME macro creates an accessor method with a specified name for a driver's object-specific context space.

Syntax
------

```ManagedCPlusPlus
void WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(
    _contexttype,
    _castingfunction
);
```

Parameters
----------

*_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

*_castingfunction*   
A C-language routine name. The macro uses this name as the name for the accessor method that it creates for the object's context space.

Return value
------------

This macro does not return a value.

Remarks
-------

For more information about using this macro, see [Framework Object Context Space](https://msdn.microsoft.com/library/windows/hardware/ff542873).

Examples
--------

The following code example defines a context structure (MY_REQUEST_CONTEXT) for a request object. Then, the example invokes the WDF_DECLARE_CONTEXT_TYPE_WITH_NAME macro to register the structure and specify that the context accessor method will be named **RequestGetMyContext**.

```cpp
typedef struct _MY_REQUEST_CONTEXT {
  LIST_ENTRY ListEntry;
  WDFMEMORY Memory;
} MY_REQUEST_CONTEXT, *PMY_REQUEST_CONTEXT;

WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(MY_REQUEST_CONTEXT, RequestGetMyContext)
```

The following code example creates a request object and then uses the **RequestGetMyContext** accessor method to obtain a pointer to the object's context space.

```cpp
WDFREQUEST Request;
WDF_OBJECT_ATTRIBUTES MyRequestObjectAttributes;
PMY_REQUEST_CONTEXT pMyContext;

WDF_OBJECT_ATTRIBUTES_INIT(&amp;MyRequestObjectAttributes);
WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE(
                                       &amp;MyRequestObjectAttributes,
                                       MY_REQUEST_CONTEXT
                                       );
status = WdfRequestCreate(
                          &amp;MyRequestObjectAttributes
                          NULL,
                          &amp;Request
                          );

if (!NT_SUCCESS(status)) {
    return status;
}

pMyContext = RequestGetMyContext(Request);
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
<td><p>1.0</p></td>
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


[**WdfObjectGetTypedContext**](wdfobjectgettypedcontext.md)

[**WDF_DECLARE_CONTEXT_TYPE**](wdf-declare-context-type.md)

 

 






