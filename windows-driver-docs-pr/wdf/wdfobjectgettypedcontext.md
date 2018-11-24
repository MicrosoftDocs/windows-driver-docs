---
title: WdfObjectGetTypedContext macro
description: The WdfObjectGetTypedContext macro returns a pointer to an object's context space.
ms.assetid: de0edae4-7c05-4419-972e-c106875dfff1
keywords:
 - WdfObjectGetTypedContext macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectGetTypedContext macro


\[Applies to KMDF and UMDF\]

The **WdfObjectGetTypedContext** macro returns a pointer to an object's context space.

Syntax
------

```ManagedCPlusPlus
PVOID WdfObjectGetTypedContext(
    Handle,
    Type
);
```

Parameters
----------

*Handle*   
A handle to a framework object.

*Type*   
The symbol name of a driver-defined structure that describes an object's context space.

Return value
------------

**WdfObjectGetTypedContext** returns a pointer to the specified object's context space.

Remarks
-------

You can use the **WdfObjectGetTypedContext** macro to obtain a pointer to any framework object's context space. Use this macro as an alternative to calling an object-specific context accessor method that is created by the [**WDF_DECLARE_CONTEXT_TYPE**](wdf-declare-context-type.md) macro or the [**WDF_DECLARE_CONTEXT_TYPE_WITH_NAME**](wdf-declare-context-type-with-name.md) macro. Note that if you use **WdfObjectGetTypedContext**, you still must use WDF_DECLARE_CONTEXT_TYPE or WDF_DECLARE_CONTEXT_TYPE_WITH_NAME to declare your object context.

For more information about these macros, see [Framework Object Context Space](https://msdn.microsoft.com/library/windows/hardware/ff542873).

Examples
--------

The following code example defines a context structure (MY_REQUEST_CONTEXT) for a request object and then registers the structure.

```cpp
typedef struct _MY_REQUEST_CONTEXT {
  LIST_ENTRY ListEntry;
  WDFMEMORY Memory;
} MY_REQUEST_CONTEXT, *PMY_REQUEST_CONTEXT;

WDF_DECLARE_CONTEXT_TYPE(MY_REQUEST_CONTEXT)
```

The following code example creates a request object and obtains a pointer to its context space.

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
                          &amp;MyRequestObjectAttributes,
                          NULL,
                          &amp;Request
                          );

if (!NT_SUCCESS(status)) {
    return status;
}
pMyContext = WdfObjectGetTypedContext(
                                      Request,
                                      MY_REQUEST_CONTEXT
                                      );
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
<tr class="odd">
<td><p>Library</p></td>
<td>Wdf01000.sys (KMDF);
WUDFx02000.dll (UMDF)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>Any level</p></td>
</tr>
</tbody>
</table>

## See also


[**WDF_DECLARE_CONTEXT_TYPE**](wdf-declare-context-type.md)

[**WDF_DECLARE_CONTEXT_TYPE_WITH_NAME**](wdf-declare-context-type-with-name.md)

 

 






