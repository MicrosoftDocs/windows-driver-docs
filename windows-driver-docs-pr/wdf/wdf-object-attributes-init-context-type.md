---
title: WDF\_OBJECT\_ATTRIBUTES\_INIT\_CONTEXT\_TYPE macro
author: windows-driver-content
description: The WDF\_OBJECT\_ATTRIBUTES\_INIT\_CONTEXT\_TYPE macro initializes a driver's WDF\_OBJECT\_ATTRIBUTES structure and inserts an object's driver-defined context information into the structure.
ms.assetid: 83e397b1-e37d-451d-9007-3b34993187c3
keywords:
 - WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDF\_OBJECT\_ATTRIBUTES\_INIT\_CONTEXT\_TYPE macro


\[Applies to KMDF and UMDF\]

The **WDF\_OBJECT\_ATTRIBUTES\_INIT\_CONTEXT\_TYPE** macro initializes a driver's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure and inserts an object's driver-defined context information into the structure.

Syntax
------

```ManagedCPlusPlus
void WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(
    _attributes,
    _contexttype
);
```

Parameters
----------

*\_attributes*   
A pointer to a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.

*\_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

Return value
------------

This macro does not return a value.

Remarks
-------

Before calling **WDF\_OBJECT\_ATTRIBUTES\_INIT\_CONTEXT\_TYPE**, you must call [**WDF\_DECLARE\_CONTEXT\_TYPE**](wdf-declare-context-type.md) or [**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](wdf-declare-context-type-with-name.md) globally (not within a function).

The **WDF\_OBJECT\_ATTRIBUTES\_INIT\_CONTEXT\_TYPE** macro combines the [**WDF\_OBJECT\_ATTRIBUTES\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552402) function and the [**WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE**](wdf-object-attributes-set-context-type.md) macro.

Examples
--------

The following code example defines a WDM\_NDIS\_REQUEST context structure. Then, the example invokes the [**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](wdf-declare-context-type-with-name.md) macro to register the structure and specify that the context accessor method will be named **RequestGetMyContext**. Then, in a function, the example allocates a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure, and then initializes the **WDF\_OBJECT\_ATTRIBUTES** structure.

```
typedef struct _WDM_NDIS_REQUEST
{
   PMP_ADAPTER  Adapter;
   NDIS_OID  Oid;
   NDIS_REQUEST_TYPE  RequestType;
   PVOID  InformationBuffer;
   ULONG  InformationBufferLength;
   PULONG  BytesReadOrWritten;
   PULONG  BytesNeeded;
} WDM_NDIS_REQUEST, *PWDM_NDIS_REQUEST;

WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(WDM_NDIS_REQUEST, RequestGetMyContext);

// above are in global space

...

WDF_OBJECT_ATTRIBUTES  attributes;

WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE( &amp;attributes, WDM_NDIS_REQUEST );
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


[**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400)

[**WDF\_OBJECT\_ATTRIBUTES\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552402)

[**WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE**](wdf-object-attributes-set-context-type.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


