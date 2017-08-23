---
title: WdfObjectGetTypedContext macro
author: windows-driver-content
description: The WdfObjectGetTypedContext macro returns a pointer to an object's context space.
ms.assetid: de0edae4-7c05-4419-972e-c106875dfff1
keywords:
 - WdfObjectGetTypedContext macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

You can use the **WdfObjectGetTypedContext** macro to obtain a pointer to any framework object's context space. Use this macro as an alternative to calling an object-specific context accessor method that is created by the [**WDF\_DECLARE\_CONTEXT\_TYPE**](wdf-declare-context-type.md) macro or the [**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](wdf-declare-context-type-with-name.md) macro. Note that if you use **WdfObjectGetTypedContext**, you still must use WDF\_DECLARE\_CONTEXT\_TYPE or WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME to declare your object context.

For more information about these macros, see [Framework Object Context Space](https://msdn.microsoft.com/library/windows/hardware/ff542873).

Examples
--------

The following code example defines a context structure (MY\_REQUEST\_CONTEXT) for a request object and then registers the structure.

```
typedef struct _MY_REQUEST_CONTEXT {
  LIST_ENTRY ListEntry;
  WDFMEMORY Memory;
} MY_REQUEST_CONTEXT, *PMY_REQUEST_CONTEXT;

WDF_DECLARE_CONTEXT_TYPE(MY_REQUEST_CONTEXT)
```

The following code example creates a request object and obtains a pointer to its context space.

```
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
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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


[**WDF\_DECLARE\_CONTEXT\_TYPE**](wdf-declare-context-type.md)

[**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](wdf-declare-context-type-with-name.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WdfObjectGetTypedContext%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


