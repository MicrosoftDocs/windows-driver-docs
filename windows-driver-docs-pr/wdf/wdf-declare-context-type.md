---
title: WDF\_DECLARE\_CONTEXT\_TYPE macro
author: windows-driver-content
description: The WDF\_DECLARE\_CONTEXT\_TYPE macro creates a name and an accessor method for a driver's object-specific context space.
ms.assetid: 5fd9950e-943a-4340-b8f1-125343effdf7
keywords:
 - WDF_DECLARE_CONTEXT_TYPE macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDF\_DECLARE\_CONTEXT\_TYPE macro


\[Applies to KMDF and UMDF\]

The WDF\_DECLARE\_CONTEXT\_TYPE macro creates a name and an accessor method for a driver's object-specific context space.

Syntax
------

```ManagedCPlusPlus
void WDF_DECLARE_CONTEXT_TYPE(
    _contexttype
);
```

Parameters
----------

*\_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

Return value
------------

This macro does not return a value.

Remarks
-------

For more information about using this macro, see [Framework Object Context Space](https://msdn.microsoft.com/library/windows/hardware/ff542873).

Examples
--------

The following code example defines a context structure (MY\_REQUEST\_CONTEXT) for a request object, registers the structure, and then invokes the WDF\_DECLARE\_CONTEXT\_TYPE macro. The macro creates an accessor method for the context structure and names the method **WdfObjectGet\_MY\_REQUEST\_CONTEXT**.

```
typedef struct _MY_REQUEST_CONTEXT {
  LIST_ENTRY ListEntry;
  WDFMEMORY Memory;
} MY_REQUEST_CONTEXT, *PMY_REQUEST_CONTEXT;

WDF_DECLARE_CONTEXT_TYPE(MY_REQUEST_CONTEXT)
```

The following code example creates a request object, and then it uses the **WdfObjectGet\_MY\_REQUEST\_CONTEXT** accessor method to obtain a pointer to the object's context space.

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
</tbody>
</table>

## See also


[**WdfObjectGetTypedContext**](wdfobjectgettypedcontext.md)

[**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](wdf-declare-context-type-with-name.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF_DECLARE_CONTEXT_TYPE%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


