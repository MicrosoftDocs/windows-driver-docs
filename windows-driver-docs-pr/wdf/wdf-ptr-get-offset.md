---
title: WDF_PTR_GET_OFFSET macro
description: The WDF_PTR_GET_OFFSET macro subtracts an address from another address and returns the resulting offset value.
ms.assetid: b5159207-ba5c-4924-a06e-725ccd3c8a12
keywords:
 - WDF_PTR_GET_OFFSET macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WDF_PTR_GET_OFFSET macro


The **WDF_PTR_GET_OFFSET** macro subtracts an address from another address and returns the resulting offset value.

Syntax
------

```ManagedCPlusPlus
size_t WDF_PTR_GET_OFFSET(
    _base,
    _addr
);
```

Parameters
----------

*_base*   
Specifies the value to subtract from the starting address.

*_addr*   
Specifies the starting address.

Return value
------------

Returns the offset between the two specified addresses.

Remarks
-------

The macro is defined as follows:

```ManagedCPlusPlus
#define WDF_PTR_GET_OFFSET(_base, _addr) \
        (size_t) (((PUCHAR) _addr) - ((PUCHAR) _base))
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

 

 






