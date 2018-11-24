---
title: WDF_PTR_ADD_OFFSET_TYPE macro
description: The WDF_PTR_ADD_OFFSET_TYPE macro adds an offset value to an address and returns the resulting address cast to the specified type.
ms.assetid: b46d0bbe-8401-4c97-8327-fecd3af50eca
keywords:
 - WDF_PTR_ADD_OFFSET_TYPE macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF_PTR_ADD_OFFSET_TYPE macro


The **WDF_PTR_ADD_OFFSET_TYPE** macro adds an offset value to an address and returns the resulting address cast to the specified type.

Syntax
------

```ManagedCPlusPlus
_type WDF_PTR_ADD_OFFSET_TYPE(
    _ptr,
    _offset,
    _type
);
```

Parameters
----------

*_ptr*   
Specifies an address.

*_offset*   
Specifies the offset value in bytes.

*_type*   
Specifies the data type to return.

Return value
------------

Returns a pointer to the resulting address. You select the data type of the return value in the *_type* parameter of the macro.

Remarks
-------

The macro is defined as follows:

```ManagedCPlusPlus
#define WDF_PTR_ADD_OFFSET_TYPE(_ptr, _offset, _type) \
    ((_type) (((PUCHAR) (_ptr)) + (_offset)))
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
<td><p>1.5</p></td>
</tr>
<tr class="odd">
<td><p>Minimum UMDF version</p></td>
<td><p>2.0</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdfcore.h (include Wdf.h)</td>
</tr>
</tbody>
</table>

 

 






