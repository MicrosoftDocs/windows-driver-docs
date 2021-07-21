---
title: WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE macro
description: The WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE macro initializes a driver's WDF_OBJECT_ATTRIBUTES structure and inserts an object's driver-defined context information into the structure.
keywords:
 - WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE macro


\[Applies to KMDF and UMDF\]

The **WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE** macro initializes a driver's [**WDF_OBJECT_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure and inserts an object's driver-defined context information into the structure.

## Syntax

```ManagedCPlusPlus
void WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(
    _attributes,
    _contexttype
);
```

## Parameters

*_attributes*   
A pointer to a [**WDF_OBJECT_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure.

*_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

## Return value

This macro does not return a value.

## Remarks

Before calling **WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE**, you must call [**WDF_DECLARE_CONTEXT_TYPE**](wdf-declare-context-type.md) or [**WDF_DECLARE_CONTEXT_TYPE_WITH_NAME**](wdf-declare-context-type-with-name.md) globally (not within a function).

The **WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE** macro combines the [**WDF_OBJECT_ATTRIBUTES_INIT**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdf_object_attributes_init) function and the [**WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE**](wdf-object-attributes-set-context-type.md) macro.

## Examples

The following code example defines a WDM_NDIS_REQUEST context structure. Then, the example invokes the [**WDF_DECLARE_CONTEXT_TYPE_WITH_NAME**](wdf-declare-context-type-with-name.md) macro to register the structure and specify that the context accessor method will be named **RequestGetMyContext**. Then, in a function, the example allocates a [**WDF_OBJECT_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure, and then initializes the **WDF_OBJECT_ATTRIBUTES** structure.

```cpp
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

WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE( &attributes, WDM_NDIS_REQUEST );
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td><a href="https://go.microsoft.com/fwlink/p/?linkid=531356" data-raw-source="[Universal](https://go.microsoft.com/fwlink/p/?linkid=531356)">Universal</a></td>
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


[**WDF_OBJECT_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes)

[**WDF_OBJECT_ATTRIBUTES_INIT**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdf_object_attributes_init)

[**WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE**](wdf-object-attributes-set-context-type.md)

 

