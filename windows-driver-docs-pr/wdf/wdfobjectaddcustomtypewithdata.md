---
title: WdfObjectAddCustomTypeWithData macro
author: windows-driver-content
description: The WdfObjectAddCustomTypeWithData macro associates a framework object with a custom type, and optionally associates this pair with a data buffer and event callback functions.
ms.assetid: 237F9BAA-A2E2-4F20-B52E-8F093B326E45
keywords:
 - WdfObjectAddCustomTypeWithData macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

*\_handle*   
A handle to a framework object.

*\_type*   
The driver-defined name for the custom type.

*\_data*   
A pointer to a driver-supplied data buffer, or NULL. This parameter is optional.

*\_cleanup*   
A pointer to the driver's [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) callback function, or NULL. This parameter is optional.

*\_destroy*   
A pointer to the driver's [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) callback function, or NULL. This parameter is optional.

Return value
------------

**WdfObjectAddCustomTypeWithData** returns STATUS\_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:

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
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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


[**WDF\_DECLARE\_CUSTOM\_TYPE**](wdf-declare-custom-type.md)

[**WdfObjectAddCustomType**](wdfobjectaddcustomtype.md)

[**WdfObjectGetCustomTypeData**](wdfobjectgetcustomtypedata.md)

[**WdfObjectIsCustomType**](wdfobjectiscustomtype.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WdfObjectAddCustomTypeWithData%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


