---
title: WDF_DECLARE_CONTEXT_TYPE macro
description: The WDF_DECLARE_CONTEXT_TYPE macro creates a name and an accessor method for a driver's object-specific context space.
ms.assetid: 5fd9950e-943a-4340-b8f1-125343effdf7
keywords:
 - WDF_DECLARE_CONTEXT_TYPE macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF_DECLARE_CONTEXT_TYPE macro


\[Applies to KMDF and UMDF\]

The WDF_DECLARE_CONTEXT_TYPE macro creates a name and an accessor method for a driver's object-specific context space.

Syntax
------

```ManagedCPlusPlus
void WDF_DECLARE_CONTEXT_TYPE(
    _contexttype
);
```

Parameters
----------

*_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

Return value
------------

This macro does not return a value.

Remarks
-------

For more information about using this macro, see [Framework Object Context Space](https://msdn.microsoft.com/library/windows/hardware/ff542873).

Examples
--------

The following code example defines a context structure (MY_REQUEST_CONTEXT) for a request object, registers the structure, and then invokes the WDF_DECLARE_CONTEXT_TYPE macro. The macro creates an accessor method for the context structure and names the method **WdfObjectGet_MY_REQUEST_CONTEXT**.

```cpp
typedef struct _MY_REQUEST_CONTEXT {
  LIST_ENTRY ListEntry;
  WDFMEMORY Memory;
} MY_REQUEST_CONTEXT, *PMY_REQUEST_CONTEXT;

WDF_DECLARE_CONTEXT_TYPE(MY_REQUEST_CONTEXT)
```

The following code example creates a request object, and then it uses the **WdfObjectGet_MY_REQUEST_CONTEXT** accessor method to obtain a pointer to the object's context space.

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
pMyContext = WdfObjectGet_MY_REQUEST_CONTEXT(Request);
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

[**WDF_DECLARE_CONTEXT_TYPE_WITH_NAME**](wdf-declare-context-type-with-name.md)

 

 






