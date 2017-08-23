---
title: WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE macro
author: windows-driver-content
description: The WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE macro inserts an object's driver-defined context information into the object's WDF\_OBJECT\_ATTRIBUTES structure.
ms.assetid: cac8b8f4-cc6b-4e6c-ad0b-dee58e4673ff
keywords:
 - WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE macro


\[Applies to KMDF and UMDF\]

The WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE macro inserts an object's driver-defined context information into the object's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.

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

*\_attributes*   
A pointer to an object's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.

*\_contexttype*   
The structure type name of a driver-defined structure that describes the contents of an object's context space.

Return value
------------

This macro does not return a value.

Remarks
-------

You should use the WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE macro after calling [**WDF\_OBJECT\_ATTRIBUTES\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552402).

For more information about using the WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE macro, see [Framework Object Context Space](https://msdn.microsoft.com/library/windows/hardware/ff542873).

For a code example that uses this macro, see [**WDF\_DECLARE\_CONTEXT\_TYPE**](wdf-declare-context-type.md).

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


[**WDF\_DECLARE\_CONTEXT\_TYPE**](wdf-declare-context-type.md)

[**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400)

[**WDF\_OBJECT\_ATTRIBUTES\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552402)

[**WDF\_OBJECT\_ATTRIBUTES\_INIT\_CONTEXT\_TYPE**](wdf-object-attributes-init-context-type.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


