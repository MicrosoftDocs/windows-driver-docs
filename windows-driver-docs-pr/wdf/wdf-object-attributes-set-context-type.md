---
title: WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro
description: The WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro inserts an object's driver-defined context information into the object's WDF_OBJECT_ATTRIBUTES structure.
keywords:
 - WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro


\[Applies to KMDF and UMDF\]

The WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro inserts an object's driver-defined context information into the object's [**WDF_OBJECT_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure.

## Syntax

```ManagedCPlusPlus
void WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE(
    _attributes,
    _contexttype
);
```

## Parameters

*_attributes*   
A pointer to an object's [**WDF_OBJECT_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure.

*_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

## Return value

This macro does not return a value.

## Remarks

You should use the WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro after calling [**WDF_OBJECT_ATTRIBUTES_INIT**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdf_object_attributes_init).

For more information about using the WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro, see [Framework Object Context Space](./framework-object-context-space.md).

For a code example that uses this macro, see [**WDF_DECLARE_CONTEXT_TYPE**](wdf-declare-context-type.md).

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


[**WDF_DECLARE_CONTEXT_TYPE**](wdf-declare-context-type.md)

[**WDF_OBJECT_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes)

[**WDF_OBJECT_ATTRIBUTES_INIT**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdf_object_attributes_init)

[**WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE**](wdf-object-attributes-init-context-type.md)

 

