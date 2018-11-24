---
title: WdfObjectIsCustomType macro
description: The WdfObjectIsCustomType macro determines whether a framework object is of a specified custom type.
ms.assetid: EE3CC41D-6FBA-49A2-A2A0-C7E818F6FAAA
keywords:
 - WdfObjectIsCustomType macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectIsCustomType macro


\[Applies to KMDF and UMDF\]

The **WdfObjectIsCustomType** macro determines whether a framework object is of a specified custom type.

Syntax
------

```ManagedCPlusPlus
BOOLEAN WdfObjectIsCustomType(
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

Returns TRUE if the specified object is of the specified custom type. Otherwise, returns FALSE.

Remarks
-------

For more information about object custom types, see [Framework Object Custom Types](https://msdn.microsoft.com/library/windows/hardware/hh406457).

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

[**WdfObjectGetCustomTypeData**](wdfobjectgetcustomtypedata.md)

 

 






