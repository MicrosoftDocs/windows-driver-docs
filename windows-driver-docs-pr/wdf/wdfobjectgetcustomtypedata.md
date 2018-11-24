---
title: WdfObjectGetCustomTypeData macro
description: The WdfObjectGetCustomTypeData macro retrieves the data that the driver previously associated with a framework object and custom type.
ms.assetid: 60A6546B-84C6-4A53-BAA1-3719DCBA63B4
keywords:
 - WdfObjectGetCustomTypeData macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectGetCustomTypeData macro


\[Applies to KMDF and UMDF\]

The **WdfObjectGetCustomTypeData** macro retrieves the data that the driver previously associated with a framework object and custom type.

Syntax
------

```ManagedCPlusPlus
PULONG WdfObjectGetCustomTypeData(
  [in]  Handle,
  [in]  Type
);
```

Parameters
----------

*Handle* \[in\]  
A handle to a framework object.

*Type* \[in\]  
The symbol name of a custom type.

Return value
------------

**WdfObjectGetCustomTypeData** returns the data that the driver associated with a framework object and custom type in a previous call to [**WdfObjectAddCustomTypeWithData**](wdfobjectaddcustomtypewithdata.md).

Remarks
-------

For more information about object driver types, see [Framework Object Custom Types](https://msdn.microsoft.com/library/windows/hardware/hh406457).

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
<td><p>1.11</p></td>
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


[**WDF_DECLARE_CUSTOM_TYPE**](wdf-declare-custom-type.md)

[**WdfObjectAddCustomType**](wdfobjectaddcustomtype.md)

[**WdfObjectAddCustomTypeWithData**](wdfobjectaddcustomtypewithdata.md)

[**WdfObjectIsCustomType**](wdfobjectiscustomtype.md)

 

 






