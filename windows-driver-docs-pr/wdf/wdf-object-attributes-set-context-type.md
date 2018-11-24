---
title: WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro
description: The WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro inserts an object's driver-defined context information into the object's WDF_OBJECT_ATTRIBUTES structure.
ms.assetid: cac8b8f4-cc6b-4e6c-ad0b-dee58e4673ff
keywords:
 - WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro


\[Applies to KMDF and UMDF\]

The WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro inserts an object's driver-defined context information into the object's [**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.

Syntax
------

```ManagedCPlusPlus
void WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE(
    _attributes,
    _contexttype
);
```

Parameters
----------

*_attributes*   
A pointer to an object's [**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.

*_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

Return value
------------

This macro does not return a value.

Remarks
-------

You should use the WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro after calling [**WDF_OBJECT_ATTRIBUTES_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552402).

For more information about using the WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro, see [Framework Object Context Space](https://msdn.microsoft.com/library/windows/hardware/ff542873).

For a code example that uses this macro, see [**WDF_DECLARE_CONTEXT_TYPE**](wdf-declare-context-type.md).

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


[**WDF_DECLARE_CONTEXT_TYPE**](wdf-declare-context-type.md)

[**WDF_OBJECT_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400)

[**WDF_OBJECT_ATTRIBUTES_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552402)

[**WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE**](wdf-object-attributes-init-context-type.md)

 

 






