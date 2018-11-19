---
title: WdfObjectAddCustomTypeWithData macro
description: The WdfObjectAddCustomTypeWithData macro associates a framework object with a custom type, and optionally associates this pair with a data buffer and event callback functions.
ms.assetid: 237F9BAA-A2E2-4F20-B52E-8F093B326E45
keywords:
 - WdfObjectAddCustomTypeWithData macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# WdfObjectAddCustomTypeWithData macro


\[Applies to KMDF and UMDF\]

The **WdfObjectAddCustomTypeWithData** macro associates a framework object with a custom type, and optionally associates this pair with a data buffer and event callback functions.

Syntax
------

```ManagedCPlusPlus
NTSTATUS WdfObjectAddCustomTypeWithData(
    _handle,
    _type,
    _data,
    _cleanup,
    _destroy
);
```

Parameters
----------

*_handle*   
A handle to a framework object.

*_type*   
The driver-defined name for the custom type.

*_data*   
A pointer to a driver-supplied data buffer, or NULL. This parameter is optional.

*_cleanup*   
A pointer to the driver's [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) callback function, or NULL. This parameter is optional.

*_destroy*   
A pointer to the driver's [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) callback function, or NULL. This parameter is optional.

Return value
------------

**WdfObjectAddCustomTypeWithData** returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_OBJECT_PATH_INVALID</strong></td>
<td><p>The specified handle cannot have a custom type added to it.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td><p>The custom type could not be allocated.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_OBJECT_NAME_EXISTS</strong></td>
<td><p>The driver has already added the specified custom type.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_DELETE_PENDING</strong></td>
<td><p>The object that the Handle parameter specifies is being deleted. In this situation, the framework does not add the custom type.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If your driver calls **WdfObjectAddCustomTypeWithData** with a pointer to a data buffer, the driver can provide an [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) or [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) callback function to deallocate the memory buffer when the object is deleted.

For more information about object custom types, see [Framework Object Custom Types](https://msdn.microsoft.com/library/windows/hardware/hh406457).

For a code example, see [**WdfObjectAddCustomType**](wdfobjectaddcustomtype.md).

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

[**WdfObjectGetCustomTypeData**](wdfobjectgetcustomtypedata.md)

[**WdfObjectIsCustomType**](wdfobjectiscustomtype.md)

 

 






